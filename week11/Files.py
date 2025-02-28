# outfile = open("C:\\Users\\Stack\\Documents\\python_prog\\week11\\testing.txt", "a")
# outfile.write("THIS IS APPENDED")
# outfile.close()

# #to open for append, then closing
# with open("staff.txt", "a") as infile:
#     infile.write("lilly\n")

# with open("C:\\Users\\Stack\\Documents\\python_prog\\week11\\testing.txt", "r") as file: #if no mode provided, default is read
#     print(file.read())

# #prints each line one by one
# with open("C:\\Users\\Stack\\Documents\\python_prog\\week11\\testing.txt", "r") as file: #if no mode provided, default is read
#     print(file.readline())
#     print(file.readline())
#     #can also do for line in file: print(line, end="")

# lst = ["apple", "banana", "grapes"]
# with open("C:\\Users\\Stack\\Documents\\python_prog\\week11\\testing.txt", "w") as file: #if no mode provided, default is read
#     for item in lst:
#         file.write(item + "\n")

lst = ["welcome all to sheridan", "hello world", "Hi all", "all"]
with open("C:\\Users\\Stack\\Documents\\python_prog\\week11\\testing.txt", "w") as outfile:
    for item in lst:
        outfile.write(f"{item}\n")

key = "all"

with open("C:\\Users\\Stack\\Documents\\python_prog\\week11\\testing.txt") as infile:
    for line in infile:
        if key in line: 
            print(line)


