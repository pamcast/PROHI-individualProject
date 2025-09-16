import streamlit as st

st.set_page_config(
    page_title="PROHI Dashboard",
    page_icon="👋",
)

# Sidebar configuration
st.sidebar.image("./assets/heart.jpg", width=600)
st.sidebar.success("Select a tab above.")

# # Page information
#Add a page called About
page = st.sidebar.radio("Select a page:", ["Home", "About"])

if page == "Home":
    st.write("# Welcome to PROHI Dashboard! 👋")

    st.markdown(
        """
        ## Aims

        After completing the course the student should be able to:
        - explain basic project management methods
        - be able to account for success factors in Health Informatics projects
        - understand basic methods and tools in the field of data science and machine learning
        - explain process models for data mining projects
        - explain the difference between rule-based methods and machine learning methods
        - apply basic project management methods
        - work in an international multidisciplinary project group
        - independently lead and implement a limited project in health informatics - document the steps in the design of a prototype for a health informatics project
        - apply the steps in a process model for data mining projects
        - apply methods from the field of text mining on different types of health informatics problems
        - explain and argue for their positions regarding the implementation of a health informatics project
        - explain how to work with sensitive health information in a safe and ethical way.

        """
    )
    # # DATAFRAME MANAGEMENT
    import pandas as pd
    import numpy as np

    df = pd.read_csv("heart.csv")
    st.dataframe(df)

    heart_count= df["HeartDisease"].value_counts()[1]
    total_patients= df.shape[0]
    patient_coronary = heart_count / total_patients *100

    heart_count_no= df["HeartDisease"].value_counts()[0]
    patient_coronary_no = heart_count_no / total_patients *100

    col1.metric("Patients with Heart Disease (%)", f"{patient_coronary:.2f}", border=True)
    col2.metric("Patients without Heart Disease (%)", f"{patient_coronary_no:.2f}", border=True)


elif page == "About":
    st.title("Pamela Castillo")
    st.markdown("""
        The project I conducted during the Data Science course was based on a Kaggle dataset containing 11 features, 
        aimed at predicting heart disease. Before performing exploratory data analysis (EDA), I started with 
        data preparation by identifying missing values and renaming features. During the EDA, I used descriptive 
        statistics to answer questions that helped me understand the dataset better. The data was not imbalanced. 
        Then, I performed clustering using K-means and hierarchical clustering. Finally, I applied supervised 
        machine learning models, including Random Forests, Decision Trees, Support Vector Machines, and Logistic 
        Regression, to classify patients with and without cardiovascular disease. The best-performing model was 
        the Decision Tree, which achieved the highest accuracy and F1 score.
    """)




###UNCOMMENT THE CODE BELOW TO SEE EXAMPLE OF INPUT WIDGETS




