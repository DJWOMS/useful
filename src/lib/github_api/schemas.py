from typing import List
from datetime import datetime
from pydantic import BaseModel


class GitHubRepo(BaseModel):
    repo_id: int
    created_at: datetime
    updated_at: datetime
    stars: int
    forks: int
    watch: int
    topics: List[str]
    languages: dict = None
    description: str = None

