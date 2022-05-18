from transformers import BertTokenizer, BertForMaskedLM, DistilBertTokenizer, DistilBertForMaskedLM
from transformers import TrainingArguments
from transformers import Trainer
from datasets import load_dataset
from transformers import DataCollatorForLanguageModeling

import sys

#BASE = "bert-base-multilingual-cased"
BASE = "distilbert-base-multilingual-cased"
DATA = "data/wikiqa"
DATASET = sys.argv[1] if len(sys.argv) > 1 else "token_lex_0.0"
print(f"Using {DATASET}")

OUTPUT_DIR = f"finetune_output_distilbert_tcs/{DATASET}"
DATASET_FILE = f"{DATASET}_cs.txt"
TRAIN_FILE = f"{DATASET}_cs_train.txt"
EVAL_FILE = f"{DATASET}_cs_eval.txt"

#tokenizer = BertTokenizer.from_pretrained(BASE)
#model = BertForMaskedLM.from_pretrained(BASE)

tokenizer = DistilBertTokenizer.from_pretrained(BASE)
model = DistilBertForMaskedLM.from_pretrained(BASE)

# https://huggingface.co/course/chapter3/3
# https://github.com/UKPLab/sentence-transformers/blob/master/examples/unsupervised_learning/MLM/train_mlm.py

# Defaults for TCS:
# Learning rate: 5e-5 (this is a default)
# batch masking probability: 0.15 (this is default in data collator)
# sequence length: 512 (not default, data collator)
# epochs: 2 (this is not default)
# batch size: 4 (this is not default, can't run this on current GPUs so using 2)
# gradient accumulation step: 10 (not default)


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

data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=True, pad_to_multiple_of=512)

training_args = TrainingArguments(
    output_dir=OUTPUT_DIR,
    overwrite_output_dir=True,
    num_train_epochs=4,
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    gradient_accumulation_steps=10,
    prediction_loss_only=True,
    save_strategy="epoch",
    learning_rate=5e-5
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
