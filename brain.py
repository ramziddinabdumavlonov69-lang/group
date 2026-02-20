
from memory import Memory

memory = Memory()

def process_input(text):
    text_lower = text.lower()

    # Agar foydalanuvchi fakt kiritayotgan bo‘lsa
    if "mening" in text_lower and "nima" not in text_lower:
        memory.add_memory("fact", text)
        return "Ma'lumot saqlandi."

    # Savol bo‘lsa
    if "nima" in text_lower:
        keyword = text_lower.replace("nima", "").strip()
        results = memory.search_memory(keyword)

        if results:
            answer = results[0][0]
        else:
            answer = "Ma'lumot topilmadi."

        memory.add_log(text, answer)
        return answer

    return "Tushunmadim. Qaytadan yozing."
