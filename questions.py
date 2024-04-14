

def load_questions():
    beginner_prompt = '''Wyobraz ze masz taka platforme: Platforma do nauki języków obcych: platformę e-learningową umożliwiającą użytkownikom\n
    naukę języków obcych poprzez interaktywne lekcje, quizy, ćwiczenia gramatyczne, konwersacje z botem, a także wymianę wiedzy i doświadczeń z innymi użytkownikami. |n
    I teraz chcesz zaprojektowac zadania, cwiczenia, i quizy dla swoich uczniow ktorzy chca sie nauczyc jezyka polskiego na A1 a ich jezyk ojczysty to angielski, zacznij od zrobienia dla nich prostych ale uczacych quizow, chce 10 pytan  jednokrotengo wyboru'''

    medium_prompt = '''Wyobraź sobie, że masz taką platformę: Platforma do nauki języków obcych: platformę e-learningową umożliwiającą użytkownikom
naukę języków obcych poprzez interaktywne lekcje, quizy, ćwiczenia gramatyczne, konwersacje z botem, a także wymianę wiedzy i doświadczeń z innymi użytkownikami.
I teraz chcesz zaprojektować zadania, ćwiczenia, i quizy dla swoich uczniów, którzy chcą doskonalić język polski na poziomie średnio-zaawansowanym (B1-B2), a ich język ojczysty to angielski. Zacznij od stworzenia dla nich zaawansowanych quizów edukacyjnych, chcę 10 pytań jednokrotengo wyboru, które będą testować ich zdolności językowe w różnych kontekstach, w tym idiomy, złożone struktury gramatyczne oraz rozumienie tekstu na poziomie zaawansowanym.'''
    hard_prompt = '''Wyobraź sobie, że zarządzasz platformą do nauki języków obcych: to zaawansowana platforma e-learningowa, która umożliwia użytkownikom pogłębianie znajomości języka polskiego poprzez zaawansowane interaktywne lekcje, specjalistyczne quizy, skomplikowane ćwiczenia gramatyczne i stylowe, oraz możliwość prowadzenia zaawansowanych konwersacji z botem. Platforma sprzyja również wymianie wiedzy i doświadczeń z innymi użytkownikami na podobnym poziomie zaawansowania. Twoim zadaniem jest teraz zaprojektowanie serii zadań, ćwiczeń i quizów, które będą wyzwaniem dla uczniów aspirujących do biegłości w języku polskim. Utwórz 10 pytań   jednokrotengo wyboru quizowych, które obejmują analizę literackich tekstów, zaawansowaną gramatykę, oraz polskie frazeologizmy i kulturowe niuanse, dostosowane do poziomu C1-C2.
'''
    return [beginner_prompt,medium_prompt,hard_prompt]



#
# "**Quiz** - sprawdza wiedzę z języku - Funkcjonalność
# **Chatbot** - NLTK/spaCy do konwersacji
# **Lekcje** -> fiszki korzystając z API quizleta , API duolingo itp.
# **Strona głowna** -> Interfejs z Tkinter
# -Mialaby tekst motywacyjny ktora sie zmienia kazdego dnia
# -Liste wyboru języków
# -Przycisk do kontynuacji lekcji albo przycisk do rozpoczęcia lekcji
# Rejestracja/Logowanie (opcjonalnie) -> to by wymaga uzycia na przyklad SQLlite , sledzenie postepu uzytkownika"