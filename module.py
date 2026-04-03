#username = input("Enter your name")
#user opens the app
#user enters name and dob
#user decides if they want to store their data
#user tell the program what they want, options are compatibility, star sign 
# user receives their data

# class for data storage of the user
# class for compatibility
# class for star sign 
# dataset of all star signs and their behaviors
# dataset of user infomation 
# dataset of intermittent messages to the user will receive MAYBE

#first step - Json file that should have all the sign and their dates
        # Json file that has compatibility of all the sign and percentage
# to create logic code
import json


def load_data(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def is_valid_date(month, day):
    days_in_month = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    if month not in days_in_month:
        return False

    if day < 1 or day > days_in_month[month]:
        return False

    return True


def get_sign_from_date(month, day, zodiac_data):
    user_date = month * 100 + day

    for sign, info in zodiac_data.items():
        start_month, start_day = map(int, info["start"].split("-"))
        end_month, end_day = map(int, info["end"].split("-"))

        start_value = start_month * 100 + start_day
        end_value = end_month * 100 + end_day

        if start_value <= end_value:
            if start_value <= user_date <= end_value:
                return sign
        else:
            # for Capricorn because it crosses the year
            if user_date >= start_value or user_date <= end_value:
                return sign

    return None


def show_main_menu():
    print("\n===== ZODIAC MENU =====")
    print("1. Personality Analysis")
    print("2. Compatibility Lab")
    print("3. Discovery Search")
    print("4. Exit")


def show_personality(sign, zodiac_data):
    info = zodiac_data[sign]
    content = info["content"]

    print("\n===== PERSONALITY ANALYSIS =====")
    print("Sign:", sign.capitalize(), info["symbol"])
    print("Element:", info["element"])
    print("Lucky Colors:", ", ".join(info["lucky_colors"]))
    print("Lucky Numbers:", ", ".join(str(num) for num in info["lucky_numbers"]))
    print("\nOverview:", content["overview"])
    print("\nFun Fact:", content["fun_fact"])
    print("\nEmotional Tendency:", content["emotional_tendency"])
    print("\nCompatibility Notes:", content["compatibility_notes"])
    print("\nGeneral Advice:", content["general_advice"])
    print("\nHidden Talent:", content["hidden_talent"])


def get_sign_index(signs_list, sign_name):
    for i in range(len(signs_list)):
        if signs_list[i] == sign_name:
            return i
    return -1


def show_compatibility(user_sign, other_sign, signs_list, compatibility_matrix):
    user_index = get_sign_index(signs_list, user_sign)
    other_index = get_sign_index(signs_list, other_sign)

    if user_index == -1 or other_index == -1:
        print("Invalid sign name.")
        return

    score = compatibility_matrix[user_index][other_index]

    print("\n===== COMPATIBILITY CHECK =====")
    print(user_sign.capitalize(), "and", other_sign.capitalize(), "compatibility score:", score, "%")

    if score >= 90:
        print("Result: Excellent match!")
    elif score >= 75:
        print("Result: Very good match!")
    elif score >= 60:
        print("Result: Good match!")
    elif score >= 40:
        print("Result: Average match.")
    else:
        print("Result: Challenging match.")


def search_zodiac(keyword, zodiac_data):
    keyword = keyword.lower().strip()
    found = False

    print("\n" + "="*30)
    print("      DISCOVERY SEARCH")
    print("="*30)

    for sign, info in zodiac_data.items():
        element = info["element"].lower()
        content = info["content"]

        # BƯỚC 1: Tạo biến 'text' TRƯỚC
        text = (
            info["element"] + " " +
            content["overview"] + " " +
            content["fun_fact"] + " " +
            content["emotional_tendency"] + " " +
            content["compatibility_notes"] + " " +
            content["general_advice"] + " " +
            content["hidden_talent"]
        ).lower()

        # BƯỚC 2: Kiểm tra keyword TRONG 'text' SAU
        if keyword in text:
            print(f"✅ Found: {sign.capitalize()} {info['symbol']} - {info['element']}")
            found = True

    if not found:
        print(f"❌ No zodiac sign found for: '{keyword}'")
    
    return found


def ask_continue():
    answer = input("\nDo you want to return to the menu? (yes/no): ").lower()
    if answer == "yes":
        return True
    return False
