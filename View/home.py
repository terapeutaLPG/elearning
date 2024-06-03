import json
import os
import re
import streamlit as st
import sys

sys.path.append('./../Questions')
from gemini import load_dotenv, load_model, make_prompt

###############################################################

load_dotenv()

def load_prompts_from_json(file_path="../Questions/questions-data.json"):
    with open(file_path, 'r', encoding='utf-8') as file:
        prompts = json.load(file)
    return prompts

if 'prompts' not in st.session_state:
    st.session_state.prompts = load_prompts_from_json()

if 'level_difficulty' not in st.session_state:
    st.session_state.level_difficulty = None

if 'choose_level' not in st.session_state:
    st.session_state.choose_level = None

if 'show_levels' not in st.session_state:
    st.session_state.show_levels = False

if 'points' not in st.session_state:
    st.session_state.points = 0

if 'answered_questions' not in st.session_state:
    st.session_state.answered_questions = {}

if 'questions' not in st.session_state:
    st.session_state.questions = None

if 'correct_answers' not in st.session_state:
    st.session_state.correct_answers = None

def handle_checkbox_change():
    levels = ["beginner_prompt", "medium_prompt", "hard_prompt"]
    for i, level in enumerate(levels, 1):
        if st.session_state.get(level):
            st.session_state.choose_level = st.session_state.prompts[level]
            st.session_state.level_difficulty = i

def display_level_options():
    if st.button('Pokaż poziomy'):
        st.session_state.show_levels = True

    if st.session_state.show_levels:
        st.checkbox("Level Beginner", key="beginner_prompt", on_change=handle_checkbox_change)
        st.checkbox("Level Medium", key="medium_prompt", on_change=handle_checkbox_change)
        st.checkbox("Level Hard", key="hard_prompt", on_change=handle_checkbox_change)

def split_by_odpowiedzi(content):
    pattern = r'(?<=\bodpowiedzi\b)[\s\S]*'
    parts = re.split(pattern, content, maxsplit=1)
    st.write('Parts', parts)
    return parts

def load_questions():
    if 'choose_level' in st.session_state and st.session_state.choose_level is not None:
        api_key = os.getenv('GEMINI_API_KEY')

        with st.spinner('Pobieranie pytań...'):
            model = load_model(api_key)
            downloaded_questions = make_prompt(model, st.session_state.choose_level)
        if 'odpowiedzi' in downloaded_questions.lower():
            questions_section, answers_section = split_by_odpowiedzi(downloaded_questions)
            st.write('Section')
            st.write(questions_section)
            questions = re.findall(r"\d+\.\s*(.*?)\n\((A|B|C|D)\)", questions_section)
            try:
                correct_answers = eval(re.search(r"odpowiedzi\s*=\s*(\[[^\]]*\])", answers_section).group(1))
            except AttributeError:
                correct_answers = []
            st.write(questions)
            st.write(correct_answers)
            if len(questions) != len(correct_answers):
                st.error("Mismatch between the number of questions and the number of provided correct answers.")
                return
            for idx, (question_text, choices) in enumerate(zip(questions, correct_answers), start=1):
                st.markdown(f"**Question {idx}:** {question_text}")
                user_answer = st.radio(f"Select your answer for question {idx}:", ['A', 'B', 'C', 'D'])
                if st.button('Submit Answer', key=f'sub{idx}'):
                    if user_answer == choices:
                        st.success('Correct answer!')
                    else:
                        st.error('Wrong answer!')

def main():
    st.header('Polish e-learning platform')
    st.subheader('Wybierz poziom jaki w jakim chciałbyś ćwiczyć ?')

    display_level_options()

    if st.session_state.level_difficulty:
        level_msg = ['beginner', 'medium', 'hard'][st.session_state.level_difficulty - 1]
        st.write(f"Wybrałeś level {level_msg}")

    if st.session_state.choose_level:
        load_questions()

main()
st.write(st.session_state)

# import json
# import os
# import re
# import streamlit as st
# import sys
#
# sys.path.append('./../Questions')
# from gemini import load_dotenv, load_model, make_prompt
#
# ###############################################################
#
# load_dotenv()
#
# def load_prompts_from_json(file_path="../Questions/questions-data.json"):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         prompts = json.load(file)
#     return prompts
#
# if 'prompts' not in st.session_state:
#     st.session_state.prompts = load_prompts_from_json()
#
# if 'level_difficulty' not in st.session_state:
#     st.session_state.level_difficulty = None
#
# if 'choose_level' not in st.session_state:
#     st.session_state.choose_level = None
#
# if 'show_levels' not in st.session_state:
#     st.session_state.show_levels = False
#
# if 'points' not in st.session_state:
#     st.session_state.points = 0
#
# if 'answered_questions' not in st.session_state:
#     st.session_state.answered_questions = {}
#
# if 'questions' not in st.session_state:
#     st.session_state.questions = None
#
# if 'correct_answers' not in st.session_state:
#     st.session_state.correct_answers = None
#
# def handle_checkbox_change():
#     levels = ["beginner_prompt", "medium_prompt", "hard_prompt"]
#     for i, level in enumerate(levels, 1):
#         if st.session_state.get(level):
#             st.session_state.choose_level = st.session_state.prompts[level]
#             st.session_state.level_difficulty = i
#             st.rerun()
#
# def display_level_options():
#     if st.button('Pokaż poziomy'):
#         st.session_state.show_levels = True
#
#     if st.session_state.show_levels:
#         st.checkbox("Level Beginner", key="beginner_prompt", on_change=handle_checkbox_change)
#         st.checkbox("Level Medium", key="medium_prompt", on_change=handle_checkbox_change)
#         st.checkbox("Level Hard", key="hard_prompt", on_change=handle_checkbox_change)
#
# def split_by_odpowiedzi(content):
#     pattern = r'(?<=\bodpowiedzi\b)[\s\S]*'
#     parts = re.split(pattern, content, maxsplit=1)
#     st.write('Parts', parts)
#     return parts
#
# def load_questions():
#     if 'choose_level' in st.session_state and st.session_state.choose_level is not None:
#         api_key = os.getenv('GEMINI_API_KEY')
#
#         with st.spinner('Pobieranie pytań...'):
#             model = load_model(api_key)
#             downloaded_questions = make_prompt(model, st.session_state.choose_level)
#         if 'odpowiedzi' in downloaded_questions.lower():
#             questions_section, answers_section = split_by_odpowiedzi(downloaded_questions)
#             st.write('Section')
#             st.write(questions_section)
#             questions = re.findall(r"\d+\.\s*(.*?)\n\((A|B|C|D)\)", questions_section)
#             try:
#                 correct_answers = eval(re.search(r"odpowiedzi\s*=\s*(\[[^\]]*\])", answers_section).group(1))
#             except AttributeError:
#                 correct_answers = []
#             st.write(questions)
#             st.write(correct_answers)
#             if len(questions) != len(correct_answers):
#                 st.error("Mismatch between the number of questions and the number of provided correct answers.")
#                 return
#             for idx, (question_text, choices) in enumerate(zip(questions, correct_answers), start=1):
#                 st.markdown(f"**Question {idx}:** {question_text}")
#                 user_answer = st.radio(f"Select your answer for question {idx}:", ['A', 'B', 'C', 'D'])
#                 if st.button('Submit Answer', key=f'sub{idx}'):
#                     if user_answer == choices:
#                         st.success('Correct answer!')
#                     else:
#                         st.error('Wrong answer!')
#
# def main():
#     st.header('Polish e-learning platform')
#     st.subheader('Wybierz poziom jaki w jakim chciałbyś ćwiczyć ?')
#
#     display_level_options()
#
#     if st.session_state.level_difficulty:
#         level_msg = ['beginner', 'medium', 'hard'][st.session_state.level_difficulty - 1]
#         st.write(f"Wybrałeś level {level_msg}")
#
#     if st.session_state.choose_level:
#         load_questions()
#
# main()
# st.write(st.session_state)











#innnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn
# import json
# import os
# import re
# import streamlit as st
# import sys
#
# sys.path.append('./../Questions')
# from gemini import load_dotenv, load_model, make_prompt
#
# ###############################################################
#
# load_dotenv()
#
#
# def load_prompts_from_json(file_path="../Questions/questions-data.json"):
#     with open(file_path, 'r', encoding='utf-8') as file:
#         prompts = json.load(file)
#     return prompts
#
#
# if 'prompts' not in st.session_state:
#     st.session_state.prompts = load_prompts_from_json()
#
# if 'level_difficulty' not in st.session_state:
#     st.session_state.level_difficulty = None
#
# if 'choose_level' not in st.session_state:
#     st.session_state.choose_level = None
#
# if 'show_levels' not in st.session_state:
#     st.session_state.show_levels = False
#
# if 'points' not in st.session_state:
#     st.session_state.points = 0
#
# if 'answered_questions' not in st.session_state:
#     st.session_state.answered_questions = {}
#
# if 'questions' not in st.session_state:
#     st.session_state.questions = None
#
# if 'correct_answers' not in st.session_state:
#     st.session_state.correct_answers = None
#
#
# def handle_checkbox_change():
#     levels = ["beginner_prompt", "medium_prompt", "hard_prompt"]
#     for i, level in enumerate(levels, 1):
#         if st.session_state.get(level):
#             st.session_state.choose_level = st.session_state.prompts[level]
#             st.session_state.level_difficulty = i
#             st.experimental_rerun()
#
#
# def display_level_options():
#     if st.button('Pokaż poziomy'):
#         st.session_state.show_levels = True
#
#     if st.session_state.show_levels:
#         st.checkbox("Level Beginner", key="beginner_prompt", on_change=handle_checkbox_change)
#         st.checkbox("Level Medium", key="medium_prompt", on_change=handle_checkbox_change)
#         st.checkbox("Level Hard", key="hard_prompt", on_change=handle_checkbox_change)
#
#
# def split_by_odpowiedzi(content):
#     # This regex pattern looks for any occurrence of 'odpowiedzi' followed by any characters until a newline or end of string
#     pattern = r'(?<=\bodpowiedzi\b)[\s\S]*'
#
#     # Perform the split using re.split which provides parts before and after the keyword
#     parts = re.split(pattern, content, maxsplit=1)
#     st.write('Parts', parts)
#     return parts
#
#
# def load_questions():
#     if 'choose_level' in st.session_state and st.session_state.choose_level is not None:
#         api_key = os.getenv('GEMINI_API_KEY')
#
#         with st.spinner('Pobieranie pytań...'):
#             model = load_model(api_key)
#             downloaded_questions = make_prompt(model, st.session_state.choose_level)
#             # st.write(downloaded_questions)
#         # Split into questions and answers sections
#         if 'odpowiedzi' in downloaded_questions.lower():
#             questions_section, answers_section = split_by_odpowiedzi(downloaded_questions)
#             st.write('Section')
#             st.write(questions_section)
#             # Find questions using a tailored pattern (adjusted as needed)
#             questions = re.findall(r"\d+\.\s*(.*?)\n\((A|B|C|D)\)", questions_section)
#
#             # Try to extract answers, handle possible absence
#             try:
#                 # Assumes answers are listed directly in a Python list format as shown in the output
#                 correct_answers = eval(re.search(r"odpowiedzi\s*=\s*(\[[^\]]*\])", answers_section).group(1))
#             except AttributeError:
#                 correct_answers = []  # No answers found, handle this appropriately in your logic
#             st.write(questions)
#
#             st.write(correct_answers)
#
#             # Check if the number of questions and answers match
#             if len(questions) != len(correct_answers):
#                 st.error("Mismatch between the number of questions and the number of provided correct answers.")
#                 return
#
#             # Display questions and options
#             for idx, (question_text, choices) in enumerate(zip(questions, correct_answers), start=1):
#                 st.markdown(f"**Question {idx}:** {question_text}")
#                 user_answer = st.radio(f"Select your answer for question {idx}:", ['A', 'B', 'C', 'D'])
#
#                 # Placeholder for submitting answers
#                 if st.button('Submit Answer', key=f'sub{idx}'):
#                     if user_answer == choices:
#                         st.success('Correct answer!')
#                     else:
#                         st.error('Wrong answer!')
#
#         # Optionally, display the total correct answers at the end
#
#
# def main():
#     st.header('Polish e-learning platform')
#     st.subheader('Wybierz poziom jaki w jakim chciałbyś ćwiczyć ?')
#
#     display_level_options()
#
#     if st.session_state.level_difficulty:
#         level_msg = ['beginner', 'medium', 'hard'][st.session_state.level_difficulty - 1]
#         st.write(f"Wybrałeś level {level_msg}")
#
#     if st.session_state.choose_level:
#         load_questions()
#
#
# main()
# st.write(st.session_state)
