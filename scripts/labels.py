"""Final hand-checked labels for scam-ham-india.

Every 'spam' row was read by hand. Original 'spam' mixes real promotions with scams, so it is split into:
  kind = personal (original ham) | bulk (genuine promotions and official notices) | scam
Scams also get a scam type. Rows 2060+ are synthetic scam templates; rows before that are real SMS.
The split keeps near-duplicates together (IndoSmish warns that duplicates across splits inflate accuracy).
"""
import csv, re, json, sys, hashlib, collections

rows = list(csv.DictReader(open(sys.argv[1], encoding="utf-8")))

# Real scams found among the early (real) rows, by row number.
EARLY_SCAMS = {
    837: "task", 877: "task", 1261: "task", 1671: "task", 1915: "task",
    1685: "wallet_bonus", 2025: "wallet_bonus", 2030: "wallet_bonus", 2037: "wallet_bonus", 2039: "wallet_bonus",
    2043: "wallet_bonus", 2052: "wallet_bonus", 2054: "wallet_bonus", 2056: "wallet_bonus",
    2032: "prize", 2033: "prize", 2059: "fake_loan", 2040: "generic",
}
EARLY_GENUINE_PERSONAL = {1345}  # a personal message mislabelled as spam
LATE_BULK = {2061}  # a genuine loan promotion inside the synthetic block
FIXED_TYPES = {2060: "fake_loan", 2186: "job_fee", 2193: "task"}

def synthetic_type(t):
    s = t.lower()
    if re.search(r"upi pin", s): return "electricity" if "electricity" in s else "upi_pin"
    if re.search(r"\b(job|hiring|candidate|candidature|interview|recruitment|selected for the position|role|internship|salary)\b", s):
        return "task" if re.search(r"youtube|tasks|telegram|daily", s) else "job_fee"
    if re.search(r"loan", s): return "fake_loan"
    if re.search(r"wallet", s) and re.search(r"bonus|cashback|credited", s) and "kyc" not in s: return "wallet_bonus"
    if re.search(r"won|winner|lottery|lucky|jackpot|prize|giveaway|bonanza", s): return "prize"
    if re.search(r"cvv|card number", s): return "card_cvv"
    if re.search(r"whatsapp account|instagram|netflix|google account|6 digit code|ported", s): return "account_takeover"
    if re.search(r"debited|charged|renewal", s): return "debit_alert"
    if re.search(r"kyc|aadhaar|aadhar|pan", s): return "kyc"
    if re.search(r"otp|login|logging|net banking", s): return "otp"
    return "generic"

out = []
for i, r in enumerate(rows):
    t = r["text"]
    if r["label"] == "ham" or i in EARLY_GENUINE_PERSONAL: kind, typ = "personal", ""
    elif i in LATE_BULK: kind, typ = "bulk", ""
    elif i >= 2060: kind, typ = "scam", FIXED_TYPES.get(i) or synthetic_type(t)
    elif i in EARLY_SCAMS: kind, typ = "scam", EARLY_SCAMS[i]
    else: kind, typ = "bulk", ""
    # Near-duplicate groups stay in one split: numbers and links removed, lowercased.
    key = re.sub(r"https?://\S+|\b\S+\.(in|ly|co|me|to|im|cc)/\S*|\d[\d,.]*", "", t.lower())
    key = re.sub(r"\b(sbi|hdfc|icici|axis bank|kotak mahindra|punjab national bank|bank of baroda|paytm|gpay|phonepe|bhim upi|amazon pay|amit|priya|vikram|sneha|infosys|tcs|hcl|wipro|flipkart|tata group|reliance)\b", "X", key)
    key = re.sub(r"\W+", " ", key).strip()[:70]
    h = int(hashlib.sha1(key.encode()).hexdigest(), 16) % 100
    out.append({"i": i, "text": t, "kind": kind, "type": typ, "split": "test" if h < 35 else "tune", "group": key})

json.dump(out, open(sys.argv[2], "w"), ensure_ascii=False, indent=0)
C = collections.Counter
print("kinds:", C(o["kind"] for o in out))
print("scam types:", C(o["type"] for o in out if o["kind"] == "scam").most_common())
print("split x kind:", C((o["split"], o["kind"]) for o in out))
print("groups:", len({o["group"] for o in out}), " scam template groups:", len({o["group"] for o in out if o["kind"]=="scam"}))
