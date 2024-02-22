import math

#funkcje do liczenia pola figur
def pole_kwadratu(a):
    return a*a

def pole_prostokata(a,b):
    return a*b

def pole_trojkata(a,h):
    return 1/2*a*h

def pole_trapezu(a,b,h):
    return ((a+b)*h)/2

def pole_kola(r):
    return math.pi*r**2


print("1: Kwadrat")
print("2: Prostokąt")
print("3: Trójkąt")
print("4: Trapez")
print("5: Koło")



while(True):
    userInput = input("Podaj co chcesz zrobić?")
    if(userInput=="1"):
        a=input("Podaj długość boku:")
        pole=pole_kwadratu(int(a))
        print("Pole kwadratu:",pole)
    elif(userInput=="2"):
        a = input("Podaj długość boku 1:")
        b = input("Podaj długość boku 2:")
        pole = pole_prostokata(int(a),int(b))
        print("Pole prostokąta:", pole)
    elif (userInput == "3"):
        a = input("Podaj długość boku :")
        h = input("Podaj wysokość:")
        pole = pole_trojkata(int(a),int(h))
        print("Pole trójkąta:", pole)
    elif (userInput == "4"):
        a = input("Podaj długość boku 1:")
        b = input("Podaj długość boku 2:")
        h = input("Podaj wysokość:")
        pole = pole_trapezu(int(a),int(b),int(h))
        print("Pole trapezu:", pole)
    elif (userInput == "5"):
        r = input("Podaj długość promienia:")
        pole = pole_kola(int(r))
        print("Pole koła:", pole)
    elif(userInput=="e"):
        break;
    else:
        print("Wprowadzono złą liczbę")