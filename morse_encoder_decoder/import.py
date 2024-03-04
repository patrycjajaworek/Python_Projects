import function_enc_dec
morse_code = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
            'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
            'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..'}

def main():

    try:

        tekst=str(input("podaj tekst do zakodowania:"))
        obiekt=function_enc_dec.Codec(morse_code)
        wynik=obiekt.kodowanie(tekst)
        print(wynik)
        print(obiekt.odkodowanie(wynik))
    except ValueError as error:
        print(error)
    finally:
        print("Koniec programu")

if __name__ == "__main__":
    main()
