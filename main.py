from storage_module import load_data, save_report, read_report 
from module import (
    is_valid_date,
    get_sign_from_date,
    show_main_menu,
    show_personality,
    show_compatibility,
    show_zodiac_story,
    ask_continue
)

class ZodiacApp:
    def __init__(self, filename):
        self.data = load_data(filename)
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
        self.user_name = input("Enter your name: ").strip()

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
                        
                        specific_sign_info = self.zodiac_data[self.user_sign]
                        save_choice = input("\nWould you like to save your profile to the report file? (yes/no): ").lower().strip()
                        
                        if save_choice in ['yes', 'y']:
                            specific_sign_info = self.zodiac_data[self.user_sign]
                            save_report(self.user_name, month, day, self.user_sign, specific_sign_info)
                        else:
                            print("Understood. Your information will not be saved.")
                        # ------------------------------
                        
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
            choice = input("Choose an option (1-5): ")

            if choice == "1":
                show_personality(self.user_sign, self.zodiac_data)
            
            elif choice == "2":
                while True:
                    print("\n--- Compatibility Check ---")
                    print("Available signs: " + ", ".join([s.capitalize() for s in self.signs_list]))
                    other_sign = input("Enter a sign (or 'menu' to go back): ").lower().strip()

                    if other_sign == 'menu':
                        break

                    if other_sign in self.signs_list:
                        show_compatibility(self.user_sign, other_sign, self.signs_list, 
                                           self.compatibility_matrix, self.zodiac_data)
                        
                        while True:
                            again = input("\nCheck another sign? (yes/no): ").lower().strip()
                            if again in ['yes', 'no']:
                                break
                            print("Please type 'yes' or 'no'.")
                        
                        if again in ['no', 'n']:
                            break
                    else:
                        print("Sign not recognized.")

            elif choice == "3":
                print(f"\n--- Legend of {self.user_sign.capitalize()} ---")
                show_zodiac_story(self.user_sign, self.zodiac_data)

            elif choice == "4":
                read_report()

            elif choice == "5": 
                print(f"\nThank you for using the Zodiac System, {self.user_name}. Goodbye!")
                exit()

            else:
                print("Invalid choice.")
                continue

            while True:
                user_choice = input("\nDo you want to return to the menu? (yes/no): ").lower().strip()
                if user_choice in ['yes', 'y']:
                    break
                elif user_choice in ['no', 'n']:
                    print(f"\nThank you for using the Zodiac System, {self.user_name}. Goodbye!")
                    exit() 
                else:
                    print("Please type 'yes' or 'no'.")

if __name__ == "__main__":
    app = ZodiacApp("zodiac_data.json")
    app.run()
