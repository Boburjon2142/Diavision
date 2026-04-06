from ai_engine.services.risk_engine import RiskEngine


def run_risk_assessment(cleaned_data):
    return RiskEngine(cleaned_data).evaluate()
