with open("WikiQA-train.txt", encoding="utf-8") as f:
    d = f.readlines()

d = [s.split("\t", maxsplit=1)[1][:-3] + "\n" for s in d]

with open("train-clean.txt", "w+", encoding="utf-8") as f:
    f.writelines(d)
