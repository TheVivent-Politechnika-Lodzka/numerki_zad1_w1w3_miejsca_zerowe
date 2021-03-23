import error as err
import functions as fun

def search_x(func, a, b):
    # policz przybliżenie pierwiastka w przedziale
    x1 = a - (func(a) / (func(b) - func(a))) * (b - a)

    # jeżeli f(x1)f(a) < 0,
    # to następny przedział to [a, x1]
    if (func(a)*func(x1) < 0):
        b = x1
    # jeżeli f(x1)f(a) > 0,
    # to następny przedział to [x1, b]
    if (func(a)*func(x1) > 0):
        a = x1

    # zwróć przybliżenie i następny przedział
    return x1, a, b

def search_by_iterations(func, a, b, i):
    '''
    przyjmuje:\n
    func - wskaźnik na funckcję\n
    a   - lewy kraniec przedziału\n
    b   - prawy kraniec przedziału\n
    i   - ilość iteracji\n
    zwraca:\n
    x - przybliżenie x0\n
    i - ilość iteracji\n
    A - błąd w wariancie A\n
    B - błąd w wariancie B
    '''
    points = []

    if (a > b): a,b = b,a

    # wykonaj zadaną ilość iteracji 
    # regułą falsi
    prev_x = 0
    x = 0
    for i in range(1, i+1):
        prev_x = x
        x,a,b = search_x(func, a, b)
        points.append([x, func(x)])

    A = err.error_A(func, x, prev_x)
    B = err.error_B(func, x, prev_x)

    return points, i, A, B

def search_by_error(func, error, eps, a, b):
    '''
    przyjmuje:\n
    func   - wskaźnik na funckcję\n
    error - wskaźnik na funckcję błędu\n
    eps   - założony błąd\n
    a     - lewy kraniec przedziału\n
    b     - prawy kraniec przedziału\n
    zwraca:\n
    x - przybliżenie x0\n
    i - ilość iteracji\n
    A - błąd w wariancie A\n
    B - błąd w wariancie B
    '''
    points = []

    # jeżeli user podał przedział odwrotnie, to zamień
    if (a > b): a,b = b,a


    # wykonaj pierwsze 2 pętle ręcznie
    x,a,b = search_x(func, a, b)
    points.append([x, func(x)])
    prev_x = x
    x,a,b = search_x(func, a, b)
    points.append([x, func(x)])
    
    i = 2
    
    while error(func, x, prev_x) > eps:
        prev_x = x
        x,a,b = search_x(func, a, b)
        points.append([x, func(x)])
        i+=1

    # wykonaj obliczenia dla błędów
    A = err.error_A(func, x, prev_x)
    B = err.error_B(func, x, prev_x)

    # zwróc wszystko
    return points, i, A, B




################################
'''GUI'''
################################

func, der, func_text = fun.print_fun()
i, eps, A, B = 0, 0, 0, 0
error_text = ""

print()
print("0. Iteracyjnie")
print("1. przez błąd A (" + err.error[0][0] + ")")
print("2. przez błąd B (" + err.error[1][0] + ")")
opt = int(input("Wybierz tryb szukania pierwiastka: "))
print()
a = float(input("Podaj lewy koniec przedziału szukania: "))
b = float(input("Podaj prawy koniec przedziału szukania: "))

if (func(a)*func(b)>=0):
    print("Założenie o przeciwnych znakach na krańcach przedziału nie jest spełnione!!!")
    exit()

if opt == 0:
    i = int(input("Podaj ilość iteracji do wykonania: "))
    points, i, A, B = search_by_iterations(func, a, b, i)
elif opt == 1 or opt == 2:
    if opt == 1:
        error_text = err.error[0][0]
        error = err.error[0][1]
    if opt == 2:
        error_text = err.error[1][0]
        error = err.error[1][1]
    eps = float(input("Podaj epsilon: "))
    points, i, A, B = search_by_error(func, error, eps, a, b)
else:
    print("błędny błąd")
    exit()


print()
print("##################")
print("Wariant 3 - reguła falsi")
print("funkcja: " + func_text)
print("Zakres: " + str(a) + " - " + str(b))
print("Otatni punkt: f(" + str(points[len(points)-1][0]) + ") = " + str(points[len(points)-1][1]))
print("Błąd wariantu A [" + err.error[0][0] + "]: " + str(A))
print("Błąd wariantu B [" + err.error[1][0] + "]: " + str(B))
print("ilość iteracji: " + str(i))
print("warunek stopu: ", end="")
if opt == 0: print("ilość iteracji")
if opt == 1: print("błąd wariantu A (Epsilon: " + str(eps) + ")")
if opt == 2: print("błąd wariantu B (Epsilon: " + str(eps) + ")")
print("Wszystkie punkty:")
print(" x | f(x)")
for line in points:
    print(str(line[0]) + " | " + str(line[1]))


#####
'''
Dostępne tutaj zmienne przydatne przy rysowaniu wykresu:
func   - wskaźnik na funkcję
a,b    - zakres szukania
points - wszystkie punkty znalezione po drodze do wyniku
'''

import charts as ch
ch.create_chart(func, a, b, points, "wariant_3/" + input("nazwij plik: "))