class Token:
    def __init__(self,tipo, lexema, fila, columna):
        self.tipo = tipo
        self.lexema = lexema
        self.fila = fila
        self.columna = columna

palabrasReservadas = ("and", "bool", "break", "do", "else", "end", "false",
                      "for", "function", "if", "input", "loop", "next", "num",
                      "or", "print", "repeat", "return", "true", "unless",
                      "until", "var", "when", "while")

cod = '''
var z:num;
z := 0;
while (z < 10)
  {
  z := z + 1;
  print z;
  }
end

'''

def delta(est, c):
    #est = estado; c = caracter
    if est == 0:
        pass
    elif est == 1:
        pass
    elif est == 2:
        return -1
    elif est == 3:
        return -1
    elif est == 4:
        pass
    elif est == 5:
        return -1
    elif est == 6:
        return -1
    elif est == 7:
        pass
    elif est == 8:
        return -1
    elif est == 9:
        return -1
    elif est == 10:
        return -1
    elif est == 11:
        pass
    elif est == 12:
        return -1
    elif est == 13:
        return -1
    elif est == 14:
        return -1
    elif est == 15:
        pass
    elif est == 16:
        return -1
    elif est == 17:
        return -1
    elif est == 18:
        pass
    elif est == 19:
        return -1
    elif est == 20:
        return -1
    elif est == 21:
        pass
    elif est == 22:
        return -1
    elif est == 23:
        return -1
    elif est == 24:
        pass
    elif est == 25:
        return -1
    elif est == 26:
        return -1
    elif est == 27:
        pass
    elif est == 28:
        return -1
    elif est == 29:
        pass
    elif est == 30:
        pass
    elif est == 31:
        return -1
    elif est == 32:
        return -1
    elif est == 33:
        return -1
    elif est == 34:
        return -1
    elif est == 35:
        return -1
    elif est == 36:
        return -1
    elif est == 37:
        return -1
    elif est == 38:
        pass
    elif est == 39:
        return -1
    elif est == 40:
        pass
    elif est == 41:
        return -1
    elif est == 42:
        pass
    elif est == 43:
        pass
    elif est == 44:
        return -1
    elif est == 45:
        pass
    elif est == 46:
        pass
    elif est == 47:
        return -1
    elif est == 48:
        return -1
    elif est == 49:
        pass
    elif est == 50:
        return -1
    elif est == 51:
        pass
    elif est == 52:
        pass
    elif est == 53:
        pass
    elif est == 54:
        pass
    elif est == 55:
        return -1
    else:
        print("error")




def analizarLexico(codigo):
    linea=0
    estadoAux=0
    for caracter in codigo:
        estadoAux = delta(estadoAux,caracter)

analizarLexico(cod)
