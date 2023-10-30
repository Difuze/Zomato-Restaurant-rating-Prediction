import streamlit as st
import pandas as pd
import pickle
# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

# Load the saved model
with open('model1.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Create a Streamlit app
st.title('Restaurant Rating Prediction')

# Collect user input
online_order = st.selectbox('Online Order (Yes/No):', ['Yes', 'No'])
book_table = st.selectbox('Book Table (Yes/No):', ['Yes', 'No'])
location = st.text_input('Location:')
city = st.text_input('City:')
type1 = st.text_input('Type:')
votes = st.number_input('Votes:', value=0)
cost = st.number_input('Cost:', value=0)
rest_type_count = st.number_input('Rest Type Count:', value=0)

# Create a DataFrame with user input
user_input = pd.DataFrame({
    "online_order": [online_order],
    "book_table": [book_table],
    "location": [location],
    "votes": [votes],
    "cost": [cost],
    "type": [type1],
    "city": [city],
    "rest_type_count": [rest_type_count]
})

if st.button('Predict'):
    # Make predictions using the loaded model
    prediction = model.predict(user_input)
    st.write(f'Predicted Target: {prediction[0]}')


    if prediction[0] == 0:
        st.write("Poor Ratings")
    elif prediction[0] == 1:
        st.write("It can be better")
    elif prediction[0] == 2:
        st.write("Good")
    elif prediction[0] == 3:
        st.write("Very Good")
    elif prediction[0] == 4:
        st.write("Excellent")
    else:
        st.write("Fantastic")