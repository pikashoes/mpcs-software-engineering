# To Do:
#
# Implement a class named CoinMachine.
#

class CoinMachine:
    
    #Initialize with number of coins in inventory
    def __init__(self, initQ, initD, initN, initP):

        self.keys = ["quarter", "dime", "nickel", "penny"]
        self.coinValues = { "quarter":25, "dime":10, 
                            "nickel":5, "penny":1 }
        
        self.coinCount = {  "quarter": initQ, "dime": initD,
                            "nickel": initN, "penny": initP }
        
        self.final = []
    
    #Amount is between 0 and 99 cents   
    #Returns 0 if not enough change, return 1 if successful
    def getChange(self, amount):
        index = 0
        while amount != 0:
            for coin in self.keys:
                value = self.coinValues[coin]
                num = amount // value
                count = self.coinCount[coin]
#                print(value, num, count)
                
                if count > num:
                    count -= num
                elif count > 0 and count <= num:
                    diff = num - count
                    count -= diff
                    num -= diff
                else:
                    num = 0
                    
                self.final.append([coin, num])
                amount -= num * value
                index += 1
                
                if index > 3 and amount > 0:
                    ind = 0
                    return ("ERROR")
        
        ind = 0
        
        for item in self.final:
            if item[1] != 0 and item[1] != 1:
                if ind == 3: #If it's pennies, then we can't write "pennys"
                    print("Dispensing: " + str(item[1]) + " pennies")
                else:
                    print("Dispensing: " + str(item[1]) + " " + self.keys[ind] + "s")
            elif item[1] != 0 and item[1] == 1:
                print("Dispensing: " + str(item[1]) + " " + self.keys[ind])
            ind += 1
        return self.final        
            

#Main Method
def main():
    coinM = CoinMachine(1, 0, 0, 0)
    coinM.getChange(50)

main()