class AlertEngine:
    def __init__(self, readings, assessment):
        self.readings = readings
        self.assessment = assessment

    def current_status(self):
        if self.assessment and self.assessment.risk_level == "high":
            return {"level": "critical", "title": "AI signal", "message": "AI yuqori xavf va muntazam monitoring ehtiyojini qayd etdi."}
        if [item for item in self.readings if float(item.value) > 8.5]:
            return {"level": "warning", "title": "AI xavfsizlik ogohlantirishi", "message": "AI noodatiy yuqori ko‘rsatkichlarni sezdi. Qo‘shimcha o‘lchov va shifokor bilan aloqa tavsiya etiladi."}
        return {"level": "info", "title": "AI sog‘liq monitoringi faol", "message": "Joriy ko‘rsatkichlar bo‘yicha keskin signal aniqlanmadi, kuzatuv davom etmoqda."}
