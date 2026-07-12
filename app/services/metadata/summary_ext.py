from .base import BaseMetadataExtractor
from app.schemas.metadata import Summary
class SummaryExtractor(BaseMetadataExtractor):
    
    def extract(self, section):
        return [Summary(summary=section.content)]