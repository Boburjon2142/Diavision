from ai_engine.services.food_engine import FoodEngine


def analyze_food(meal_name):
    return FoodEngine(meal_name).analyze()
