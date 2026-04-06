class FoodEngine:
    FOOD_RULES = {
        "osh": ("caution", "1 kichik kosa", ["Ko‘proq sabzavotli variant", "Jigarrang guruchli ovqat"], "AI glyukemik xavfni o‘rta darajada deb baholadi."),
        "somsa": ("caution", "1 dona", ["Tandir sabzavot", "Qaynatilgan tuxum va salat"], "AI yog‘ va oq un ulushi sabab ehtiyotkorlikni tavsiya qildi."),
        "shashlik": ("recommended", "100-120 g", ["Ko‘katli salat", "Bug‘da pishgan sabzavot"], "AI oqsil ulushi yuqoriligini ijobiy belgi sifatida ko‘rdi."),
        "non": ("caution", "1-2 bo‘lak", ["Butun donli non", "Kepakli baton"], "AI tez so‘riluvchi uglevod ulushini hisobga oldi."),
        "cola": ("avoid", "Tavsiya etilmaydi", ["Suv", "Shakarsiz limonli ichimlik"], "AI yuqori shakar yuklamasini xavfli deb topdi."),
    }

    def __init__(self, meal_name):
        self.meal_name = meal_name.strip().lower()

    def analyze(self):
        label, portion, alternatives, explanation = self.FOOD_RULES.get(self.meal_name, ("recommended", "Mo‘tadil porsiya", ["Ko‘proq sabzavot qo‘shish", "Shakarsiz ichimlik"], "AI ushbu taom uchun keskin xavf aniqlamadi, ammo porsiya nazoratini tavsiya qiladi."))
        return {"label": label, "label_display": {"recommended": "Tavsiya etiladi", "caution": "Ehtiyot bilan", "avoid": "Tavsiya etilmaydi"}[label], "portion": portion, "alternatives": alternatives, "alternatives_text": ", ".join(alternatives), "confidence": "AI ishonch ko‘rsatkichi: qoidaviy tahlil", "explanation": explanation}
