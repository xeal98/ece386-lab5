# Art Institute of Chicago API

Prompt engineering to have a LLM make a Python script to query exhibitions.

***Student**, Complete below.*

## Stats

### How many different prompts did you have to try before it worked?
We had to try about 5 different prompts before we got the desired effect. Each time it didn't work, we added more to the prompt so that the LLM had more to work with. We were also suggested to go that way because of how long the prompt that Capt. Yarbrough used was. 

### How well did the final produced script work?
The final produced script worked reasonably well. It was able to search the Art Instiute of Chicago API and print the number of exhibitions that the user wants to see. It then displays the names for each of the artwork pieces in those exhibitions. It continues looping until the user types quit, so it meets the requirements. Rushaan was able to produce a script that even included the ability to go back a step with less lines of prompting; however, that might have just been luck in prompting. 

### What are some of the artwork titles from the exhibition "Ink on Paper: Japanese Monochromatic Prints (2009)"
Some works from that exhibition include Summer Bush Clover, Two Actors in a Drama, Standing Beauty, and Ancient People. 

## Prompt

### Share the conversation URL
https://claude.ai/share/525f7418-b8f7-4f83-99ab-611e9357e28b
### Paste your prompt here
This is the prompt that created the code within this folder: 

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