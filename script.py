import sys

# print sys.version
print(sys.executable)


def greet(who_to_greet):
    test = "Test"
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


print(greet("Ray"))
print(greet("Shawn")