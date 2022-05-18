from typing import List
import os

from autocorrect import Speller


class CMIEvaluator:
    def __init__(self, data, count, comparison_files, out_file=None):
        self.data = data
        self.count = count
        self.out = out_file or f"{data}/out_cmi_{count}.txt"
        self.comparison = sorted(comparison_files)
        self.spell = Speller(fast=True)

    def first_n_file(self, path: str) -> List[str]:
        out = []
        with open(f"{self.data}/{path}", "r", encoding="utf-8") as f:
            for _ in range(self.count):
                out.append(f.readline().strip())
        return out

    def score(self):
        with open(self.out, "w+", encoding="utf-8") as out_file:
            for fname in self.comparison:
                cands = [c for c in self.first_n_file(fname) if len(c.split())]
                cmi_sum = 0
                for cand in cands:
                    tokens = cand.split()
                    en = sum(self.spell(t) == t and t.isascii() for t in tokens)
                    hi = len(tokens) - en
                    cmi_sum += min(en, hi) / len(tokens)
                if len(cands):
                    cmi = cmi_sum / len(cands)
                else:
                    cmi = None
                out_file.write(f"{fname} average cmi: {cmi}\n")


if __name__ == "__main__":
    DATA = "../data/wikiqa"
    COUNT = 1000  # num sentences to use
    comp_files = [path for path in os.listdir(DATA) if path.endswith("cs.txt")]

    CE = CMIEvaluator(DATA, COUNT, comp_files)
    CE.score()
