# Improving Car Insurance Premium Pricing through Predictive Modelling

## Table of Contents
* Introduction
* Dataset
* Project Structure
* Installation
* Usage 
* Results 
* Technologies Used
* Future Improvements

## Introduction
A small South African insurance provider is looking to improve how it sets insurance premiums for new and existing customers. The current pricing strategy uses basic demographic data and manual risk assessments which often leads to inconsistent pricing, customer dissatisfaction, and potential revenue loss due to underpricing or overpricing. 

## Dataset
> **Note**: The dataset used in this project was generated with the assistance of ChatGPT to simulate realistic datasets. The techniques and models used here are relevant and can be used with real-world data. 

- Number of records: 15000 rows
- Features: Age, Employment status, Credit score, Number of accidents, Number of claims, and vehicle information such as make, year, mileage


## 🗃️ Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── README.md          <- The top-level README for developers using this project
├── app.py
├── assets             <- Contains images and visual assets for documentation/app
├── data
│   ├── processed      <- The final, canonical data sets for modeling
│   └── raw            <- The original, immutable data dump
│
├── models             <- Trained and serialized models, model predictions, or model summaries
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
│                         generated with `pip freeze > requirements.txt`
│
└── src                         <- Source code for this project
    │
    ├── __init__.py             <- Makes src a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
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
## ⚙️ Installation

```bash
# Clone the repository
git clone git clone https://github.com/your_username/project_name.git 
cd car-insurance-predictor-using-ml

# Create virtual environmentt (optional)
python -m venv env
source env/bin/activate # On Windows use: env\Scripts\activate

#Install dependencies
pip install -r requirements.txt
```

## App Deployment

An interactive app has been built using **Streamlit** to demonstrate the prediction of car insurance premiums. Users can input customer and vehicle information through a simple UI and recieve a premium estimate based on the trained machine learning model. 

### To run the app locally

```bash
cd streamlit
streamlit run app.py
```

The app will open in your browser at: 

```plaintext
http://localhost:8501
```

### 🌐 Live Demonstration

A live version of the app is hosted at: *app_link*

### App Preview

## Results

## Technologies Used

## Future Improvements

## Contributors

## License
This project is for educational and demonstration purposes only. Feel free to use, modify, and build upon it.


