import logging
import transformers
from bert_score import BERTScorer
import os
from typing import List

transformers.tokenization_utils.logger.setLevel(logging.ERROR)
transformers.configuration_utils.logger.setLevel(logging.ERROR)
transformers.modeling_utils.logger.setLevel(logging.ERROR)


class BERTScoreEvaluator:
    def __init__(self, data, count, ref_file, comparison_files, out_file=None):
        self.data = data
        self.count = count
        self.out = out_file or f"{data}/out_bertscore_{count}.txt"
        self.comparison = sorted(comparison_files)
        self.scorer = BERTScorer(model_type="bert-base-multilingual-cased")
        self.refs = self.first_n_file(ref_file)

    def first_n_file(self, path: str) -> List[str]:
        out = []
        with open(f"{self.data}/{path}", "r", encoding="utf-8") as f:
            for _ in range(self.count):
                out.append(f.readline().strip())
        return out

    def score(self):
        with open(self.out, "w+", encoding="utf-8") as out_file:
            for fname in self.comparison:
                cands = self.first_n_file(fname)
                p, r, f = self.scorer.score(cands, self.refs)
                out_file.write(f"{fname}: Precision {p.mean()}, "
                               f"Recall {r.mean()}, F1 {f.mean()}\n")


if __name__ == "__main__":
    DATA = "../data/wikiqa"
    COUNT = 1000  # num sentences to use
    reference = "train-clean.txt"
    comp_files = [path for path in os.listdir(DATA) if path.endswith("cs.txt")]

    BSE = BERTScoreEvaluator(DATA, COUNT, reference, comp_files)
    BSE.score()


