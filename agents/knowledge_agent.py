from models.embeddings_generator import embed_texts

class KnowledgeAgent:
    def __init__(self):
        self.index = []

    def add_documents(self, docs):
        texts = [d['text'] for d in docs]
        embs = embed_texts(texts)
        for d,e in zip(docs, embs):
            self.index.append({'id': d.get('id'), 'text': d.get('text'), 'emb': e})

    def search(self, diagnosis_summary, top_k=3):
        q = diagnosis_summary.get('short_summary','') or ' '.join(diagnosis_summary.get('reasons',[]))
        results = [d for d in self.index if q.lower() in d['text'].lower()]
        return results[:top_k]
