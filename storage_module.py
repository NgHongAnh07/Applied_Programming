import json

def load_zodiac_data():
    """Loads the main zodiac database from JSON."""
    try:
        with open('zodiac_data.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: zodiac_data.json not found.")
        return None

def save_user_report(report_text):
    """Appends a user's result to reports.txt."""
    with open('reports.txt', 'a', encoding='utf-8') as file:
        file.write(report_text + "\n" + "-"*30 + "\n")
    print("Report saved successfully to reports.txt!")