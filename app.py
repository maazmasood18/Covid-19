
import os
import sys
import numpy as np
import cv2
from PIL import Image, ImageOps

import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import load_img

from werkzeug.utils import secure_filename
import pickle
import datacodes as datacode

# load model
model = load_model("Covid_TrainedModel.h5")
model2 = pickle.load(open('BoostedRF_Trained.pkl', 'rb'))

def transform_img(file_path):
    print(file_path)
    img = image.load_img(file_path, target_size=(224, 224))

    # Preprocessing the image
    x = np.array(img)
    # x = np.true_divide(x, 255)
    ## Scaling
    x=x/255
    x = np.expand_dims(x, axis=0)
    return x

def prediction2(location, country, gender, age, vis_wuhan, from_wuhan, 
                     symptom1, symptom2, symptom3, symptom4, symptom5, symptom6, diff_sym_hos):
    
    for i in range(datacode.location_len):
        if location == datacode.location_box[i]:
            location = datacode.location_num[i]    

    for i in range(datacode.country_len):
        if country == datacode.country_box[i]:
            country = datacode.country_num[i]

    for i in range(datacode.symptom1_len):
        if symptom1 == datacode.symptom1_box[i]:
            symptom1 = datacode.symptom1_num[i]

    for i in range(datacode.symptom2_len):
        if symptom2 == datacode.symptom2_box[i]:
            symptom2 = datacode.symptom2_num[i]
    
    for i in range(datacode.symptom3_len):
        if symptom3 == datacode.symptom3_box[i]:
            symptom3 = datacode.symptom3_num[i]
    
    for i in range(datacode.symptom4_len):
        if symptom4 == datacode.symptom4_box[i]:
            symptom4 = datacode.symptom4_num[i]   

    values = np.array([[location, country, gender, age, vis_wuhan, from_wuhan, 
                        symptom1, symptom2, symptom3, symptom4, symptom5, symptom6, diff_sym_hos]])
    
    predicted = model2.predict(values)
                                
    print("final_prediction:", predicted)
    
    if predicted == 0:
        pred = "Good/Ok Condition"
    else:
        pred = "Critical Condition"
    return pred


with st.sidebar:
    choose = option_menu("COVID-19", ["Home", "Pandemic", "Diagnosis", "Performance"],
                         icons=['house', 'pencil', 'camera fill', 'kanban', 'book','person lines fill'],
                         menu_icon="Detection-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

# Main function:
def main():    
    if choose == "Home":
        col1, col2 = st.columns( [0.8, 0.2])
        with col1:               # To display the header text using css style
            st.markdown(""" <style> .font {
                font-size:35px ; font-family: 'Cooper Black'; color: Black;} 
                </style> """, unsafe_allow_html=True)
            st.markdown('<p class="font">Impact of Artificial Intelligence in COVID-19 Pandemic: A Comprehensive Review</p>', unsafe_allow_html=True)    
    
    
        st.write("ABSTRACT: -The goals of a health-care system are, to provide effective treatment with minimum cost and risk factors, delivery of medical services on time, and be ready to counter any emergency situation. To achieve these goals, a health-care system must be well prepared. The preparation is depending upon data, and the data scientists to analyze that data. Artificial Intelligence (AI) introduced a novelty in health-care, with its different tools which are built upon Machine Learning (ML) and Deep Learning (DL) algorithms. Besides clinical procedures and treatments, these algorithms are used for analyzing data and provides help in decision making. Similarly, to tackle this pandemic Novel Coronavirus disease 2019 (COVID-19) the computer scientists played their role individually and with the help of biological scientists to provide the solutions related to risk management (How much this pandemic can spread and affect the people), diagnosis of this disease with minimum time and cost and suggesting that which medical treatment should adopt")    
        plogo = Image.open(r'css/home.jpg')
        st.image(plogo, width=700 )
        
        st.markdown(""" <style> .font {
                font-size:35px ; font-family: 'Cooper Black'; color: Black;} 
                </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Medical Treatments</p>', unsafe_allow_html=True)    
        plogo2 = Image.open(r'css/treatments.jpg')
        st.image(plogo2, width=700 )
    
    elif choose == "Pandemic":
        # Front end Elements:
        html_temp = """
            <div style ="background-color:blue;padding:13px">
            <h1 style ="color:white;text-align:center;">Pandemic Spread/ Affect Detection</h1>
            </div>
            """
        # Display aspect of front end
        st.markdown(html_temp, unsafe_allow_html=True)
        location = st.selectbox("location", ('Afghanistan', 'Aichi Prefecture', 'Alappuzha', 'Algeria', 'Amiens', 'Andalusia', 
                'Annecy', 'Araq', 'Arizona', 'Baden-Wuerttemberg', 'Bahrain', 'Barcelona', 
                'Bavaria', 'Beijing', 'Belgium', 'Bern', 'Bois-Guillaume', 'Bordeaux', 'Brest', 
                'California', 'Canary Islands', 'Castellon', 'Castile and Leon', 'Chiba Prefecture', 
                'Chongqing', 'Croatia', 'Dijon', 'Egypt', 'Fo Tan', 'France', 'Frankfurt', 
                'Fujian', 'Fukuoka Prefecture', 'Gansu', 'Gifu Prefecture', 'Guangxi', 'Guilan', 
                'Guizhou', 'Hamburg', 'Haneda', 'Hanoi', 'Hebei', 'Hechi, Guangxi', 'Heilongjiang', 
                'Henan', 'Hesse', 'Ho Chi Minh City', 'Hokkaido', 'Hong Kong', 'Hubei', 'Hunan', 
                'Illinois', 'Inner Mongolia', 'Innsbruck', 'Ishikawa', 'Israel', 'Japan', 'Jiangsu', 
                'Jiangxi', 'Jilin', 'Johor', 'Jonkoping', 'Kanagawa', 'Kathmandu', 'Kerala', 'Kowloon', 
                'Kumamoto City', 'Kumamoto Prefecture', 'Kuwait', 'Kwai Chung', 'Kwun Tong', 'Kyoto', 
                'Langkawi', 'Lapland', 'Lebanon', 'Liaoning', 'Lile', 'London', 'Lyon', 'Macau', 
                'Madrid', 'Malaysia', 'Mallorca', 'Manila', 'Massachusetts', 'Mie', 'Montpellier', 
                'Nagano Prefecture', 'Nagoya City', 'Nantes', 'Nara Prefecture', 'Ngau Chi Wan', 
                'Nice', 'Ningxia', 'Nortern Ireland', 'North Rhine-Westphalia', 'NSW', 
                'Okinawa Prefecture', 'Osaka Prefecture', 'Paris', 'Phillipines', 
                'Preah Sihanouk Province', 'Qom', 'Queensland', 'Rhineland-Palatinate', 
                'Rome', 'Sagamihara', 'Saint-Mande', 'Saitama Prefecture', 'Sapporo', 'Seoul', 
                'Shaanxi', 'Shandong', 'Shanghai', 'Shanxi', 'Shanxi (陕西)', 'Shenzhen, Guangdong', 
                'Sichuan', 'Singapore', 'South Australia', 'South Korea', 'Sri Lanka', 'Strasbourg', 
                'Taiwan', 'Tehran', 'Tenerife', 'Texas', 'Thailand', 'Thanh Hoa', 'Tianjin', 'Tokyo', 
                'Toronto', 'Tsing Yi', 'Tubingen', 'Tyumen', 'UAE', 'UK', 'Valencia', 'Vancouver', 
                'Victoria', 'Vietnam', 'Vinh Phuc', 'Wakayama Prefecture', 'Wales', 'Wan Chai', 
                'Washington', 'Wisconsin', 'Wuhan, Hubei', 'Xinjiang', 'Yau Ma Tei', 'York', 
                'Yunnan', 'Zabaikalsky', 'Zaragoza', 'Zhejiang', 'Zhuhai'))

        country = st.selectbox("country", ('Afghanistan', 'Algeria', 'Australia', 'Austria', 'Bahrain', 'Belgium', 'Cambodia', 
               'Canada', 'China', 'Croatia', 'Egypt', 'Finland', 'France', 'Germany', 'Hong Kong', 
               'India', 'Iran', 'Israel', 'Italy', 'Japan', 'Kuwait', 'Lebanon', 'Malaysia', 'Nepal', 
               'Phillipines', 'Russia', 'Singapore', 'South Korea', 'Spain', 'Sri Lanka', 'Sweden', 
               'Switzerland', 'Taiwan', 'Thailand', 'UAE', 'UK', 'USA', 'Vietnam'))
    
        gender = st.selectbox("gender (Female, Male, NA)", (0, 1, 2))
        age = st.number_input("age")
        vis_wuhan = st.selectbox("vis_wuhan ('No', 'Yes')", (0, 1))
        from_wuhan = st.selectbox("from_wuhan ('No', 'Yes')", (0, 1))
    
        symptom1 = st.selectbox("symptom1", ('chest discomfort', 'chills', 'cold', 'cough', 'cough with sputum', 
                'difficulty breathing', 'fatigue', 'fever', 'flu symptoms', 'headache', 
                'high fever', 'joint pain', 'malaise', 'mild cough', 'mild fever', 'myalgia', 
                'NA', 'nausea', 'physical discomfort', 'reflux', 'runny nose', 'sore body', 
                'sore throat', 'throat discomfort', 'throat pain', 'tired', 'vomiting'))

        symptom2 = st.selectbox("symptom2", ('abdominal pain', ' aching muscles', ' breathlessness', ' chest pain', ' chill', 
                ' chills', ' cold', ' cough', ' coughing', ' diarrhea', ' difficulty breathing', 
                ' fatigue', ' fever', ' headache', ' itchy throat', ' joint pain', ' loss of appetite',
                ' malaise', ' muscle aches', ' muscle pain', ' myalgia', 'NA', ' nasal discharge', 
                ' pneumonia', ' respiratory distress', ' runny nose', ' shortness of breath', 
                ' sneeze', ' sore throat', ' sputum', ' thirst', ' vomiting'))

        symptom3 = st.selectbox("symptom3", ('breathlessness', 'chest pain', 'chills', 'cough', 'diarrhea', 
                'difficult in breathing', 'dyspnea', 'fever', 'flu', 'headache', 'joint pain', 
                'malaise', 'muscle aches', 'muscle cramps', 'muscle pain', 'myalgias', 'NA', 
                'pneumonia', 'runny nose', 'shortness of breath', 'sore throat', 'sputum', 
                'throat discomfort', 'vomiting')) 
    
        symptom4 = st.selectbox("symptom4", ('cough', 'diarrhea', 'dyspnea', 'fever', 'headache', 'heavy head', 'joint pain',
                'malaise', 'NA', 'nausea', 'runny nose', 'sore throat', 'vomiting'))
        
        symptom5 = st.selectbox("symptom5 (Cough, NA, Shortness of Breath, Vomiting)", (0, 1, 2, 3))
        symptom6 = st.selectbox("symptom6 (Diarrhea, NA)", (0, 1))
        diff_sym_hos = st.number_input("diff_sym_hos [sym_on_day - hosp_vis_day]")

        if st.button("Submit"):
            result = prediction2(location, country, gender, age, vis_wuhan, from_wuhan, 
                              symptom1, symptom2, symptom3, symptom4, symptom5, symptom6, diff_sym_hos)
            st.success(f"Prediction : {result}")    
    
    elif choose == "Diagnosis":   
        # Front end Elements:
        html_temp = """
            <div style ="background-color:blue;padding:13px">
            <h1 style ="color:white;text-align:center;">COVID-19 Diagnosis for CT images</h1>
            </div>
            """
        # Display aspect of front end
        st.markdown(html_temp, unsafe_allow_html=True)
    
        st.write("Impact of Artificial Intelligence in COVID-19 Pandemic: A Comprehensive Review")


        file = st.file_uploader("Please upload an image file", type=["jpg", "png"])

        if file is None:
    
            st.text("Please upload an image file")
    
        else:
            uploadedImage = Image.open(file)
            st.image(uploadedImage, use_column_width=True)
            # Save the file path from ./test
            basepath = os.path.dirname(os.path.realpath(__file__))
            file_path = os.path.join(basepath, 'test/', secure_filename(file.name))

            transform_img_data = transform_img(file_path)
            prediction = model.predict(transform_img_data)
            preds=np.argmax(prediction, axis=1)
    
            if np.argmax(prediction) == 0:
                st.write("\n Result: COVID-19 Detected")
            elif np.argmax(prediction) == 1:
                st.write("\n Result: COVID-19 not Detected")
            else:
                st.write("Prediction: other")
    
            st.text("Probability (0: COVID-19, 1: Normal")
            st.write(prediction)
            
    
    elif choose == "Performance":
        col1, col2 = st.columns( [0.8, 0.2])
        with col1:               # To display the header text using css style
            st.markdown(""" <style> .font {
                font-size:35px ; font-family: 'Cooper Black'; color: Black;} 
                </style> """, unsafe_allow_html=True)
            st.markdown('<p class="font">Performance</p>', unsafe_allow_html=True)    
                 # To display brand log
    
        st.write("Algorithm:  DenseNet(Densely Connected Convolutional Networks)")
        st.write("Accuracy % score: 100")             
        plogo = Image.open(r'css/performance.png')
        st.image(plogo, width=700 )
        
        st.write("Algorithm:  Boosted Random Forest)")
        st.write("Accuracy % score: 93.33")           
        plogo2 = Image.open(r'css/models_per.png')
        st.image(plogo2, width=700 )

if __name__ == '__main__':
    main()
        