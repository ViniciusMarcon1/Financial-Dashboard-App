# 💸 Financial Dashboard App 

An open-source personal tool to seamlessly consult, interact with, and visualize your financial data.

---

## 📝 Description

The Financial Dashboard App serves as an all-in-one solution for managing your personal finances. It allows you to upload your bank statements in CSV format, automatically analyzes your transactions, and presents the insights through an interactive dashboard. You can categorize your purchases and explore detailed financial overviews, making it easier to understand and manage your spending.

---

## 📚 Index

- [Installation](#installation)
- [Usage](#usage)
- [Contact](#contact)


---

## 🚀 Installation

1. First Clone The repository with: 

```bash
git clone https://github.com/ViniciusMarcon1/Financial-Dashboard-App.git
cd financial_dashboard_app
```

2. Them create and start a virtual enviroment with venv

- For MacOS/Linux:
```bash 
python -m venv venv
source venv/bin/activate
```

- For Windowns:
```bash 
python -m venv venv
venv\Scripts\activate
```

3. Install all the Dependencies 

```bash 
pip install streamlit pandas numpy plotly numpy seaborn
```

4. Run the app

```bash 
streamlit run main.py
```

## Usage 

The Financial Dashboard App is extremely intuitive and easy to use. The expected file format is a CSV containing four essential columns:
- Date — the date of the transaction.
- Amount — the value or amount of the transaction.
- Description — a brief description, typically including the name of the vendor or entity involved.
- Debit/Credit — indicates whether the transaction is a debit or credit.

On the Financial Dashboard page, you’ll be able to apply various filters to the data you’ve uploaded and explore multiple charts and visual tools to assist with your analysis.

## Contact 

For more information contact me at: 
- https://www.linkedin.com/in/vinicius-marcon/