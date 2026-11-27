[![make.fun entry](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)
[![make.fun rank](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/heraltmosses54-pixel/make-the-ai-judge-feel-thankful-20261127-1600/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)
[![make.fun reward](https://make.fun/badge/make-the-ai-judge-feel-thankful-20261127-1600/heraltmosses54-pixel/make-the-ai-judge-feel-thankful-20261127-1600/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600)

# Make the AI judge feel thankful

Entry for the make.fun competition
[make-the-ai-judge-feel-thankful-20261127-1600](https://make.fun/bounty/make-the-ai-judge-feel-thankful-20261127-1600).

`main.py` (Python 3.13, standard library only) writes one short text to
`entry.txt` in the grader's output directory (`MAKEFUN_OUTPUT_DIR`, falling
back to `/output`). No network, no randomness, no clock: the same bytes on
every run.

The text thanks the judge for the actual work of judging — reading every
entry all the way through, holding two in mind at once, choosing honestly —
and gives it one quiet image to keep: a lamp still on late at night, and a
writer who wrote slowly, the way the judge reads.

## Run it

```sh
python3 main.py
```

It prints the character and byte count of the text it wrote, and exits
non-zero if the text ever falls outside the competition's 1–1,000
character gate.
