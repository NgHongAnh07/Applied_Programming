from storage_module import (
    load_data,
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
        self.signs_list = self.data["signs_list"]
        self.zodiac_data = self.data["zodiac_data"]
        self.compatibility_matrix = self.data["compatibility_matrix"]
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
                        print("\nHello,", self.user_name)
                        print("Your zodiac sign is:", self.user_sign.capitalize(), self.zodiac_data[self.user_sign]["symbol"])
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
                print("\nAvailable signs:")
                print(", ".join(self.signs_list))
                other_sign = input("Enter another zodiac sign: ").lower()

                if other_sign in self.signs_list:
                    show_compatibility(
                        self.user_sign,
                        other_sign,
                        self.signs_list,
                        self.compatibility_matrix
                    )
                else:
                    print("Invalid zodiac sign.")

            elif choice == "3":
                keyword = input("Enter a keyword (example: fire, water, loyalty, creativity): ")
                search_zodiac(keyword, self.zodiac_data)

            elif choice == "4":
                print("\nThank you for using the Zodiac System. Goodbye!")
                break

            else:
                print("Invalid choice. Please choose again.")
                continue

            if not ask_continue():
                print("\nThank you for using the Zodiac System. Goodbye!")
                break


if __name__ == "__main__":
    app = ZodiacApp("zodiac_data.json")
    app.run()

# Inside Choice 2
print("\n--- Compatibility Lab ---")
print("Available signs: " + ", ".join([s.capitalize() for s in self.signs_list]))