# Structured Outputs

***Student:** Complete below.*

## How well did it work?
Using gemma3 at 4B parameters proved to be fairly effective at finding the desired information in the given sentence. It was able to parse it into a json file rather easily, albeit did take just a little bit of time to do so. This is a lightweight model that proves it is good at certain tasks. It answered all of our questions accurately that we had to give it, so it worked well for this case. 

## Paste a few input/output combos
Input:
```
Alex White is trying to make a reservation at the Broadmoor for a party of 4
    at 3 o'clock tonight.
```

Output:
`users=[User(name='Alex White', time=3, partySize=4)]`

Input:
```
I have two pets.
A cat named Luna who is 5 years old and loves playing with yarn. She has grey fur.
I also have a 2 year old black cat named Loki who loves tennis balls.
```

Output:
`pets=[Pet(name='Luna', animal='cat', age=5, color='grey', favorite_toy='yarn'), Pet(name='Loki', animal='cat', age=2, color='black', favorite_toy='tennis balls')]`
*use code blocks for the JSON*
