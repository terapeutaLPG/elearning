### zaimportuj streamlit

import re
import streamlit as st


### funckje()-> zwracały takie bloczki z tekstem


## funckja 1 -> tekst pokazywała ''Hello World''

## funckja 2 -> tekst "Witaj w naszej aplikacji"


# Stworz funkcje o nazwie "home"
# która tworzy tytuł  ("Learn Polish A1 - Level")
# ktora tworzy tekst ("Welcome to the Polish learning platform for beginners")
def home():
    st.title("Learn Polish AI - Level ")
    st.write("Welcome to the Polish learning platform for begginers")


home()

# Pytania :

## Quiz z języka polskiego dla początkujących (angielski ojczysty) - poziom A1
text = '''
**1. Jak się masz?**

a) Cześć!
b) Mam się dobrze, dziękuję.
c) Do widzenia!
d) Na razie!

**2. Jak masz na imię?**

a) Nazywam się [Twoje imię].
b) Mam na imię [Twoje imię].
c) Jestem [Twoje imię].
d) To [Twoje imię].

**3. Skąd jesteś?**

a) Jestem z Polski.
b) Mieszkam w Polsce.
c) Pochodzę z Polski.
d) Wszystkie powyższe odpowiedzi są poprawne.

**4. Jaki jest twój zawód?**

a) Jestem studentem/studentką.
b) Nie pracuję.
c) Jestem [Twój zawód].
d) To zależy.

**5. Czy mówisz po angielsku?**

a) Tak, mówię po angielsku.
b) Trochę rozumiem po angielsku.
c) Nie mówię po angielsku.
d) Uczę się angielskiego.

**6. Jakie jest polskie słowo na "dziękuję"?**

a) Proszę.
b) Przepraszam.
c) Dziękuję.
d) Dzień dobry.

**7. Jakie jest polskie słowo na "proszę"?**

a) Proszę.
b) Przepraszam.
c) Dziękuję.
d) Dzień dobry.

**8. Jak powiedzieć "do widzenia" po polsku?**

a) Proszę.
b) Przepraszam.
c) Dziękuję.
d) Do widzenia!

**9. Jakie jest polskie słowo na "dzień dobry"?**

a) Proszę.
b) Przepraszam.
c) Dziękuję.
d) Dzień dobry.

**10. Jakie jest polskie słowo na "dobranoc"?**

a) Proszę.
b) Przepraszam.
c) Dziękuję.
d) Dobranoc!
'''


def questions():
    # zrob przycisk ktory
    if st.button("Questions"):

        questions = re.split(r'\n(?=\*\*\d+\. )', text.strip())
        index = 1
        for question in questions:
            question_splitted = question.replace('!', '.').split(".")[1:]

            st.write(question_splitted)

            question_beginning, first_answer = question_splitted[0].split('**')

            st.write(f'qts b {first_answer}')

            question_splitted[0] = f'{index}.{question_beginning}'

            question_splitted.insert(1, first_answer)
            st.write()
            for single_answer in question_splitted:
                st.write(single_answer)

             st.write(question_splitted)
            st.text("")
            st.write("---")

        index += 1


questions()
# def cards():
#     if st.button("Choose a level")


#musi laldnie odczytywac odpowiedzi
