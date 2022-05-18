from typing import List
import os
from nltk.translate.bleu_score import corpus_bleu

class BLEUEvaluator:
    def __init__(self, data, count, comparison_files, out_file=None):
        self.data = data
        self.count = count
        self.out = out_file or f"{data}/out_bleuscore_{count}.txt"
        self.comparison = sorted(comparison_files)

    def first_n_file(self, path: str) -> List[str]:
        out = []
        with open(f"{self.data}/{path}", "r", encoding="utf-8") as f:
            for _ in range(self.count):
                out.append(f.readline().strip())
        return out

    def score(self):
        with open(self.out, "w+", encoding="utf-8") as out_file:
            refs = [[r] for r in self.first_n_file("train-clean.txt")]
            for fname in self.comparison:
                cands = [c for c in self.first_n_file(fname) if len(c.split())]
                bleu = corpus_bleu(refs, cands)
                out_file.write(f"{fname} BLEU-4: {bleu}\n")


if __name__ == "__main__":
    DATA = "../data/wikiqa"
    COUNT = 1000  # num sentences to use
    comp_files = [path for path in os.listdir(DATA) if path.endswith("cs.txt")]

    CE = BLEUEvaluator(DATA, COUNT, comp_files)
    CE.score()
