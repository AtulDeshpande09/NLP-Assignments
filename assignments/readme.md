### Assignments : 

🛠️ ASSIGNMENT 0: The Web Scraping Engine (Data Gathering)

- [x] Task: Write a Python script using `requests` and `BeautifulSoup` to scrape the full paragraph text from these three Wikipedia pages:
    
    1. `https://en.wikipedia.org/wiki/Maharashtra` ➡️ Save raw text as `maha.txt`
    2. `https://en.wikipedia.org/wiki/Friendship` ➡️ Save raw text as `friends.txt`
    3. `https://en.wikipedia.org/wiki/Twice_exceptional` ➡️ Save raw text as `2e.txt`
    

🔤 ASSIGNMENT 1: Text Preprocessing Pipeline (Using `friends.txt`)

- [x] Task: Use NLTK or spaCy to read your `friends.txt` file and build a cleaning routine:
    
    1. Tokenize into sentences and words.
    2. Strip out all standard English stop words and punctuation.
    3. Run the filtered words through both the Porter Stemmer and WordNet Lemmatizer.
    
- Output: Print a comparative text table showing `[Original Word] -> [Stem] -> [Lemma]`. Explain in your README why lemmas preserve morphological root integrity better than stems.

🏷️ ASSIGNMENT 2: Syntactic Tagging (Using `2e.txt`)

- [x] Task: Read your scraped `2e.txt` file. Use `spaCy`'s English model to parse the text and tag grammatical categories.
- Output: Loop through tokens and map out each word alongside its Universal POS tag (`token.pos_`) and detailed tag (`token.tag_`). Identify contextual areas where the model tripped up due to lexical ambiguity.

🔍 ASSIGNMENT 3: NER Categorical Distribution (Using `maha.txt`)

- [x] Task: Read your `maha.txt` file. Use `spaCy` to extract all Named Entities from the text.
- Output: Use Python's `collections.Counter` to map the categorical frequency distribution of entity types. Print a clean dashboard showing the dynamic tally counts (e.g., `ORG: X times`, `PERSON: Y times`, `GPE: Z times`). Separately isolate and print all unique tokens labeled as `PERSON`.

📊 ASSIGNMENT 4: Unsupervised Topic Modeling (Statistical ML)

- Dataset: Download "A Million News Headlines" from Kaggle: `https://www.kaggle.com/datasets/therohk/million-headlines` or Use your custom `maha.txt`, `friends.txt`, and `2e.txt` as three unique documents.
- [x] Task: Sample a subset of headlines, clean them using your preprocessing engine, and use `gensim` to train an Unsupervised Latent Dirichlet Allocation (LDA) model. ( you can also implement custom LDA for better understanding )
- Output: Print out the top dominant keywords for your discovered topics and explain if a human linguist can easily infer a clear thematic title from the mathematical clusters.

🔢 ASSIGNMENT 5: Vector Space Representation (Cross-Document Modeling)

- Dataset: Use your custom `maha.txt`, `friends.txt`, and `2e.txt` as three unique documents.
- [x] Task: Feed these 3 files into `scikit-learn`'s `CountVectorizer` (Bag-of-Words) and `TfidfVectorizer`.
- Output: Generate readable pandas DataFrames showing the vocabulary dimensions. Find key terms unique to one document and explain in your markdown how TF-IDF mathematically shifts the weights to represent document uniqueness compared to basic frequency counts.

🧠 ASSIGNMENT 6: Deep Learning Transformers (Fine-Tuning BERT)

- Dataset: Download the Twitter/Reddit Sentiment Dataset from Kaggle: `https://www.kaggle.com/code/chanchal24/twitter-and-reddit-sentimental-analysis-dataset`
- [x] Task: Build a Google Colab notebook using the Hugging Face `transformers` API. Load a pre-trained `distilbert-base-uncased` model, append a classification prediction head, and fine-tune it on this dataset.
- Output: Save your model weights, print out the final F1-score evaluation metrics, and test the classification head using unique sentences you write yourself.

💬 ASSIGNMENT 7: Generative AI & Model Customization (Fine-Tuning GPT-2)

- Dataset: Download the Technical Question Answering Dataset from Kaggle: `https://www.kaggle.com/datasets/atuldeshpande96/technical-question-answering-dataset`
- [x] Task: Format the rows into clear instruction prompts (e.g., `"Question: <Q> \n Answer: <A>"`). Use Hugging Face to fine-tune a pre-trained GPT-2 (or a similar causal language model) on this domain-specific technical corpus.
- Output: Generate automated model responses using custom technical questions and analyze how well the generative architecture mimics domain knowledge.

