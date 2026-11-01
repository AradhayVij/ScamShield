#!/bin/zsh
# Usage: scripts/build_site.sh
# Wraps app/scamshield.html (the claude.ai version, which has no <html>/<head>) into a normal
# web page at index.html, so it opens by double-click and works on GitHub Pages.
cd "$(dirname "$0")/.."
{
  cat <<'HEAD'
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="description" content="Paste a suspicious SMS, WhatsApp or email in English or Hindi to see the scam risk, the tricks used, and a comic of what would happen if you fell for it.">
<style>
/* The same small reset claude.ai adds around the app */
:root { color-scheme: light; padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px); }
body { margin: 0; font: 14px system-ui, -apple-system, "Segoe UI", sans-serif; }
img { max-width: 100%; }
[hidden] { display: none !important; }
</style>
</head>
<body>
HEAD
  cat app/scamshield.html
  printf '\n</body>\n</html>\n'
} > index.html
echo "built index.html ($(wc -c < index.html) bytes)"
