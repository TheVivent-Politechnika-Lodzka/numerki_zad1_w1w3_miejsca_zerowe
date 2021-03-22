# obliczanie błędu w wariancie A
def error_A(fun, xi, xi_m1):
    return (abs(xi-xi_m1))

# obliczanie błędu w wariancie B
def error_B(fun, xi, xi_m1):
    return abs(fun(xi))

error = [
    ["|xi−xi−1|<ε", error_A, "błąd A"],
    ["|f(xi)|<ε", error_B, "błąd B"]
]

# wyświetla możliwe "błędy"
# zwraca wybrany
def print_error():
    for i in range(len(error)):
        print(str(i) + ". " + error[i][0])
    i = int(input("Wybierz błąd: "))
    return error[i][1], error[i][2]
