# Create a Python script that assigns a grade to a student based on their exam score

# Ensure the scorre entered is within the valid range (0-100). If not, print an error message.

# functions allow me to wrap up code and reuse it
# functions are defined with the def keyword
def scoreMe():
    score = int(input("Enter your score:"))
    print("You entered", score)
    # As the user to input a score. Assume the score is out of 100
    # Implement the logic to determine the grade based on the score:
    # A score of 90 and above is an "A"
    if score >= 90:
        print("A")
    # A score of 80-89 is a "B"
    elif score >= 80 and score < 90:
        print("B")
    # A score of 70=79 is a "C"
    elif score >= 70 and score < 80:
        print("C")
    # A score of 60-69 is a "D"
    elif score >= 60 and score < 70:
        print("D")
    # A score below 60 is an "F"
    else:
        print("F")

# call the function
scoreMe()
scoreMe()
scoreMe()
scoreMe()
