from scipy.cluster.hierarchy import ward, dendrogram
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt

# Calculate distances
nmf_202x5 = nmf.transform(tfidf)
titles = df2['title'].tolist()
dist = 1 - cosine_similarity(nmf_202x5)

# Define the linkage matrix
linkage_matrix = ward(dist)

# Define dendrogram layout
fig, ax = plt.subplots(figsize=(15, 20))
ax = dendrogram(linkage_matrix, orientation="right", labels=titles)
plt.tick_params(axis='x', which='both', bottom='off', top='off',
                     labelbottom='off')
plt.tight_layout()

# Save dendrogram as an SVG file
plt.savefig('ward_clusters4.svg', dpi=200) 