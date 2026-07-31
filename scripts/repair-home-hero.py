#!/usr/bin/env python3
"""Restore Lancaster's relabeled hero copy above the captured hero image."""

from pathlib import Path
import re
import sys


public = Path(sys.argv[1]) / "public"
marker = "rr-lancaster-home-hero"
style = f"""<style id="{marker}">
#comp-m28o2bbb{{position:relative!important;min-height:650px!important;overflow:hidden!important}}
#comp-m28o2bbb:after{{
  content:""!important;position:absolute!important;inset:0!important;z-index:1!important;
  background:linear-gradient(90deg,rgba(0,0,0,.66),rgba(0,0,0,.16))!important;
  pointer-events:none!important
}}
#comp-m28o2bbb .comp-m28o2bbb-container{{
  position:absolute!important;inset:0!important;z-index:3!important;
  display:flex!important;align-items:center!important;width:100%!important;
  max-width:none!important;height:100%!important;visibility:visible!important;
  opacity:1!important;transform:none!important
}}
#comp-m28o2bbb #comp-m46dd4a6{{
  position:relative!important;inset:auto!important;display:block!important;
  width:min(1120px,calc(100% - 64px))!important;height:auto!important;
  margin:0 auto!important;visibility:visible!important;opacity:1!important;
  transform:none!important
}}
#comp-m28o2bbb #comp-m46dd4a6-container,
#comp-m28o2bbb #comp-m46cf2tj,
#comp-m28o2bbb #comp-m46d8rf8{{
  position:relative!important;inset:auto!important;display:block!important;
  width:100%!important;height:auto!important;visibility:visible!important;
  opacity:1!important;transform:none!important
}}
#comp-m28o2bbb #comp-m46cf2tj h1{{
  display:block!important;width:min(900px,100%)!important;margin:0 0 22px!important;
  color:#fff!important;font-size:clamp(44px,6vw,82px)!important;line-height:1.02!important;
  text-shadow:0 3px 24px rgba(0,0,0,.65)!important;visibility:visible!important;
  opacity:1!important;transform:none!important
}}
#comp-m28o2bbb #comp-m46d8rf8 h2{{
  display:block!important;width:min(720px,100%)!important;margin:0!important;
  color:#fff!important;font-size:clamp(18px,2vw,28px)!important;line-height:1.35!important;
  text-shadow:0 2px 18px rgba(0,0,0,.65)!important;visibility:visible!important;
  opacity:1!important;transform:none!important
}}
@media(max-width:760px){{
  #comp-m28o2bbb{{min-height:580px!important}}
  #comp-m28o2bbb #comp-m46dd4a6{{width:calc(100% - 36px)!important}}
  #comp-m28o2bbb #comp-m46cf2tj h1{{font-size:clamp(36px,12vw,54px)!important}}
}}
</style>"""

changed = 0
for path in (public / "home.html", public / "index.html"):
    if not path.is_file():
        continue
    original = path.read_text(errors="ignore")
    updated = re.sub(
        rf'<style id="{marker}">.*?</style>',
        "",
        original,
        flags=re.S,
    )
    updated = updated.replace("</head>", style + "</head>", 1)
    if updated != original:
        path.write_text(updated)
        changed += 1

print(f"Lancaster home hero repaired: pages={changed}")
