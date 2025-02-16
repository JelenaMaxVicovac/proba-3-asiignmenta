from product import Product
class ProductManager():
    def __init__(self):
        self.lista =[]
    
    def input_product(self,product):
        self.lista.append(product)
        print (f"Product {product} has been added")
        
    def display_products(self):
        print (self.lista)

            
            
            
        
    
        


   
    