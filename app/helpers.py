def generate_text(length):
    """Генерирует рандомный текст заданной длинны."""
    all_characters = string.ascii_letters + string.digits
    random_text = ''.join(random.choice(all_characters) for _ in range(length))
    return random_text
