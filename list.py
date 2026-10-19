#Lists: ordered,mutable, allows duplicate elements

mylist=["banana","cherry","apple"]
print(mylist)

#length
print(len(mylist))

#index
print(mylist[0])

print(mylist[-1])
print(mylist[-2])

#looping
for i in mylist:
    print(i)

#checking items
if "cherry" in mylist:
    print("yes")
else:
    print("no")
         

#append

mylist.append("lemon")
print(mylist)

#insert

mylist.insert(2,"guava")
print(mylist)

#pop

mylist.pop()
print(mylist)


#remove

mylist.remove("cherry")
print(mylist)

#reverse
mylist.reverse()

print(mylist)

#sort
#sort will return none and it will modify the orginal list
num = [10,2,6,1,34,56]
num.sort()
print(num)

#sorted
#sorted will return a new modified list by creating a new copy of the sorrted one without affecting the orginal one 
sortedlist= sorted(num)
print(sortedlist)


multiple = [1] * 5
print(multiple)

newlist = [2]*4

#concat

joined = multiple + newlist
print(joined)



#slicing

slicelist = [1,2,3,4,5,6,7,8]

a= slicelist[1:5]

print(a)

#postion 
b = slicelist[1::3]

# slicing all means create a copy with slice

d = slicelist[:]
print(d)


print(b)

# reverse using slice
c = slicelist[::-1]
print(c)


#copying

# this pattern will modify the orginal list , because both ponting towards same memory space, Use ,copy() or slice[:] to create a copy without affecting the orginal one.
list_org = ["apple","grape","orange"]

list_copy = list_org 

list_copy.append("tomato")
print(list_copy)
print(list_org)

#copy
copied = list_org.copy()
print(copied)
copied.append("lemon")

print(list_org)
print(copied)

# use slice[:] 

slice_copy = list_org[:]
print(slice_copy)
slice_copy.append("mango")
print(list_org)


# new list with  new expression 

arr = [1,2,3,4,5,6]

double = [i*i for i in arr]
print(double)

























