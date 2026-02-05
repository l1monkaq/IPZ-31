def process_data(text):
    if not text.strip():
        return "Помилка: введіть текст"
    
    words = len(text.split())
    chars = len(text)
    return f"Слів: {words}, Символів: {chars}"