# x={6,89,45,34,90}
# print(x)


# x.add(100)
# print(x)
# x.add(90)
# print(x)

# x.add([11,22]) Typee error
# x.add((11,22))
# print(x)
# y={1,2}
# x.update(y)
# print(x)

# colors={"red","green","pink","orange"}
# print(colors)
# colors_new=list(colors)
# print(colors_new)
# i=colors_new.index("red")
# colors_new[i]="light_red"
# print(colors_new)
# colors_new1=set(colors_new)
# print(colors_new1)

#wap

# mylist=[12,12,45,23,78,45,1,1,1]
# print(mylist)
# new_list=set(mylist)
# print(new_list)

# or using loop 

# new_mylist=[]
# for i in mylist:
#     if i not in new_mylist:
#         new_mylist.append(i)
# print(new_mylist)

# comprehension 

#wap to create myset and add number elements as entered count

# myset={}
# count=int(input("Enter count for numbers = "))
# for i in range(count):
#     number=int(input(f"enter number"))
#     myset.append(numberlist)
# print(myset)

# myset=set()
# print(myset,type(myset))
# count=int(input("Enter count for numbers = "))
# for i in range(count):
#     number=int(input(f"enter {i+1} number"))
#     myset.add(number)
# print(myset)

#set comprehension
# count=int(input("Enter count for numbers = "))
# myset1=({int(input(f"enter {i+1} number =")) for i in range(count)})
# print(myset1)

#wap to print 10 to 1 in set using comprehension
# print({i for i in range(-10,0)})
# x={12,-321,56,343,-5,35}
# print({i for i in x if i>0})

#wap to show sum of element of below list

# mylist=[12,3,4,5,11]
# sum=0
# for i in  mylist:

#     sum+=i
# print(sum)

# mylist=[12,3,4,5,11]
# print([i**3 for i in mylist])

