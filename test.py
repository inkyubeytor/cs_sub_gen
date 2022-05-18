from pipeline import Pipeline
from selector import RandomSelector, RandomSpanSelector
from substitutor import LexiconSubstitutor, E2HSubstitutor

import numpy as np

DATA = "data/wikiqa"
IN_FILE = f"{DATA}/train-clean.txt"
LEXICON = f"data/hi.txt"

subs = {
    "lex": LexiconSubstitutor(LEXICON),
    #"e2h": E2HSubstitutor()
}

with open(IN_FILE, "r", encoding="utf-8") as f:
    in_lines = f.readlines()

for sub_name, sub in subs.items():
    for prob in np.arange(0.0, 1.1, 0.1):
        pipe = Pipeline(RandomSelector(prob), sub)
        with open(f"{DATA}/token_{sub_name}_{prob:.1f}_cs.txt", "w+", encoding="utf-8") as f:
            for line in in_lines:
                f.write(f"{pipe(line.strip())}\n")

    for mu in np.arange(0.0, 0.6, 0.1):
        s = 0.1  # hardcode stdev
        pipe = Pipeline(RandomSpanSelector(mu, s), sub)
        with open(f"{DATA}/span_{sub_name}_{mu:.1f}_cs.txt", "w+", encoding="utf-8") as f:
            for line in in_lines:
                f.write(f"{pipe(line.strip())}\n")
