from ai_engine.services.habit_engine import HabitEngine


def recommend_time_windows(reminders):
    return HabitEngine(reminders).reminder_recommendations()
