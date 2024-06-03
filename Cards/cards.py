#### zaimplementuj ta samo funkcjonalnosc co w pliku provide _questions.py
# czyli chce zebys zaladowal w tym pliku model, dal dla uzytkownika mozliwosc wyboru poziomiu fiszek, i pozniej mu te fiszki wyswietlil
from gemini import load_model,make_prompt

from dotenv import load_dotenv

import os
# beginner prompt:
# Wyobraz ze masz taka platforme: Platforma do nauki języków obcych: platformę e-learningową umożliwiającą użytkownikom\n
#   naukę języków obcych poprzez interaktywne lekcje, quizy, ćwiczenia gramatyczne, konwersacje z botem, a także wymianę wiedzy i doświadczeń z innymi użytkownikami. |n
#   I teraz chcesz zaprojektowac  fiszki dla swoich uczniow ktorzy chca sie nauczyc jezyka polskiego na A1 a ich jezyk ojczysty to angielski, zacznij od zrobienia dla nich prostych ale uczacych fiszek, chce 10 fiszek

from cards_prompts import cards_prompts_difficulty


prompts = cards_prompts_difficulty() # zdania te z pliku questions.py
load_dotenv()

api_key = os.getenv('GEMINI_API_KEY')
model = load_model(api_key)


def cards_prompts():
    poziom = None
    while True:
        print("Fiszki uzywasz do wyboru odpowiedzi, która jest według ciebie prawidłowa")
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

dif_choice, selected_user_level = cards_prompts()         # uzycie def
print("twoj poziom zaawansowany jaki wybrales to: ",dif_choice)
print(selected_user_level)
imported_prompt = make_prompt(model,selected_user_level)
print(imported_prompt)

#zrobic streamlita
