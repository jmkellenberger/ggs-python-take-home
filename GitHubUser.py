from typing import Dict, Iterable
from GitHubRepo import GitHubRepo


class GitHubUser:
    def __init__(self, username: str):
        self.username = username

    def repos(self) -> Iterable[GitHubRepo]:
        endpoint = f"https://api.github.com/users/{self.username}/repos"
        # TODO: Query & parse endpoint
        return []

    def oldest_repo(self) -> GitHubRepo:
        return GitHubRepo('hello_world', 'https://github.com/jdoe/hello_world')

    def languages_used(self) -> Dict[str, int]:
        return {'Python': 4, 'PHP': 3, 'C++': 2, 'Elixir': 1}

    def most_used_language(self) -> str:
        return 'Python'

    def licences_used(self) -> Iterable[str]:
        return ['GNU General Public License v2.0',
                'MIT License',
                'Creative Commons Zero v1.0 Universal']


def main():
    user = GitHubUser('s3cur3')
    print(f"Stats for {user.username}:")
    print(f"  - Oldest repo: {user.oldest_repo().name}")
    print(f"  - Favorite language: {user.most_used_language()}")
    print(f" - Licenses used:")
    for license in user.licences_used():
        print(f"   - {license}")


if __name__ == '__main__':
    main()
