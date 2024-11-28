import requests
from random import choice

user_input = input("What would you like to search for? ")
res = requests.get(
    "https://icanhazdadjoke.com/search",
    headers={"Accept": "application/json"},
    params={"term": user_input}
).json()
results = res["results"]
num_jokes = res["total_jokes"]
if num_jokes > 1:
    print(f"I found {num_jokes} jokes about {user_input}")
    print(choice(results)["joke"])
    
elif num_jokes == 1:
     print(f"I found {num_jokes} joke about {user_input}")
     print(results[0]["joke"])
  
else:
   print(f"Sorry,I found no jokes about {user_input}")
