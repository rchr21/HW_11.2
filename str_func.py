def uppercase_string(input_string):
    """Функция возвращает строку с большой буквы"""
    return input_string.upper()


def capitalize_words(input_string):
    """Преобразует каждое слово в строке, делая заглавной первую букву каждого слова."""
    words = input_string.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)
