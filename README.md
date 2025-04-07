# 📉 Customer Churn Prediction

A machine learning project to predict whether a telecom customer will churn (stop using the service) based on their demographic and usage data. This project uses the [Telco Customer Churn dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) and a Random Forest Classifier to classify customers as "Churn" or "No Churn," while also providing churn probabilities.

---

## ✨ Features

- **Data Preprocessing**: Cleans data by handling missing values, encoding categorical variables, and scaling numerical features.  
- **Model**: Employs a Random Forest Classifier for binary classification (Churn: Yes/No).  
- **Evaluation**: Measures performance with accuracy, F1-score, and a confusion matrix visualization.  
- **Feature Importance**: Highlights key factors driving churn, such as tenure and monthly charges.  
- **Interactive Prediction**: Allows users to input a test set index to predict churn and view the probability.

---

## 📂 Project Structure

CustomerChurnPrediction/
├── main/
│   └── churn_prediction.py       # Main script to run the model
├── churn_prediction.ipynb        # Jupyter Notebook for exploration
├── WA_Fn-UseC_-Telco-Customer-Churn.csv  # Dataset (to be downloaded)
└── README.md                     # Project documentation

---

## 🛠️ Setup

### Prerequisites
- **Python**: Version 3.6 or higher  
- A terminal or command-line interface

### Required Libraries
- `pandas`  
- `scikit-learn`  
- `matplotlib`  
- `seaborn`

### Install Libraries
Install the required libraries using pip:

```bash
pip install pandas scikit-learn matplotlib seaborn

Download the Dataset
Download the dataset from Kaggle.  

Place the file WA_Fn-UseC_-Telco-Customer-Churn.csv in the project root directory (CustomerChurnPrediction/).

 How to Run
Navigate to the Project Directory:
Open a terminal and change to the project directory:
bash

cd CustomerChurnPrediction

Run the Script:
Execute the main script to train the model and interact with predictions:
bash

python main/churn_prediction.py

 Example Output
When you run the script, you’ll see the following:

Accuracy: 0.7984
F1-Score: 0.5538

Top 5 Features:
tenure                0.1712
MonthlyCharges        0.1403
TotalCharges          0.1309
Contract_Two year     0.0701
Contract_One year     0.0502

Test set contains 1409 customers (index 0 to 1408)

Enter the customer index to predict churn (or -1 to exit): 0
Customer at index 0:
Prediction: No Churn
Churn Probability: 12.34%

 License
This project is licensed under the MIT License.

