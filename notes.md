# Methods

## Tokenization
 * split on space
 * TODO: spacy (maybe en only)

## Selection of unit to substitute
 * random words
 * random span
 * TODO: unit in parse tree
   * spacy parsing?

## Translation method for substitution
 * lexicon
   * given lexicon
   * TODO: supervised alignment (seeded) lexicon
   * TODO: unsupervised alignment lexicon
 * TODO: parallel corpus
   * needs method of aligning parts of parallel corpus
 * TODO: translation (covers pseudo parallel case)
   * moses?