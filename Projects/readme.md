# 🚀 Projects: End-to-End Applications & Experiments

This directory contains applied, end-to-end projects that combine machine learning, automation, and full-stack development. While the `/others` folder focuses on fundamental algorithms from scratch, the projects here are built to solve specific problems or explore applied use cases.

## 📂 Project Overview

| Project | Description | Tech Stack |
| :--- | :--- | :--- |
| **[AgriBot](./seq2seq_chatbot/)** | AI chatbot for agricultural queries (crop management, soil health). | PyTorch, Flask, React, TailwindCSS |
| **[YT Comment Bot](./comment_bot/)** | Automation script to comment on YouTube videos. | Python, Selenium |
| **[Bio-Embeddings](./WE_bio_application/)** | Word2Vec-style embeddings for biological sequences (6-mers). | Python, Skip-gram |

---

## 🤖 1. AgriBot (Seq2Seq Chatbot)
**Directory:** `seq2seq_chatbot/`

AgriBot is an AI-powered chatbot designed to assist farmers with agricultural queries, including crop management, fertilizer recommendations, and soil health. 

* **Architecture:** Built using a custom **Seq2Seq model enhanced with an Attention mechanism**.
* **Full-Stack Implementation:** 
  * **Backend:** Flask API serving the model predictions.
  * **Frontend:** Modern, responsive UI built with **React** and styled with **TailwindCSS**.
* ⚠️ **Note on Performance:** This project was built primarily as a proof-of-concept and a full-stack implementation exercise. The current model is trained on a limited dataset. For production-level accuracy and natural conversations, it requires a significantly larger and more diverse agricultural dataset.

## 🤖 2. YouTube Comment Bot
**Directory:** `comment_bot/`

A web automation tool designed to interact with YouTube via browser automation. 

* **Functionality:** The bot takes a predefined list of YouTube video links and a list of comments as input, then automatically navigates to the videos and posts the comments.
* **Tech Stack:** Built using **Python** and **Selenium** for browser automation.
* **Use Case:** Useful for automated outreach, marketing campaigns, or testing web automation workflows. *(Note: Please use responsibly and in accordance with YouTube's Terms of Service).*

## 🧬 3. Biological Sequence Word Embeddings
**Directory:** `WE_bio_application/`

An innovative application of NLP techniques to bioinformatics, inspired by `gene2vec` and `word2vec`.

* **Concept:** Treats biological sequences (DNA/RNA/Proteins) as "sentences" and applies language modeling to understand biological context.
* **Implementation:** 
  * Tokenizes biological sequences into **6-mers** (subsequences of length 6).
  * Creates context pairs from these tokens.
  * Trains a **Skip-gram** architecture to generate dense vector embeddings for the 6-mers.
* **Goal:** To capture the semantic and structural relationships between biological subsequences in a continuous vector space.

---

## 🛠️ General Setup Instructions

Because these projects utilize different tech stacks (Deep Learning, Web Automation, Full-Stack Web), **each project folder contains its own specific `README.md` and `requirements.txt` / `package.json`**. 

To get started with any project:
1. Navigate into the specific project directory:
   ```bash
   cd projects/<project_name>
   ```
2. Follow the setup instructions in that specific folder's README to install dependencies and run the application.

---
*Looking for fundamental algorithm implementations? Check out the [`/others`](../others/) folder. For academic coursework, see the [`/assignments`](../assignments/) folder.*
