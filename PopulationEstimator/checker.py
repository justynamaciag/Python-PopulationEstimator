import numpy as np

def find_function(data):
    x = np.array(data.dates)
    y = np.array(data.values)
    z = np.polyfit(x,y,3)
    return np.poly1d(z)

def calculate(year, data1, data2, l):
    fun1 = find_function(data1)
    fun2 = find_function(data2)

    for i in range (2017, year):
        l = l*fun1(i) - fun2(i)*l/1000

    return l


def check_dependence(val1, val2):

    k=0
    while(val2<val1):
        val2*=1.25
        k+=1

    return k





