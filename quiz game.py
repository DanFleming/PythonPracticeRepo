print("Welcome to the quiz!")

playing = input("Do you want to play? (y or n) ")

if playing != "y":
    quit()

print("Okay! Let's play!")

score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    score += 1
    print("correct!")
else:
    print("incorrect!")

answer = input("What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    score += 1
    print("correct!")
else:
    print("incorrect!")

answer = input("What does RAM stand for? ").lower()
if answer == "random access memory":
    score += 1
    print("correct!")
else:
    print("incorrect!")

answer = input("What does PSU stand for? ").lower()
if answer == "power supply":
    score += 1
    print("correct!")
else:
    print("incorrect!")

print("You got " + str(score) + " questions right!")
print("That's " + str((score / 4) * 100) + "%")
