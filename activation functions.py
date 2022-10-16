import math
def sigmoid(x):
    return 1/(1+math.exp(-x))
# print(sigmoid(0.5))


def tanh(x):
    val = (math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x))
    return print(val)

# tanh(1)

def relu(x):
    val = max(0,x)
    return print(val)


# relu(1)


def leaky_relu(x):
    val = max(0.1*x,x)
    return print(val)

leaky_relu(2)