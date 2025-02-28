# def showMessage(msg):
#     print("Inside")
#     print(msg)
#     print("outside")


# #def main
# def main():
#     print("main")
#     message = "Argument Passed!"
#     showMessage(message)
#     print("main ends")

# print("program begins")
# main()
# print("program ends")

# def calculateMpg(milesDriven, gallonsUsed):
#     mpg = milesDriven / gallonsUsed
#     mpg = round(mpg, 1)
#     return mpg

# miles, gallons = input("Please enter the miles driven and gallons: ").split()
# miles, gallons = float(miles), float(gallons)
# mpg = calculateMpg(miles, gallons)
# print("The MPG is: ", mpg) 

# def getInput():
#     pass #skips the function

# def calcGrossPay():
#     pass

# def calcOvertime():
#     pass

# def calcWithHoldings():
#     pass

# def calcNetPay():
#     pass

# def main():
#     getInput()
#     calcGrossPay()
#     calcOvertime()
#     calcWithHoldings()
#     calcNetPay()

# if __name__ == '__main__': #if imported, does not get executed
#     main()

def calcDiscount(purchaseAmount, discountPercent):
    discountAmount = purchaseAmount * (discountPercent/100)
    totalBill = purchaseAmount - discountAmount
    return totalBill

def main():
    purchaseAmount = float(input("Enter the purchase amount: "))
    discountAmount = int(input("Enter the discount precentage: "))
    finalBill = calcDiscount(purchaseAmount, discountAmount)
    print("Final Bill:", finalBill)

if __name__ == '__main__':  
    main()