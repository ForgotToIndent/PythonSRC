# grade = int(input("Provide the student's grade: "))

# while grade < 0 or grade > 100:
#     print("Invalid grade entered")
#     grade = int(input("Provide the student's grade: "))

# print(grade)


# #1+2+3+4+5
# add = 0 #the accumulator
# for i in range(1,6):
#     print(i)
#     add = add + i #running total

# print(add)

# sum = 0
# for i in range(5):
#     ui = int(input("Enter digits: "))
#     sum = sum + ui
# print(sum)

# sum2 = 0
# check = "y"
# comp = ""
# while check == "y":
#     ui2 = input("enter letter: ")
#     comp += ui2
#     check = input("Do you want to continue? y or n")
# print(comp)

# sum = 0
# count = 0
# ui = int(input("Enter digits: "))
# while ui != 0:
#         sum = sum + ui
#         count += 1
#         ui = int(input("Enter next digit: "))

# print(sum)
# average = sum / count
# print("Average is:",average)
# #or use break to end loop. for example 'if' condition, then break


# for i in range (10):
#     if i == 6:
#         continue
#     print(i)
# print("loop end")


vowel = "aeiouAEIOU"
count = 0
while count < 5:
    v = input("Enter a vowel: ")
    if v in vowel:
        print(v, "is a vowel!")
        count += 1
    else:
        print("Not a vowel")
        continue
