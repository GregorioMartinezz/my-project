# Si múltiplo de 3 -> Fizz
# Si múltiplo de 5 -> Buzz
# Si múltiplo de 3 y 5 -> FizzBuzz

TXT_FIZZ = 'Fizz'
TXT_BUZZ = 'Buzz'
listado = []

for i in range(101):
    fizz = i % 3 == 0
    buzz = i % 5 == 0

    if fizz and buzz:
        listado.append(TXT_FIZZ + TXT_BUZZ)
    elif fizz:
        listado.append(TXT_FIZZ)
    elif buzz:
        listado.append(TXT_BUZZ)
    else:
        listado.append(i)

assert 81 not in listado, '81 no debe estar en la lista'

print(listado)
