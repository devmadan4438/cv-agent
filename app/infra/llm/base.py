from abc import ABC, abstractmethod

class LLMBase(ABC):

    @abstractmethod
    def get_client(self, entity):
        pass