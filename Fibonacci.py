#Parte 1
number_1 = int(input('Ingrese un valor: '))

fib_list= [1,1]
while fib_list[-1] <= number_1:
    fib_list.append(fib_list[-2] + fib_list[-1])
    print(fib_list)

#Parte 2
print(sum(fib_list))

#Parte 3
number_2 = 0
number_3 = []
for number_2 in fib_list:
    if number_2%2==1:
        number_3.append(number_2)
        print(number_3)
print(sum(number_3))

# Parte 4
numnber_4 = 0
number_5 = [2]
for number_4 in range(2,len(fib_list)):
    if number_4%2 == 1:
        number_5.append(number_4)
        print(number_5)
print(sum(number_5))