functions.py:
    zawiera funkcję `print_fun()` która wyświetla
    dostępne funkcje, a następnie zwraca żądaną funkcję
    WRAZ Z JEJ POCHODNĄ. Przykład użycia:
    ```
    fun, dev = print_fun()
    print(fun(1)) 
    print(dev(1))
    ```

error.py:
    mała biblioteka zawierająca metody liczenia błędów. Nie ma konieczności
    z korzystania z niej. Wykorzystywana jest wyłącznie przez wariant_1.py oraz
    wariant_3.py. Działa podobnie jak functions.py. Jej funkcje "bez sensu"
    przyjmują argumenty których nie używają, co pozwala skrócić kod w plikach
    wariant_x o 1/3 (nie trzeba budować specjalnych metod gdzie jedyne co się
    różni to sposób liczenia błędu). Zalecam korzystanie z drugiej metody
    "liczenia" błędu, ponieważ wydaje się być dokładniejsza i mniej podatna
    na błędy.


wariant_1.py oraz wariant_3.py:
    - w sumie po prostu osobne programy które realizują dane warianty.
    Wcześniej działało to inaczej, ale w sumie tak jest prościej, ze
    względu na to, że wariant_1 nie wymaga od użytkownika pobrania
    zakresu szukania miejsca zerowego, więc funkcje za bardzo się
    różniły, żeby robić z tego jeden program

charts.py
    - zawiera tylko funkcję `create_chart()` do tworzenia wykresów w
    formie plików w odpowiednich folderach

######
inne notatki:
    - teraz jestem całkiem zadowolony z tego jak wygląda całość

    - co do wykresów. Trzeba by może je jakoś uładnić i tyle