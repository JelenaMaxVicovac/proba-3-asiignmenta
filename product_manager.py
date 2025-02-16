import product
class ProductManager():
    #kreiranje liste proizvoda
    def __init__(self):
        self.lista =[]
    
    # funkcija za unos proizvoda u listu
    def input_product(self,product):
        self.lista.append(product)  
        
     #funkcija za prikaz proizvoda   
    def display_products(self):
        for i in self.lista:
            i.display_info()
            print ("--------")
            
    # funkcija za prikaz ukuone vrednosti svih proizvoda
    def total_value(self):
        suma=0
        for i in self.lista:
            suma+=i.price*i.quantity
        print (f"Ukupna vrednost svih proizvoda je:{suma}")
    
    #funkcija za uklanjanje prema imenu
    def name_removal(self,name):
        for i in self.lista:
            if i.name == name:
                self.lista.remove(i)
                print (f"Product {i.name} has been removed")
           

            
            
            
        
    
        


   
    