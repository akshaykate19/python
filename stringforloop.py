#method-count,find,replace,join,index,split,splitline,z fill

#iterate string
name="Itedant"
# for i in name:
#     print(i)

#reverse string
# print("reverse string:",name[::-1])

# newstr=""
# for i in name:
#     newstr=i+newstr

# print(newstr)

# withoutvowel_str=""
# for i in name:
#     if i not in "aeiouAEIOU":
#         withoutvowel_str=withoutvowel_str+i
# print(withoutvowel_str)

#wap to print number of occuances of enered 
#character from any string

# str=input("Enter string =")
# char=input("Enter Character =")
# count=0

# for i in str:
#     if char==i:
#         count+=1

# print(f"{char} character count into {str} is {count}")

#wap to print numbe f occurances of entered 


str=input("Enter string=")
chkstr=input("Enter char/word to find and show count = ")
count=0
check=""
for i in range(len(str)):
    # print(i,str[i])
    k=i
    for j in range(len(chkstr)):
        try:
            check+=str[k]
            k+=1
        except:
            None
    if check==chkstr:
        count+=1
    check=""

if count!=0:
    print(f"{chkstr} found in {str} and count={count}")
else:
    print(f"{chkstr} not found in {str}")