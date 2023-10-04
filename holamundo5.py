def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    # Define a function that takes two arguments and returns the first one
    def select_first(a, b):
        return a
    # Call the pair function with the select_first function
    return pair(select_first)

def cdr(pair):
    # Define a function that takes two arguments and returns the second one
    def select_second(a, b):
        return b
    # Call the pair function with the select_second function
    return pair(select_second)

# Example 
pair = cons(3, 4)
print(car(pair))  
print(cdr(pair))  
