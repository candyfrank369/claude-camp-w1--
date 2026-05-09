LANG = {
    "zh": {
        "title": "=== 小费计算器 ===",
        "lang_prompt": "语言 / Language: [1] 中文  [2] English：",
        "lang_invalid": "请输入 1 或 2。",
        "dishes_prompt": "请输入菜品金额（多道菜用空格分隔，如：88 45 32）：",
        "negative_price": "金额不能为负数，请重新输入。",
        "invalid_number": "请输入有效的数字，多道菜用空格分隔。",
        "no_input": "未输入任何菜品金额，程序退出。",
        "tip_prompt": "\n请输入小费比例（%，例如输入 15 表示 15%）：",
        "negative_tip": "小费比例不能为负数，请重新输入。",
        "invalid_tip": "请输入有效的数字。",
        "header": "\n========== 账单明细 ==========",
        "dish_line": "  第 {} 道菜：¥{:.2f}",
        "divider": "─" * 32,
        "meal_total": "  餐费合计：¥{:.2f}",
        "tip_line": "  小费（{}%）：¥{:.2f}",
        "grand_total": "  应付总金额：¥{:.2f}",
        "footer": "================================",
    },
    "en": {
        "title": "=== Tip Calculator ===",
        "lang_prompt": "语言 / Language: [1] 中文  [2] English: ",
        "lang_invalid": "Please enter 1 or 2.",
        "dishes_prompt": "Enter dish prices separated by spaces (e.g. 88 45 32): ",
        "negative_price": "Price cannot be negative. Please try again.",
        "invalid_number": "Invalid input. Use numbers separated by spaces.",
        "no_input": "No prices entered. Exiting.",
        "tip_prompt": "\nEnter tip percentage (e.g. 15 for 15%): ",
        "negative_tip": "Tip percentage cannot be negative. Please try again.",
        "invalid_tip": "Please enter a valid number.",
        "header": "\n========== Bill Summary ==========",
        "dish_line": "  Dish {}: ${:.2f}",
        "divider": "─" * 34,
        "meal_total": "  Subtotal: ${:.2f}",
        "tip_line": "  Tip ({}%): ${:.2f}",
        "grand_total": "  Total: ${:.2f}",
        "footer": "==================================",
    },
}

# 选语言
while True:
    choice = input("语言 / Language: [1] 中文  [2] English：").strip()
    if choice == "1":
        t = LANG["zh"]
        break
    elif choice == "2":
        t = LANG["en"]
        break
    else:
        print("请输入 1 或 2 / Please enter 1 or 2.")

print(f"\n{t['title']}\n")

# 输入菜品金额
dishes = []
while True:
    entry = input(t["dishes_prompt"]).strip()
    parts = entry.split()
    valid = True
    temp = []
    for p in parts:
        try:
            price = float(p)
            if price < 0:
                print(t["negative_price"])
                valid = False
                break
            temp.append(price)
        except ValueError:
            print(t["invalid_number"])
            valid = False
            break
    if valid and temp:
        dishes = temp
        break

if not dishes:
    print(t["no_input"])
else:
    meal_total = sum(dishes)

    # 输入小费比例
    while True:
        tip_input = input(t["tip_prompt"]).strip()
        try:
            tip_rate = float(tip_input)
            if tip_rate < 0:
                print(t["negative_tip"])
                continue
            break
        except ValueError:
            print(t["invalid_tip"])

    tip_amount = meal_total * tip_rate / 100
    grand_total = meal_total + tip_amount

    print(t["header"])
    for i, price in enumerate(dishes, 1):
        print(t["dish_line"].format(i, price))
    print(t["divider"])
    print(t["meal_total"].format(meal_total))
    print(t["tip_line"].format(tip_rate, tip_amount))
    print(t["grand_total"].format(grand_total))
    print(t["footer"])
