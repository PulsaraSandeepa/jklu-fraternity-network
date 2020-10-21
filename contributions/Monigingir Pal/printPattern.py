#Function to print a spaced pyramid based on number of rows
def printPyramid(height) :
    for i in range(0, height):
        # print the first row
        # print spaces and do not move to new line
        for gap in range(1, (height-i)+1):
            print(" " * 2, end="")
        # print stars and do not move to new line
        for star in range(0, i+1):
            print("*   ",end="")
        # go to next row
        print()

#Input method
if __name__=='__main__':
    height = int(input("Enter number rows : "))
    printPyramid(height)

