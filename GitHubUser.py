from GitHubRepo import GitHubRepo
from json import loads
from typing import Dict, Iterable
from urllib.request import urlopen
from urllib.parse import urlencode

class GitHubUser:
    def __init__(self, username: str):
        self.username = username
        self.repos = self.build_repos_list()
    
    def create_repo(self, repo: hash) -> GitHubRepo:
        repo = GitHubRepo(  repo['name'],
                            repo['html_url'], 
                            repo['language'],
                            repo['license'])
        return repo
    
    def last_page(self, link_header) -> 'bool':
        if link_header is None or "next" not in link_header:
            return True
        else: 
            return False
        
    def next_page(self, link_header) -> str:
        return link_header.split(';')[0]

    def build_repos_list(self) -> Iterable[GitHubRepo]:
        endpoint = f"https://api.github.com/users/{self.username}/repos"
        params = {'per_page': 100, 'sort': 'created'}
        url = f"{endpoint}?{urlencode(params)}"
        repos_list = []
        
        while True:
            with urlopen(url) as response:
                json_content = loads(response.read().decode())
                for repo in json_content:
                    repos_list.append(self.create_repo(repo))
                    
                link_header = response.getheader('link')
                if self.last_page(link_header):
                    break
                else:
                    url = self.next_page(link_header)
                    
        return repos_list
    
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
    # print(f"  - Oldest repo: {user.oldest_repo().name}")
    print(f"  - Favorite language: {user.most_used_language()}")
    print(f" - Licenses used:")
    for license in user.licences_used():
        print(f"   - {license}")


if __name__ == '__main__':
    main()
