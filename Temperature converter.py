LANGUAGES = {
    "1": {
        "name": "中文",
        "title": "温度转换器",
        "option1": "1. 摄氏 → 华氏",
        "option2": "2. 华氏 → 摄氏",
        "choose": "请选择 (1 或 2): ",
        "input_c": "请输入摄氏温度: ",
        "input_f": "请输入华氏温度: ",
        "invalid": "无效选择，请输入 1 或 2",
        "cold": "提醒：天气寒冷，记得多穿衣服！",
        "hot": "提醒：天气炎热，记得多喝水！",
    },
    "2": {
        "name": "English",
        "title": "Temperature Converter",
        "option1": "1. Celsius → Fahrenheit",
        "option2": "2. Fahrenheit → Celsius",
        "choose": "Choose (1 or 2): ",
        "input_c": "Enter Celsius temperature: ",
        "input_f": "Enter Fahrenheit temperature: ",
        "invalid": "Invalid choice. Please enter 1 or 2.",
        "cold": "Reminder: It's cold outside, dress warmly!",
        "hot": "Reminder: It's hot outside, stay hydrated!",
    },
    "3": {
        "name": "日本語",
        "title": "温度変換器",
        "option1": "1. 摂氏 → 華氏",
        "option2": "2. 華氏 → 摂氏",
        "choose": "選択してください (1 または 2): ",
        "input_c": "摂氏温度を入力してください: ",
        "input_f": "華氏温度を入力してください: ",
        "invalid": "無効な選択です。1 または 2 を入力してください。",
        "cold": "注意：寒いので、暖かくして出かけましょう！",
        "hot": "注意：暑いので、こまめに水分補給をしましょう！",
    },
}

def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def temperature_advice(celsius, lang):
    if celsius <= 10:
        print(lang["cold"])
    elif celsius >= 35:
        print(lang["hot"])

def select_language():
    print("请选择语言 / Select language / 言語を選択:")
    for key, value in LANGUAGES.items():
        print(f"  {key}. {value['name']}")
    choice = input(">>> ").strip()
    return LANGUAGES.get(choice, LANGUAGES["1"])

def main():
    lang = select_language()
    print()
    print(lang["title"])
    print(lang["option1"])
    print(lang["option2"])

    choice = input(lang["choose"]).strip()

    if choice == "1":
        c = float(input(lang["input_c"]))
        f = celsius_to_fahrenheit(c)
        print(f"{c}°C = {f:.2f}°F")
        temperature_advice(c, lang)
    elif choice == "2":
        f = float(input(lang["input_f"]))
        c = fahrenheit_to_celsius(f)
        print(f"{f}°F = {c:.2f}°C")
        temperature_advice(c, lang)
    else:
        print(lang["invalid"])

if __name__ == "__main__":
    main()
