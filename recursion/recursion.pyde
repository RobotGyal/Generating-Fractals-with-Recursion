# FRACTAL TREE
# KOSH CURVE
# CANTOR SET
# MANDELBROT SET



def setup():
  print("The recursive factorial is: ", factorial(4))
  
  
def draw():
  pass


def factorial(n):
    """ Calls itself to provide recursion """
    if n == 1:
        return 1
    else:
        return n * (factorial(n-1))
