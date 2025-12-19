from pydantic import BaseModel
from typing import Dict, List, Optional

class LearningState(BaseModel):
    paper_title: str = ""
    sections: Dict[str, str] = {}
    weak_concepts: List[str] = []
    last_section: Optional[str] = None