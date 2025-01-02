from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(max_features=1000)
X = vectorizer.fit_transform(cleaned_texts)  # cleaned_texts adalah daftar teks yang sudah dibersihkan
