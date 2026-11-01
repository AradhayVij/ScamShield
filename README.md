# ScamShield

A web app that checks a suspicious SMS, WhatsApp or email message, in English or Hindi, and says how likely it is to be a scam. It explains each trick it found in simple words, and shows a short comic of what would happen to Dadi or Dadaji if they believed the message.

- Live site: https://aradhayvij.github.io/ScamShield/
- Or download the repo and double-click `index.html`. No install or internet is needed except for the fonts.
- The "Ask Claude for a second opinion" button (AI check, screenshot reading) only appears in the claude.ai version of the page. Everywhere else the button stays hidden and the quick check works on its own.

## Folder layout

| Path | What it is |
|------|------------|
| `index.html` | The web page to open. Built from `app/scamshield.html` by `scripts/build_site.sh` |
| `app/scamshield.html` | The source of the app in one file: pattern rules, scoring, comics, English and Hindi text |
| `scripts/build_site.sh` | Rebuilds `index.html` after you edit `app/scamshield.html` |
| `data/scam_hum_india.csv` | Original dataset, unchanged (2,272 rows, columns `text,label`) |
| `data/labeled.json` | Our hand-checked labels, used by the scripts |
| `data/labeled.csv` | The same labels as a spreadsheet: `row, kind, scam_type, split, text` |
| `scripts/first_pass.py` | First rough sort of the "spam" rows by keyword, used only as a starting point for manual review |
| `scripts/labels.py` | Final labels (with the manual decisions written in it) and the tune/test split |
| `scripts/eval.sh` | Runs the app's quick check on the labelled data and prints the scores |
| `scripts/check_handwritten.sh` | Runs the quick check on our own English, Hindi and Hinglish test messages |
| `tests/handwritten_messages.js` | Those hand-written messages |
| `results/results.md` | Scores before and after improving the rules |

## Dataset

- Source: [carnageiron/scam-ham-india](https://huggingface.co/datasets/carnageiron/scam-ham-india) on Hugging Face, licence Apache-2.0. See `data/NOTICE.md`. The project's own code is MIT (`LICENSE`).
- The original only has two labels, `ham` and `spam`. Its "spam" mixes real scams with normal adverts (Airtel, Vi, Shoppers Stop) and official notices, so it cannot be used as is.
- We read all 895 "spam" rows by hand and gave each one a `kind`:
  - `scam`: 179 rows, each with a `scam_type`
  - `bulk`: 715 rows, genuine adverts and official notices (including warnings like "Beware of fake calls...")
  - `personal`: 1,378 rows, the original `ham` plus one personal message that was labelled spam by mistake
- Scam types found: prize 60, kyc 35, job_fee 31, wallet_bonus 11, debit_alert 9, task 7, otp 7, card_cvv 6, account_takeover 5, upi_pin 4, fake_loan 2, electricity 1, generic 1.
- Rows 2060 onwards are mostly synthetic scam templates. Rows before that are real SMS, with about 18 real scams in them (for example the "Rs.15,OOO credited t0 your wallet" messages).
- The dataset has no Hindi messages, and no digital arrest, family or parcel-fee scams.

## How the test was done

1. Messages that are near copies of each other (same text with different amounts, names or banks) were grouped, so a group is never split across tune and test.
2. The groups were split by a fixed hash: about two thirds `tune`, one third `test`.
3. The rules were improved by looking only at mistakes on `tune`.
4. The `test` part was run once at the end. Its numbers are the ones we report. We did not change the rules after looking at it.

A message counts as "likely scam" at 60% or more, and as "flagged" at 25% or more.

## Results (test part, 57 scams, 475 personal, 257 adverts and notices)

| | Before | After |
|---|---|---|
| Scams marked "likely scam" | 35.1% | 77.2% |
| Scams flagged at least "be careful" | 84.2% | 94.7% |
| Personal messages wrongly flagged | 1.5% | 1.1% |
| Adverts and notices wrongly flagged | 40.9% | 3.1% |

On the `tune` part the new rules reach 95.9%. The gap to 77.2% shows the rules partly fit the examples we studied, which is why the test number is the honest one.

The risk percentage is a score, not a calibrated probability. It is `1 - e^(-score/45)`, where the score adds up the weights of the signals found, plus bonuses for risky combinations (a lure such as a prize together with an ask such as "pay a fee"), minus points for signs of a normal advert or a safety warning.

## How to re-run

Run these from the `ScamShield` folder. The scripts use macOS's built-in JavaScript engine (`osascript`), so Node is not needed. Python is only needed to rebuild the labels.

```bash
scripts/eval.sh app/scamshield.html data/labeled.json test
```

```bash
scripts/eval.sh app/scamshield.html data/labeled.json tune details
```

```bash
scripts/check_handwritten.sh
```

```bash
~/miniconda3/envs/crazyformation/bin/python -I scripts/labels.py data/scam_hum_india.csv data/labeled.json
```

## Known limits

- Most scam messages in the dataset are written samples, so real-world accuracy may be lower than 77%.
- Hindi and Hinglish rules were only checked on 12 messages we wrote ourselves.
- It is a rule-based checker. New scam wording that no rule covers will be missed. The "Ask Claude" button gives a second opinion for those cases.

## Future scope

- Collect 100 to 200 real forwarded scam messages from family groups and Chakshu reports, especially in Hindi, and test on them.
- Train a small model once there is enough real labelled data, and compare it with the rules.
- WhatsApp or Telegram bot, so people can forward a message instead of opening a web page.
- Family guardian alert: when a high-risk message is checked, a trusted family member is notified.
