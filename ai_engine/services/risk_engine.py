class RiskEngine:
    def __init__(self, payload):
        self.payload = payload

    def evaluate(self):
        score = 8
        factors = []
        age = self.payload["age"]
        bmi = float(self.payload["bmi"])
        sugar = float(self.payload["blood_sugar"])
        waist = self.payload["waist_cm"]
        if age >= 45:
            score += 18
            factors.append({"name": "Yosh omili", "score": 18, "reason": "45 yoshdan yuqori foydalanuvchilarda xavf oshadi."})
        if bmi >= 30:
            score += 22
            factors.append({"name": "BMI yuqori", "score": 22, "reason": "Tana vazni ortishi insulin rezistentligiga ta’sir qilishi mumkin."})
        elif bmi >= 25:
            score += 12
            factors.append({"name": "BMI nazorat talab qiladi", "score": 12, "reason": "Ortiqcha vazn metabolik yuklamani oshiradi."})
        if waist >= 100:
            score += 12
            factors.append({"name": "Bel aylanasi", "score": 12, "reason": "Qorin atrofidagi yog‘ to‘planishi xavf belgisi bo‘lishi mumkin."})
        if self.payload["family_history"]:
            score += 14
            factors.append({"name": "Oilaviy tarix", "score": 14, "reason": "Oilada diabet bo‘lsa kuzatuv kuchaytiriladi."})
        if sugar >= 7:
            score += 22
            factors.append({"name": "Qon shakari", "score": 22, "reason": "AI qon shakarida ko‘tarilish belgilarini aniqladi."})
        elif sugar >= 6:
            score += 10
            factors.append({"name": "Qon shakari chegaraviy", "score": 10, "reason": "Chegaraviy o‘zgarishlar kuzatuv talab qiladi."})
        if self.payload["physical_activity"].lower() in ["kam", "past", "harakatsiz"]:
            score += 10
            factors.append({"name": "Faollik past", "score": 10, "reason": "Kam harakat metabolik riskni oshiradi."})
        if float(self.payload["sleep_hours"]) < 6:
            score += 6
            factors.append({"name": "Uyqu yetarli emas", "score": 6, "reason": "Uyqu rejimi buzilishi glyukozaga ta’sir qilishi mumkin."})
        if self.payload["stress_level"].lower() in ["yuqori", "high", "kuchli"]:
            score += 8
            factors.append({"name": "Stress", "score": 8, "reason": "Yuqori stress gormonal muvozanatga ta’sir qiladi."})
        score = min(score, 96)
        if score >= 65:
            risk_level = "high"
            warning = "Yuqori xavf qayd etildi. Yaqin kunlarda shifokor bilan maslahatlashish tavsiya etiladi."
            next_steps = "Laborator tahlillar, shifokor qabuliga yozilish va 7 kunlik monitoring rejasini boshlash."
        elif score >= 35:
            risk_level = "medium"
            warning = "O‘rta xavf aniqlangan. Turmush tarzini tuzatish va muntazam nazorat muhim."
            next_steps = "14 kunlik shakar kuzatuvi, uyqu va ovqatlanish rejimini yaxshilash."
        else:
            risk_level = "low"
            warning = "Joriy xavf past ko‘rinmoqda, ammo profilaktik nazoratni davom ettiring."
            next_steps = "Profilaktik monitoring va sog‘lom odatlarni saqlash."
        explanation = self._build_explanation(risk_level, score, factors)
        recommendations_text = self._recommendations(risk_level, sugar)
        return {"risk_level": risk_level, "risk_percentage": score, "factors": factors[:5], "explanation": explanation, "recommendations_text": recommendations_text, "next_steps": next_steps, "warning": warning}

    def _build_explanation(self, risk_level, score, factors):
        factor_names = ", ".join(factor["name"].lower() for factor in factors[:3]) or "asosiy xavf omillari topilmadi"
        label = "yuqori" if risk_level == "high" else "o‘rta" if risk_level == "medium" else "past"
        return f"AI sizning xavf profilingizni tahlil qildi. Joriy baho {score}% va daraja {label} deb belgilandi. Asosiy omillar: {factor_names}. Bu natija tashxis emas, balki profilaktik ko‘rsatkichdir."

    def _recommendations(self, risk_level, sugar):
        base = ["Kun davomida suv iste’molini nazorat qiling.", "Haftasiga kamida 150 daqiqa yengil-jadal jismoniy faollikni rejalashtiring."]
        if risk_level == "high":
            base.extend(["Shifokor ko‘rigiga yoziling va laborator tahlillarni rejalashtiring.", "Ovqatdan keyingi shakar o‘lchovlarini 7 kun davomida yozib boring."])
        elif float(sugar) >= 6:
            base.append("Shirin ichimliklar va oq unli mahsulotlarni kamaytiring.")
        else:
            base.append("Barqaror odatlarni davom ettiring va oyiga kamida bir marta riskni yangilang.")
        return "\n".join(base)
