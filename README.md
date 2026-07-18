# Ukrainian Morphological Rules Engine
A deterministic, rule-based computational linguistics engine designed to decode Ukrainian grammatical cases using structural string mutations instead of static dictionary lookups.

## Core Architecture
This project treats Ukrainian nouns as objects passing through a conditional validation pipeline, extracting grammatical traits (Gender, Stem Type) directly from the input token's shape.
