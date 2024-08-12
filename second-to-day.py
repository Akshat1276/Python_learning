def convertor(second):
    hour = second/3600
    minute = (second%3600)/60
    second = second%3600
    sec = second % 60
    print("The given seconds correspond to.......%i hours  %i minutes  %i seconds", hour, minute, sec)

x = int(input("Enter the Seconds:  "))
convertor(x)