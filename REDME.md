📱 Smartphone Addiction Risk Prediction

Project Overview

The Smartphone Addiction Risk Prediction project is a machine learning application developed to predict the level of smartphone addiction risk among teenagers.

The application uses information such as academic performance, social interactions, depression level, sleep, exercise, daily smartphone usage, and time spent on education to generate a predicted risk level.

The model classifies the risk into three categories:

 🟢 Low Risk
 🟠 Moderate Risk
 🔴 High Risk

The project demonstrates how data science and machine learning can be used to identify patterns related to smartphone use and provide an early risk indication.

🎯 Project Objectives

The main objectives of this project are to:

 Develop a machine learning model for smartphone addiction risk prediction.
 Use lifestyle and behavioral factors to identify patterns associated with smartphone use.
 Apply feature engineering to improve the prediction process.
 Build an interactive Streamlit application.
 Display prediction probabilities for each risk category.
 Demonstrate a practical application of data science and machine learning.

📊 Input Features

The application uses the following features:

| Feature                      | Description                                  |
| ---------------------------- | -------------------------------------------- |
| Gender                       | Gender of the user                           |
| Academic Performance         | Academic performance score                   |
| Social Interactions          | Level of social interaction                  |
| Depression Level             | Depression-related score used in the dataset |
| Sleep Hours                  | Average hours of sleep                       |
| Exercise Hours               | Average hours spent exercising               |
| Daily Smartphone Usage Hours | Daily smartphone usage                       |
| Time on Education Hours      | Time spent on educational activities         |

Engineered Features

Additional features are calculated from the input data:

Sleep Deficit – estimates the difference between 9 hours and reported sleep.
Exercise-to-Usage Ratio – compares exercise time with smartphone usage time.
Education-to-Usage Ratio – compares education time with smartphone usage time.

🤖 Machine Learning Model

The project uses a trained Logistic Regression classification model to predict smartphone addiction risk.

Two saved files are required:

```text
logistic_addiction_classifier (1).pkl
addiction_preprocessor (1).pkl
```

The preprocessor transforms the user input into the format required by the trained machine learning model.

🖥️ Application

The application was developed using Streamlit.

The user enters the required information through an interactive interface and clicks:

Predict Addiction Risk

The application then displays:

1. The predicted addiction risk level.
2. The probability of each risk category.

🛠️ Technologies Used

 Python
 Pandas
 Scikit-learn
 Joblib
 Streamlit
 Jupyter Notebook
 GitHub

📁 Project Structure

```text
smartphone-addiction-risk-prediction/
│
├── app.py
├── logistic_addiction_classifier (1).pkl
├── addiction_preprocessor (1).pkl
├── requirements.txt
└── README.md
```

 ▶️ How to Run the Application

 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

 2. Open the project folder

```bash
cd smartphone-addiction-risk-prediction
```

 3. Install the required packages

```bash
pip install -r requirements.txt
```

 4. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your web browser.

 ⚠️ Disclaimer

This project is intended for **educational and screening purposes only**. The prediction is based on the information entered into the application and should not be considered a medical or psychological diagnosis.

The results should be interpreted carefully and should not replace assessment or guidance from a qualified professional.

 👩‍💻 Author

Tabitha Koech

Aspiring Data Scientist | Science Educator | Data Analytics & Machine Learning

This project was developed as part of my practical learning and application of Data Science, Artificial Intelligence, and Machine Learning skills.
