## What is lemmatize (or lemmatization)?
Lemmatization is the NLP process of reducing a word to its base or dictionary form, called a lemma.

Example:

running → run

better → good

cars → car

It uses vocabulary + grammar rules, not just chopping off endings.

1️⃣ Testing a lemmatizer
Checking whether your NLP pipeline correctly converts words to their lemmas.

Example in spaCy:

python
```
import spacy
nlp = spacy.load("en_core_web_sm")

doc = nlp("The children are running faster than their parents.")
for token in doc:
    print(token.text, "→", token.lemma_)
```

2️⃣ Evaluating lemmatization accuracy
Used in NLP research or model evaluation:

Compare predicted lemmas vs. gold-standard lemmas

Compute accuracy or error rate

3️⃣ A simple exercise or quiz
Sometimes tutorials call it a “lemmatization text” meaning:

“Try lemmatizing these words and check the output.”

⭐ Why lemmatization matters
It helps with:

Text normalization

Search relevance

Chatbot understanding

Intent classification

Document parsing

AI agent preprocessing