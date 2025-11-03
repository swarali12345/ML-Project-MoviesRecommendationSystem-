
# 🎵 Music Recommendation System using NLP

## 📖 Overview
This project is a **Music Recommendation System** that uses **Natural Language Processing (NLP)** techniques to recommend songs based on the user’s input or favorite track.  
It analyzes song metadata, lyrics, and other textual features to find similar music tracks using content-based filtering.

---

## 🚀 Features
- 🎧 Recommends songs similar to a user-selected track  
- 🧠 NLP-based text similarity using TF-IDF and cosine similarity  
- 🗂️ Dataset preprocessing and feature extraction  
- 💬 User-friendly interface (Streamlit or CLI)  
- ⚡ Fast and lightweight — no external APIs required  

---

## 🧰 Tech Stack
- **Python 3.x**
- **Pandas / NumPy** – Data handling  
- **Scikit-learn** – TF-IDF Vectorization, Cosine Similarity  
- **NLTK / spaCy** – Text cleaning and preprocessing  
- **Streamlit** *(optional)* – For interactive web UI  

---

## 🧪 How It Works
1. **Data Preprocessing**
   - Load dataset (song title, artist, lyrics, genre, etc.)
   - Clean and normalize text using NLP (lowercasing, stopword removal, lemmatization)
2. **Feature Extraction**
   - Convert lyrics/metadata to numerical vectors using **TF-IDF Vectorizer**
3. **Similarity Calculation**
   - Compute pairwise **cosine similarity** between song vectors
4. **Recommendation**
   - Return top N most similar songs based on similarity scores
  


<img width="1852" height="918" alt="Screenshot 2025-11-03 212506" src="https://github.com/user-attachments/assets/c283c759-22ef-4969-ae3b-30d178d0f720" />
<img width="1901" height="927" alt="Screenshot 2025-11-03 212532" src="https://github.com/user-attachments/assets/87b5a9b7-ca7b-44ee-9733-535882ee42fd" />
![Uploading Screenshot 2025-11-03 212602.png…]()




---


