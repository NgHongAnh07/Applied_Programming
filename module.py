import json

def is_valid_date(month, day):
    """Checks if the entered month and day are valid."""
    days_in_month = {
        1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    if month not in days_in_month:
        return False
    if day < 1 or day > days_in_month[month]:
        return False
    return True

def get_sign_from_date(month, day, zodiac_data):
    """Determines the zodiac sign based on birth date, handling the Capricorn wrap-around."""
    user_date = month * 100 + day

    for sign, info in zodiac_data.items():
        start_month, start_day = map(int, info["start"].split("-"))
        end_month, end_day = map(int, info["end"].split("-"))

        start_value = start_month * 100 + start_day
        end_value = end_month * 100 + end_day

        if start_value > end_value: # Capricorn case
            if user_date >= start_value or user_date <= end_value:
                return sign
        else:
            if start_value <= user_date <= end_value:
                return sign
    return None

def show_main_menu():
    """Displays the main selection menu."""
    print("\n" + "="*30)
    print("      ZODIAC MAIN MENU")
    print("="*30)
    print("1. Personality Analysis")
    print("2. Compatibility Check")
    print("3. Zodiac Stories")
    print("4. View My Saved Reports") 
    print("5. Exit")
    print("="*30)

def show_personality(sign, zodiac_data):
    """Displays detailed personality analysis from the JSON content."""
    info = zodiac_data[sign]
    content = info["content"]

<<<<<<< HEAD
    print("\n===== PERSONALITY ANALYSIS =====")
    print("Sign:", sign.capitalize(), info["symbol"])
    print("Element:", info["element"])
    print("Lucky Colors:", ", ".join(info["lucky_colors"]))
    print("Lucky Numbers:", ", ".join(str(num) for num in info["lucky_numbers"]))
    print("\nOverview:", content["overview"])
    print("\nFun Fact:", content["fun_fact"])
    print("\nEmotional Tendency:", content["emotional_tendency"])
    print("\nGeneral Advice:", content["general_advice"])
    print("\nHidden Talent:", content["hidden_talent"])

=======
    print("\n" + "*"*45)
    print(f"🌟 ANALYSIS: {sign.upper()} {info['symbol']}")
    print("*"*45)
    print(f"Element        : {info['element']}")
    print(f"Lucky Colors   : {', '.join(info['lucky_colors'])}")
    print(f"Lucky Numbers  : {', '.join(map(str, info['lucky_numbers']))}")
    print("-" * 25)
    print(f"📖 Overview: {content['overview']}")
    print(f"\n💡 Fun Fact: {content['fun_fact']}")
    print(f"\n❤️ Emotional: {content['emotional_tendency']}")
    print(f"\n🎯 Talent   : {content['hidden_talent']}")
    print(f"\n🧭 Advice   : {content['general_advice']}")
    print("*"*45)
>>>>>>> origin/hanh

def get_sign_index(signs_list, sign_name):
    """Finds the index of a sign for matrix lookup."""
    try:
        return signs_list.index(sign_name.lower())
    except ValueError:
        return -1

def show_compatibility(user_sign, other_sign, signs_list, compatibility_matrix, zodiac_data):
    """Checks compatibility using Matrix scores and pulls the pair description text."""
    u_idx = get_sign_index(signs_list, user_sign)
    o_idx = get_sign_index(signs_list, other_sign)

    if u_idx == -1 or o_idx == -1:
        print("Invalid zodiac sign. Please try again.")
        return

    score = compatibility_matrix[u_idx][o_idx]
    
    print(f"\nMATCH: {user_sign.capitalize()} & {other_sign.capitalize()}")
    print(f"Compatibility Score: {score}%")
    
    if score >= 90: result = "Excellent Match! (Soulmates)"
    elif score >= 70: result = "Very Good Match!"
    elif score >= 50: result = "Good Potential."
    else: result = "Challenging Connection."
    print(f"Final Result: {result}")

<<<<<<< HEAD
    print("\n===== COMPATIBILITY CHECK =====")
    print(user_sign.capitalize(), "and", other_sign.capitalize(), "compatibility score:", score, "%")
=======
    # --- CRITICAL FIX FOR PAIR COMPATIBILITY ---
    # Force both signs to lowercase to match JSON keys
    u_key = user_sign.lower()
    o_key = other_sign.lower()
>>>>>>> origin/hanh

    # Access: zodiac_data -> [user_sign] -> pair_compatibility -> [other_sign]
    pair_desc = zodiac_data.get(u_key, {}).get("pair_compatibility", {}).get(o_key)
    
    if pair_desc:
        print(f"\nRelationship Deep Dive: \n\"{pair_desc}\"")
    else:
<<<<<<< HEAD
        print("Result: Challenging match.")
    
    data = load_data("zodiac_data.json")
    message = data.get("zodiac_data", {}).get(user_sign, {}).get("pair_compatibility", {}).get(other_sign)

    if message:
        print(message)
    else:
        print("Compatibility description not found.")
=======
        print("\n(Specific relationship details not found for this pair.)")

def show_zodiac_story(sign, zodiac_data):
    """Displays the mythological story of the chosen zodiac sign."""
    sign_key = sign.lower()
    info = zodiac_data.get(sign_key, {})
    stories = info.get("zodiac story", {})
>>>>>>> origin/hanh

    if not stories:
        print(f"\n📖 No legend found for {sign.capitalize()} yet.")
        return
    print(f"      THE LEGEND OF {sign.upper()}")
    print("="*42)

    for title, story_text in stories.items():
        print(f"\n✨ {title}")
        print("-" * len(title))
        print(story_text)

def ask_continue():
    """Asks the user if they want to return to the main menu."""
    ans = input("\nGo back to the Main Menu? (yes/no): ").lower().strip()
    return ans == "yes"
