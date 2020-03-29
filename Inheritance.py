class MenuItem:
    sizeDict = {'s': 8, 'm': 10, 'l': 12, 'xl': 14}
    ingrDict = {'Pepperoni': 1, 'Peppers': 1, 'Bacon': 2, 'Extra Cheese': 3}
    invDict = {'Pepperoni': 10, 'Peppers': 10, 'Bacon': 5, 'Cheese': 20, 'Coke': 10, 'Coke Zero': 10, 'Beer': 5, 'Wine': 5, 'Meatballs': 10, 'Parmesan': 100, 'Chicken': 10}
    
    def __init__(self, itemSize, ingredients):
        self.itemSize = itemSize
        self.ingredients = ingredients
        
    def Order(self):
        self.cost = MenuItem.sizeDict[self.itemSize]
        for i in self.ingredients:
            self.cost = self.cost + MenuItem.ingrDict[i]
            self.UpdateInventory(i)
        print ("Thank you for your order! Your order will cost: $", self.cost)
            
    def UpdateInventory(self, i):
        MenuItem.invDict[i] = MenuItem.invDict [i] - 1
            
class Pizza(MenuItem):
    sizeDict = {'s': 8, 'm': 10, 'l': 12, 'xl': 14}
    ingrDict = {'Pepperoni': 1, 'Peppers': 1, 'Bacon': 2, 'Extra Cheese': 3}
    
    def Order(self):
        self.cost = Pizza.sizeDict[self.itemSize]
        for i in self.ingredients:
            self.cost = self.cost + Pizza.ingrDict[i]
            self.UpdateInventory(i)
        print ("Thank you for your order! Your pizza will cost: $", self.cost)
    
class Drink(MenuItem):
    sizeDict = {'s': 1, 'm': 1.5, 'l': 2, 'xl': 2.5}
    ingrDict = {'Coke': 0, 'Coke Zero': 0, 'Beer': 1, 'Wine': 2}
    
    def Order(self):
        self.cost = Drink.sizeDict[self.itemSize]
        for i in self.ingredients:
            self.cost = self.cost + Drink.ingrDict[i]
            self.UpdateInventory(i)
        print ("Thank you for your order! Your drink will cost: $", self.cost)
    
class Pasta(MenuItem):
    sizeDict = {'s': 6, 'm': 8, 'l': 10, 'xl': 14}
    ingrDict = {'Meatballs': 3, 'Parmesan': 1, 'Chicken': 2}
    
    def Order(self):
        self.cost = Pasta.sizeDict[self.itemSize]
        for i in self.ingredients:
            self.cost = self.cost + Pasta.ingrDict[i]
            self.UpdateInventory(i)
        print ("Thank you for your order! Your pasta will cost: $", self.cost)
    
def main():
    p = Pizza('s', ['Pepperoni', 'Peppers'])
    d = Drink('xl', ['Wine'])
    pa = Pasta('m', ['Meatballs', 'Parmesan', 'Chicken'])
    p.Order()
    d.Order()
    pa.Order()
    print("Current Inventory:", MenuItem.invDict)
    
main()
    
    
    