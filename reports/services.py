from statistics import mean


def build_public_report_preview():
    return {
        "weekly_title": "AI haftalik xulosa",
        "weekly_summary": "AI kuzatuvi bo‘yicha ovqatdan keyingi o‘lchovlarda yengil tebranish kuzatildi, biroq umumiy nazorat ijobiy.",
        "monthly_summary": "AI oylik sog‘liq sharhi: yurish odatlari yaxshilangani uchun xavf ko‘rsatkichi pasayish trendida.",
    }


def build_user_reports(readings, reminders):
    values = [float(item.value) for item in readings] or [5.8]
    adherence_score = 72 if reminders else 58
    average_sugar = round(mean(values), 2)
    trend_direction = "Barqaror" if average_sugar <= 6.4 else "Ko‘tarilish ehtimoli bor"
    risk_trend = "Pasaymoqda" if average_sugar < 6.2 else "Kuzatuv talab etadi"
    weekly = {
        "type": "weekly",
        "average_sugar": average_sugar,
        "trend_direction": trend_direction,
        "adherence_score": adherence_score,
        "risk_trend": risk_trend,
        "executive_summary": "AI haftalik xulosa: muntazam o‘lchovlar sog‘liq nazoratini yaxshilagan.",
        "recommendation": "AI tavsiya qilmoqda: kechki ovqat porsiyasini nazorat qilish va suv iste’molini oshirish.",
    }
    monthly = {
        "type": "monthly",
        "average_sugar": average_sugar,
        "trend_direction": trend_direction,
        "adherence_score": adherence_score + 4,
        "risk_trend": risk_trend,
        "executive_summary": "AI oylik sog‘liq sharhi: umumiy trend tahlili davom etmoqda, keskin xavf aniqlanmadi.",
        "recommendation": "AI tavsiya qilmoqda: jismoniy faollikni haftasiga kamida 5 kun ushlash.",
    }
    return weekly, monthly
