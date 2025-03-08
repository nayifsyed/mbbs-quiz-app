import streamlit as st

def quiz_app():
    # Display "Code By Nayif" at the top
    st.markdown("### Code By Nayif")
    st.write("---")  # Add a horizontal line for separation

    # App title and description
    st.title("🩺 MBBS Quiz App")
    st.write("Test your medical knowledge with this interactive quiz! ✅")
    
    # Questions and Answers Data
    questions = [
        (" Which cranial nerve controls the majority of the eye movements?", ["Optic nerve", "Oculomotor nerve", "Trochlear nerve", "Abducens nerve"], "Oculomotor nerve"),
        (" Which structure connects the two cerebral hemispheres?", ["Corpus callosum", "Thalamus", "Pons", "Basal ganglia"], "Corpus callosum"),
        (" What is the primary function of the juxtaglomerular apparatus in the kidney?", ["Regulate sodium balance", "Produce renin", "Control urine concentration", "Filter blood"], "Produce renin"),
        (" Which blood vessel supplies the liver with oxygenated blood?", ["Portal vein", "Hepatic artery", "Inferior vena cava", "Celiac trunk"], "Hepatic artery"),
        (" Which part of the brain is responsible for regulating body temperature?", ["Cerebrum", "Cerebellum", "Hypothalamus", "Medulla oblongata"], "Hypothalamus"),
        (" Which enzyme catalyzes the rate-limiting step of glycolysis?", ["Hexokinase", "Phosphofructokinase", "Pyruvate kinase", "Glucose-6-phosphatase"], "Phosphofructokinase"),
        (" What is the primary function of chylomicrons?", ["Transport glucose", "Transport lipids", "Break down proteins", "Synthesize cholesterol"], "Transport lipids"),
        (" Which amino acid is a precursor for serotonin?", ["Glycine", "Tyrosine", "Tryptophan", "Phenylalanine"], "Tryptophan"),
        (" What is the main site of gluconeogenesis?", ["Brain", "Liver", "Muscles", "Kidney"], "Liver"),
        (" Which enzyme is deficient in phenylketonuria (PKU)?", ["Tyrosinase", "Phenylalanine hydroxylase", "Glucose-6-phosphate dehydrogenase", "Lactase"], "Phenylalanine hydroxylase"),
        (" Which type of necrosis is characteristic of tuberculosis?", ["Coagulative", "Liquefactive", "Caseous", "Fibrinoid"], "Caseous"),
        (" Which genetic mutation is responsible for sickle cell disease?", ["Glu → Val", "Glu → Lys", "Val → Gly", "Lys → Asp"], "Glu → Val"),
        (" What is the most common cause of myocardial infarction?", ["Atherosclerosis", "Hypertension", "Diabetes", "Aortic stenosis"], "Atherosclerosis"),
        (" Which tumor marker is elevated in hepatocellular carcinoma?", ["CEA", "CA-125", "Alpha-fetoprotein (AFP)", "PSA"], "Alpha-fetoprotein (AFP)"),
        (" Which type of hypersensitivity reaction is responsible for anaphylaxis?", ["Type I", "Type II", "Type III", "Type IV"], "Type I"),
        (" Which bacteria produce toxins that block neurotransmitter release, leading to flaccid paralysis?", ["Clostridium botulinum", "Clostridium tetani", "Bacillus anthracis", "Corynebacterium diphtheriae"], "Clostridium botulinum"),
        (" Which antibiotic inhibits bacterial DNA gyrase?", ["Penicillin", "Tetracycline", "Fluoroquinolones", "Macrolides"], "Fluoroquinolones"),
        (" Which antiviral drug is a neuraminidase inhibitor used to treat influenza?", ["Acyclovir", "Oseltamivir", "Zidovudine", "Ritonavir"], "Oseltamivir"),
        (" What is the mechanism of action of beta-blockers?", ["Block calcium channels", "Inhibit angiotensin II", "Block beta-adrenergic receptors", "Activate GABA receptors"], "Block beta-adrenergic receptors"),
        (" Which drug is used to treat Plasmodium falciparum malaria?", ["Chloroquine", "Artemisinin", "Amphotericin B", "Rifampin"], "Artemisinin"),
        (" What is the most common cause of community-acquired pneumonia?", ["Staphylococcus aureus", "Klebsiella pneumoniae", "Streptococcus pneumoniae", "Mycoplasma pneumoniae"], "Streptococcus pneumoniae"),
        (" Which artery is most commonly affected in an ischemic stroke?", ["Middle cerebral artery", "Anterior cerebral artery", "Posterior cerebral artery", "Vertebral artery"], "Middle cerebral artery"),
        (" What is the primary treatment for diabetic ketoacidosis?", ["Oral hypoglycemics", "IV insulin and fluids", "Beta-blockers", "Diuretics"], "IV insulin and fluids"),
        (" Which ECG finding is most characteristic of hyperkalemia?", ["ST depression", "Peaked T waves", "Prolonged QT interval", "Delta wave"], "Peaked T waves"),
        (" What is the first-line treatment for anaphylactic shock?", ["Hydrocortisone", "Epinephrine", "Antihistamines", "Beta-blockers"], "Epinephrine"),
        (" Which fetal heart rate pattern is associated with umbilical cord compression?", ["Early decelerations", "Late decelerations", "Variable decelerations", "Sinusoidal pattern"], "Variable decelerations"),
        (" Which hormone maintains the corpus luteum during early pregnancy?", ["Estrogen", "LH", "Progesterone", "hCG"], "hCG"),
        (" Which stage of labor involves the delivery of the baby?", ["First stage", "Second stage", "Third stage", "Fourth stage"], "Second stage"),
        (" Which complication is most commonly associated with preeclampsia?", ["Eclampsia", "Gestational diabetes", "Placenta previa", "Abruptio placentae"], "Eclampsia"),
        (" What is the most common site of ectopic pregnancy?", ["Cervix", "Ovary", "Ampulla of fallopian tube", "Abdomen"], "Ampulla of fallopian tube")
    ]
    
    # Initialize session state to store answers & score
    if "score" not in st.session_state:
        st.session_state.score = 0
        st.session_state.answered = [False] * len(questions)

    # Display questions
    for idx, (question, options, correct_answer) in enumerate(questions):
        st.subheader(f"Q{idx + 1}: {question}")
        user_answer = st.radio("Choose the correct answer:", options, key=f"q{idx}")
        
        # Submit button for each question
        if st.button(f"Submit Answer {idx + 1}", key=f"submit_{idx}"):
            if not st.session_state.answered[idx]:  # Ensure the question is answered only once
                if user_answer == correct_answer:
                    st.success("✅ Correct!")
                    st.session_state.score += 4
                else:
                    st.error(f"❎ Wrong! The correct answer is {correct_answer}")
                    st.session_state.score -= 1
                st.session_state.answered[idx] = True  # Mark as answered
    
    # Display Final Score
    st.write("---")
    st.subheader(f"🎯 Your Final Score: {st.session_state.score}")

if __name__ == "__main__":
    quiz_app()
