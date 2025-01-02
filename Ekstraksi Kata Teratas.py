def get_top_words_per_cluster(model, vectorizer, n_top_words=3):
    words = vectorizer.get_feature_names_out()
    top_words = {}
    for i, centroid in enumerate(model.cluster_centers_):
        top_words[f"Cluster {i}"] = [words[idx] for idx in centroid.argsort()[-n_top_words:]]
    return top_words

top_words = get_top_words_per_cluster(KMeans, vectorizer)
