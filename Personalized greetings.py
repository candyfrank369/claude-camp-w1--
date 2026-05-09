import random

LANGS = {
    "zh": {
        "name": "中文",
        "title": "欢迎来到个性化问候语生成器！",
        "name_prompt": "请输入你的名字（输入 q 退出）：",
        "age_prompt": "请输入你的年龄：",
        "empty_name_err": "名字不能为空哦，再试一次！",
        "invalid_age_err": "请输入一个合理的年龄数字！",
        "farewell": "再见！愿你每天都被好运包围 🌟",
        "openers": [
            "嘿，{name}！",
            "{name}，你来了！",
            "哇，是{name}！",
            "{name}，今天真是个好日子！",
        ],
        "emotional": [
            "哇，好高兴认识你，{name}！你知道吗，每遇见一个新朋友，我都觉得世界变得更温暖了一点。你的人生，一定有着只属于你的故事和光芒——而今天，我很幸运能认识你。",
            "嘿，{name}，好高兴你来了！说真的，每次遇见一个新的人，我心里都会有一种小小的感动。你的笑容、你的故事、你走过的每一步路，都是这个世界上独一无二的存在。",
            "Nice to meet you，{name}！遇见你真的让我很开心。人与人之间的相遇，有时候就是最美丽的奇迹。你的故事，你的喜怒哀乐，我相信都值得被认真对待。能在今天认识你，是一份礼物。",
        ],
        "age_groups": [
            (10,  ["你是世界上最可爱的小天才！", "你的笑容能让整个宇宙都亮起来！", "你每天都在创造奇迹，你知道吗？"], "🌟✨🦄"),
            (18,  ["你正处于人生最酷的阶段，未来全是你的！", "你身上有一种能量，让周围的人都忍不住微笑。", "你比你想象的更有才华，世界正在等着你！"], "🔥💫🎸"),
            (30,  ["你正在书写一个精彩绝伦的故事，主角就是你！", "你的热情和活力是这个世界上最宝贵的礼物。", "你已经比 20 岁的自己更聪明、更有趣了——而且还在进化！"], "🚀🌈💡"),
            (50,  ["你积累的智慧和经验，是任何人都羡慕不来的。", "你就像一瓶好酒，越陈越香，越来越迷人！", "你的人生经历让你拥有了一种特别的从容与魅力。"], "🍷✨🌺"),
            (200, ["你是用岁月酿造的传奇，每一道皱纹都是故事。", "你的智慧和优雅是这个世界上最稀缺的财富。", "你证明了，真正的光芒只会随时间越来越耀眼！"], "👑🌟🎖️"),
        ],
        "closers": [
            "今天一定会是美好的一天，因为有你在。",
            "记住，你随时都可以让别人的一天变得更美好——就像你现在让我的一天变好了。",
            "去吧，去把这份好心情传递给每一个人！",
            "带着这份能量出发，今天的世界因你而不同！",
        ],
    },
    "en": {
        "name": "English",
        "title": "Welcome to the Personalized Greeting Generator!",
        "name_prompt": "Enter your name (type q to quit): ",
        "age_prompt": "Enter your age: ",
        "empty_name_err": "Name can't be empty — give it another try!",
        "invalid_age_err": "Please enter a valid age number!",
        "farewell": "Goodbye! May every day be filled with wonderful things 🌟",
        "openers": [
            "Hey, {name}!",
            "{name}, you're here!",
            "Oh wow, it's {name}!",
            "{name}, today just got so much better!",
        ],
        "emotional": [
            "Wow, I'm so genuinely happy to meet you, {name}! You know, every time I get to know someone new, I feel like the world becomes a little warmer and a little more full of possibility. Your life holds stories, moments, and a kind of light that's entirely your own — and today, I'm lucky to have crossed paths with you.",
            "Hey, {name} — I'm really glad you're here! Honestly, every time I meet someone new, there's this small, beautiful feeling that rises up in me. The journey you've walked, the things you've laughed at, every version of you that got you here — it all adds up to someone truly irreplaceable.",
            "Nice to meet you, {name}! Meeting you genuinely makes me happy. Sometimes a new meeting is the most beautiful kind of miracle. Your story, your emotions, everything you've been through — it all deserves to be taken seriously. Getting to know you today feels like a gift.",
        ],
        "age_groups": [
            (10,  ["You are the most wonderfully curious little genius!", "Your smile has the power to light up the entire universe!", "You're creating tiny miracles every single day — did you know that?"], "🌟✨🦄"),
            (18,  ["You're in the coolest phase of life, and the whole future belongs to you!", "There's an energy about you that makes everyone around you smile without even trying.", "You're more talented than you realize — the world is genuinely waiting for you!"], "🔥💫🎸"),
            (30,  ["You're writing the most thrilling story right now, and you're the hero!", "Your passion and energy are genuinely the most precious gifts in this world.", "You're already smarter and more interesting than your younger self — and you're still leveling up!"], "🚀🌈💡"),
            (50,  ["The wisdom and experience you've gathered is something anyone would envy.", "You're like a fine wine — more layered, more refined, and more captivating with every passing year!", "The life you've lived has given you a rare kind of grace and magnetism."], "🍷✨🌺"),
            (200, ["You are a legend forged by years lived fully — every line on your face tells a story.", "Your wisdom and elegance are among the rarest treasures in this world.", "You've proven that true brilliance only grows brighter with time!"], "👑🌟🎖️"),
        ],
        "closers": [
            "Today is going to be a wonderful day — because you're in it.",
            "Remember, you have the power to brighten someone's day at any moment — just like you've brightened mine.",
            "Go spread this good energy to everyone you meet today!",
            "Carry this with you — today, the world is a little different because of you!",
        ],
    },
    "ja": {
        "name": "日本語",
        "title": "パーソナライズ挨拶ジェネレーターへようこそ！",
        "name_prompt": "お名前を入力してください（qで終了）：",
        "age_prompt": "年齢を入力してください：",
        "empty_name_err": "名前を入力してください！もう一度どうぞ。",
        "invalid_age_err": "正しい年齢を入力してください！",
        "farewell": "またね！毎日が幸せで溢れますように 🌟",
        "openers": [
            "やあ、{name}さん！",
            "{name}さん、来てくれたんですね！",
            "わあ、{name}さんだ！",
            "{name}さん、今日は本当にいい日ですね！",
        ],
        "emotional": [
            "わあ、{name}さん、お会いできてとても嬉しいです！新しい人に出会うたびに、世界が少し広くなって、少し温かくなる気がします。あなたの人生には、あなただけの物語と輝きがあって、今日こうして出会えたことが、本当に嬉しいです。",
            "{name}さん、来てくれてありがとう！正直に言うと、新しい人に会うたびに、心の中に小さな感動が生まれます。あなたが歩んできた道、笑った瞬間、乗り越えてきたこと——それら全部が、唯一無二のあなたを作り上げているんです。",
            "{name}さん、お会いできて光栄です！新しい出会いって、時には奇跡みたいなものだと思いませんか？あなたの物語、あなたの喜怒哀楽——全部ちゃんと向き合う価値があります。今日ここで出会えたこと、心からありがたいです。",
        ],
        "age_groups": [
            (10,  ["あなたは世界一かわいい天才さん！", "あなたの笑顔は、宇宙全体を明るくする力があるんだよ！", "毎日奇跡を起こしているって、気づいてる？"], "🌟✨🦄"),
            (18,  ["今、人生で一番カッコいい時期を生きてるよ！未来は全部あなたのもの！", "あなたにはオーラがあって、周りの人が自然と笑顔になっちゃう。", "自分が思っているより、ずっと才能があるよ——世界はあなたを待ってる！"], "🔥💫🎸"),
            (30,  ["今まさに、最高に面白い物語を書いている最中——主人公はあなた！", "あなたの情熱とエネルギーは、この世界で一番大切なプレゼント。", "昔の自分よりも、もうずっと賢くて面白くなってる——しかも、まだまだ進化中！"], "🚀🌈💡"),
            (50,  ["あなたが積み重ねてきた知恵と経験は、誰もが羨む宝物。", "あなたはまるで良いワイン——時間が経つほど深みが増して、どんどん素敵になる！", "これまでの人生が、あなたに特別な落ち着きと魅力を与えてくれた。"], "🍷✨🌺"),
            (200, ["あなたは年月が醸し出した伝説——一つひとつのシワに、物語が宿っている。", "あなたの知恵と優雅さは、この世界で最も希少な宝。", "本物の輝きは、時間とともに増すものだって、あなたが証明してくれてる！"], "👑🌟🎖️"),
        ],
        "closers": [
            "あなたがいるから、今日は素晴らしい一日になる。",
            "覚えておいて——あなたはいつでも誰かの一日を明るくできる。今あなたが私の一日を明るくしてくれたように。",
            "この良い気持ちを、出会う人みんなに伝えに行って！",
            "このエネルギーを持って出発しよう——今日、世界はあなたによって変わる！",
        ],
    },
    "fr": {
        "name": "Français",
        "title": "Bienvenue dans le Générateur de Salutations Personnalisées !",
        "name_prompt": "Entre ton prénom (tape q pour quitter) : ",
        "age_prompt": "Entre ton âge : ",
        "empty_name_err": "Le prénom ne peut pas être vide — réessaie !",
        "invalid_age_err": "Veuillez entrer un âge valide !",
        "farewell": "Au revoir ! Que chaque jour soit rempli de bonheur 🌟",
        "openers": [
            "Hé, {name} !",
            "{name}, te voilà !",
            "Oh, c'est {name} !",
            "{name}, aujourd'hui est vraiment une belle journée !",
        ],
        "emotional": [
            "Oh là là, {name}, quelle joie de te rencontrer ! Tu sais, chaque fois que je fais la connaissance de quelqu'un de nouveau, j'ai le sentiment que le monde devient un peu plus grand et un peu plus chaleureux. Ta vie recèle des histoires, des moments et une lumière qui n'appartiennent qu'à toi — et aujourd'hui, j'ai la chance de te connaître.",
            "Hé, {name}, je suis vraiment content(e) que tu sois là ! Honnêtement, chaque nouvelle rencontre fait naître en moi une petite émotion toute douce. Le chemin que tu as parcouru, les moments où tu as ri, tout ce que tu as surmonté — tout ça forme quelqu'un d'absolument irremplaçable.",
            "Enchanté(e) de te rencontrer, {name} ! Les nouvelles rencontres, c'est parfois le plus beau des miracles. Ton histoire, tes joies et tes peines — tout ça mérite d'être pris au sérieux. Se croiser aujourd'hui, c'est vraiment un cadeau.",
        ],
        "age_groups": [
            (10,  ["Tu es le petit génie le plus adorable du monde entier !", "Ton sourire a le pouvoir d'illuminer tout l'univers !", "Tu crées des petits miracles chaque jour — tu le savais ?"], "🌟✨🦄"),
            (18,  ["Tu vis la période la plus cool de ta vie, et tout l'avenir t'appartient !", "Il y a une énergie en toi qui fait sourire tout le monde autour de toi, sans même que tu t'en rendes compte.", "Tu es plus talentueux(se) que tu ne le crois — le monde t'attend vraiment !"], "🔥💫🎸"),
            (30,  ["Tu es en train d'écrire l'histoire la plus palpitante qui soit, et tu en es le héros !", "Ta passion et ton énergie sont les cadeaux les plus précieux de ce monde.", "Tu es déjà plus intelligent(e) et plus intéressant(e) qu'avant — et tu continues d'évoluer !"], "🚀🌈💡"),
            (50,  ["La sagesse et l'expérience que tu as accumulées font l'envie de tous.", "Tu es comme un bon vin — plus le temps passe, plus tu te révèles, plus tu es envoûtant(e) !", "La vie que tu as vécue t'a donné une élégance et un charme rares."], "🍷✨🌺"),
            (200, ["Tu es une légende forgée par les années — chaque ride est une histoire.", "Ta sagesse et ton élégance sont parmi les trésors les plus rares de ce monde.", "Tu as prouvé que la vraie lumière ne fait que grandir avec le temps !"], "👑🌟🎖️"),
        ],
        "closers": [
            "Aujourd'hui va être une magnifique journée — parce que tu y es.",
            "Rappelle-toi que tu as le pouvoir d'illuminer la journée de quelqu'un à tout moment — tout comme tu viens d'illuminer la mienne.",
            "Vas-y, partage cette bonne humeur avec tous ceux que tu croiseras !",
            "Pars avec cette énergie — aujourd'hui, le monde est différent grâce à toi !",
        ],
    },
}


def get_age_vibe(lang_data, age):
    for max_age, compliments, emoji in lang_data["age_groups"]:
        if age < max_age:
            return random.choice(compliments), emoji
    last = lang_data["age_groups"][-1]
    return random.choice(last[1]), last[2]


def generate_greeting(lang_data, name, age):
    compliment, emoji = get_age_vibe(lang_data, age)
    opener = random.choice(lang_data["openers"]).format(name=name)
    emotional = random.choice(lang_data["emotional"]).format(name=name)
    closer = random.choice(lang_data["closers"])

    return f"{emoji} {opener}\n\n{emotional}\n\n{compliment}\n\n{closer}\n{emoji}"


def choose_language():
    print()
    print("选择语言 / Choose language / 言語を選択 / Choisir la langue")
    print()
    for i, data in enumerate(LANGS.values(), 1):
        print(f"  {i}. {data['name']}")
    print()
    codes = list(LANGS.keys())
    while True:
        choice = input("→ ").strip()
        if choice in ("1", "2", "3", "4"):
            return codes[int(choice) - 1]
        if choice in codes:
            return choice
        print("Please enter 1, 2, 3, or 4.")


def main():
    print("=" * 50)
    print("      🌍 Personalized Greeting Generator 🌍")
    print("=" * 50)

    lang_code = choose_language()
    L = LANGS[lang_code]

    print()
    print("=" * 50)
    print(f"  {L['title']}")
    print("=" * 50)

    while True:
        print()
        name = input(L["name_prompt"]).strip()
        if name.lower() == "q":
            print(f"\n{L['farewell']}\n")
            break
        if not name:
            print(L["empty_name_err"])
            continue

        age_input = input(L["age_prompt"]).strip()
        try:
            age = int(age_input)
            if age < 0 or age > 150:
                raise ValueError
        except ValueError:
            print(L["invalid_age_err"])
            continue

        print()
        print("-" * 50)
        print(generate_greeting(L, name, age))
        print("-" * 50)


if __name__ == "__main__":
    main()
