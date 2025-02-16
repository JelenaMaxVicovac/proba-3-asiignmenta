import product
class Cart():
    def __init__(self):
        self.cart_items=[]
    
    #metod za dodavanje proizvoda u korpu 
    def add_item(self,product):
        self.cart_items.append(product)
    
        
    #metod za racunanje vrednosti korpe
    def cart_value(self):
        vrednost=0
        for item in self.cart_items:
            vrednost+=item.price
        print (f"Total value in Cart: {vrednost}")
        
    #prikaz sadrzaja korpe
    def display_cart(self):
        print ("Sadrzaj korpe:")
        for item in self.cart_items:
            print (item.name)


         