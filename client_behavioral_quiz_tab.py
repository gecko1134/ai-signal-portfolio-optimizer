import streamlit as st
from behavioral_questionnaire import QUESTIONS, calculate_behavior_score

def render_behavior_quiz():
    st.title("Client Behavioral Questionnaire")

    responses = []
    raw_responses = []

    for q in QUESTIONS:
        choice = st.radio(q["question"], list(q["options"].keys()), key=q["question"])
        responses.append(q["options"][choice])
        raw_responses.append((q["question"], choice))

    if st.button("Submit Assessment"):
        profile, score = calculate_behavior_score(responses)
        st.success(f"Identified Behavioral Profile: {profile} (Score: {score})")