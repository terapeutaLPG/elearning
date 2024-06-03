import sys
sys.path.append(r'C:\Users\Igor\Desktop\elearning_platform\myenv\Lib\site-packages')

import openai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('GEMINI_API_KEY')
def load_model(api_key):
    openai.api_key = api_key
    return openai

def make_prompt(model, prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt + ' oraz chcę dobra / prawidłowe odpowiedzi do wszystkich pytań w jednej liście w Pythonie',
        max_tokens=100
    )
    questions = response.choices[0].text
    return questions

#
# api_key = os.getenv('GEMINI_API_KEY')
# def load_model(api_key ):
#
#
#
#     genai.configure(api_key=api_key)
#
#     genai.configure(api_key = api_key)
#
#
#     model = genai.GenerativeModel('gemini-pro')
#
#
#     return model
#
# def make_prompt(model , prompt):
#     response = model.generate_content(prompt + 'oraz chcę dobra / prawidłowe odpowiedzi  do wszystkich pytań  w jednej liście  w Pythonie' )
#     questions = response.text
#
#     return questions

#
# prompt  = '''Wyobraz ze masz taka platforme: Platforma do nauki języków obcych: platformę e-learningową umożliwiającą użytkownikom\n
#     naukę języków obcych poprzez interaktywne lekcje, quizy, ćwiczenia gramatyczne, konwersacje z botem, a także wymianę wiedzy i doświadczeń z innymi użytkownikami. |n
#     I teraz chcesz zaprojektowac zadania, cwiczenia, i quizy dla swoich uczniow ktorzy chca sie nauczyc jezyka polskiego na A1 a ich jezyk ojczysty to angielski, zacznij od zrobienia dla nich prostych ale uczacych quizow, chce 10 pytan'''
#
#


