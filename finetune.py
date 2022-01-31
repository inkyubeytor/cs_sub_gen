from transformers import BertTokenizer, BertForMaskedLM
from transformers import TrainingArguments
from transformers import Trainer
from datasets import load_dataset
from transformers import DataCollatorForLanguageModeling

BASE = "bert-base-multilingual-cased"
DATA = "data/wikiqa"
DATASET = "token_lex_0.7"

OUTPUT_DIR = f"finetune_output/{DATASET}"
DATASET_FILE = f"{DATASET}_cs.txt"
TRAIN_FILE = f"{DATASET}_cs_train.txt"
EVAL_FILE = f"{DATASET}_cs_eval.txt"

tokenizer = BertTokenizer.from_pretrained(BASE)
model = BertForMaskedLM.from_pretrained(BASE)

# https://huggingface.co/course/chapter3/3
# https://github.com/UKPLab/sentence-transformers/blob/master/examples/unsupervised_learning/MLM/train_mlm.py

# Defaults for TCS:
# Learning rate: 5e-5
# batch masking probability: 0.15
# sequence length: 512
# epochs: 2
# batch size: 4
# gradient accumulation step: 10
# TODO: use seeds


def data(fname):
    return f"{DATA}/{fname}"


with open(data(DATASET_FILE), encoding="utf-8") as f:
    all_data = f.readlines()
    train_data = all_data[:-2000]
    eval_data = all_data[-2000:]
    with open(data(TRAIN_FILE), "w+", encoding="utf-8") as g:
        g.writelines(train_data)
    with open(data(EVAL_FILE), "w+", encoding="utf-8") as g:
        g.writelines(eval_data)


raw_datasets = load_dataset('text', data_files={
    'train': data(TRAIN_FILE),
    'eval': data(EVAL_FILE)
})


def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)


tokenized_datasets = raw_datasets.map(tokenize_function, batched=True)
full_train_dataset = tokenized_datasets["train"]
full_eval_dataset = tokenized_datasets["eval"]

data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=True)

training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    overwrite_output_dir=True,
    per_device_train_batch_size=1,
    per_device_eval_batch_size=1,
    prediction_loss_only=True,
    save_strategy="epoch",
)

print(training_args)

trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=full_train_dataset,
    eval_dataset=full_eval_dataset
)

trainer.train()
