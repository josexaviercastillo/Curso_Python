#operadores de suma y resta
a = 10
b = 5           
suma = a + b     # suma es 15
resta = a - b    # resta es 5
print(suma , resta )

#operadores de multiplicacion y division
multiplicacion = a * b  # multiplicacion es 50
division = a / b        # division es 2.0
print(multiplicacion, division)

#operadores de modulo o resto y exponente
modulo = a % b        # modulo es 0
exponente = a ** b    # exponente es 100000
print(modulo, exponente)

#operadores de division entera devuelve un entero int
division_entera = a // b  # division entera es 2
print(division_entera)

#operadores combinados el valor de la variable se modifica con la operacion
a += 5   # ahora a es 15
b *= 2   # ahora b es 10

print("Nuevo valor de a:", a)
print("Nuevo valor de b:", b)

#operadores de precedencia y paréntesis controlan el orden de las operaciones
# sin paréntesis, la multiplicación se realiza antes que la suma
resultado = a + b * 2  # resultado es 35 (b*2 se evalúa primero)
print("Resultado con precedencia:", resultado)
resultado_parentesis = (a + b) * 2  # resultado es 50 (a+b se evalúa primero)
print("Resultado con paréntesis:", resultado_parentesis)

#operadores unarios
negativo = -a  # negativo es -15
positivo = +b  # positivo es 10
print("Negativo de a:", negativo)
print("Positivo de b:", positivo)


