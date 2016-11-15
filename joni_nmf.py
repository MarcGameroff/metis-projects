import pandas as pd
from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF

n_topics = 5
n_top_words = 15

# Set stopwords
more_stop_words = ['ve', 'll', 'don', 'won', 'em', 'like', 'oh']
stop_words = text.ENGLISH_STOP_WORDS.union(more_stop_words)

# Load lyrics
joni_songs = pd.read_csv('joni_df7.csv', encoding='latin-1')
dataset = joni_songs['lyrics']

# Convert lyrics to a matrix of TF-IDF features
vectorizer = TfidfVectorizer(max_df=.95, min_df=3, stop_words=stop_words)
tfidf = vectorizer.fit_transform(dataset)

# Fit the NMF model
nmf = NMF(n_components=n_topics, random_state=1).fit(tfidf)
feature_names = vectorizer.get_feature_names()

# Print the top 15 words in each of the 5 topics
for topic_idx, topic in enumerate(nmf.components_):
    print("Topic #%d:" % topic_idx)
    print(" ".join([feature_names[i]
                   for i in topic.argsort()[:-n_top_words - 1:-1]]))
    print()
