from typing import List
import os
from nltk.translate.bleu_score import corpus_bleu, SmoothingFunction
import random


class BLEUEvaluator:
    def __init__(self, data, count, comparison_files, out_file=None, rounds=1):
        self.data = data
        self.count = count
        self.out = out_file or f"{data}/out_selfbleu_{count}.txt"
        self.comparison = sorted(comparison_files)
        self.rounds = rounds

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
                refs = cands.copy()
                sum_score = 0
                for _ in range(self.rounds):
                    random.shuffle(cands)
                    sum_score += corpus_bleu(refs, cands, weights=(1./3., 1./3., 1./3.), smoothing_function=SmoothingFunction().method1)
                bleu = sum_score / self.rounds
                out_file.write(f"{fname} Self-BLEU-3: {bleu}\n")


if __name__ == "__main__":
    DATA = "../data/wikiqa"
    COUNT = 1000  # num sentences to use
    comp_files = [path for path in os.listdir(DATA) if path.endswith("cs.txt")]

    CE = BLEUEvaluator(DATA, COUNT, comp_files)
    CE.score()
