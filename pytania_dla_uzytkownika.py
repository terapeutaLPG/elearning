from gemini import load_model,make_prompt
# load questions
from dotenv import load_dotenv
from pprint import pprint
from questions import load_questions
import os
from questions import load_questions
prompts = load_questions() # zdania te z pliku questions.py
load_dotenv()

api_key = os.getenv('GEMINI_API_KEY')
model = load_model(api_key)


def difficulty_level():
    poziom = None
    while True:
        print("Witaj, wybierz sobie jaki chcesz poziom zaawansowania języka od A1-C2")
        choice = input("twoj poziom ktory wybierasz to 1 , 2, 3: ")

        user_prompt = None
        poziom = ""
        if choice == "1":
            poziom = "easy"

            user_prompt = prompts[0]
            break
        elif choice == "2":
            poziom = "medium"
            user_prompt = prompts[1]
            break
        elif choice == "3":
            poziom = "hard"
            user_prompt = prompts[2]
            break
        else:
            print("zle wybrałeś! ")
    return poziom,user_prompt

dif_choice, selected_user_level = difficulty_level()         # uzycie def
print("twoj poziom zaawansowany jaki wybrales to: ",dif_choice)
print(selected_user_level)
imported_prompt = make_prompt(model,selected_user_level)
print(imported_prompt)
# ans = make_prompt(model,"jaki jest dzien tygodnia")
# print(ans)