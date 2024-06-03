from gemini import load_model, make_prompt
from dotenv import load_dotenv
from pprint import pprint
from questions import load_questions
import os
import json
# Załaduj dane z pliku JSON

##prompts = load_questions('questions-data.json')
#load_dotenv()
#prompts = load_questions('questions-data.json')
def load_questions(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data
prompts = load_questions('questions-data.json')


api_key = os.getenv('GEMINI_API_KEY')
model = load_model(api_key)

def difficulty_level():
    poziom = None
    while True:
        print("Witaj, wybierz sobie jaki chcesz poziom zaawansowania języka od A1-C2")
        choice = input("Twoj poziom ktory wybierasz to 1, 2, 3: ")

        user_prompt = None
        poziom = ""
        if choice == "1":
            poziom = "easy"
            user_prompt = prompts['beginner_prompt']
            break
        elif choice == "2":
            poziom = "medium"
            user_prompt = prompts['medium_prompt']
            break
        elif choice == "3":
            poziom = "hard"
            user_prompt = prompts['hard_prompt']
            break
        else:
            print("Zle wybrałeś! ")
    return poziom, user_prompt

dif_choice, selected_user_level = difficulty_level()  # Uzycie def
print("Twoj poziom zaawansowany jaki wybrales to: ", dif_choice)
print(selected_user_level)
imported_prompt = make_prompt(model, selected_user_level)
print(imported_prompt)

# ans = make_prompt(model,"jaki jest dzien tygodnia")
# print(ans)