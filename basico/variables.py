                       #Nombramiento de variables 

#de forma CAMELCASE -- (se lo realiza con la primera letra de la palabra en mayuscula)
NombreCompleto= "Juan"

#de forma snake_case -- (se lo realiza con separacion mediante guiones bajos)
nombre_completo= "Juan"

                        #Concatenación de variables

#concatenacion con el signo + snake_case
bienvenida= "hola " + "Cómo estás"
print(bienvenida)

#concatenacion con f-string camelCase
edad= 25
presentacion= f"Hola, mi nombre es nombre completo y tengo {edad} años."
print(presentacion) 

                        #Operadores de pertenencia in y not in
                    
print(edad in presentacion) #True 
print(edad not in presentacion) #False  
