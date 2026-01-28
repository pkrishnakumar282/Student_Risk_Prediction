import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression

df = pd.read_csv("student-mat.csv")

features = ["studytime", "failures", "absences", "G1", "G2"]
df = df[features + ["G3"]]

def risk_label(score):
    if score >= 15:
        return "Low"
    elif score >= 10:
        return "Medium"
    else:
        return "High"

df["Risk_Level"] = df["G3"].apply(risk_label)
df.drop("G3", axis=1, inplace=True)

le = LabelEncoder()
df["Risk_Level"] = le.fit_transform(df["Risk_Level"])

X = df.drop("Risk_Level", axis=1)
y = df["Risk_Level"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)

model = LogisticRegression(
    solver='lbfgs',
    max_iter=1000
)

model.fit(X_train, y_train)

joblib.dump(model, "student_model.pkl")
joblib.dump(scaler, "scaler.pkl")
joblib.dump(le, "label_encoder.pkl")

print("✅ Model trained and saved successfully")
