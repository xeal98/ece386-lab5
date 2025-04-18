from ollama import chat
from pydantic import BaseModel
 
 
class User(BaseModel):
  name: str
  time: int
  partySize: int
 
 
class UserList(BaseModel):
  users: list[User]


response = chat(
  messages=[
    {
        'role': 'user',
        'content': '''
            Alex White is trying to make a reservation at the Broadmoor for a party of 4
            at 3 o'clock tonight.
        ''',
    }
  ],
  model='gemma3:4b',
  format=UserList.model_json_schema(),
)
 
users = UserList.model_validate_json(response.message.content)
print(users)