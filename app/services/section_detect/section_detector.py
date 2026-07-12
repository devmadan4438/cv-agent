from collections import defaultdict
from rapidfuzz import fuzz
from app.utils.helpers import normalize

from app.schemas.document import ParsedDocument
from app.schemas.cv_sections import ResumeSection

import logging
logger = logging.getLogger(__name__)

SECTION_MAP = {
    "summary": [
        "summary",
        "professional summary",
        "profile",
        "objective",
        "career objective",
    ],

    "experience": [
        "experience",
        "work experience",
        "professional experience",
        "employment history",
        "work history",
    ],

    "skills": [
        "skills",
        "technical skills",
        "professional skills",
        "core skills",
        "technical expertise",
    ],

    "projects": [
        "projects",
        "project",
        "personal projects",
    ],

    "education": [
        "education",
        "academic qualification",
        "qualifications",
    ],

    "certifications": [
        "certifications",
        "certificates",
        "training",
    ],

    "activities": [
        "extra activities",
        "activities",
        "achievements",
    ],
}

class SectionDetector:

    def _match_heading(self, text: str):
        text = normalize(text)
        best = None
        score = 0

        for section, aliases in SECTION_MAP.items():

            for alias in aliases:

                s = fuzz.token_set_ratio(text, alias)

                if s > score:

                    score = s
                    best = section

        if score >= 85:

            return best

        return None
    
    def detect(self, document):
        logger.info("Detect sections")

        sections = defaultdict(list)

        current = "header"

        for page in document.pages:

            for line in page.lines:

                heading = self._match_heading(line.text)

                if (
                    heading
                    and len(line.text.split()) <= 5
                    and (
                        line.is_bold
                        or line.font_size >= 12
                    )
                ):
                    current = heading
                    continue

                sections[current].append(line.text)

        return [
            ResumeSection(
                name=name,
                content="\n".join(content),
            )
            for name, content in sections.items()
        ]