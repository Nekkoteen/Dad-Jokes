import requests
from random import choice
import pyfiglet 


heading = pyfiglet.figlet_format("Dad Jokes")

print(heading)
    
user_input = ""

while True:
    user_input = input("What would you like to search for? ")
    if user_input == "quit":
            break
    url ="https://icanhazdadjoke.com/search" 
    res = requests.get(url, 
        headers={"Accept": "application/json"}, 
        params={"term": user_input}).json()

    num_jokes = res["total_jokes"]
    results = res["results"]
    
    if num_jokes > 1:
        print(f"I found {num_jokes} jokes about {user_input}")
        print(choice(results)["joke"])
        print()
        
        more =""
        while more != "n":
            more = input("Would you like to hear another? (y/n) ").lower()
            print()
            if more =="y":
                print(choice(results)["joke"])
                print()
    elif num_jokes == 1:
        print(f"I found {num_jokes} joke about {user_input}")
        print(results[0]["joke"])
        print()
        
    else:
            print(f"Sorry,I found no jokes about {user_input}")    
        
print("Goodbye")

