# Applied_Programming
"Horoscope_Project"
# [Project Title] -  "Horoscope_Project"

**Team Members:** [Zon Phoo], [Jiaxi Lu ], [Anh Nguyen], [Nokutenda Gift Remwa]  
**Date:** [7.2.2026]  
**Version:** 1.0


## 1. Project Overview.
This project is a Zodiac Management System made for people who like astrology. It helps users check their zodiac sign, check the matching percentage with their partner, find their lucky color, and learn about their future. All the information is kept in one place, so it is easy to use and understand.

## 2. Goals & Objectives
*It should be able to tell the user anything they need to know about astrology especially in relation to themself*
* **Core Goal:**  To build a central "Hub" that breaks down the broad zodiac topic into specific, interactive sub-modules (Identity, Compatibility, Search).
* **Secondary Goal:** To manage a library of personality traits and relationship scores using structured formats like 2D Arrays and external JSON/TXT files.

## 3. The User Journey
*We are gonna create a GUI or at least try but if that is too hard we’ll just use the command line interface for the interaction.*
  1. Onboarding: The user is greeted and asked for their name and birthdate to determine their zodiac sign. 
  2. Navigation: They enter a central menu to select sub-modules like Personality Analysis, Compatibility Testing, or Keyword Search. 
  3. Feedback & Loop: After receiving their results, the user can choose to export a local report or return to the main menu for other features until they decide to exit.

* **The Experience:**
   1.When the program starts, the user is greeted with a welcome message and a brief explanation of the Zodiac Management System.
  2.The user is presented with a main menu containing options such as:
    - Zodiac Identity Calculator
    - Compatibility Checker
    - Zodiac Search
    - View Saved Reports
    - Exit Program
3.Based on the user’s selection, the system navigates them to the corresponding module.
4.The user enters the required information (such as birth date or zodiac signs).
6.The system processes the request and displays results in a clear, readable format.
7.The user is then given the option to return to the main menu, save results, or exit the program.
* **Inputs:**
* We will accept keyboard strings for names and keywords, integers for menu navigation, and formatted date strings (e.g., MM-DD) for astrological calculations.


## 4. Program Logic (Step-by-Step)
*Describe the path our code takes from start to finish. Use a numbered list to show the sequence of events.*

  1. **Initialization:** The program imports necessary libraries (e.g., datetime for calculations, json/os for file handling) and loads the zodiac database from external files into memory.
  2. **Input Phase:** The system prompts the user for their name and birthdate. The Identity Engine immediately validates the date and calculates the user's specific zodiac sign as the primary session variable.
  3. **Processing Phase:** A central menu is displayed, presenting the user with a list of sub-modules (e.g., Personality Analysis, Compatibility Lab, or Discovery Search).
  4. **Output Phase:**  Based on the menu selection, the code branches into specific functions:
      Logic A: Mapping dates to text descriptions.
      Logic B: Comparing two signs using a 2D Matrix to generate a compatibility score.
      Logic C: Filtering the zodiac database based on user-inputted keywords (elements/traits).
  5. **Loop/Cleanup:** The program asks if the user wants to return to the Central Hub for another feature or exit. Upon exit, all file streams are closed, and a farewell message is displayed.


## 5. Team Responsibility Breakdown
*How are we dividing the work? Each member should have a primary area of focus.*
* **Jiaxi Lu:** Responsible for designing and maintaining data storage structures, including 2D arrays and external JSON/TXT files. Handles file input/output operations and ensures data consistency across the system.
* **Anh Nguyen:** Focuses on user interaction, including menu design, prompts, and input validation. Ensures that the program is user-friendly, handles invalid inputs gracefully, and provides clear navigation between modules.
* **Zon Phoo:** Develops the main program logic, including zodiac sign determination, compatibility calculations, and search functionality. Ensures that astrological rules are correctly translated into code and also responsible all the coding part.
* **Nokutenda Remwa:** Responsible for testing all modules, identifying bugs, and verifying program accuracy. Ensures that edge cases are handled properly and that the system runs smoothly as a complete application.


## 6. Module & Function Breakdown
*List the main parts of our code and which team member is responsible for them.*
* **`main.py`**: Serves as the entry point of the application. Handles program initialization, menu navigation, and coordination between all modules (Handled by: [Anh Nguyen])
* **`logic_module.py`**: Contains all core calculation logic, including zodiac sign determination, compatibility scoring, and search-related rules. (Handled by: [Zon Phoo])
* **`storage_module.py`**: Manages data storage and retrieval, including reading from and writing to external JSON/TXT files. Ensures data persistence for saved user reports and zodiac trait libraries. (Handled by: [Jiaxi])
 ** testing_module.py **: Managing and seeing the testing processes forbugs and optimisation. (Handled by: [Nokutenda Remwa])

## 7. Data Storage & Structures
*How are we keeping track of information?*
* **Variables/Collections:** Dictionaries: To store the "Astral Profile" of the current user (e.g., {"name": "Alice", "sign": "Leo"}).
2D Arrays (Nested Lists): To store the Compatibility Matrix, where row and column indices represent different signs to retrieve a matching score.
Lists: To store filtered results for the search engine (e.g., a list of all "Fire" signs).
* **Persistence:** We will store all personality traits and celebrity lists in a structured zodiac_data.json or .txt file for easy retrieval.


## 8. Development Timeline (Milestones)
*We are gonna definitely finish in time no question about that.*
1. **Milestone 1:** [7-2-2026] - We will have the basic project structure and main menu working.
2. **Milestone 2:** [15-2-2026] - We will have our individual modules connected and talking to each other.
3. **Milestone 3:** [8-3-2025] - We will finish testing for bugs and submit the final version.

### Team Checklist:
* **Consistency:** Are we all using the same variable naming style (e.g., `snake_case`)?
* **Communication: We will communicate using Discord, Teams and WhatsApp.
* **Integration:** Yes everyone’s responsibilities align with each other. 
