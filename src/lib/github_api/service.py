from fastapi import HTTPException
from github import Github, GithubException

from .schemas import GitHubRepo


class GithubService:
    git = Github()

    async def get_repo(self, user: str, name: str):
        try:
            repo = self.git.get_repo(f'{user}/{name}')
        except GithubException:
            raise HTTPException(status_code=404, detail='Repository does not exist')
        git_repo = GitHubRepo(
            repo_id=repo.id,
            created_at=repo.created_at,
            updated_at=repo.updated_at,
            stars=repo.stargazers_count,
            forks=repo.forks_count,
            watch=repo.watchers_count,
            topics=repo.get_topics(),
            languages=repo.get_languages(),
            description=repo.description
        )
        return git_repo


github_s = GithubService()
