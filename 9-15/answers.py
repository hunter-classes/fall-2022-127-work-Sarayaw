#Chapter 7 Answers
#this is #7
is_even= int(input("Enter a number: "))
if is_even % 2 == 0:
    print("True")
else:
    print("False")
    
    
    
#This is #8
is_odd= int(input("Enter a number: "))
if is_odd % 2 == 0:
    print("False")
else:
    print("True")



#This is #10
def is_rightangled(a, b, c):
    return abs((a ** 2 + b ** 2) - (c ** 2)) < 0.001

#This is #11
def is_rightangled(a, b, c):
    if a > b and a > c:
        return abs((b ** 2 + c ** 2) - (a ** 2)) < 0.001
    elif b > a and b > c:
        return abs((a ** 2 + c ** 2) - (b ** 2)) < 0.001
    else:
        return abs((a ** 2 + b ** 2) - (c ** 2)) < 0.001




#CodingBat Answers

#String_1---->hello_name
def hello_name(name):
    return "Hello " + name + "!"
  
#String_1---->make_out_word
def make_out_word(out, word):
    return out[:2] + word + out[2:]
  
#String_1----->first_two
def first_two(str):
    return str[:2]
