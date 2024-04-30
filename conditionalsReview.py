# Ask the user to input the current weather. This can be simplified to three categories for ease: "sunny", "rainy", or "cold".

weather = input("What is the current weather? (sunny, rainy, cold)" :)

# Implement the decision structure to advise on what to wear:
# If the weather is "sunny", recommend "wear sunglasses and a hat".
# If the weather is "rainy", recommend "carry an umbrella and wear waterproof boots".
# If the weather is "cold", recommend "wear a warm coat and gloves".
# If the input doesn't match any category, inform the user with a message saying the input was not recognized.

if weather == "sunny":
    print("Wear sunglasses and a hat.")
elif weather == "rainy":
    print("Carry an umbrella and wear waterproof boots.")
elif weather == "cold":
    print("Wear a warm coat and gloves.")
else:
    print("Input not recognized. Please enter sunny, rainy, or cold.")

#Next 
# Ask the user to input their age and location. Assume location to be either "urban" or "rural".

age = int(input("What is your age?"))
location = input("What is your location? (Urban, rural):")

# logical and comparison operators
# >,<, >=, <=, ==, !=, and, or, not


# Implement the eligibility checks using comparison and logical operators:
# Participants must be at least 18 years old.
# Participants must live in an "urban" area.
# Display a message indicating whether the user is eligible or not based on these conditions.

if age >= 18 and location == "Urban":
    print("You are eligible to participate.")
else:
    print("You are not eligible to participate.")

# Next
# check to see if the user is eligible to vote
# Ask the user to input their age and citizenship status.
# Assume citizenship status to be either "yes" or "no"

age = int(input("What is your age?"))
citizenship = input("Do you have citizenship? (yes, no):")

if age >= 18 and citizenship == "yes":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
