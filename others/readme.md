# 📁 Others: NLP Fundamentals & Miscellaneous Implementations

This directory contains from-scratch implementations of fundamental Natural Language Processing (NLP) algorithms, text processing pipelines, and miscellaneous utility scripts. 

The primary goal of this folder is educational: by building these algorithms from scratch in Python, we can deeply understand the underlying mathematics, logic, and mechanics of text processing without relying on high-level abstractions.

## 📂 Directory Structure

### 📄 Root Files
* **`preprocess_pipeline.py`** & **`preprocess_pipeline.ipynb`**: A comprehensive demonstration of an end-to-end text preprocessing pipeline. Includes both a standard Python script and an interactive Jupyter Notebook for step-by-step visualization.

### 📦 Sub-directories (From-Scratch Implementations)

| Folder | Description |
| :--- | :--- |
| **[BoW](./BoW/)** | From-scratch implementation of the **Bag of Words** vectorization technique. |
| **[TF-IDF](./TF-IDF/)** | From-scratch implementation of **Term Frequency-Inverse Document Frequency** for text weighting. |
| **[LDA](./LDA/)** | From-scratch implementation of **Latent Dirichlet Allocation** for topic modeling. |
| **[Ngram](./Ngram/)** | From-scratch implementation of **N-gram** language models (specifically focusing on **Bigrams**). |
| **[Word-Embedding](./Word-Embedding/)** | From-scratch implementation of the **Word2Vec Skip-gram** architecture for word embeddings. |
| **[Tokenization](./Tokenization/)** | Demonstrations of basic tokenization techniques, including **Word**, **Sentence**, and **Byte-Pair Encoding (BPE)**. |
| **[regex](./regex/)** | Simple, practical demonstrations of **Regular Expressions** using Python's built-in `re` module. |
| **[NER](./NER/)** | A simple **Named Entity Recognition** model built entirely from scratch. |
| **[CFG Parser](./CFG%20Parser/)** | **Context-Free Grammar** parser built from scratch. Includes applications for grammar validation and limited sentence generation. |

## 💡 Note on "From-Scratch" Implementations
While libraries like `scikit-learn`, `NLTK`, or `spaCy` provide optimized versions of these tools, the scripts in the sub-directories above are written from the ground up. They primarily rely on core Python and standard numerical libraries (like `NumPy`) to perform matrix operations and probability calculations. 

---
*For course assignments, please see the [`/assignments`](../assignments/) folder. For larger, end-to-end applications, check out the [`/projects`](../projects/) folder.*

