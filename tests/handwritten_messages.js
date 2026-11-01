const extra = [
 "Dear vehicle owner, an e-challan of Rs 1,500 has been issued against your vehicle MH12AB4521 for over-speeding. Pay within 24 hours to avoid court case and licence suspension: https://echallan-parivahan.xyz/pay",
 "प्रिय वाहन मालिक, आपकी गाड़ी पर ₹1,500 का ई-चालान जारी हुआ है। कोर्ट केस से बचने के लिए 24 घंटे में भुगतान करें: https://echallan-parivahan.xyz/pay",
 "Priya grahak, aapka Indane gas connection aaj raat band ho jayega kyunki aapka KYC pending hai. Turant 9876501234 par call karein.",
 "Amazon: Your refund of Rs 2,349 for order #402-8812 could not be processed. Click https://amzn-refund-help.top/claim and enter your card details to receive it today.",
 "प्रिय उपभोक्ता, आपका बिजली कनेक्शन आज रात 9:30 बजे काट दिया जाएगा। पिछला बिल अपडेट नहीं हुआ है। तुरंत बिजली अधिकारी को 9123409876 पर कॉल करें।",
 "Your challan of Rs 500 for signal jumping is paid. Receipt: echallan.parivahan.gov.in/receipt/88231",
 "Bhai mera account block ho gaya, password reset karna padega",
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
