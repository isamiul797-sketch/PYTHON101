# fruits = ["apple", "banana", "cherry"]
#
# index = 0
#
# while index < len(fruits):
#     print(fruits[index])
#     index += 1


# word = "python"
#
# index = 0
# while index < len(word):
#     print(word[index])
#     index += 1


# index = 0
# end = 30
#
# while index < end:
#     if  index == 18:
#         index = index + 3
#         # break
#         continue
#     print(index)
#     index += 3


examresult = {'phy':70, 'chem':90, 'math':87}

keys = list(examresult.keys())

index = 0
while index < len(keys):
    eachkey = keys[index]
    output = "subject: " +eachkey,"marks: " +str(examresult[eachkey])
    print(output)
    index += 1

