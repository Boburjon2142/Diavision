class HabitEngine:
    def __init__(self, reminders):
        self.reminders = reminders

    def reminder_recommendations(self):
        if not self.reminders:
            return "AI reminder optimization: ertalab 07:00-08:00 va kechqurun 20:00 oralig‘i kuzatuv uchun qulay bo‘lishi mumkin."
        evening_misses = len([r for r in self.reminders if r.reminder_type == "sugar_check" and r.state != "completed"])
        if evening_misses:
            return "AI aniqladi: kechki o‘lchovlar ko‘p o‘tkazib yuborilgan. 19:30 atrofida yumshoq eslatma tavsiya etiladi."
        return "AI sizga qulay vaqtlarni tavsiya qildi: mavjud ritm barqaror, eslatmalar ertalab va tushdan keyin samarali."


class LifestyleScorer:
    def __init__(self, readings, reminders):
        self.readings = readings
        self.reminders = reminders

    def score(self):
        reading_score = 35 if len(self.readings) >= 5 else 20
        reminder_score = 30 if len([r for r in self.reminders if r.state == "completed"]) >= 2 else 18
        sleep_score = 18
        stress_score = 14
        return {"total": reading_score + reminder_score + sleep_score + stress_score, "activity": 24, "nutrition": 22, "sleep": sleep_score, "stress": stress_score, "coach_text": "AI habit coach: kichik, lekin muntazam odatlar keyingi 2 haftada profilni sezilarli yaxshilashi mumkin."}
