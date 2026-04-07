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
    Saves the COMPLETE user profile, including personality, 
    compatibility, and discovery information.
    """
    try:
        with open(filename, "a", encoding="utf-8") as file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            element = sign_data.get("element", "Unknown")
            symbol = sign_data.get("symbol", "")
            colors = ", ".join(sign_data.get("lucky_colors", []))
            numbers = ", ".join(str(n) for n in sign_data.get("lucky_numbers", []))
            content = sign_data.get("content", {})
            
            pair_comp = sign_data.get("pair_compatibility", {})
            pair_lines = [f"- {k.capitalize()}: {v}" for k, v in pair_comp.items()]
            compatibility_details = "\n".join(pair_lines) if pair_lines else "No details available."

            zodiac_story = sign_data.get("zodiac story", {})
            story_lines = [f"{title}: {desc}" for title, desc in zodiac_story.items()]
            discovery_story = "\n".join(story_lines) if story_lines else "No story found."

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
                f"📖 OVERVIEW: {content.get('overview', 'N/A')}\n\n"
                f"💡 FUN FACT: {content.get('fun_fact', 'N/A')}\n\n"
                f"🤝 COMPATIBILITY NOTES: {content.get('compatibility_notes', 'N/A')}\n\n"
                f"📊 COMPATIBILITY LAB RESULTS:\n{compatibility_details}\n\n"
                f"📚 DISCOVERY STORY:\n{discovery_story}\n"
                f"==================================================\n"
            )
            
            file.write(report)
            print(f"\n SUCCESS: Your complete profile has been saved to '{filename}'.")
            
    except Exception as e:
        print(f"\n Failed to write to {filename}. Error: {e}")

def read_report(filename="reports.txt"):
    """
    Reads the reports.txt file and prints it to the terminal.
    """
    if not os.path.exists(filename):
        print(f"\nNo saved reports found yet in '{filename}'.")
        return

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
            if not content.strip():
                print("\n📂The report file is empty.")
            else:
                print("      YOUR SAVED ZODIAC HISTORY")
                print(content)
                print("=" * 40)
    except Exception as e:
        print(f"\n Error reading the report: {e}")
