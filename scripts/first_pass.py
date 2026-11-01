"""First-pass suggestions for sorting the dataset's 'spam' rows. Every row is then reviewed by hand."""
import csv, re, sys, json
rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8")))
CATS = [  # order matters: first match wins
 ("arrest",   r"\b(cbi|police|arrest|narcotics|customs|money laundering|court|warrant|cyber cell)\b"),
 ("upi_pin",  r"\b(upi pin|enter (your )?pin|collect request|scan (the )?qr)\b"),
 ("remote",   r"\b(anydesk|teamviewer|quicksupport|\.apk|screen ?share)\b"),
 ("kyc",      r"\b(kyc|pan card|aadhaar|aadhar)\b"),
 ("power",    r"\belectric|power (supply|cut)|light bill\b"),
 ("parcel",   r"\b(parcel|courier|shipment|package|delivery)\b"),
 ("job",      r"\b(part[- ]?time|work from home|daily salary|job|hiring|recruit|earn (rs|₹)|per day|daily income)\b"),
 ("investment", r"\b(invest|trading|stock|crypto|bitcoin|returns|double)\b"),
 ("loan",     r"\b(loan)\b"),
 ("refund",   r"\b(refund|income tax|tax return)\b"),
 ("prize",    r"\b(won|winner|lottery|lucky draw|jackpot|prize|reward|gift|bonus|cash points)\b"),
 ("family",   r"\b(mum|mom|dad|new number|lost my phone)\b"),
 ("bank_otp", r"\b(otp|cvv|blocked|suspend|debited|card|account|login|password|verify)\b"),
 ("telecom",  r"\b(sim|recharge|data|pack|airtel|vi\b|jio|bsnl|plan|missed call|calling at)\b"),
]
out = []
for i, r in enumerate(rows):
    if r["label"] == "ham": continue
    t = r["text"]
    cat = next((c for c, p in CATS if re.search(p, t, re.I)), "other")
    out.append({"i": i, "cat": cat, "text": t})
json.dump(out, open(sys.argv[2], "w"), ensure_ascii=False, indent=0)
from collections import Counter; print(Counter(o["cat"] for o in out))
