# ece386-lab5

[LLM Prompt Engineering](https://usafa-ece.github.io/ece386-book/b4-llm/lab-prompt-engineering.html)

ECE 386, AI Hardware Applications

## Alex's Attempt at AI Coding
Prompt:
Create python code to access Art Institute of Chicago API  
```
#TODO
1. Accepts a search term from the user.

2. Searches the ArtIC API for exhibitions matching that term and that have artwork titles.

3. Prompts the user for a number of exhibitions they would like to view.

4. Displays the titles of the artwork for those exhibition to the user.

5. Loops until user exit.
```

It should start with: `import requests`

Example function:
```
def search_exhibitions(term: str) -> list[int]:
    '''Make a request to exhibitions/search for the search term,
    using Elasticsearch `exists` option to only return results where the `artwork_titles` field is not empty
    Process the result and return a list of exhibitions IDs.
    '''
```
More info can be found at [this link](https://api.artic.edu/docs/#quick-start)

