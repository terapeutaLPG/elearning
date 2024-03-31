import requests
from pprint import pprint
from colorama import Fore, Style
from translator import translate_sentence
url = "https://opentdb.com/api.php?amount=10&difficulty=easy&type=boolean"

import translator
response = requests.get(url).json()





# for loopa ktory bedzie wyswietlas pytania i odpowiedzi

# bohaterowie = ['Adam','Piotre,','Janusz','Maciej']
# pytanie_1 = {'category': 'History',
#   'correct_answer': 'True',
#   'difficulty': 'easy',
#   'incorrect_answers': ['False'],
#   'question': 'The French Kingdom helped the United States gain their '
#               'independence over Great Britain during the Revolutionary War.',
#   'type': 'boolean'}
#
# print(pytanie_1["question"])


#  petle dla wszystkich pytan i pozniej w kazdym pytaniu wyswietl jego tresc, odpowiedzi, kategorie w konsoli
# pytania={
#     "gra":"csgo"
# }
# .gitignore
# nazwy plików do ignorowania, nazwę folderów, oraz
# wszystkiego
# chodzi o to że pomijamy te pliki z .gitignore kiedy robimy commita naszego kodu (czyli kiedy uploadejemy zmiany do serwera online)

pprint(response)
# for response in ['results']:
#     pprint('category_answer':['results'])

# {   # klucz-wartość
#     "status code":0,
#     results:[{"category", "correct_ans":True .....}, {"category":"General knwoledge", question:YOu can legally drink alco....}, {}]
# }
                # klucz daje nam wartość do której jest przypisany
# print(response["results"])
print("tutaj")

for question in response['results']:
    # przetlumaczyl pytanie na polski przykladowo
    question_text = question["question"]
    question_text = translator.translate_sentence(question_text)
    print(question_text)
    print(f'''
    {Fore.CYAN + question_text + Style.RESET_ALL}: Pytanie
    {Fore.GREEN + question["correct_answer"] + Style.RESET_ALL} : to poprawna odpowiedź
    {Fore.RED + question["incorrect_answers"][0] + Style.RESET_ALL }: jest to zła odpowiedź
    ''')
    # incorrect_answers ['False'] + "dsadsa"

    # wyswietl treść pytania i możliwe odpowiedzi jako
    # pytanie X:
    # A :prawda
    # B: nieprawda

    # print(question["category"],question["question"] )
    # translated_sentence = translate_sentence(text =  question["question"])
    #
    # print(translated_sentence)

    # Quiz - albo znalezc dobre API, albo z neta gdzies znalezc duza lista pytan z odpowiedzi dla osob uczacy sie jezyka po angielsku, pozniej wklepac do chat gpt zeby zamienil to w liste pythonowa i na biezaco tlumaczyc pytania i odpowiedzi funkcja
    # uzytkwonik bedzie mial odpowiedzi, bedzie odpowiadal i po kazdym quizie bedzie zbieral punkty i jak zdobedzie X punktow to zdobywa poziomy nauki jezyka
    # ustalic jezyki obce jakie ten projekt uczy


