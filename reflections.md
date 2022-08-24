# Reflections

This project was a wonderful learning experience. I had previously only used [Requests](https://requests.readthedocs.io/en/latest/) to handle HTTP requests in Python and I enjoyed digging into the standard library docs to handle the API call with urllib.

My final implementation of the program has some weaknesses. I'm not completely satisfied with `GitHubUser.request_repos()`, as it currently stands out amongst the rest of the GitHubUser methods in:  

  1. Doing quite a bit (Establishing the URL, calling the URL, paginating, building a list of Repo objects to return, etc)  

  2. Relying on a handful of extracted methods that exist only to serve it

My knee-jerk reaction would be to extract it out as it's own class to remove all of the HTTP logic from `GitHubUser`, which is currently responsible for making HTTP requests *and* returning User stats.

Similarly, `GitHubUser.oldest_repo()` as it currently stands, is wholly dependent on the HTTP request implementation sending GitHub the `'sort': 'created'` parameter. If the implementation or GitHub API were to change, then the method's return value would not necessarily be correct. As it stands, I felt that given the current implementation, simply pulling the last item out of the Repos list was more elegant than storing a `'created_at'` instance variable in `GitHubRepo`, iterating over the user's repos and returning the oldest value.

## Testing

Rather than relying on TDD, the development of this program relied on exploratory testing using my personal GitHub account and the driver script in `main()`, with the tests being written after the fact. This stemmed mostly from my inexperience with writing tests for API calls.

I was initially at a loss in regards to testing a program that relied on an external API returning data which could change at any time.

My initial implementation of the HTTP request was messy, and even in it's current form it is difficult to test effectively.

My solution was to store the data from an API call in a fake, and add a parameter and conditional to `GitHubUser` allowing me to optionally instantiate a user with the API response to parse, bypassing the HTTP request altogether.

A cleaner solution would have been to leave the `GitHubUser` code alone, and create a mock object in the test setup to return the response fake during the HTTP request, which would allow more effective testing of the `GitHubUser` code, as well as provide future users better documentation on how the code is meant to be used.

Writing the test suite for this project was a great opportunity to identify gaps in my understanding of the `unittest` library and general testing methodology, which I plan to rectify through further research. It also highlighted weaknesses in my implementation and reinforced my desire to refactor the code pertaining to HTTP requests.
