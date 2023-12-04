#!/usr/bin/python3
def no_c(my_string):
    gen = [i for i in my_string if i != 'c' and i != 'C']
    return "".join(gen)


print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))
