import streamlit as st
import pandas as pd

def calculate_cows_score(cows_data):
    score = 0
    for k, v in cows_data.items():
        score += v
    return score


st.title("COWS Score Calculator")
st.markdown("""
    ## Clinical Opiate Withdrawal Scale (COWS) Score Calculator
    This Streamlit app calculates the COWS score for opiate withdrawal, which is used to assess the severity of withdrawal symptoms in patients undergoing treatment for opiate addiction. The COWS score is calculated based on 11 parameters, with higher scores indicating more severe withdrawal symptoms. Please provide the necessary information below to calculate the COWS score.
""")

cows_data = {}
cows_data['resting_pulse_rate'] = st.number_input("1. Resting Pulse Rate", value=0)
cows_data['sweating'] = st.slider("2. Sweating", 0, 3, 0)
cows_data['restlessness'] = st.slider("3. Restlessness", 0, 3, 0)
cows_data['pupil_size'] = st.slider("4. Pupil Size", 0, 5, 0)
cows_data['bone_joint_aches'] = st.slider("5. Bone or Joint Aches", 0, 4, 0)
cows_data['runny_nose_tearing'] = st.slider("6. Runny Nose or Tearing", 0, 4, 0)
cows_data['gi_upset'] = st.slider("7. GI Upset", 0, 4, 0)
cows_data['tremor'] = st.slider("8. Tremor", 0, 4, 0)
cows_data['yawning'] = st.slider("9. Yawning", 0, 4, 0)
cows_data['anxiety_irritability'] = st.slider("10. Anxiety or Irritability", 0, 3, 0)
cows_data['gooseflesh_skin'] = st.slider("11. Gooseflesh Skin", 0, 3, 0)

if st.button("Calculate COWS Score"):
    score = calculate_cows_score(cows_data)
    st.write(f"### COWS Score: {score}")
    if score < 5:
        st.write("Mild withdrawal")
    elif score < 13:
        st.write("Moderate withdrawal")
    elif score < 25:
        st.write("Moderately severe withdrawal")
    else:
        st.write("Severe withdrawal")
