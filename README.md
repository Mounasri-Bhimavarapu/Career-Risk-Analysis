# Career Risk Analyzer

A Streamlit final-year project prototype with:
- Machine-learning risk classification (Random Forest)
- Role-based skill-gap review
- Actionable recommendations
- SQLite assessment storage
- Dashboard and assessment history

## Setup
1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Install dependencies:
   `pip install -r requirements.txt`
4. Run:
   `streamlit run app.py`

## Important limitation
`career_risk_data.csv` contains synthetic, generated records and rule-assigned labels for demonstrating the end-to-end pipeline. The displayed model score is only a held-out score on that synthetic dataset. It does not establish accuracy, fairness, or predictive validity for real careers. Replace it with a documented, representative, consented dataset and validate the features, labels, thresholds, and recommendations before making real-world claims.

## Database
The app creates `career_risk.db` automatically in the working directory and stores submitted assessments locally.
