# %%


# # You can access all models by uncommenting the following command
models = {
    "w2v": Word2Vec.load("models/w2v"),
    "tfidf": TfidfModel.load("models/tfidf"),
    "dct": Dictionary.load("models/dct"),
}


from gensim.corpora import Dictionary
from gensim.models import TfidfModel
from gensim.models import Word2Vec
import numpy as np

from gensim.corpora import Dictionary
from gensim.models import TfidfModel
from gensim.models import Word2Vec
import numpy as np


def get_tfidf_weights(models, sentence):
    transformed = models["dct"].doc2bow(sentence.split())
    tfidf_dct = {
        models["dct"][key]: value for (key, value) in models["tfidf"][transformed]
    }
    return tfidf_dct


def embed_sentence(models, sentence):
    w2v = models["w2v"]

    w2v_embeddings = []
    tfidf_weights = get_tfidf_weights(models, sentence)

    tfidf_weighted_sum = np.zeros(w2v.vector_size)
    sum_of_weights = 0
    for word in sentence.split():
        if word in w2v.wv.vocab:
            vector = w2v.wv[word]
            w2v_embeddings.append(vector)
            weight = tfidf_weights.get(word, 0)

            tfidf_weighted_sum += vector * weight
            sum_of_weights += weight
        else:
            w2v_embeddings.append(np.zeros(w2v.vector_size))

    w2v_embedding = np.mean(w2v_embeddings, axis=0).tolist()

    if sum_of_weights > 0:
        tfidf_embedding = (tfidf_weighted_sum / sum_of_weights).tolist()
    else:
        tfidf_embedding = np.zeros(w2v.vector_size).tolist()

    return {"w2v_embedding": w2v_embedding, "tfidf_embedding": tfidf_embedding}


# Load the models
w2v = Word2Vec.load("models/w2v")
tfidf = TfidfModel.load("models/tfidf")
dictionary = Dictionary.load("models/dct")

models = {"w2v": w2v, "tfidf": tfidf, "dct": dictionary}

# Define a sentence
sentence = "i have a dream"

# Get the embeddings
embeddings = embed_sentence(models, sentence)

# Print the embeddings
print("Word2Vec embedding:", embeddings["w2v_embedding"])
print("TFIDF embedding:", embeddings["tfidf_embedding"])

# %%
