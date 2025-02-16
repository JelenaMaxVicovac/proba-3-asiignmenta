import product
import product_manager

#kreiranje instance klase ProductManager
manager=product_manager.ProductManager()

#kreiranje nekoliko objekata klase Produkt
pr1=product.Product("cokolada",250,10)
pr2=product.Product("smoki",75,15)
pr3=product.Product("mleko",135,12)

#dodavanje objekata u listu i prikaz iste
manager.input_product(pr1)
manager.input_product(pr2)
manager.input_product(pr3)
manager.display_products()

#prikaz ukupne vrednosti svih proizvoda
manager.total_value()