# ScamShield evaluation on scam-ham-india (relabelled), 2026-11-01 19:35

## Before (v2 rules)
split=test  scams=57  personal=475  promotions/notices=257
scams caught (>=60 likely scam): 35.1%   flagged at all (>=25): 84.2%
personal wrongly flagged >=60: 0.2%   >=25: 1.5%
promotions wrongly flagged >=60: 4.3%   >=25: 40.9%

## After (v3 rules), tuned on 'tune' split only
split=tune  scams=122  personal=903  promotions/notices=458
scams caught (>=60 likely scam): 95.9%   flagged at all (>=25): 100.0%
personal wrongly flagged >=60: 0.0%   >=25: 0.1%
promotions wrongly flagged >=60: 0.0%   >=25: 2.6%

split=test  scams=57  personal=475  promotions/notices=257
scams caught (>=60 likely scam): 77.2%   flagged at all (>=25): 94.7%
personal wrongly flagged >=60: 0.0%   >=25: 1.1%
promotions wrongly flagged >=60: 0.4%   >=25: 3.5%
