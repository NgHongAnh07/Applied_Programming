
import json
import os
from datetime import datetime

def load_data(filename="zodiac_data.json"):
    """
    Safely loads data from the external JSON file.
    Includes error handling to prevent the app from crashing if the file is missing or corrupted.
    """
    # 1. Check if the file exists in the directory
    if not os.path.exists(filename):
        print(f"\n❌ CRITICAL ERROR: Could not find '{filename}'.")
        print("Please make sure the JSON file is in the same folder as your scripts.")
        return None
        
    # 2. Try to open and parse the JSON file
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
            
    # 3. Catch JSON formatting errors (e.g., missing commas, misplaced brackets)
    except json.JSONDecodeError as e:
        print(f"\n❌ CRITICAL ERROR: JSON formatting error in '{filename}'.")
        print(f"Error Details: {e}")
        return None
        
    # 4. Catch any other unexpected errors during the file read process
    except Exception as e:
        print(f"\n❌ UNEXPECTED ERROR: Could not read '{filename}'.")
        print(f"Error Details: {e}")
        return None


def save_report(user_name, sign_name, filename="reports.txt"):
    """
    Automatically appends the user's calculation record to the reports log.
    """
    try:
        # Open file in "a" (append) mode so new records are added to the end without overwriting
        with open(filename, "a", encoding="utf-8") as file:
            # Get the current system time for the timestamp
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Write a formatted log entry into the text file
            file.write(f"[{timestamp}] User: {user_name} | Calculated Sign: {sign_name.capitalize()}\n")
            
    except Exception as e:
        print(f"❌ Failed to write to {filename}. Error Details: {e}")


# This block only runs if you execute storage_module.py directly.
# It will NOT run when imported by main.py.
if __name__ == "__main__":
    print("Testing storage_module.py...")
    
    # 1. Test loading data
    test_data = load_data("zodiac_data.json")
    if test_data:
        print("✅ Success! The JSON file was loaded perfectly.")
        # Safely count how many signs are in the list
        sign_count = len(test_data.get('signs_list', []))
        print(f"Found {sign_count} zodiac signs in the database.")
        
    # 2. Test saving a report
    print("\nTesting report generation...")
    save_report("TestUser_Jiaxi", "Aries")
    print("✅ Success! Check 'reports.txt' in your folder to see the generated log.")
