# Function that finds the letter grade from the exam score
def getGrade(score):
    if score < 0 or score > 100:
        print("Error: Score must be between 0 and 100.")
        return ""

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


# Ask the user for their exam score
examScore = float(input("Enter your exam score: "))

# Call the function and save the letter grade
letterGrade = getGrade(examScore)

# Print the grade if the score was valid
if letterGrade != "":
    print("Your letter grade is:", letterGrade)