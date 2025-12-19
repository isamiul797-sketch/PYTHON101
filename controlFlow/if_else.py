# age = 20
#
# if age >= 18:
#     print("You are old enough to vote")
# else:
#     print("You aren't old enough to vote")

# try:
#     mark = int(input("Enter the mark (0-100): "))
#
#     # Validate mark range
#     if mark < 0 or mark > 100:
#         print("Invalid mark! Please enter a value between 0 and 100.")
#     elif mark >= 80:
#         print("A+")
#     elif mark >= 70:
#         print("A")
#     elif mark >= 60:
#         print("A-")
#     elif mark >= 50:
#         print("B")
#     elif mark >= 40:
#         print("C")
#     elif mark >= 33:
#         print("D")
#     else:
#         print("F")
#
# except ValueError:
#     print("Invalid input! Please enter an integer.")

age = 20
has_permission = False

if age >= 18:
    if has_permission:
        print("you can Enter in club")
    else:
        print("you can't enter in club")

else:
    print("you can't enter in club")