# Name: Parth Deshmukh
# PRN: 1302250642
# Task: Traditional vs ML - Low Income Segment Evaluation

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

excel_file = "Loan approval data.xlsx"
df = pd.read_excel(excel_file)

X = df[["Income", "Credit_Score", "Existing_Loan"]]
y = df["Approved"]

model = DecisionTreeClassifier(max_depth=4, criterion="entropy", random_state=10)
model.fit(X, y)

def traditional_rules(income, credit_score, existing_loan):
    if income >= 45000 and credit_score >= 690:
        return "Approved (Traditional Rule)"
    return "Rejected (Traditional Rule)"

applicant = [[48000, 700, 22000]]
ml_res = "Approved (ML)" if model.predict(applicant)[0] == 1 else "Rejected (ML)"
trad_res = traditional_rules(48000, 700, 22000)

print(f"Traditional Decision : {trad_res}")
print(f"ML Decision          : {ml_res}")
