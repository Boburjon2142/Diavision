from ai_engine.services.trend_engine import TrendEngine


def get_tracker_summary(readings):
    return TrendEngine(readings).build_summary()
