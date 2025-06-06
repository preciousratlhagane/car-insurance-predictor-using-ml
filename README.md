# Improving Car Insurance Premium Accuracy with Predictive Analytics

## 🗞️ Table of Contents
* [Introduction](#introduction)
* [Dataset](#dataset)
* [Project Structure](#project-structure)
* [Installation](#️installation)
* [App Deployment](#app-deployment)
* [Results](#results)
* [Technologies Used](#technologies-used)
* [Future Improvements](#future-improvements)
* [License](#license)


--------
## 💭 Introduction<a class="anchor" id="introduction"></a>
A small South African insurance provider wants to improve how it sets insurance premiums for new and existing customers. The current pricing strategy uses basic demographic data and manual risk assessments, often leading to inconsistent pricing, customer dissatisfaction, and potential revenue loss due to underpricing or overpricing. 


--------
## 📔 Dataset<a class="anchor" id="dataset"></a>
> **Note**: The dataset used in this project was generated with the assistance of ChatGPT to simulate realistic datasets. The techniques and models used here are relevant and can be used with real-world data. 

- **Number of records:** 15000 customers
- **Key Features:** 
    - Customer demographics: Age, Employment Status, Credit Score, Marital Status
    - Driving history: Number of Accidents, Number of Claims, Years Driving
    - Vehicle information: Make, Model, Manufacture Year, Annual Mileage, Anti-Theft Device
    - Policy information: Policy Term, Vehicle Usage, Credit Category


--------
## 🗃️ Project Structure <a class="anchor" id="project-structure"></a>

```
├── LICENSE            <- Open-source license if one is chosen
├── README.md          <- The top-level README for developers using this project
├── streamlit
│   └── app.py
├── assets             <- Contains images and visual assets for documentation/app
├── data
│   ├── processed      <- The final, canonical data sets for modelling
│   └── raw            <- The original, immutable data dump
│
├── models             <- Trained and serialised models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         Generated with `pip freeze > requirements.txt`
│
└── src                         <- Source code for this project
    │
    ├── __init__.py             <- Makes src a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modelling
    │
    │    
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    │
    └── services                <- Service classes to connect with external platforms, tools, or APIs
        └── __init__.py 
```

--------
## ⚙️ Installation <a class="anchor" id="installation"></a>

```bash
# Clone the repository
git clone https://github.com/your_username/project_name.git 
cd car-insurance-predictor-using-ml

# Create virtual environment (optional)
python -m venv env
# Activate the environment
# On macOS/Linux:
source env/bin/activate
# On Windows:
env\Scripts\activate

#Install dependencies
pip install --upgrade pip  # Optional but recommended
pip install -r requirements.txt
```


--------
## ⌨️ App Deployment <a class="anchor" id="app-deployment"></a>

An interactive app has been built using Streamlit to demonstrate the prediction of car insurance premiums. Through a simple UI, users can input customer and vehicle information and receive a premium estimate based on the trained machine learning model. 

### To run the app locally

```bash
streamlit run streamlit/home.py
```

The app will open in your browser at: 

```plaintext
http://localhost:8501
```

### 🌐 Live Demonstration

A live version of the app is hosted at: *app_link*

### 🖥️ App Preview


--------
## Results <a class="anchor" id="results"></a>
The best-performing model was **Ridge model**, achieving:
- MAE: 15,72
- RMSE: 20,35
- R² Score: 0,99

> **Note**: The unusually high R² score is largely because the premiums in the original dataset were determined using a predefined formula based on the numerical input features. This means the model is essentially learning to approximate that formula by adding categorical features. In a real-world scenario with more variability and noise, performance metrics are expected to be lower but remain a good indication of predictive power. 


--------
## Technologies Used <a class="anchor" id="technologies-used"></a>
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black) ![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white) ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white) ![Seaborn](https://img.shields.io/badge/Seaborn-4c72b0?style=for-the-badge&logo=python&logoColor=white) ![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white) 


--------
## 🧪 Future Improvements <a class="anchor" id="future-improvements"></a>
- Perform hyperparameter tuning with GridSearchCV or Optuna to improve model accuracy
- Integrate real-world datasets(e.g Kaggle, Google Dataset Search, public APIs) to enhance data diversity and quality. 
- Implement user authentication and persistent user history in the Streamlit application


--------
## 📜 License <a class="anchor" id="license"></a>
This project is for educational and demonstration purposes only. You can use, modify, and build upon it.


