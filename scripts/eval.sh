#!/bin/zsh
# Usage: eval.sh <page.html> <labeled.json> <split: tune|test> [details]
# Pulls analyze() out of the page and runs it on every labelled message with macOS's JavaScript engine.
PAGE=$1; DATA=$2; SPLIT=$3; DETAILS=${4:-}
ENGINE=$(sed -n '/<script>/,/<\/script>/p' "$PAGE" | sed '1d;$d' | sed '/^\/\/ ---------- Comic: drawn scenes/,$d')
OUT=$(mktemp -t sseval).js
{
  printf '%s\n' "$ENGINE"
  printf 'const DATA = %s;\n' "$(cat "$DATA")"
  cat <<JS
const rows = DATA.filter(o => o.split === "$SPLIT");
const by = {};
const lines = [];
for (const o of rows) {
  const r = analyze(o.text);
  const b = by[o.kind] ??= { n: 0, ge25: 0, ge60: 0 };
  b.n++; if (r.p >= 25) b.ge25++; if (r.p >= 60) b.ge60++;
  if ("$DETAILS") {
    const wrong = (o.kind === "scam" && r.p < 60) || (o.kind !== "scam" && r.p >= 25);
    if (wrong) lines.push([o.kind, o.type || "-", r.p, o.i, r.hits.map(h => h.rule.id).join(","), o.text.slice(0, 95)].join(" | "));
  }
}
const pct = (a, n) => n ? (100 * a / n).toFixed(1) + "%" : "-";
const s = by.scam || { n: 0 }, p = by.personal || { n: 0 }, k = by.bulk || { n: 0 };
[ "split=$SPLIT  scams=" + s.n + "  personal=" + p.n + "  promotions/notices=" + k.n,
  "scams caught (>=60 likely scam): " + pct(s.ge60, s.n) + "   flagged at all (>=25): " + pct(s.ge25, s.n),
  "personal wrongly flagged >=60: " + pct(p.ge60, p.n) + "   >=25: " + pct(p.ge25, p.n),
  "promotions wrongly flagged >=60: " + pct(k.ge60, k.n) + "   >=25: " + pct(k.ge25, k.n),
  ...lines ].join("\n")
JS
} > "$OUT"
osascript -l JavaScript "$OUT"
