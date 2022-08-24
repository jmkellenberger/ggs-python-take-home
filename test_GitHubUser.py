import unittest
from GitHubUser import GitHubUser
from test_data import api_reponse_fake
  
class TestGitHubUser(unittest.TestCase):
        
    def setUp(self):
        self.user = GitHubUser('Enbala', api_reponse_fake)
        
    def test_initialization(self):
        self.assertEqual(len(self.user.repos), 6)
        
    def test_oldest_repo(self):
        self.assertEqual(self.user.oldest_repo().name, 'ex_machina')
    
    def test_languages_used(self):
        languages = {'Rust': 1, 'Elixir': 3, None: 1, 'C': 1}
        self.assertEqual(self.user.languages_used(), languages)
    
    def test_favorite_language(self):
        self.assertEqual(self.user.most_used_language(), 'Elixir')
    
    def test_licenses_used(self):
        licenses = ['Apache License 2.0',
                    'None',
                    'MIT License',
                    'GNU General Public License v3.0']
        self.assertEqual(self.user.licences_used(), licenses)
        
    def test_user_with_no_public_repositories(self):
        self.user = GitHubUser('mhissain')
        self.assertEqual(len(self.user.repos), 0)
        self.assertEqual(self.user.oldest_repo().name, 'None')
        self.assertEqual(self.user.most_used_language(), 'None')
        self.assertEqual(self.user.licences_used(), [])
  
if __name__ == '__main__':
    unittest.main()