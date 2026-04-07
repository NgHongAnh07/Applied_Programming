import json
import os
from datetime import datetime


def load_data(filename="zodiac_data.json"):
    if not os.path.exists(filename):
        print(f"\n CRITICAL ERROR: Could not find '{filename}'.")
        return None
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"\n ERROR: {e}")
        return None


def save_report(user_name, month, day, sign_name, session_data, filename="reports.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as file: 
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            report = (
                f"==================================================\n"
                f"🕒 [GENERATED AT: {timestamp}]\n"
                f"👤 USERNAME: {user_name.upper()}\n"
                f"📅 BIRTHDAY: {str(month).zfill(2)}-{str(day).zfill(2)}\n"
                f"✨ ZODIAC SIGN: {sign_name.upper()}\n"
                f"--------------------------------------------------\n"
            )

            if "Personality Analysis" in session_data:
                report += f"PERSONALITY ANALYSIS:\n{session_data['Personality Analysis']}\n\n"

            if "Compatibility Result" in session_data:
                report += f"COMPATIBILITY CHECK:\n{session_data['Compatibility Result']}\n\n"

            if "Zodiac Story" in session_data:
                report += f"ZODIAC STORIES:\n{session_data['Zodiac Story']}\n"

            report += f"==================================================\n"
            file.write(report)
            print(f"\nSUCCESS: Report updated in '{filename}'.")
    except Exception as e:
        print(f"\nError saving report: {e}")

def read_report(current_user, filename="reports.txt"):
    if not os.path.exists(filename):
        print(f"\nNo saved reports found.")
        return
    try:
        with open(filename, "r", encoding="utf-8") as file:
            print(file.read())
    except Exception as e:
        print(f"Error: {e}")