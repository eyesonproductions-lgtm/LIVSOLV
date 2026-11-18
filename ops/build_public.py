"""Stage only public website assets. Never publish repository source or paid files."""
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "public"
MEDIA = {".png", ".jpg", ".jpeg", ".webp", ".svg", ".gif", ".ico", ".css", ".js", ".woff", ".woff2", ".ttf"}

NOTICE_ID = "livsolv-safety-notice"
NOTICE = '''<aside id="livsolv-safety-notice" aria-label="Safety disclaimer" style="display:block;clear:both;box-sizing:border-box;max-width:1100px;margin:24px auto;padding:20px 24px;border-top:1px solid #c4cec5;background:#f5f1e7;color:#253c30;font:14px/1.6 system-ui,sans-serif;text-align:left"><strong>Safety disclaimer.</strong> LIVSOLV provides general educational information, not individualized medical, veterinary, legal, electrical or other professional advice. Follow current local emergency instructions and the exact product label or manual. Conditions and equipment vary; no guarantee of safety, accuracy, completeness or results is made. Seek qualified help when needed. In an emergency, contact local emergency services. <a href="/safety-disclaimer.html" style="color:#103a2c;text-decoration:underline;font-weight:700">Read the full safety and liability disclaimer.</a></aside>'''


def with_safety_notice(html):
    """Render a visible notice into every public page, without JavaScript."""
    if NOTICE_ID in html:
        raise RuntimeError("Source contains the generated safety-notice marker")
    if not re.search(r"</body\s*>", html, flags=re.I):
        raise RuntimeError("Public HTML is missing a closing body")
    return re.sub(r"</body\s*>", lambda _: NOTICE + "</body>", html, count=1, flags=re.I)


def build():
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir()
    paths = list(ROOT.glob("*.html")) + [ROOT / "robots.txt", ROOT / "sitemap.xml"]
    paths += list((ROOT / "downloads").glob("*.html"))
    paths += [p for p in (ROOT / "assets").rglob("*") if p.is_file() and p.suffix.lower() in MEDIA]
    for src in paths:
        if src.is_symlink() or not src.is_file() or not src.resolve().is_relative_to(ROOT):
            raise RuntimeError("Refusing nonregular or external public asset")
        if src.stat().st_size > 25 * 1024 * 1024:
            raise RuntimeError("Public asset exceeds Cloudflare size limit")
        dest = OUT / src.relative_to(ROOT)
        dest.parent.mkdir(parents=True, exist_ok=True)
        if src.suffix.lower() == ".html":
            dest.write_text(with_safety_notice(src.read_text(encoding="utf-8")), encoding="utf-8")
        else:
            shutil.copyfile(src, dest)
    assert (OUT / "index.html").is_file()
    for file in OUT.rglob("*"):
        if file.is_file():
            assert file.suffix.lower() not in {".zip", ".pdf", ".xlsx", ".md", ".py", ".yml", ".json"}
            if file.suffix.lower() == ".html":
                assert file.read_text(encoding="utf-8").count('id="' + NOTICE_ID + '"') == 1
    print(f"Staged {len(paths)} public website files; no paid bundle or internal documents.")

if __name__ == "__main__":
    build()

