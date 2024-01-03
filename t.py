import random
import string

def generate_text(length):
    all_characters = string.ascii_letters + string.digits
    random_text = ''.join(random.choice(all_characters) for _ in range(length))
    return random_text

text = generate_text(1000)
print(text)