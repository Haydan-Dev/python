# Docstrings & PEP-8
# python docstrings are the strings literals 
# that appear right after the definition , 
# method,class,or module.


# this method is better for other languages 
def square(n):
    '''Takes in a number n , return the square of n'''
    print(n*n)
square(10)

# Note : docstring ko always def function (): ke baad turant likhna hota hai.

# this method is better for python language
def square(n):
    '''Takes in a number n , return the square of n'''
    return n**2
print(square(10))
Power_of_10 = square(10)
print(Power_of_10)
print(square.__doc__)

# PEP-8
# is a document that provide guidelines and best practice on how to write python code .
# It was written in 2001 by Guido van Rossum , Barry warsaw
# Nick Coghlan. the primary focus of PEH 8 is to 
# Improve the Readablity and consistancy of pyhone code.

def connect_to_server(ip_address, port=8080):
    """
    Connects to the Home Server using the given IP and Port.
    
    Parameters:
    ip_address (str): The public IP of the server.
    port (int): Port number (default is 8080).
    
    Returns:
    str: A success message if connected.
    """
    return f"Successfully connected to {ip_address} on port {port}"

# Ab niche wali lines ko dhyan se dekhna
print("--- TEST 1: Docstring Access ---")
print(connect_to_server.__doc__)

print("\n--- TEST 2: Real Help Manual ---")
help(connect_to_server)  # <--- Ye hai asli magic!