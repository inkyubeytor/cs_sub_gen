import logging
import transformers
from bert_score import BERTScorer
import os
from typing import List

transformers.tokenization_utils.logger.setLevel(logging.ERROR)
transformers.configuration_utils.logger.setLevel(logging.ERROR)
transformers.modeling_utils.logger.setLevel(logging.ERROR)


DATA = "data/wikiqa"
COUNT = 1000  # num sentences to use
OUT = f"{DATA}/out_{COUNT}.txt"

reference = "train-clean.txt"
comparison = sorted([path for path in os.listdir(DATA) if path.endswith("cs.txt")])


def first_n_file(n: int, path: str) -> List[str]:
    out = []
    with open(f"{DATA}/{path}", "r", encoding="utf-8") as f:
        for _ in range(n):
            out.append(f.readline().strip())
    return out


scorer = BERTScorer(model_type="bert-base-multilingual-cased")

refs = first_n_file(COUNT, reference)

with open(OUT, "w+", encoding="utf-8") as out_file:
    for fname in comparison:
        cands = first_n_file(COUNT, fname)
        p, r, f = scorer.score(cands, refs)
        out_file.write(f"{fname}: Precision {p.mean()}, "
                       f"Recall {r.mean()}, F1 {f.mean()}\n")
