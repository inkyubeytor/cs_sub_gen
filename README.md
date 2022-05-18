# Substitutive Generation
The environment for this process can be built from `cs_sub_gen.yml`.

## Data
The dataset used for substitutive generation is the WikiQA dataset.

## Generation
To perform generation, construct a pipeline out of a selector and a substitutor.
Then, apply this pipeline to each line of the dataset.
Examples of such generation are seen in the file `test.py`.

# Finetuning BERT models
The environment to use for finetuning BERT models is found in `finetune_bert.yml`.
To finetune BERT models on data, use `finetune.py`.
This uses HuggingFace training scripts.
All training parameters are modified directly in this file.

# Evaluation
All evaluation models are implemented as subclasses of a base evaluator class.
The 3 evaluations implemented are Code-Mixing Index (`cmi.yml`), BERTscore (`bertscore.yml`), and Self-BLEUscore (`bleuscore.yml`).
Each evaluation requires its own environment to be activated.
They are all found in the `evaluator/` directory.

