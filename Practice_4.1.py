Name_list = ["a", "b" , "c"]
salary_list = [5600, 2000, 3700]
products = []

for x in salary_list:
    products.append(0.3*x + x)
S_products = sum(products)
print("The sum equals to: ", S_products)
print(products)
