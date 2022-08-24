
class GitHubRepo:
    def __init__(self, name, url, language, license_used):
        self.name = name
        self.url = url
        self.language = language
        self.license = self.parse_license(license_used)
    
    def parse_license(self, license_used) -> str:
        return 'None' if license_used is None else license_used['name']