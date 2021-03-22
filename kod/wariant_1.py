import error as err
import functions as fun

def search_x(func, der, x):
    # oblicz i zwróc przybliżenie pierwiastka
    return x - (func(x)/der(x))

def search_by_iterations(func, der, x, i):
    '''
    przyjmuje:\n
    func - wskaźnik na funckcję\n
    der - wskaźnik na pochodną\n
    x   - x od którego ma zacząć szukanie\n
    i   - ilość iteracji do wykonania\n
    zwraca:\n
    x - przybliżenie x0\n
    i - ilość iteracji\n
    A - błąd w wariancie A\n
    B - błąd w wariancie B
    '''
    points = []
    points.append([x, func(x)])


    # wykonaj zadaną ilość iteracji 
    # metodą stycznych
    prev_x = 0
    for i in range(1, i+1):
        prev_x = x
        x = search_x(func, der, x)
        points.append([x, func(x)])

    A = err.error_A(func, x, prev_x)
    B = err.error_B(func, x, prev_x)

    return points, i, A, B

def search_by_error(func, der, error, x, eps):
    '''
    przyjmuje:\n
    func   - wskaźnik na funckcję\n
    der   - wskaźnik na pochodną\n
    error - wskaźnik na funckcję liczenia błędu\n
    x     - x od którego ma zacząć szukanie\n
    eps   - epsilon\n
    zwraca:\n
    x - przybliżenie x0\n
    i - ilość iteracji\n
    A - błąd w wariancie A\n
    B - błąd w wariancie B
    '''
    all_x = []
    all_x.append([x, func(x)])

    # wykonaj pierwsze 2 pętle ręcznie
    x = search_x(func, der, x)
    all_x.append([x, func(x)])
    prev_x = x
    x = search_x(func, der, x)
    all_x.append([x, func(x)])
    
    i = 2
    
    while error(func, x, prev_x) > eps:
        prev_x = x
        x = search_x(func, der, x)
        all_x.append([x, func(x)])
        i+=1

    # wykonaj obliczenia dla błędów
    A = err.error_A(func, x, prev_x)
    B = err.error_B(func, x, prev_x)

    # zwróc wszystko
    return all_x, i, A, B


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
start_x = float(input("Od jakiego x zacząć szukanie: "))

if opt == 0:
    i = int(input("Podaj ilość iteracji do wykonania: "))
    points, i, A, B = search_by_iterations(func, der, start_x, i)
elif opt == 1 or opt == 2:
    if opt == 1:
        error_text = err.error[0][0]
        error = err.error[0][1]
    if opt == 2:
        error_text = err.error[1][0]
        error = err.error[1][1]
    eps = float(input("Podaj epsilon: "))
    points, i, A, B = search_by_error(func, der, error, start_x, eps)
else:
    print("błędny błąd")
    exit()

print()
print("##################")
print("Wariant 1 - metoda stycznych")
print("funkcja: " + func_text)
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
points - wszystkie punkty znalezione po drodze do wyniku

# ze względu na brak zakresu, można go sobie tu
# pobrać albo przyjąć pierwszy i ostatni punkt jako
# zakres wykresu (ew rozszerzyć o 1 w każdą stronę):
'''
a,b = points[0][0], points[0][0]
for line in points:
    if (a>line[0]): a = line[0]
    if (b<line[0]): b = line[0]
if (a > b): a,b = b,a
a-=0.1
b+=0.1

import charts as ch
ch.create_chart(func, a, b, points, "wariant_1/" + input("nazwij plik: "))