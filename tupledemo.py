#create tuple
tup=()
print(tup,type(tup))
t1=tuple()
print(t1,type(t1))

t2=(500)
print(t2,type(t2))

t3=(500,100,"Hello")
print(t3,type(t3))

my_tuple=(3,45,64,6764,34,100)
print(my_tuple)
#index
print("first element = ",my_tuple[0])
print("last element = ",my_tuple[-1])

#sclicing
print(my_tuple[::-1])
print(my_tuple[2:5])

#operation
tuple1=(1,2,3)
tuple2=(4,5,6)
print(tuple1+tuple2)
# print(tuple1+100) Error hai ye error

#tuple function
tuple3=(1,5,4,2,3)
print
print(sorted(tuple3))
print(sorted(tuple3,reverse=True))

#tuple method-index(),count()
tuple4=("hello","red","organge","green",1000,300,700)
print(tuple4.index(300))
print(tuple4.count(300))

#immutability
# tuple4[0]="welcome" #type error
print(tuple4)

#traversing of tuple
my_tup=(100,200,300,400,1,2,3)

# for i in my_tuple:
#     print(i)

#ascending
for i in sorted(my_tuple):
    print(i)

#descending

for i in sorted(my_tuple)[::-1]:
     print(i)