# Module ; we want to stop it being executed directly
import sys


if __name__ == '__main__':
    sys.exit()

def myfunc():
    pass

print(__name__)
