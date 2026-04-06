def build_recommendation_lines(factors, payload):
    lines = []
    if factors:
        lines.append("AI asosiy xavf omillarini aniqladi va ularni kamaytirish bo‘yicha ustuvor yo‘nalishlarni tuzdi.")
    if payload.get("family_history"):
        lines.append("Oilaviy tarix mavjudligi sabab profilaktik laborator nazoratni tezlashtirish foydali bo‘lishi mumkin.")
    if float(payload.get("blood_sugar", 0)) >= 6:
        lines.append("Qon shakaridagi chegara holatlari uchun ovqatdan keyingi monitoring alohida ahamiyatga ega.")
    lines.append("Bu tavsiyalar shifokor maslahatining o‘rnini bosmaydi.")
    return lines
