#knowing the types 
# x=9
# y="hai"
# print(type(x))
# print(type(y))


#Assigning multiple Variables
# x = y = z = "Orange"
# print(x)
# print(y)
# print(z)
# x, y, z = "Orange", "Banana", "Cherry" {assign in order}
# print(x)
# print(y)
#print(z)


#unpacking variables
# sports = ["Soccer", "Basketball", "Cricket"]
# x,y,z=sports
# print(x)
# print(y)
# print(z)


#output variables
# x="I"
# y="am"
# z="learning"
# print(x,y,z) this is one way to store or output it it gives all 3 values combined 
#you can use the same thing with + as the mediator like:
# x="I"
# y="am"
# z="learning"
# print(x + y + z) but the + keeps it combined with no spacing must remember that


#########
# ####global variables (variables that are created outside of a function)
#[so it is like assigning a certain constant task to a function
# which when called out later in the code comes the way you assigned it]
#examples:
# x="bishal"
# def myname():
#  print("my name is "+ x)
# myname() [remember that you should not keep this INSIDE the above function]

##another example:

# x="mango"
# def fruit():
#     x="apple"
#     print("My favorite fruit is " + x)
# fruit()
# print ("I like "+ x)

#if you use the term global no matter what value you assign in the beginning the variable will be whatever is ther in the global variable
# x="mango"
# def fruit():
#     global x
#     x ="apple"
#     print("My favorite fruit is " + x)
# fruit()
# print ("I like "+ x)


