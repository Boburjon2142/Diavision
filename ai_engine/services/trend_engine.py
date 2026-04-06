from statistics import mean


class TrendEngine:
    def __init__(self, readings):
        self.readings = readings

    def build_summary(self):
        if not self.readings:
            return {"average": "—", "insight": "AI trend insight: ma’lumot yetarli emas, dastlabki o‘lchovlarni qo‘shing.", "trend": "Boshlanish bosqichi"}
        values = [float(item.value) for item in self.readings]
        avg = round(mean(values), 2)
        direction = "barqaror"
        if len(values) >= 3 and values[0] > values[-1] + 0.7:
            direction = "ko‘tarilish"
        elif len(values) >= 3 and values[0] + 0.7 < values[-1]:
            direction = "pasayish"
        unstable = max(values) - min(values) > 3
        insight = f"AI trend insight: o‘rtacha ko‘rsatkich {avg} mmol/L, umumiy yo‘nalish {direction}."
        if unstable:
            insight += " AI beqaror tebranishni sezdi va ovqatlanish vaqti bilan o‘lchovni tekshirishni tavsiya qiladi."
        return {"average": avg, "insight": insight, "trend": direction}
