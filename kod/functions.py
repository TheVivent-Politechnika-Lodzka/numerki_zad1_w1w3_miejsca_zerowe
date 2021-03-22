from numpy import sin, cos, tan, exp, arctan

def cot(x):
    return 1/tan(x)

def csc(x):
    return 1/sin(x)

#####
def f0(x):

    # policzenie schematem hornera
    # 3*x^5 - 5*x^4 + 1.2*x^3 + 5x^2 + 10x - 1
    coefficients = [3, -5, 1.2, 5, 10, -1]
    result = coefficients[0]
    for i in range(1, 6):
        result = result*x + coefficients[i]

    return result

def d0(x):

    # policzenie schematem hornera
    coefficients = [15, -20, 3.6, 10, 10]
    result = coefficients[0]
    for i in range(1,5):
        result = result*x + coefficients[i]
        
    return result
#####

#---#       sin(5x) + ctg(x) - 10x -15x^2
def f1(x):
    result = sin(5*x) + cot(x) - 10*x - 15*x*x
    return result

def d1(x):
    cscx = csc(x)
    result = - 10 - 30*x + 5*cos(5*x) - cscx*cscx
    return result
#---#       -10 - 30 x + 5 cos(5 x) - csc^2(x)

#####
def f2(x):
    result = cos(exp(-0.001*x*x)) - 0.6
    return result

def d2(x):
    strange_e = exp(-0.001*x*x) 
    result = 0.002 * strange_e * x * sin (strange_e)
    return result
#####

#---#   sin(5x) + exp(ctg(x))
def f3(x):
    result = sin(5*x) + exp(cot(x))
    return result

def d3(x):
    cscx = csc(x)
    result = 5*cos(5*x) - exp(cot(x))*cscx*cscx
    return result
#---#   5 cos(5 x) - exp(cot(x)) csc^2(x)

#####
def f4(x):
    result = arctan(20*sin(x))-0.4
    return result

def d4(x):
    sinx = sin(x)
    result = (20*cos(x)) / (1+400*sinx*sinx)
    return result
#####   12 x^3 + cos(x) - 2.6 csc^2(0.2 x) + 5 sin(5 x)


'''
1. Funkcja którą można obliczyć hornerem                - gotowe
2. funkcja trygonometryczna                             - gotowe
3. funkcja złożona                                      - gotowe
4. funkcja gdzie pierwsza pochodna nie ma stałego znaku - gotowe
5. funkcja gdzie druga pochodna nie ma stałego znaku    - gotowe
6. funkcja gdzie obie pochodne nie mają stałego znaku   - gotowe
'''

functions = [
    # 0:
    ["3*x^5 - 5*x^4 + 1.2*x^3 + 5x^2 + 10x - 1", f0, d0],
    # x0 = 0.1
    # pierwsza pochodna:    ```10 + 10x + 3.6 x^2 - 20 x^3 + 15 x^4```
    #   (-∞, ∞)             - funkcja ma stały znak (+)
    #   (-∞, ∞)             - funkcja jest ciągła
    # druga pochodna:
    #   (-0.313, ∞)         - funkcja ma stały znak (+)
    #   (-∞, -0.313)        - funkcja ma stały znak (-)
    #   (-∞, ∞)             - funcja jest ciągła
    
    # 1:
    ["sin(5x) + ctg(x) - 10x -15x^2", f1, d1],
    # x0 = 0.296
    # pierwsza pochodna:    ```-10 - 30 x + 5 cos(5 x) - csc^2(x)```
    #   (0, ∞)              - funkcja ma stały znak (-)
    #   (0, 3)              - funkcja jest ciągła
    # druga pochodna:
    #   (0.331, 3.646)      - funkcja ma stały znak (-)
    #   (0, 2.7>            - funkcja jest ciągła

    # 2:
    ["cos(exp(-0.001*x^2)) - 0.6", f2, d2],
    # x0 = -8.688, 8.688
    # pierwsza pochodna:    ```0.002 e^(-0.001 x^2) x sin(e^(-0.001 x^2))```
    #   (-∞, ∞)/{0}         - funkcja ma stały znak
    #   (-∞, ∞)             - funkcja jest ciągła
    # druga pochodna:
    #   (-16.662, 16.662)   - ma stały znak (+)
    #   (reszta)            - ma stały znak (-)
    #   (-∞, ∞)             - jest ciągła

    # 3:
    ["sin(5x) + exp(ctg(x))", f3, d3],
    # nie sprawdzona
    # x0 = -pi/2, -1.4927, -0.5839, 0
    # okresowo występują x0
    # szukać <1.53, 2.2>
    # pierwsza pochodna:    ```5 cos(5 x) - exp(cot(x)) csc^2(x)```

    # 4:
    ["arctan(20sin(x))-0.4", f4, d4]
    # nie sprawdzona
    # pierwsza pochodna:    ```(20cos(x)) / (1 + 400sin^2(x))``` 
    # x0 = to skomplikowane
]

def print_fun():
    for i in range(len(functions)):
        print(str(i) + ". " + functions[i][0])
    i = int(input("Wybierz funkcję: "))
    return functions[i][1], functions[i][2], functions[i][0]