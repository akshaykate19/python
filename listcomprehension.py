# for i in range(1,11):
#     print(i,end=" ")

#List comprehension
#Syntax [output for iterable_variable in sequence_object if condition]

#print 1 to 10
# print([i for i in range(1,11)])

# print([i*i for i in range(1,11)])

#print even number from 1 to 10 

# for i in range(1,11):
#     if i%2==0:
#      print(i,end=" ")


# print([i for i in range(1,11) if i%2==0])

#WAP to create mylist add number as per count enter

# mylist=[]
# count=int(input("Enter Count For Number = "))
# for i  in range(count):
#     number=int(input(f"Enter {i+1} Number = "))
#     mylist.append(number)
# print(mylist)

# or 

# count=int(input("Enter Count For Number = "))
# mylist_new=[input("Enter Number")for i in range(count)]
# print(mylist_new)

# mylist=[12,4,2,67,256,600,2]
# even=[]
# odd=[]
# for i in mylist:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)

# or
# [even.append(i) if i%2==0 else odd.append(i)  for i in mylist]
# print(even)
# print(odd)

