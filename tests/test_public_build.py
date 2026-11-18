"""Check universal notices and public/private file boundaries."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

MODULE_PATH = Path(__file__).resolve().parents[1] / 'ops/build_public.py'
spec = importlib.util.spec_from_file_location('build_public', MODULE_PATH)
build_public = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build_public)

class PublicBuildTests(unittest.TestCase):
    def test_all_public_html_gets_notice_without_changing_source(self):
        original_root, original_out = build_public.ROOT, build_public.OUT
        try:
            with tempfile.TemporaryDirectory() as temp:
                root = Path(temp)
                build_public.ROOT, build_public.OUT = root, root / 'public'
                for name in ['index.html', 'future-guide.html', 'downloads/checklist.html']:
                    target = root / name
                    target.parent.mkdir(parents=True, exist_ok=True)
                    target.write_text('<!doctype html><html><body>Useful content</body></html>')
                for name in ['robots.txt', 'sitemap.xml']:
                    (root / name).write_text('unchanged')
                (root / 'assets').mkdir()
                (root / 'assets/photo.svg').write_text('<svg/>')
                for name in ['paid.zip', 'paid.pdf', 'paid.xlsx', 'internal.md']:
                    (root / 'assets' / name).write_text('private')
                build_public.build()
                for name in ['index.html', 'future-guide.html', 'downloads/checklist.html']:
                    self.assertNotIn(build_public.NOTICE_ID, (root / name).read_text())
                    rendered = (root / 'public' / name).read_text()
                    self.assertEqual(rendered.count('id="livsolv-safety-notice"'), 1)
                    self.assertIn('href="/safety-disclaimer.html"', rendered)
                    self.assertIn('Useful content', rendered)
                self.assertEqual(sorted(p.name for p in (root / 'public/assets').iterdir()), ['photo.svg'])
                self.assertEqual((root / 'public/robots.txt').read_text(), 'unchanged')
        finally:
            build_public.ROOT, build_public.OUT = original_root, original_out

    def test_missing_body_fails_instead_of_silently_omitting_notice(self):
        with self.assertRaises(RuntimeError):
            build_public.with_safety_notice('<html>broken</html>')

    def test_duplicate_source_notice_fails(self):
        with self.assertRaises(RuntimeError):
            build_public.with_safety_notice('<body id="livsolv-safety-notice"></body>')

if __name__ == '__main__':
    unittest.main()
