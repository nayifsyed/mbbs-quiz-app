import streamlit as st

# Define quiz questions as a list of dictionaries
questions = [
    {"question": "Which cranial nerve controls the majority of the eye movements?",
     "options": ["Optic nerve", "Oculomotor nerve", "Trochlear nerve", "Abducens nerve"],
     "answer": "Oculomotor nerve"},
    {"question": "Which structure connects the two cerebral hemispheres?",
     "options": ["Corpus callosum", "Thalamus", "Pons", "Basal ganglia"],
     "answer": "Corpus callosum"},
    {"question": "What is the primary function of the juxtaglomerular apparatus in the kidney?",
     "options": ["Regulate sodium balance", "Produce renin", "Control urine concentration", "Filter blood"],
     "answer": "Produce renin"},
    # Add more questions here following the same format
]

# Initialize session state for score and question index
if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.question_index = 0

st.title("🩺 MBBS Quiz - Test Your Knowledge!")
st.sidebar.header("Quiz Progress")
st.sidebar.write(f"Score: {st.session_state.score}")
st.sidebar.progress(st.session_state.question_index / len(questions))

# Display the current question
if st.session_state.question_index < len(questions):
    q = questions[st.session_state.question_index]
    st.subheader(q["question"])
    user_answer = st.radio("Select an answer:", q["options"], index=None)
    
    if st.button("Submit Answer"):
        if user_answer == q["answer"]:
            st.success("✅ Correct Answer!")
            st.session_state.score += 4  # 4 marks for correct answer
        else:
            st.error(f"❌ Wrong Answer! Correct answer is: {q['answer']}")
            st.session_state.score -= 1  # -1 for incorrect answer
        
        st.session_state.question_index += 1
        st.experimental_rerun()

else:
    st.subheader("🎉 Quiz Completed!")
    st.write(f"Your final score is **{st.session_state.score}/{len(questions) * 4}**")
    st.button("Restart Quiz", on_click=lambda: st.session_state.update(score=0, question_index=0))
