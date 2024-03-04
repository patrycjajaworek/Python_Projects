class Codec:
    def __init__(self,morse_code):
        self.morse_code = morse_code
        self.reverse = {value: key for (key, value) in morse_code.items()}
    def kodowanie(self,tekst):
        if tekst=="":
            raise ValueError("Brak tekstu")
        wynik = []
        i = ''
        for litera in tekst:
            if litera not in self.morse_code:
                raise ValueError("Brak takiego znaku ")
            elif litera != '':
                i = i + self.morse_code[litera] + ' '
                wynik.append(self.morse_code[litera])
            else:
                i = i + ''
        return wynik

    def odkodowanie(self,wynik):
        dane=[]
        n=""
        for znak in wynik:
            if znak not in self.reverse:
                raise ValueError("Brak takiego znaku")
            elif znak != '':
                n = n + self.reverse[znak] + ' '
                dane.append(self.reverse[znak])
            else:
                n = n + ''
        return dane






