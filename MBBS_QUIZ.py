import streamlit as st

# Initialize session state variables
if "score" not in st.session_state:
    st.session_state.score = 0
if "question_index" not in st.session_state:
    st.session_state.question_index = 0

questions = [
    {
        "question": "Which cranial nerve controls the majority of the eye movements?",
        "options": ["Optic nerve", "Oculomotor nerve", "Trochlear nerve", "Abducens nerve"],
        "answer": "Oculomotor nerve"
    },
    {
        "question": "Which structure connects the two cerebral hemispheres?",
        "options": ["Corpus callosum", "Thalamus", "Pons", "Basal ganglia"],
        "answer": "Corpus callosum"
    }
    # Add more questions here...
]

def check_answer(selected_option):
    correct_answer = questions[st.session_state.question_index]["answer"]
    
    if selected_option == correct_answer:
        st.success("✅ Correct! +4 points")
        st.session_state.score += 4  # Add 4 points for correct answer
    else:
        st.error(f"❌ Wrong! The correct answer is {correct_answer}. (-1 point)")
        st.session_state.score -= 1  # Deduct 1 point for incorrect answer
    
    # Move to the next question
    st.session_state.question_index += 1

# Display the current question
if st.session_state.question_index < len(questions):
    q = questions[st.session_state.question_index]
    st.write(f"**Q{st.session_state.question_index + 1}: {q['question']}**")
    
    selected_option = st.radio("Choose an answer:", q["options"], key=st.session_state.question_index)
    
    if st.button("Submit Answer"):
        check_answer(selected_option)
        st.rerun()  # Refresh app to show next question

else:
    st.write(f"🎉 **Quiz Completed!** Your final score is **{st.session_state.score}**")
    if st.button("Restart Quiz"):
        st.session_state.score = 0
        st.session_state.question_index = 0
        st.rerun()
