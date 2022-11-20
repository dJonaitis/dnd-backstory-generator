import openai

openai.api_key = 'YOUR_API_KEY'


print("Welcome to the D&D backstory generator!\n---------------------------------------")
name = input("Enter your character's name: ")
race = input("Enter your character's race: ")
dndClass = input("Enter your character's class: ")
background = input("Enter your character's background: ")

inputPrompt = f"Write a d&d background about a {race} {dndClass} named {name}, with the {background} background."
response = openai.Completion.create(model="text-davinci-002", prompt=inputPrompt, temperature=0.5, max_tokens=1000)
print(response.choices[0].text)
