# Name: Deep Agarwal
# PRN: 1302250670
# Task: Traditional vs ML - High Net-Worth Profile Check

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

excel_file = "Loan approval data.xlsx"
df = pd.read_excel(excel_file)

X = df[["Income", "Credit_Score", "Existing_Loan"]]
y = df["Approved"]

model = DecisionTreeClassifier(max_depth=2, random_state=99)
model.fit(X, y)

def traditional_rules(income, credit_score, existing_loan):
    if income >= 75000 and credit_score >= 750:
        return "Priority Approved (Traditional Rule)"
    return "Standard Evaluation Required (Traditional Rule)"

applicant = [[82000, 760, 5000]]
ml_res = "Approved (ML)" if model.predict(applicant)[0] == 1 else "Rejected (ML)"
trad_res = traditional_rules(82000, 760, 5000)

print(f"Traditional Decision : {trad_res}")
print(f"ML Decision          : {ml_res}")
