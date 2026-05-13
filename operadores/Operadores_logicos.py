#AND
Resultado_and = True & False  # Resultado_and es False
Resultado_and2 = True and True  # Resultado_and2 es True
Resultado_and3 = False and True  # Resultado_and3 es False
Resultado_and4 = False and False # Resultado_and4 es False


#OR
Resultado_or = True | False  # Resultado_or es True
Resultado_or2 = True | True  # Resultado_or2 es True
Resultado_or3 = False or True  # Resultado_or3 es True
Resultado_or4 = False or False # Resultado_or4 es False


#NOT
Resultado_not = not True  # Resultado_not es False
Resultado_not2 = not False  # Resultado_not2 es True

#Combinacion de operadores logicos
combinacion1 = (True and False) or (not False)  # combinacion1 es True
combinacion2 = not (True or False) and (False or True)  # combinacion2 es False
combinacion3 = (True and (False or True)) or (not True)  # combinacion3 es True 

print(Resultado_or)