#!/bin/zsh
# Usage: scripts/check_handwritten.sh
# Runs the page's quick check on the app's own examples and on tests/handwritten_messages.js
# (English, Hindi and Hinglish messages written for this project). Prints risk, comic story and signals.
cd "$(dirname "$0")/.."
ENGINE=$(sed -n '/<script>/,/<\/script>/p' app/scamshield.html | sed '1d;$d' | sed '/^\/\/ ---------- Comic: drawn scenes/,$d')
OUT=$(mktemp -t sscheck).js
{ printf '%s\n' "$ENGINE"; cat tests/handwritten_messages.js; } > "$OUT"
osascript -l JavaScript "$OUT"
