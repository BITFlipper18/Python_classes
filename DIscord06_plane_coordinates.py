# Two points in a plance are specified using the coordinates (x1,y1) and (x2,y2). Write a program that calculates the slope of a line through two (non-vertical) points entered by the user. Slope = [(y2-y1)/(x2-x1)]

def Slope(x1, x2, y1, y2):
    slope = ((y2-y1)/(x2-x1))
    print(f"The slope is {slope}.")


print("For the calcultion of the slope, we will need following data: ")
y2 = int(input("Enter y2-coordinate: "))
y1 = int(input("Enter y1-coordinate: "))
x2 = int(input("Enter x2-coordinate: "))
x1 = int(input("Enter x1-coordinate: "))


Slope(x1, x2, y1, y2)

# # A try-except statement can ben added in function to avoid ZeroDivisionError
# try:
# except:ZeroDivisionError
# print("Data cannot be divided by zero!!Re-run program and re-evaluate your data.")