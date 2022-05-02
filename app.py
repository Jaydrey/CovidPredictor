import streamlit as st
import  pickle
from typing import List

filename = './rfc_model.pkl'
model = pickle.load(open(filename, 'rb'))

def predict_covid_result(sample_input: List[int]) -> str:
    predict_result = model.predict([sample_input])
    if predict_result[0]==1:
        output = "There is a higher possibility of you having COVID-19!"
    else:
        output = "You have a lower possibility of contracting COVID-19"

    return output


def convert_input_numeric(info: List[str])->List[int]:
    num_info = [1 if info[x]=='Yes' else 0 for x in range(len(info)-1)]
    if 'covid' in info[-1]:
        test_condition = 2
    elif 'abroad' in info[-1]:
        test_condition = 0
    else:
        test_condition = 1
    num_info.append(test_condition)

    return num_info

def main():

    st.write(
        "# **COVID-19** Test Predictor  \n"
    )
    st.write(
        "Please **fill** in the form below!\n"
    )
    with st.form(key='covid-form'):
        headache = st.selectbox("Do you have a headache?", ('Yes', 'No'))
        sore_throat = st.selectbox("Do you have a sore throat", ('Yes', 'No'))
        short_breath = st.selectbox("Do you experience shortness of breath?", ('Yes', 'No'))
        over_60 = st.selectbox("Are you 60 years or above?", ('Yes', 'No'))
        situation = st.selectbox("Choose one that relates to you", ('been in contact with confirmed covid patient', 'been abroad', 'Other'))
        fever = st.selectbox("Do you have a fever?", ('Yes', 'No'))
        # cough = st.selectbox("Do you often cough?", ('Yes', 'No'))
        submit = st.form_submit_button(label='Submit')

    if submit:
        conv_input = convert_input_numeric([fever, sore_throat, short_breath, headache, over_60, situation])
        result = predict_covid_result(conv_input)
        st.success(result)
        st.info("Get tested today to confirm your status! Thank you")
    
    # st.text_area()

if __name__ == '__main__':
    main()