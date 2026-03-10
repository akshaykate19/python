#left incremental pyramid
# count=int(input("Enter numbe OF Row = "))
# n=1
# for i in range(count):
#     for j in range(i+1):
#         print("*", end="")
#     print()

# Right Incremental pyramid

# count=int(input("Enter numbe OF Row = "))

# for i in range(count):
#     for j in range(count , i , -1):
#         print("*", end="")
#     print()

# 
# count=int(input("Enter Row Count ="))
# for i in range(count):
#     for k in range(count,i+1,-1):
#         print(end=" ")

#     for j in range(i+1):
#         print("*",end="")
#     print()

# right decremenal pyramid

# count=int(input("Enter Row Count ="))
# for i in range(count):
#     for k in range(i):
#         print(end=" ")

#     for j in range(count,i,-1):
#         print("*",end="")
#     print()

# Hill Incremental

count=int(input("Enter Row Count ="))
for i in range(count):
    for k in range(i):
        print(end=" ")

    for j in range(count,i,-1):
        print(" *",end="")
    print()