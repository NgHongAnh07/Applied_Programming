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
        self.user_birth_month = 0  
        self.user_birth_day = 0   
        self.session_data = {} 
        self.want_to_save = False

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
                        self.user_birth_month = month 
                        self.user_birth_day = day
                        
                        print(f"\nHello, {self.user_name}")
                        print(f"Your zodiac sign is: {self.user_sign.capitalize()} {self.zodiac_data[self.user_sign]['symbol']}")
                        
                        choice = input("\nDo you want to save your activity to report later? (yes/no): ").lower().strip()
                        if choice in ['yes']:
                            self.want_to_save = True
                            print("Understand! Your activity will be saved in report file.")
                        else:
                            self.want_to_save = False
                            print("Understand. No activity will be saved to the report file.")
                        break
                    else:
                        print("Invalid date.")
            except ValueError:
                print("Numbers only please.")
    
    
    def run(self):
        self.get_user_info()

        while True:
            show_main_menu()
            choice = input("Choose an option (1-5): ")

            if choice == "1":
                show_personality(self.user_sign, self.zodiac_data)

                info = self.zodiac_data[self.user_sign]
                content = info.get('content', {})
                
                personality = (
                    f"Element        : {info.get('element', 'N/A')}\n"
                    f"Lucky Colors   : {', '.join(info.get('lucky_colors', []))}\n"
                    f"Lucky Numbers  : {', '.join(map(str, info.get('lucky_numbers', [])))}\n"
                    f"-------------------------\n"
                    f"📖 Overview: {content.get('overview', 'N/A')}\n\n"
                    f"💡 Fun Fact: {content.get('fun_fact', 'N/A')}\n\n"
                    f"❤️  Emotional: {content.get('emotional_tendency', 'N/A')}\n\n"
                    f"🎯 Talent   : {content.get('hidden_talent', 'N/A')}\n\n"
                    f"🧭 Advice   : {content.get('general_advice', 'N/A')}"
                )
                
                self.session_data["Personality Analysis"] = personality
            
            elif choice == "2":
                while True:
                    print("\n--- Compatibility Check ---")
                    print("Available signs: " + ", ".join([s.capitalize() for s in self.signs_list]))
                    other_sign = input("Enter a sign: ").lower().strip()


                    if other_sign in self.signs_list:
                        show_compatibility(self.user_sign, other_sign, self.signs_list, 
                                           self.compatibility_matrix, self.zodiac_data)
                        
                        idx1, idx2 = self.signs_list.index(self.user_sign), self.signs_list.index(other_sign)
                        score = self.compatibility_matrix[idx1][idx2]
                        deep_dive = self.zodiac_data[self.user_sign].get('pair_compatibility', {}).get(other_sign, "N/A")
                        
                        comp_res = f"Match: {self.user_sign.capitalize()} & {other_sign.capitalize()} ({score}%)\nDeep Dive: {deep_dive}"
                        
                        if "Compatibility Result" in self.session_data:
                            self.session_data["Compatibility Result"] += f"\n\n{comp_res}"
                        else:
                            self.session_data["Compatibility Result"] = comp_res

                        again = input("\nCheck another sign? (yes/no): ").lower().strip()
                        if again not in ['yes']:
                            break
                    else:
                        print("Sign not recognized.")

            elif choice == "3":
                show_zodiac_story(self.user_sign, self.zodiac_data)
                story_info = self.zodiac_data[self.user_sign].get('zodiac story', {})
                
                if story_info:
                    story_title = list(story_info.keys())[0]
                    story_text = list(story_info.values())[0]
                    
                    self.session_data["Zodiac Story"] = f"{story_title}\n{story_text}"
            
            elif choice == "4":
                if self.want_to_save:
                    save_report(self.user_name, self.user_birth_month, self.user_birth_day, self.user_sign, self.session_data)
                    
                    print("\n" + "="*20 + " YOUR REPORT " + "="*20)
                    try:
                        with open("reports.txt", "r", encoding="utf-8") as f:
                            print(f.read())
                    except FileNotFoundError:
                        print("File not found.")
                else:
                    print("\nYou chose NOT to save at the beginning. No report available.")
                    

            elif choice == "5": 
                print(f"\nThank you for using the Zodiac System, {self.user_name}. Goodbye!")
                exit() 

            else:
                print("Invalid choice.")
                continue

            while True:
                user_choice = input("\nDo you want to return to the menu? (yes/no): ").lower().strip()
                if user_choice in ['yes','no']:
                    break 
                print("Please type 'yes' or 'no'.")
            
            if user_choice in ['no']:
                print(f"\nThank you for using the Zodiac System, {self.user_name}. Goodbye!")
                exit()

if __name__ == "__main__":
    app = ZodiacApp("zodiac_data.json")
    app.run()