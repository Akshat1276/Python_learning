import math

def convertor(second):
    hour = second/3600
    minute = (second%3600)/60
    second = second%3600
    sec = second % 60
    # a = math.floor(hour)
    # b = math.floor(minute)
    print("The given seconds correspond to....   ", math.floor(hour), " hours  ", math.floor(minute)," minutes  ", math.floor(sec), " seconds")

x = int(input("Enter the Seconds:  "))
convertor(x)
# convertor(7400)
