print("Welcome to the quiz!")

playing = input("Do you want to play? (y or n) ")

if playing.lower != "y":
    quit()

print("Okay! Let's play!")

score = 0

answer = input("What does CPU stand for? ")
if answer.lower == "central processing unit":
    score += 1
    print("correct!")
else:
    print("incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower == "graphics processing unit":
    score += 1
    print("correct!")
else:
    print("incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower == "random access memory":
    score += 1
    print("correct!")
else:
    print("incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower == "power supply":
    score += 1
    print("correct!")
else:
    print("incorrect!")

print("You got " + str(score) + " questions right!")
print("That's " + str((score / 4) * 100) + "%")
