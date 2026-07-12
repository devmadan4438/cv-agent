from abc import ABC, abstractmethod

from app.schemas.cv_sections import ResumeSection


class BaseMetadataExtractor(ABC):

    @abstractmethod
    def extract(self, section: ResumeSection):
        pass