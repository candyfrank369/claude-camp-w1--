# BMI Calculator — Multi-language with personalized health advice

LANGUAGES = {
    "1": "zh",
    "2": "en",
    "3": "ja",
    "4": "fr",
}

STRINGS = {
    "zh": {
        "select_lang":    "请选择语言 / Select language / 言語を選択 / Choisir la langue:\n  1. 中文\n  2. English\n  3. 日本語\n  4. Français\n请输入编号: ",
        "enter_height":   "请输入身高（厘米，例如 170）: ",
        "enter_weight":   "请输入体重（千克，例如 65）: ",
        "bmi_result":     "您的 BMI 为: {bmi:.1f}（{category}）",
        "enter_age":      "请输入年龄: ",
        "enter_gender":   "请输入性别（男/女）: ",
        "advice_header":  "\n── 健康建议 ──",
        "invalid":        "输入无效，请重新输入。",
        "categories":     {"underweight": "偏瘦", "normal": "正常", "overweight": "偏重", "obese": "肥胖"},
        "genders":        {"male": ["男", "m", "male"], "female": ["女", "f", "female"]},
    },
    "en": {
        "select_lang":    "Please select language:\n  1. 中文\n  2. English\n  3. 日本語\n  4. Français\nEnter number: ",
        "enter_height":   "Enter height (cm, e.g. 170): ",
        "enter_weight":   "Enter weight (kg, e.g. 65): ",
        "bmi_result":     "Your BMI is: {bmi:.1f} ({category})",
        "enter_age":      "Enter your age: ",
        "enter_gender":   "Enter gender (male/female): ",
        "advice_header":  "\n── Health Advice ──",
        "invalid":        "Invalid input, please try again.",
        "categories":     {"underweight": "Underweight", "normal": "Normal", "overweight": "Overweight", "obese": "Obese"},
        "genders":        {"male": ["male", "m", "男"], "female": ["female", "f", "女"]},
    },
    "ja": {
        "select_lang":    "言語を選択してください:\n  1. 中文\n  2. English\n  3. 日本語\n  4. Français\n番号を入力: ",
        "enter_height":   "身長を入力してください（cm、例: 170）: ",
        "enter_weight":   "体重を入力してください（kg、例: 65）: ",
        "bmi_result":     "あなたのBMIは: {bmi:.1f}（{category}）",
        "enter_age":      "年齢を入力してください: ",
        "enter_gender":   "性別を入力してください（男性/女性）: ",
        "advice_header":  "\n── 健康アドバイス ──",
        "invalid":        "無効な入力です。もう一度入力してください。",
        "categories":     {"underweight": "低体重", "normal": "普通体重", "overweight": "過体重", "obese": "肥満"},
        "genders":        {"male": ["男性", "male", "m", "男"], "female": ["女性", "female", "f", "女"]},
    },
    "fr": {
        "select_lang":    "Veuillez choisir la langue:\n  1. 中文\n  2. English\n  3. 日本語\n  4. Français\nEntrez le numéro: ",
        "enter_height":   "Entrez la taille (cm, ex. 170): ",
        "enter_weight":   "Entrez le poids (kg, ex. 65): ",
        "bmi_result":     "Votre IMC est: {bmi:.1f} ({category})",
        "enter_age":      "Entrez votre âge: ",
        "enter_gender":   "Entrez le sexe (homme/femme): ",
        "advice_header":  "\n── Conseils Santé ──",
        "invalid":        "Entrée invalide, veuillez réessayer.",
        "categories":     {"underweight": "Insuffisance pondérale", "normal": "Poids normal", "overweight": "Surpoids", "obese": "Obésité"},
        "genders":        {"male": ["homme", "h", "male", "m"], "female": ["femme", "f", "female"]},
    },
}

ADVICE = {
    "zh": {
        "underweight": {
            "base": "您的体重偏低，建议增加营养摄入，规律进食，必要时咨询营养师。",
            "young_male":   "青年男性在偏瘦状态下应注重蛋白质和热量摄入，适度力量训练有助于增肌。",
            "young_female": "青年女性偏瘦可能影响荷尔蒙平衡和生育健康，建议均衡饮食，避免过度节食。",
            "middle_male":  "中年男性偏瘦需关注肌肉流失问题，建议增加优质蛋白摄入并进行抗阻训练。",
            "middle_female":"中年女性偏瘦会加速骨质流失风险，建议补充钙质和维生素D。",
            "senior":       "老年人体重偏低易导致免疫力下降，应少食多餐，注意补充蛋白质。",
        },
        "normal": {
            "base": "您的体重处于健康范围，继续保持均衡饮食和规律运动。",
            "young_male":   "保持现有生活习惯，可适当增加力量训练以塑造体型。",
            "young_female": "维持健康体重，注意补铁和叶酸，每周至少150分钟中等强度运动。",
            "middle_male":  "注意控制内脏脂肪，定期体检，保持有氧运动和力量训练的结合。",
            "middle_female":"更年期前后注意激素变化对体重的影响，保持均衡饮食和规律运动。",
            "senior":       "保持适度活动，注意补充优质蛋白和钙质，预防肌肉和骨骼老化。",
        },
        "overweight": {
            "base": "您的体重略微偏高，建议适当控制饮食热量，增加有氧运动。",
            "young_male":   "减少精制碳水和高脂食物摄入，每周进行150～300分钟中高强度运动。",
            "young_female": "避免极端节食，通过均衡饮食和运动逐步减重，每周减重不超过0.5kg为宜。",
            "middle_male":  "重点关注腰围，腰围超过90cm为腹型肥胖，心血管风险增加，建议就医评估。",
            "middle_female":"注意激素变化导致的腹部脂肪堆积，低糖低脂饮食配合规律运动效果最佳。",
            "senior":       "老年人减重需循序渐进，避免肌肉流失，建议在医生指导下制定方案。",
        },
        "obese": {
            "base": "您的体重已达肥胖范围，建议尽快咨询医生，制定系统的减重计划。",
            "young_male":   "肥胖显著增加代谢综合征风险，建议进行血糖、血压、血脂检查，并在专业指导下减重。",
            "young_female": "肥胖可能影响内分泌和生育能力，建议就医评估，配合营养师和运动教练指导。",
            "middle_male":  "心血管疾病和2型糖尿病风险极高，需立即就医并进行全面代谢评估。",
            "middle_female":"肥胖叠加更年期激素变化风险倍增，请及时就医，进行综合干预。",
            "senior":       "老年肥胖增加关节负担和心脑血管风险，请在医生监督下进行安全有效的减重治疗。",
        },
    },
    "en": {
        "underweight": {
            "base": "Your weight is below the healthy range. Consider increasing caloric intake and consulting a nutritionist.",
            "young_male":   "Focus on protein and caloric intake. Resistance training can help you build healthy muscle mass.",
            "young_female": "Low weight may disrupt hormonal balance. Aim for a balanced diet and avoid extreme calorie restriction.",
            "middle_male":  "Pay attention to muscle loss. Prioritize quality protein and resistance training.",
            "middle_female":"Low weight accelerates bone density loss. Supplement calcium and vitamin D.",
            "senior":       "Low weight weakens immunity. Eat smaller, more frequent meals with emphasis on protein.",
        },
        "normal": {
            "base": "Your weight is in the healthy range. Keep up the balanced diet and regular exercise.",
            "young_male":   "Maintain your habits. Adding strength training can help improve body composition.",
            "young_female": "Maintain a balanced diet with adequate iron and folate. Aim for 150+ min/week of moderate activity.",
            "middle_male":  "Watch for visceral fat accumulation. Combine aerobic and resistance exercise and get regular check-ups.",
            "middle_female":"Be mindful of hormonal changes around menopause. Balanced diet and regular exercise remain key.",
            "senior":       "Stay moderately active. Prioritize protein and calcium to prevent muscle and bone loss.",
        },
        "overweight": {
            "base": "Your weight is slightly above the healthy range. Moderate calorie reduction and more aerobic exercise are advised.",
            "young_male":   "Cut refined carbs and high-fat foods. Aim for 150–300 min/week of moderate-to-vigorous exercise.",
            "young_female": "Avoid crash diets. Lose weight gradually through balanced eating — no more than 0.5 kg/week.",
            "middle_male":  "Focus on waist circumference. Waist > 90 cm indicates abdominal obesity with elevated cardiovascular risk.",
            "middle_female":"Hormonal shifts can cause abdominal fat gain. A low-sugar, low-fat diet with regular exercise helps most.",
            "senior":       "Weight loss should be gradual to avoid muscle loss. Work with a physician to design a safe plan.",
        },
        "obese": {
            "base": "Your BMI falls in the obese range. Please consult a doctor promptly to develop a structured weight-loss plan.",
            "young_male":   "Obesity significantly raises metabolic syndrome risk. Get bloodwork done and follow professional guidance.",
            "young_female": "Obesity can impair hormonal health and fertility. Seek medical evaluation with support from a dietitian.",
            "middle_male":  "Cardiovascular disease and type 2 diabetes risk is very high. Seek immediate medical assessment.",
            "middle_female":"Obesity combined with menopause compounds health risks. Comprehensive medical intervention is needed.",
            "senior":       "Obesity stresses joints and the cardiovascular system. Work closely with your doctor for a safe approach.",
        },
    },
    "ja": {
        "underweight": {
            "base": "体重が健康範囲を下回っています。栄養摂取を増やし、必要であれば栄養士に相談してください。",
            "young_male":   "タンパク質と総カロリーの摂取を増やし、筋力トレーニングで筋肉量を高めましょう。",
            "young_female": "低体重はホルモンバランスを乱す可能性があります。極端な食事制限は避けてください。",
            "middle_male":  "筋肉の減少に注意し、良質なタンパク質と抵抗運動を組み合わせましょう。",
            "middle_female":"骨密度低下が加速します。カルシウムとビタミンDの補充を心がけてください。",
            "senior":       "免疫力が低下しやすいです。少量頻回食で、タンパク質を意識して摂りましょう。",
        },
        "normal": {
            "base": "体重は健康的な範囲内です。バランスの良い食事と定期的な運動を続けましょう。",
            "young_male":   "現在の生活習慣を維持しつつ、筋力トレーニングを取り入れると体組成が改善します。",
            "young_female": "鉄分と葉酸を意識した食事を続け、週150分以上の中強度運動を目標にしましょう。",
            "middle_male":  "内臓脂肪に注意し、有酸素運動と筋力トレーニングを組み合わせて定期的に健診を受けましょう。",
            "middle_female":"更年期前後のホルモン変化に注意し、バランスの良い食事と運動を維持しましょう。",
            "senior":       "適度な活動を続け、タンパク質とカルシウムを補充して筋骨格の老化を予防しましょう。",
        },
        "overweight": {
            "base": "体重がやや高めです。食事のカロリーを適度に抑え、有酸素運動を増やしましょう。",
            "young_male":   "精製炭水化物と高脂肪食品を減らし、週150〜300分の中〜高強度運動を行いましょう。",
            "young_female": "極端なダイエットは避け、週0.5kg以内を目安に緩やかに体重を減らしましょう。",
            "middle_male":  "腹囲に注目してください。腹囲90cm超は腹部肥満で心血管リスクが上昇します。",
            "middle_female":"ホルモン変化による腹部脂肪に注意。低糖・低脂肪食と定期的な運動が効果的です。",
            "senior":       "筋肉量を維持しながら緩やかに減量しましょう。医師と連携して計画を立てることを推奨します。",
        },
        "obese": {
            "base": "BMIが肥満の範囲です。早急に医師に相談し、体系的な減量計画を立ててください。",
            "young_male":   "メタボリックシンドロームのリスクが高まっています。血液検査を受け、専門家の指導のもとで減量しましょう。",
            "young_female": "肥満はホルモンや生殖機能に影響する可能性があります。医師・栄養士のサポートを受けましょう。",
            "middle_male":  "心血管疾患と2型糖尿病のリスクが非常に高いです。直ちに医師の診察を受けてください。",
            "middle_female":"肥満と更年期の複合リスクは大きいです。包括的な医療介入が必要です。",
            "senior":       "肥満は関節と心血管系に大きな負担をかけます。医師の監督のもとで安全に取り組みましょう。",
        },
    },
    "fr": {
        "underweight": {
            "base": "Votre poids est en dessous de la plage saine. Augmentez vos apports nutritifs et consultez un diététicien si besoin.",
            "young_male":   "Augmentez les apports en protéines et en calories. L'entraînement en résistance aide à développer la masse musculaire.",
            "young_female": "Un faible poids peut perturber l'équilibre hormonal. Évitez les restrictions caloriques extrêmes.",
            "middle_male":  "Surveillez la perte musculaire. Privilégiez les protéines de qualité et l'entraînement en résistance.",
            "middle_female":"La faible corpulence accélère la perte de densité osseuse. Supplémentez en calcium et vitamine D.",
            "senior":       "Un faible poids affaiblit l'immunité. Mangez en petites quantités fréquentes en privilégiant les protéines.",
        },
        "normal": {
            "base": "Votre poids est dans la plage saine. Continuez à maintenir une alimentation équilibrée et une activité régulière.",
            "young_male":   "Maintenez vos habitudes. L'entraînement en force peut améliorer votre composition corporelle.",
            "young_female": "Veillez à un apport suffisant en fer et en folates. Visez 150 min/semaine d'activité modérée.",
            "middle_male":  "Surveillez la graisse viscérale. Combinez exercice aérobie et musculation, et faites des bilans réguliers.",
            "middle_female":"Soyez attentive aux changements hormonaux liés à la ménopause. Alimentation équilibrée et exercice restent essentiels.",
            "senior":       "Restez modérément actif(ve). Privilégiez les protéines et le calcium pour prévenir la sarcopénie et l'ostéoporose.",
        },
        "overweight": {
            "base": "Votre poids est légèrement au-dessus de la plage saine. Réduisez modérément les calories et augmentez l'exercice aérobie.",
            "young_male":   "Réduisez les glucides raffinés et les aliments gras. Visez 150–300 min/semaine d'exercice modéré à intense.",
            "young_female": "Évitez les régimes draconiens. Perdez du poids progressivement — pas plus de 0,5 kg par semaine.",
            "middle_male":  "Surveillez votre tour de taille. Un tour de taille > 90 cm indique une obésité abdominale à risque cardiovasculaire.",
            "middle_female":"Les changements hormonaux favorisent la graisse abdominale. Privilégiez une alimentation pauvre en sucre et en graisses.",
            "senior":       "Perdez du poids progressivement pour éviter la fonte musculaire. Consultez votre médecin pour un plan adapté.",
        },
        "obese": {
            "base": "Votre IMC est dans la plage obésité. Consultez un médecin rapidement pour élaborer un plan de perte de poids structuré.",
            "young_male":   "L'obésité augmente significativement le risque de syndrome métabolique. Faites un bilan sanguin et suivez un suivi professionnel.",
            "young_female": "L'obésité peut affecter la santé hormonale et la fertilité. Cherchez un suivi médical avec diététicien.",
            "middle_male":  "Le risque de maladie cardiovasculaire et de diabète de type 2 est très élevé. Consultez immédiatement.",
            "middle_female":"L'obésité combinée à la ménopause multiplie les risques. Une intervention médicale globale est nécessaire.",
            "senior":       "L'obésité sollicite les articulations et le système cardiovasculaire. Travaillez en étroite collaboration avec votre médecin.",
        },
    },
}


def get_bmi_category(bmi: float) -> str:
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25.0:
        return "normal"
    elif bmi < 30.0:
        return "overweight"
    else:
        return "obese"


def get_age_group(age: int, gender: str) -> str:
    if age < 40:
        return "young_male" if gender == "male" else "young_female"
    elif age < 65:
        return "middle_male" if gender == "male" else "middle_female"
    else:
        return "senior"


def parse_float(prompt: str, invalid_msg: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print(invalid_msg)
        except ValueError:
            print(invalid_msg)


def parse_int(prompt: str, invalid_msg: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print(invalid_msg)
        except ValueError:
            print(invalid_msg)


def parse_gender(prompt: str, s: dict) -> str:
    genders = s["genders"]
    while True:
        raw = input(prompt).strip().lower()
        if raw in [g.lower() for g in genders["male"]]:
            return "male"
        if raw in [g.lower() for g in genders["female"]]:
            return "female"
        print(s["invalid"])


def main():
    # Language selection
    lang_key = None
    first_s = STRINGS["zh"]
    while lang_key is None:
        choice = input(first_s["select_lang"]).strip()
        lang_key = LANGUAGES.get(choice)
        if lang_key is None:
            print(first_s["invalid"])

    s = STRINGS[lang_key]

    # Height & weight → BMI
    height_cm = parse_float(s["enter_height"], s["invalid"])
    weight_kg = parse_float(s["enter_weight"], s["invalid"])

    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    category_key = get_bmi_category(bmi)
    category_label = s["categories"][category_key]

    print(s["bmi_result"].format(bmi=bmi, category=category_label))

    # Age & gender → personalized advice
    age = parse_int(s["enter_age"], s["invalid"])
    gender = parse_gender(s["enter_gender"], s)

    age_group = get_age_group(age, gender)
    advice_pool = ADVICE[lang_key][category_key]

    print(s["advice_header"])
    print(f"• {advice_pool['base']}")
    print(f"• {advice_pool[age_group]}")


if __name__ == "__main__":
    main()
