# a function calling it self in itself is called recursion
#  function call itself is called recursion.


# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(6))




# def countdown(number):
#     if(number>0):
#         print(number)
#         countdown(number-1)
#     else:
#         print(number)    
# countdown(10)
  


# def sumofnumbers(number):
#     if(number>1):
#        return number+sumofnumbers(number-1)   
#     elif(number == 1):
#         return 1
#     else:
#         return "Invalid number"
# print(sumofnumbers(-10))


# def power(Base,Exponent):
#     if(Exponent>=1):
#         return Base * power(Base,Exponent-1)
#     elif(Exponent ==0):
#         return 1
#     else:
#         return "Invalid Exponential or Base"
# print(power(2,3))


def sum_digit(number):
    if(number==0):
        return 0
        
    else:
        return (number%10) + sum_digit(number//10) 
print(sum_digit(112))




