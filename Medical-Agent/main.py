import streamlit as st # pyright: ignore[reportMissingImports]

st.title("👨‍⚕️ Medical Agent")
st.write("Welcome to the Medical Agent application!"
         " This application assists with medical inquiries and provides relevant information.")

symptoms_advice = {
    "fever": "A fever is a temporary increase in your body temperature, often due to an illness. "
             "Stay hydrated and rest. If your fever exceeds 103°F (39.4°C) or lasts more than three days, "
             "consult a healthcare professional.",
    "cough": "A cough can be caused by various factors including infections, allergies, or irritants. "
             "If your cough persists for more than three weeks or is accompanied by chest pain, "
             "consult a healthcare professional.",
    "headache": "Headaches can be caused by stress, dehydration, or other factors. "
                "If you experience severe headaches, sudden onset headaches, or headaches accompanied by other symptoms "
                "consult a healthcare professional.",
    "stomachache": "Stomachaches can result from indigestion, infections, or other causes. "
                   "If your stomachache is severe, persistent, or accompanied by other symptoms like vomiting or fever, "
                   "consult a healthcare professional.",
    "fatigue": "Fatigue can be caused by various factors including lack of sleep, stress, or medical conditions. "
               "If you experience persistent fatigue that does not improve with rest, consult a healthcare professional.",
    "nausea": "Nausea can be caused by infections, medications, or other factors. "
              "If your nausea is severe, persistent, or accompanied by other symptoms like vomiting or abdominal pain, "
              "consult a healthcare professional.",
    "dizziness": "Dizziness can result from dehydration, low blood sugar, or other causes. "
                 "If you experience severe dizziness, fainting, or dizziness accompanied by other symptoms, "
                 "consult a healthcare professional.",
    "sore throat": "A sore throat can be caused by infections or irritants. "
                   "If your sore throat is severe, persistent, or accompanied by difficulty swallowing or breathing, "
                   "consult a healthcare professional.",
    "shortness of breath": "Shortness of breath can be a sign of various medical conditions. "
                           "If you experience sudden or severe shortness of breath, chest pain, or difficulty breathing, "
                           "seek emergency medical attention immediately.",
    "chest pain": "Chest pain can be a symptom of serious conditions such as heart attack. "
                  "If you experience sudden, severe, or persistent chest pain, especially if accompanied by other symptoms "
                  "like shortness of breath, sweating, or nausea, seek emergency medical attention immediately.",
    "back pain": "Back pain can result from muscle strain, poor posture, or other causes. "
                 "If your back pain is severe, persistent, or accompanied by other symptoms like numbness or weakness, "
                 "consult a healthcare professional.",
    "allergic reaction": "Allergic reactions can range from mild to severe. "
                         "If you experience symptoms such as swelling of the face or throat, difficulty breathing, "
                         "or a rapid heartbeat, seek emergency medical attention immediately.",
    "dehydration": "Dehydration occurs when your body loses more fluids than it takes in. "
                   "If you experience severe thirst, dry mouth, dizziness, or confusion, seek medical attention promptly.",
    "insomnia": "Insomnia is difficulty falling or staying asleep. "
                 "If you experience persistent insomnia that affects your daily life, consult a healthcare professional.",
    "anxiety": "Anxiety is a normal response to stress, but excessive anxiety can interfere with daily life. "
               "If you experience persistent anxiety that affects your daily functioning, consult a healthcare professional.",
    "depression": "Depression is a common mental health condition that affects mood and behavior. "
                  "If you experience persistent feelings of sadness, loss of interest in activities, or changes in sleep or appetite, "
                  "consult a healthcare professional.",
    "high blood pressure": "High blood pressure (hypertension) can increase the risk of heart disease and stroke. "
                           "If you have high blood pressure, follow your healthcare provider's recommendations for lifestyle changes and medications.",
    "diabetes": "Diabetes is a chronic condition that affects how your body processes blood sugar. "
                "If you have diabetes, follow your healthcare provider's recommendations for diet, exercise, and medications.",
    "asthma": "Asthma is a chronic condition that affects the airways in your lungs. "
              "If you have asthma, follow your healthcare provider's recommendations for managing your symptoms and avoiding triggers."
}          

user_input = st.text_input("Enter your symptoms or medical inquiry:")
if user_input:
    input_lower = user_input.lower().strip()
    advice_found = False
    for key in symptoms_advice:
        if key in input_lower:
            st.write(f"**Advice for {key}:** {symptoms_advice[key]}")
            advice_found = True
    if not advice_found:
        # Display default response if no specific advice is found
        st.subheader("🤖 General Advice")
        st.write("Sorry, I don't have specific advice for your inquiry. "
                 "Please consult a healthcare professional for personalized medical advice.")
# Button to reset and ask new question
if st.button("Ask New Symptom"):
    st.rerun()
else:
    st.info("Please enter your symptoms or medical inquiry above to receive advice.")

# Sidebar with additional information
st.sidebar.title("About Medical Agent")
st.sidebar.write("👨‍⚕️ Medical Agent is a virtual health assistant designed to provide general medical advice based on user symptoms.")
st.sidebar.write("⚠️ Disclaimer: The information provided by Medical Agent is for informational purposes only and is not a substitute for professional medical advice.")