name = input("Enter student's name: ")
familyname = input("Enter student's family name: ")
score1 = int(input("Enter first score: "))
score2 = int(input("Enter second score: "))
score3 = int(input("Enter third score: "))

summation = score1 + score2 + score3
average = summation / 3

if average>=17:
    print("Great")

if average<17 and average>=12:
    print("Normal")

if average<12:
    print("Fail")
