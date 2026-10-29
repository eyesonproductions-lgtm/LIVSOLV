"""Stage only public website assets. Never publish repository source or paid files."""
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "public"
MEDIA = {".png", ".jpg", ".jpeg", ".webp", ".svg", ".gif", ".ico", ".css", ".js", ".woff", ".woff2", ".ttf"}


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
        shutil.copyfile(src, dest)
    assert (OUT / "index.html").is_file()
    for file in OUT.rglob("*"):
        if file.is_file():
            assert file.suffix.lower() not in {".zip", ".pdf", ".xlsx", ".md", ".py", ".yml", ".json"}
    print(f"Staged {len(paths)} public website files; no paid bundle or internal documents.")

if __name__ == "__main__":
    build()
