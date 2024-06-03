import streamlit as st
import json
import os
import sys
from dotenv import load_dotenv

# Dodaj ścieżkę do katalogu API, aby można było zaimportować gemini
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../API')))

from View.gemini import load_model, make_prompt

# Ładowanie zmiennych środowiskowych
load_dotenv(os.path.join(os.path.dirname(__file__), '../../.env'))


def load_questions(file_path):
    if not os.path.exists(file_path):
        st.error(f"Plik {file_path} nie istnieje!")
        return None

    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def display_questions(questions):
    if questions is None:
        st.error("Brak pytań do wyświetlenia!")
        return

    for index, question in enumerate(questions, start=1):
        st.write(f"{index}. {question}")
        st.write("---")


def main():
    st.title("Platforma do Nauki Języków Obcych")

    if "test_started" not in st.session_state:
        st.session_state.test_started = False

    if "difficulty_selected" not in st.session_state:
        st.session_state.difficulty_selected = False

    if not st.session_state.test_started:
        if st.button("Test"):
            st.session_state.test_started = True
    else:
        if not st.session_state.difficulty_selected:
            st.write("Wybierz poziom trudności:")
            if st.button("Beginner"):
                st.session_state.difficulty_selected = "Beginner"
            elif st.button("Medium"):
                st.session_state.difficulty_selected = "Medium"
            elif st.button("Hard"):
                st.session_state.difficulty_selected = "Hard"

        if st.session_state.difficulty_selected:
            # Podaj pełną ścieżkę do pliku JSON
            file_path = os.path.join(os.path.dirname(__file__), '../../Questions/questions-data.json')
            questions_data = load_questions(file_path)

            if questions_data is None:
                st.stop()

            level = st.session_state.difficulty_selected

            # Załaduj model bota Gemini
            api_key = os.getenv('GEMINI_API_KEY')
            model = load_model(api_key)

            if level == "Beginner":
                user_prompt = questions_data['beginner_prompt']
            elif level == "Medium":
                user_prompt = questions_data['medium_prompt']
            elif level == "Hard":
                user_prompt = questions_data['hard_prompt']

            # Wywołaj bota Gemini
            imported_prompt = make_prompt(model, user_prompt)

            # Wyświetl pytania
            st.write("Pytania:")
            display_questions(imported_prompt)


if __name__ == "__main__":
    main()
