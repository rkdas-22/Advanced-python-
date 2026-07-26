#Decorator
def my_decorator(func):
    def wrapper():
        print("This is before the function is called.")
        func()
        print("This is after the function is called.")
    return wrapper

@my_decorator
def say_hello():
     print("Hello! How you doing?")
     
say_hello()

#Iterator
list = [2,4,6,8]
my_iter = iter(list)

print (next(my_iter))
print (next(my_iter))
print (next(my_iter))

#Generator
def countdown(n):
    while n>0:
        yield n
        n-=1
        
for num in countdown(10):
    print(num)
    
#Closure
def outer_func(a):
    def inner_func(b):
        return a + b 
    return inner_func

add_ten = outer_func(10)
print(add_ten(39))

#Output 
# This is before the function is called.
#Hello! How you doing?
# This is after the function is called.
#2
# 4
# 6
# 10
#9
# 8
# 7
# 6
# 5
# 4
# 3
# 2
# 1
#49