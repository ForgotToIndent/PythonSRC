import random

class Coin:
    
    def __init__(self):
        self.sideUp = "heads" #class variable
    
    def toss(self):
        if random.randint(0,1) == 0:
            self.sideUp = "heads"
        else:
            self.sideUp = "tails"

    def get_side(self):
        return self.sideUp
    
def main():
    #create an instance of object
    coin1 = Coin()
    print(coin1.get_side())

main()
