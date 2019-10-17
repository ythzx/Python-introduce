# coding:utf-8

class Operation():
    def __init__(self):
        print("init")
    
    def __enter__(self):
        print("enter")
        return "Enter"
    
    def __exit__(self, type, value, trace):
        print("exit")

def get_operetion():
    return Operation()

with get_operetion() as f:
    print("get operation: {}".format(f))

"""
init
enter
get operation: Enter
exit
"""
"""
ref:
    https://blog.csdn.net/xc_zhou/article/details/80810111
    http://dongweiming.github.io/Expert-Python/#23
"""