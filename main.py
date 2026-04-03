from storage_module import load_data, save_report
from module import (
    is_valid_date,
    get_sign_from_date,
    show_main_menu,
    show_personality,
    show_compatibility,
    search_zodiac,
    ask_continue
)

class ZodiacApp:
    def __init__(self, filename):
        self.data = load_data(filename)
        # Add a safety check in case load_data returns None
        if self.data:
            self.signs_list = self.data["signs_list"]
            self.zodiac_data = self.data["zodiac_data"]
            self.compatibility_matrix = self.data["compatibility_matrix"]
        else:
            print("System failure: Data could not be loaded.")
            exit()
            
        self.user_name = ""
        self.user_sign = ""

    def get_user_info(self):
        print("===== WELCOME TO THE ZODIAC SYSTEM =====")
        self.user_name = input("Enter your name: ")

        while True:
            try:
                month = int(input("Enter your birth month (1-12): "))
                day = int(input("Enter your birth day (1-31): "))

                if is_valid_date(month, day):
                    sign = get_sign_from_date(month, day, self.zodiac_data)
                    if sign is not None:
                        self.user_sign = sign
                        print(f"\nHello, {self.user_name}")
                        print(f"Your zodiac sign is: {self.user_sign.capitalize()} {self.zodiac_data[self.user_sign]['symbol']}")
                        
                        # FIX 1: Automatically save the user's result to reports.txt
                        save_report(self.user_name, self.user_sign)
                        break
                    else:
                        print("Could not find zodiac sign. Try again.")
                else:
                    print("Invalid date. Please enter again.")
            except ValueError:
                print("Please enter numbers only.")

    def run(self):
        self.get_user_info()

        while True:
            show_main_menu()
            choice = input("Choose an option (1-4): ")

            if choice == "1":
                show_personality(self.user_sign, self.zodiac_data)

            elif choice == "2":
                # FIX 2: Corrected logic for Compatibility Lab
                print("\n--- Compatibility Lab ---")
                print("Available signs: " + ", ".join([s.capitalize() for s in self.signs_list]))
                
                other_sign = input("Enter another zodiac sign: ").lower().strip()

                if other_sign in self.signs_list:
                    show_compatibility(
                        self.user_sign,
                        other_sign,
                        self.signs_list,
                        self.compatibility_matrix
                    )
                else:
                    print("Invalid zodiac sign. Please check the spelling.")

            elif choice == "3":
                keyword = input("Enter a keyword (example: fire, water, loyalty): ")
                search_zodiac(keyword, self.zodiac_data)

            elif choice == "4":
                break

            else:
                print("Invalid choice. Please choose again.")
                continue

            if not ask_continue():
                break
        
        print(f"\nThank you for using the Zodiac System, {self.user_name}. Goodbye!")

if __name__ == "__main__":
    app = ZodiacApp("zodiac_data.json")
    app.run()
