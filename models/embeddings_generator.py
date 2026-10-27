def embed_texts(texts):
    return [[float(len(t) % 10 + i*0.01) for i in range(8)] for t in texts]
