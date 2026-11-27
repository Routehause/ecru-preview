"""Inline fonts and images into a single shareable file: smash-club-preview.html"""
import base64, pathlib, re

here = pathlib.Path(__file__).parent
html = (here / "index.html").read_text()


def uri(path, mime):
    return "data:%s;base64,%s" % (mime, base64.b64encode((here / path).read_bytes()).decode())


html = re.sub(r"url\((fonts/[\w.-]+\.woff2)\)", lambda m: "url(%s)" % uri(m.group(1), "font/woff2"), html)
html = re.sub(r'src="(img/[\w.-]+\.jpg)"', lambda m: 'src="%s"' % uri(m.group(1), "image/jpeg"), html)
out = here / "smash-club-preview.html"
out.write_text(html)
print(out, "%.0f KB" % (out.stat().st_size / 1024))
