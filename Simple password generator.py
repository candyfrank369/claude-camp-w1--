import random
import string

SYMBOLS = "!@#$%^&*-_=+"

def generate_password(length):
    if length < 5:
        print("密码长度至少需要 5 位 / Password must be at least 5 characters")
        return None

    # 保证每类字符至少出现一次，最后一位固定为符号
    required = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(SYMBOLS),
    ]

    pool = string.ascii_letters + string.digits + SYMBOLS
    middle = [random.choice(pool) for _ in range(length - 5)]
    last_symbol = random.choice(SYMBOLS)

    password_chars = required + middle
    random.shuffle(password_chars)
    password_chars.append(last_symbol)

    return ''.join(password_chars)

print("1. English")
print("2. 中文")
lang = input("Choose language / 选择语言: ").strip()

if lang == "2":
    prompt = "请输入密码长度："
    result_label = "生成的密码："
else:
    prompt = "Enter password length: "
    result_label = "Generated password: "

length = int(input(prompt))
password = generate_password(length)
if password:
    print(f"{result_label}{password}")
