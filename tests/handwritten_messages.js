const extra = [
 "Hey, are we still meeting for lunch tomorrow at 1?",
 "Your SBI a/c XX1234 debited Rs 500 on 01-11-26. Not you? Call 1800 1234 (toll free).",
 "Rs 2,000 received in your account from Ramesh via UPI. -PhonePe",
 "बधाई हो! आपने KBC लकी ड्रा में 25 लाख रुपये जीते हैं। इनाम पाने के लिए 12500 रुपये फीस जमा करें।",
 "मैं सीबीआई से बोल रहा हूँ। आपके नाम पर मनी लॉन्ड्रिंग का केस है। आपको गिरफ्तार किया जाएगा। परिवार को मत बताना।",
 "Sir aapka khata band ho jayega, turant OTP batao",
 "मम्मी यह मेरा नया नंबर है, फोन खो गया। जल्दी 5000 रुपये भेज दो, बिल भरना है।",
 "बेटा कल शाम को खाने पर आ रहे हो ना?",
 "आपके खाते में 2,000 रुपये जमा हुए हैं। - एसबीआई",
];
[...EXAMPLES.map(e=>[e.label.en,e.text]), ...extra.map(t=>[t.slice(0,30),t])].map(([l,t])=>{const r=analyze(t);return String(r.p).padStart(3)+"  "+l+"  ["+r.story+"] "+r.hits.map(h=>h.rule.id).join(",")+" "+r.good.map(g=>"+"+g.name.en).join(",")}).join("\n")
