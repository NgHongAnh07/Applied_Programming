import json
import os
from datetime import datetime

def load_data(filename="zodiac_data.json"):
    """
    Safely loads data from the external JSON file.
    """
    if not os.path.exists(filename):
        print(f"\n CRITICAL ERROR: Could not find '{filename}'.")
        return None
        
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError as e:
        print(f"\n CRITICAL ERROR: JSON formatting error in '{filename}'. Details: {e}")
        return None
    except Exception as e:
        print(f"\n UNEXPECTED ERROR: {e}")
        return None


def save_report(user_name, month, day, sign_name, sign_data, filename="reports.txt"):
    """
    Saves the COMPLETE user profile (including all text contents) to the reports log.
    """
    try:
        with open(filename, "a", encoding="utf-8") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            element = sign_data["element"]
            symbol = sign_data["symbol"]
            colors = ", ".join(sign_data["lucky_colors"])
            numbers = ", ".join(str(n) for n in sign_data["lucky_numbers"])
            content = sign_data["content"]
            
    
            report = (
                f"\n==================================================\n"
                f"🕒 [SAVED AT: {timestamp}]\n"
                f"👤 USERNAME: {user_name}\n"
                f"📅 BIRTHDAY: {str(month).zfill(2)}-{str(day).zfill(2)}\n"
                f"✨ ZODIAC SIGN: {sign_name.capitalize()} {symbol}\n"
                f"🔥 ELEMENT: {element}\n"
                f"🎨 LUCKY COLORS: {colors}\n"
                f"🎲 LUCKY NUMBERS: {numbers}\n"
                f"--------------------------------------------------\n"
                f"📖 OVERVIEW: {content['overview']}\n\n"
                f"💡 FUN FACT: {content['fun_fact']}\n\n"
                f"❤️ EMOTIONAL TENDENCY: {content['emotional_tendency']}\n\n"
                f"🧭 GENERAL ADVICE: {content['general_advice']}\n\n"
                f"🎯 HIDDEN TALENT: {content['hidden_talent']}\n"
                f"==================================================\n"
            )
            
            file.write(report)
            print(f"\n SUCCESS: Your complete profile has been saved to '{filename}'.")
            
    except Exception as e:
        print(f"\n Failed to write to {filename}. Error: {e}")

def read_report(filename="reports.txt"):
    """
    Reads the reports.txt file and prints it to the terminal 
    so the user can see their saved history.
    """
    if not os.path.exists(filename):
        print(f"\n📂 No saved reports found yet in '{filename}'.")
        return

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            if not content.strip():
                print("\n📂 The report file is empty.")
            else:
                print("\n" + "📜" * 20)
                print("      YOUR SAVED ZODIAC HISTORY")
                print("📜" * 20)
                print(content)
                print("=" * 40)
    except Exception as e:
        print(f"\nError reading the report: {e}")
