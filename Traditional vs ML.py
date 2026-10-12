# Name: Mohammad Rehan
# PRN:1302250270
# Task: Traditional vs ML - Debt-to-Income Constraint

import pandas as pd
from sklearn.tree import DecisionTreeClassifier

excel_file = "Loan approval data.xlsx"
df = pd.read_excel(excel_file)

X = df[["Income", "Credit_Score", "Existing_Loan"]]
y = df["Approved"]

model = DecisionTreeClassifier(max_depth=3, min_samples_split=2)
model.fit(X, y)

def traditional_rules(income, credit_score, existing_loan):
    dti_ratio = existing_loan / income
    if dti_ratio < 0.35 and credit_score >= 700:
        return "Approved (Traditional Rule)"
    return "Rejected (Traditional Rule)"

applicant = [[60000, 715, 18000]]
ml_res = "Approved (ML)" if model.predict(applicant)[0] == 1 else "Rejected (ML)"
trad_res = traditional_rules(60000, 715, 18000)

print(f"Traditional Decision : {trad_res}")
print(f"ML Decision          : {ml_res}")
