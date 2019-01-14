'''
Created on Nov 1, 2016

@author: zvz201
'''

def hello_world():
    return print("Hello World: ", time.strftime("%c"))


if __name__ == "__main__":
    import sys, time
    hello_world()
