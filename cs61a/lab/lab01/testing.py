def bake(cake, make):
    if cake == 0:
        cake = cake + 1
        print(cake)
    
    if cake == 1:
        print(make)
    
    return cake  
bake(0, 29)