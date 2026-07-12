from .nomic_embedding import NomicEmbedding

class EmbeddingFactory:
    mapping = {
        "nomic": NomicEmbedding(),
    }

    @classmethod
    def get(cls, model : str = 'nomic'):
        return cls.mapping.get(model, None)
  