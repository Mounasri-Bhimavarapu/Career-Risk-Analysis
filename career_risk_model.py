import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer

DATA_FILE = "career_risk_data.csv"
FEATURES = [
    "education_score", "skill_score", "experience_months", "project_score",
    "certification_score", "communication_score", "aptitude_score",
    "interview_score", "job_demand"
]
RISK_LABELS = {0: "Low Risk", 1: "Medium Risk", 2: "High Risk"}

def train_model():
    """Train on the included synthetic demonstration data; replace with validated data for research use."""
    data = pd.read_csv(DATA_FILE)
    X = data[FEATURES]
    y = data["career_risk"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    model = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("classifier", RandomForestClassifier(
            n_estimators=150, random_state=42, class_weight="balanced"
        ))
    ])
    model.fit(X_train, y_train)
    score = accuracy_score(y_test, model.predict(X_test))
    return model, score

def predict(model, values):
    row = pd.DataFrame([values], columns=FEATURES)
    prediction = int(model.predict(row)[0])
    probabilities = model.predict_proba(row)[0]
    classes = model.named_steps["classifier"].classes_
    confidence = float(max(probabilities)) * 100
    return prediction, RISK_LABELS[prediction], confidence
