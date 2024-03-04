"""
Program, który pozwoli użytkownikowi:
1) Dodawać nowe definicje
2) Szukać istniejących definicji
3) Usuwać wybrane przez niego definicje
4) Wyświetli dodane definicje
"""

definicje={}


while(True):
    print("1: Dodaj definicję")
    print("2: Znajdź definicję")
    print("3: Usuń definicję")
    print("4: Wyświetl definicje")
    print("5: Zakończ")

    userInput=input("Podaj co chcesz zrobić?")

    if(userInput=="1"):
        klucz=input("Podaj klucz do definicji:")
        slowo=input("Podaj definicje do dodania:")
        definicje[klucz]=slowo
        print("Definicja dodana:",slowo)
    elif(userInput=="2"):
        klucz=input("Podaj klucz do definicji")
        if klucz in definicje:
            print(definicje[klucz])
        else:
            print("Niewłaściwy klucz")
    elif(userInput=="3"):
        klucz=input("Podaj klucz do definicji do usunięcia")
        if klucz in definicje:
            del definicje[klucz]
            print("Definicja została usnięta")
        else:
            print("Nie znaleziono takiego klucza")
    elif(userInput=="4"):
        print(definicje)
    elif(userInput=="5"):
        break;
    else:
        print("Wprowadzono niewłaściwa liczbę")

























