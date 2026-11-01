# Data notice

`scam_hum_india.csv` is the dataset **scam-ham-india** by carnageiron on Hugging Face
(https://huggingface.co/datasets/carnageiron/scam-ham-india), licensed under the
Apache License 2.0 (https://www.apache.org/licenses/LICENSE-2.0). It is included here unchanged.

`labeled.json` and `labeled.csv` are derived from it. Changes made: every row marked `spam`
was read by hand and relabelled as `scam` (with a scam type) or `bulk` (genuine adverts and
notices); one personal message was moved from `spam` to `personal`; a tune/test split was added.
See `scripts/labels.py` for every decision.

The project's own code is under the MIT licence in `LICENSE`. The MIT licence does not apply
to the dataset files.
