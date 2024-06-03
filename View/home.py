### zaimportuj streamlit
import json
import os
import re

import streamlit as st

from gemini import load_dotenv, load_model, make_prompt

###############################################################

load_dotenv()

st.session_state.questions_btn_clicked = False


def load_prompts_from_json(file_path="../Questions/questions-data.json"):
    with open(file_path, 'r', encoding='utf-8') as file:
        prompts = json.load(file)
    return prompts


def questions():
    st.header('Polish e-learning platform ')
    if 'prompts' not in st.session_state:
        prompts = load_prompts_from_json()
        st.session_state.prompts = prompts

    if 'choose_level' not in st.session_state or st.session_state.get('choose_level') is None:
        st.write("wybierzp oziom ")
        level1 = st.checkbox("Level Beginner")
        level2 = st.checkbox("Level Medium")
        level3 = st.checkbox("Level Hard")

        choose_level = None
        if level1:
            choose_level = st.session_state.prompts["beginner_prompt"]
            st.write("Wybrałeś level Beginner")

        if level2:
            choose_level = st.session_state.prompts["medium_prompt"]
            st.write("Wybrales level Medium")
        if level3:
            choose_level = st.session_state.prompts["hard_prompt"]
            st.write("Wybrałes level Hard")
        st.session_state.choose_level = choose_level

    st.write('To jest session state')
    st.write(st.session_state)

    if st.session_state.get('choose_level', None) is not None:
        api_key = os.getenv('GEMINI_API_KEY')

        model = load_model(api_key)
        downloaded_questions = make_prompt(model, st.session_state.choose_level)

        st.write(downloaded_questions)

        questions_list = re.split(r'\n(?=\*\*\d+\. )', downloaded_questions.strip())
        index = 1

        # pokaz wszystko pytania  i odpowiedzi do pytan za pomóc st.write i zachowaj odpowiedzi prawidłowe do pytan w zmiennej answer_to_questions

        # i pozniej w pętli zrób możliwość żeby user mógł wybrac odpowiedź za pomocą checkboxa
        # i na biężąco zliczaj mu punkty, korzystaj z st.session_state zeby zapisywac punkty ucznia (np. st.session_state.points +=1)

        # i na końcu wyświetlaj wynik usera
        # jeszcze jak uzywamy modela zeby uzyskac odpowiedz to mozemy uzyc spinnera jako animacji np tutaj jest pokazane:https://docs.streamlit.io/develop/api-reference/status/st.spinner


        st.write('After answers:')
        for idx, question in enumerate(questions_list):
            question_splitted = question.replace('!', '.').split(".")[1:]
            st.write(question_splitted)


            st.write("---")

            index += 1


questions()

# def cards():
#     if st.button("Choose a level")


# trzeba dokonczyc by ze lepiej  odczytywac odpowiedzi
####################################################
"""dorobic do konca streamlita, oraz dodac bardziej format slownikow zwyczajnie zrobic ladniejsze to na streamlicie jakies
tabelki czy inne zeby dodac do tego i bedzie git"""  # np uzyc .md (markdown)
####################################################
