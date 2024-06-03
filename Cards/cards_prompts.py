# card_prompts
import json
def load_prompts_from_json(file_path='text-data-json'):
    with open(file_path, 'r', encoding='utf-8') as file:
        prompts = json.load(file)
    return prompts


def cards_prompts_difficulty():
    prompts =load_prompts_from_json() # f
    begginer_prompt = prompts['beginner_prompt']
    medium_prompt = prompts['medium_prompt']
    hard_prompt = prompts['hard_prompt']

    return [begginer_prompt,medium_prompt,hard_prompt]

























#
# def cards_prompts_difficulty():
#     beginner_prompt = '''Wyobraz ze masz taka platforme: Platforma do nauki języków obcych: platformę e-learningową umożliwiającą użytkownikom\n
#   naukę języków obcych poprzez interaktywne lekcje, quizy, ćwiczenia gramatyczne, konwersacje z botem, a także wymianę wiedzy i doświadczeń z innymi użytkownikami. |n
#   I teraz chcesz zaprojektowac  fiszki dla swoich uczniow ktorzy chca sie nauczyc jezyka polskiego na A1 a ich jezyk ojczysty to angielski, zacznij od zrobienia dla nich prostych ale uczacych fiszek, chce 10 fiszek'''
#
#     medium_prompt = '''Wyobraz ze masz taka platforme: Platforma do nauki języków obcych: platformę e-learningową umożliwiającą użytkownikom\n
#   naukę języków obcych poprzez interaktywne lekcje, quizy, ćwiczenia gramatyczne, konwersacje z botem, a także wymianę wiedzy i doświadczeń z innymi użytkownikami. |n
#   I teraz chcesz zaprojektowac  fiszki dla swoich uczniow ktorzy chca sie nauczyc jezyka polskiego na B1-B2 a ich jezyk ojczysty to angielski, zacznij od zrobienia dla nich prostych ale uczacych fiszek, chce 10 fiszek'''
#     hard_prompt = '''Wyobraz ze masz taka platforme: Platforma do nauki języków obcych: platformę e-learningową umożliwiającą użytkownikom\n
#   naukę języków obcych poprzez interaktywne lekcje, quizy, ćwiczenia gramatyczne, konwersacje z botem, a także wymianę wiedzy i doświadczeń z innymi użytkownikami. |n
#   I teraz chcesz zaprojektowac  fiszki dla swoich uczniow ktorzy chca sie nauczyc jezyka polskiego na C1-C2 a ich jezyk ojczysty to angielski, zacznij od zrobienia dla nich prostych ale uczacych fiszek, chce 10 fiszek'''
#
#     return [beginner_prompt,medium_prompt,hard_prompt]
#

# wyciagnac te napisy wyzej do zewnetrznego pliku po to aby moc zmieniac tresc tego ale nie w kodzie ale np zeby miec .json





















#
# "**Quiz** - sprawdza wiedzę z języku - Funkcjonalność
# **Chatbot** - NLTK/spaCy do konwersacji
# **Lekcje** -> fiszki korzystając z API quizleta , API duolingo itp.
# **Strona głowna** -> Interfejs z Tkinter
# -Mialaby tekst motywacyjny ktora sie zmienia kazdego dnia
# -Liste wyboru języków
# -Przycisk do kontynuacji lekcji albo przycisk do rozpoczęcia lekcji
# Rejestracja/Logowanie (opcjonalnie) -> to by wymaga uzycia na przyklad SQLlite , sledzenie postepu uzytkownika"