from GitHubRepo import GitHubRepo
from json import loads
from typing import Dict, Iterable
from urllib.request import urlopen
from urllib.parse import urlencode

class GitHubUser:
    def __init__(self, username: str, repos: list = []):
        self.username = username
        self.repos = self.parse_repos(repos) if repos else self.request_repos()
        self.languages = self.languages_used()
    
    def create_repo(self, repo: hash) -> GitHubRepo:
        repo = GitHubRepo(  repo['name'],
                            repo['html_url'], 
                            repo['language'],
                            repo['license'])
        return repo
    
    def last_page(self, link_header: str) -> 'bool':
        if link_header is None or "next" not in link_header:
            return True
        else: 
            return False
        
    def next_page(self, link_header: str) -> str:
        return link_header.split(';')[0]
    
    def paginate(self, link_header: str) -> str:
        if self.last_page(link_header):
            return ''
        else:
            return self.next_page(link_header)
        
    def parse_repos(self, json_content: list) -> Iterable[GitHubRepo]:
        repos = []
        for repo in json_content:
            repos.append(self.create_repo(repo))
        return repos

    def request_repos(self) -> Iterable[GitHubRepo]:
        endpoint = f"https://api.github.com/users/{self.username}/repos"
        params = {'per_page': 100, 'sort': 'created'}
        url = f"{endpoint}?{urlencode(params)}"
        repos_list = []
        
        while url:
            with urlopen(url) as response:
                json_content = loads(response.read().decode())
                repos_list += self.parse_repos(json_content)
                url = self.paginate(response.getheader('link'))

        return repos_list
    
    def oldest_repo(self) -> GitHubRepo:
        no_repos = self.create_repo({'name': 'None',
                                     'html_url':'None',
                                     'language': 'None',
                                     'license': None})
        return self.repos[-1] if len(self.repos) > 0 else no_repos

    def languages_used(self) -> Dict[str, int]:
        languages_dict = {}
        for repo in self.repos:
            language = repo.language
            
            if language in languages_dict:
                languages_dict[language] += 1
            else:
                languages_dict[language] = 1
                
        return languages_dict

    def most_used_language(self) -> str:
        if self.languages:
            return max(self.languages, key = self.languages.get)
        else:
            return 'None'

    def licences_used(self) -> Iterable[str]:
        licenses = []
        
        for repo in self.repos:
            if repo.license in licenses:
                continue
            else:
                licenses.append(repo.license)
                
        return licenses


def main():
    user = GitHubUser('mhissain')
    print(f"Stats for {user.username}:")
    print(f"  - Oldest repo: {user.oldest_repo().name}")
    print(f"  - Favorite language: {user.most_used_language()}")
    print(f" - Licenses used:")
    for license in user.licences_used():
        print(f"   - {license}")


if __name__ == '__main__':
    main()
