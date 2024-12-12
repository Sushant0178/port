    
def cont_words():
    words = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

    emty_dict = {}
    
    for i in words:
        if i in emty_dict:
            emty_dict[i] +=1 
        else:
            emty_dict[i]=1
    print(emty_dict)
    for key , value in emty_dict.items():
        print(f"{key}:{value}")
        

# # Input two numbers
# a = 5
# b = 10

# print(f"Before swapping: a = {a}, b = {b}")

# # Swap the values using a temporary variable
# temp = a
# a = b
# b = temp

# print(f"After swapping: a = {a}, b = {b}")

# a = 3 
# b = 4

# a = a+b
# b = a-b
# a = a-b

# print(f"a = {a} b = {b}")

# words = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

# a =  {}

# for i in words:
#     if i in a:
#         a[i]+=1
#     else:
#         a[i]=1

# print(a)

# for key ,value in a.items():
#     print(f"{key}:{value}")


a = 1
b = 2

# a,b=b,

# temp  =  a
# a = b
# b = temp 

# a = a+b
# b = a-b
# a = a-b



words = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

a = {}

for i in words:
    if i in a:
        a[i]+=1
    else:
        a[i]=1

print(a)



