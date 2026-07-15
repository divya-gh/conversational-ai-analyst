## what is spacy?
spaCy is an open‑source Natural Language Processing (NLP) library for Python, designed to be fast, production‑ready, and developer‑friendly. It’s widely used in conversational AI, data extraction, and AI agent workflows — so it fits perfectly with the kind of systems you build.

⭐ Core idea
spaCy helps machines understand human language by providing tools to process text and extract meaning.

🧠 What spaCy does
It provides a full NLP pipeline with components like:

Tokenization — breaking text into words and symbols

Part‑of‑Speech tagging — identifying nouns, verbs, adjectives

Dependency parsing — understanding grammatical structure

Named Entity Recognition (NER) — detecting people, places, dates

Sentence segmentation — splitting text into sentences

Word vectors — numerical meaning representations

Text classification — labeling documents

📦 Why developers love spaCy
Fast — built in Cython, optimized for production

Accurate — strong statistical models

Modular — easy to customize pipelines

Integrates well — works with transformers, LangChain, LangGraph, FastAPI, etc.

Great for enterprise — stable, predictable behavior

🔧 Example usage
python
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Divya is building AI agents using LangGraph.")

for ent in doc.ents:
    print(ent.text, ent.label_)
🧩 When to use spaCy
Use it when you need:

Conversational AI preprocessing

Resume or document parsing

Entity extraction

Rule-based + statistical NLP

Lightweight pipelines without heavy transformer overhead

--------------------------------------------------------------------

## what is a spacy model?
A spaCy model is a pre‑built package of linguistic knowledge that spaCy uses to analyze text. Think of it as the “brain” that lets spaCy understand language.

⭐ Quick definition
A spaCy model is a trained statistical + rule‑based pipeline that can perform tasks like tokenization, part‑of‑speech tagging, named entity recognition, dependency parsing, text classification, and more.

🧠 What’s inside a spaCy model?
Each model typically includes:

Tokenizer — splits text into words, punctuation, etc.

Tagger — assigns part‑of‑speech tags (NOUN, VERB, ADJ…).

Parser — identifies grammatical relationships between words.

NER component — finds entities like PERSON, ORG, DATE.

Word vectors (optional) — numerical representations of meaning.

Lexical rules — language‑specific rules for normalization.

📦 Examples of spaCy models
en_core_web_sm — small English model (fast, lightweight).

en_core_web_md — medium model with word vectors.

en_core_web_lg — large model with more vectors and accuracy.

xx_ent_wiki_sm — multilingual NER model.

🔧 How you load a spaCy model
python
import spacy
nlp = spacy.load("en_core_web_sm")

doc = nlp("Divya is building AI agents using LangGraph.")
for ent in doc.ents:
    print(ent.text, ent.label_)
🧩 Why spaCy models matter
They let you build:

Conversational AI

Chatbots

Data extraction pipelines

Resume parsers

Document classifiers

NLP‑powered agents (like the ones you build with LangGraph)