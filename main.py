from my_tools import doctor, treatments, research, general, fitness, mealplan, email_info, contact_doctor
from Tools.find_dr import find_doctor_function
from Tools.recipes import recipe_function

# 1. Opening message
print("\nHi, this is your personal Healthee Assistant! What can I help you with today?\n")

# 2. Give user options to choose from
options = ["Medical Question", "Fitness Question", "Nutrition/Diet Question"]
for i, option in enumerate(options):
    print(f"{i+1}. {option}")


# Get user choice for main categories
choice = int(input("\nPlease enter the number corresponding to your choice: "))


# 3. Handle user choice
if choice == 1:  # Medical Question
    medical_options = ["Diagnose", "Treatments", "Research", "Find Doctors", "General Question"]
    for i, option in enumerate(medical_options):
        print(f"{i+1}. {option}")
    
    medical_choice = int(input("\nPlease enter the number corresponding to your medical question choice: "))

    # 4. Call relevant Python tool based on user's medical choice
    if medical_choice == 1:
        symptoms = input("\nWhat are your symptoms?\n")
        response = doctor(symptoms)
        print("\n" + response + "\n")
        contact_doctor()

    elif medical_choice == 2:
        symptoms = input("\nWhat do you need treatment for?\n")
        response = treatments(symptoms)
        print("\n" + response + "\n")
        email_info()
        

    elif medical_choice == 3:
        symptoms = input("\nWhat diagnosis to you need articles for?\n")
        response = research(symptoms)
        print("\n" + response + "\n")
        email_info()

    elif medical_choice == 4:
        message = input("\nWhat is your diagnosis and zipcode?\n")
        response = find_doctor_function(message)
        print("\n" + response + "\n")
        contact_doctor()
  
    elif medical_choice == 5:
        message = input("\nWhat can I help you with?\n")
        response = general(message)
        print("\n" + response + "\n")
        contact_doctor()

    else:
        print("Invalid choice. Exiting.")

elif choice == 2:  # Fitness Question
    message = input("\nWhat can I help you with?\n")
    response = fitness(message)
    print("\n" + response + "\n")
    email_info()
    

elif choice == 3:  # Nutrition/Diet Question
    food_option = ["Meal-Plan", "Recipes", "General Question"]
    for i, option in enumerate(food_option):
        print(f"{i+1}. {option}")
    
    food_choice = int(input("\nPlease enter the number corresponding to your nutrition/diet question choice: "))

    # 4. Call relevant Python tool based on user's medical choice
    if food_choice == 1:
        message = input("How can I help you?\n")
        response = mealplan(message)
        print("\n" + response + "\n")
        email_info()

    elif food_choice == 2:
        message = input("\nWhat do you want to cook?\n")
        response = recipe_function(message)
        print("\n" + response + "\n")
        email_info()   

    elif food_choice == 3:
        message = input("\nWhat can I help you with?\n")
        response = general(message)
        print("\n" + response + "\n")
        contact_doctor()

else:
    print("\nHave a healthy day!")



