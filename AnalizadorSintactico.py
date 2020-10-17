#Cristian Adolfo Baquero Pico

import sys

class Token:
    def __init__(self, tipo, lexema, fila, columna):
        self.tipo = tipo
        self.lexema = lexema
        self.fila = fila
        self.columna = columna

    def __str__(self) -> str:
        if self.lexema in palabrasReservadas:
            return "<" + str(self.lexema) + "," + str(self.fila) + "," + str(self.columna) + ">"
        else:
            if self.tipo == "id":
                return "<" + str(self.tipo) + "," + str(self.lexema) + "," + str(self.fila) + "," + str(
                    self.columna) + ">"
            elif self.tipo == "tk_num" or self.tipo == "fid":
                return "<" + str(self.tipo) + "," + str(self.lexema) + "," + str(self.fila) + "," + str(
                    self.columna) + ">"
            else:
                return "<" + str(self.tipo) + "," + str(self.fila) + "," + str(self.columna) + ">"


palabrasReservadas = ("and", "bool", "break", "do", "else", "end", "false",
                      "for", "function", "if", "input", "loop", "next", "num",
                      "or", "print", "repeat", "return", "true", "unless",
                      "until", "var", "when", "while", "not")


def delta(est, c):
    # est = estado; c = caracter

    if est == 0:
        if c == ">":
            return (1, 0, None)
        elif c == "<":
            return (2, 0, None)
        elif c == "+":
            return (3, 0, None)
        elif c == "-":
            return (4, 0, None)
        elif c == "*":
            return (5, 0, None)
        elif c == "/":
            return (6, 0, None)
        elif c == "%":
            return (7, 0, None)
        elif c == ":":
            return (8, 0, None)
        elif c == "=":
            return (9, 0, None)
        elif c == "!":
            return (10, 0, None)
        elif c == "{":
            return (0, 0, "tk_llave_izq")
        elif c == "}":
            return (0, 0, "tk_llave_der")
        elif c == "(":
            return (0, 0, "tk_par_izq")
        elif c == ")":
            return (0, 0, "tk_par_der")
        elif c == ",":
            return (0, 0, "tk_coma")
        elif c == ";":
            return (0, 0, "tk_puntoycoma")
        elif c.isalpha() or c == "_":
            return (11, 0, None)
        elif c == "@":
            return (13, 0, None)
        elif c.isdigit():
            return (15, 0, None)
        elif c == "#":
            return (18, 0, None)
        elif c == " ":
            return (0, 0, "espacio")
        elif c == "\n":
            return (0, 0, "saltoLinea")
        elif c == "\t":
            return (0, 0, "tabulacion")
        elif c == "\r":
            return (0, 0, "retorno")
        else:
            return (0, 0, "Error léxico")

    elif est == 1:
        if c == "=":
            return (0, 0, "tk_mayor_igual")
        else:
            return (0, 1, "tk_mayor")
    elif est == 2:
        if c == "=":
            return (0, 0, "tk_menor_igual")
        else:
            return (0, 1, "tk_menor")
    elif est == 3:
        if c == "=":
            return (0, 0, "tk_sum_asig")
        elif c == "+":
            return (0, 0, "tk_incremento")
        else:
            return (0, 1, "tk_mas")
    elif est == 4:
        if c == "=":
            return (0, 0, "tk_res_asig")
        elif c == "-":
            return (0, 0, "tk_decremento")
        else:
            return (0, 1, "tk_menos")
    elif est == 5:
        if c == "=":
            return (0, 0, "tk_mul_asig")
        else:
            return (0, 1, "tk_mul")
    elif est == 6:
        if c == "=":
            return (0, 0, "tk_div_asig")
        else:
            return (0, 1, "tk_div")
    elif est == 7:
        if c == "=":
            return (0, 0, "tk_mod_asig")
        else:
            return (0, 1, "tk_mod")
    elif est == 8:
        if c == "=":
            return (0, 0, "tk_asignacion")
        else:
            return (0, 1, "tk_dospuntos")
    elif est == 9:
        if c == "=":
            return (0, 0, "tk_igualdad")
        else:
            return (0, 1, "Error léxico")
    elif est == 10:
        if c == "=":
            return (0, 0, "tk_diferente")
        else:
            return (0, 1, "Error léxico")
    elif est == 11:
        if c.isalpha() or c == "_":
            return (11, 0, None)
        elif c.isdigit():
            return (12, 0, None)
        else:
            return (0, 1, "REVISAR")
    elif est == 12:
        if c.isalnum() or c == "_":
            return (12, 0, None)
        else:
            return (0, 1, "id")
    elif est == 13:
        if c.isalpha() or c == "_":
            return (14, 0, None)
        else:
            return (0, 1, "Error léxico")
    elif est == 14:
        if c.isalnum() or c == "_":
            return (14, 0, None)
        else:
            return (0, 1, "fid")
    elif est == 15:
        if c.isdigit():
            return (15, 0, None)
        elif c == ".":
            return (16, 0, None)
        else:
            return (0, 1, "tk_num")
    elif est == 16:
        if c.isdigit():
            return (17, 0, None)
        else:
            return (0, 2, "tk_num")
    elif est == 17:
        if c.isdigit():
            return (17, 0, None)
        else:
            return (0, 1, "tk_num")
    elif est == 18:
        if c == "\n":
            return (0, 0, "comentario")
        else:
            return (18, 0, None)
    else:
        print("errorEnEstados")


def definirToken(devolver, tipoToken, devueltos, fila, columna, buffer):
    if devolver > 0:
        endLoc = len(buffer)
        startLoc = endLoc - devolver
        devueltos += buffer[startLoc: endLoc]
        nuevoBuffer = buffer[0: startLoc]
        columna -= devolver
    else:
        nuevoBuffer = buffer

    buffer = ""
    if tipoToken == "saltoLinea" or tipoToken == "comentario":
        fila += 1
        columna = 1
    elif tipoToken == "espacio" or tipoToken == "retorno":
        pass  # ya había sumado 1 antes en la columna
    elif tipoToken == "tabulacion":
        columna += 3  # ya había sumado 1 antes
    else:
        if nuevoBuffer in palabrasReservadas:
            token = Token(nuevoBuffer, nuevoBuffer, fila, (columna - len(nuevoBuffer)))
            print(token)
        else:
            if tipoToken == "REVISAR":
                token = Token("id", nuevoBuffer, fila, (columna - len(nuevoBuffer)))
                print(token)
            elif tipoToken == "tk_num" or tipoToken == "fid":
                token = Token(tipoToken, nuevoBuffer, fila, (columna - len(nuevoBuffer)))
                print(token)
            else:
                token = Token(tipoToken, nuevoBuffer, fila, (columna - len(nuevoBuffer)))
                print(token)

    return devueltos, fila, columna, buffer

def analizarLexico(codigo):
    codigo += " "  # para que detecte el último lexema del código
    fila = 1
    columna = 1
    estadoAux = 0
    buffer = ""
    devueltos = ""
    bucleInterno = True

    for caracter in codigo:

        if not bucleInterno:
            break

        buffer += caracter
        columna += 1
        estadoAux, devolver, tipoToken = delta(estadoAux, caracter)

        if tipoToken is not None:

            if tipoToken == "Error léxico":
                print(">>> Error léxico(línea:" + str(fila) + ",posición:" + str(columna - 1 - devolver) + ")")
                break

            devueltos, fila, columna, buffer = definirToken(devolver, tipoToken, devueltos, fila, columna, buffer)

            for caracterDev in devueltos:
                buffer += caracterDev
                columna += 1
                estadoAux, devolver, tipoToken = delta(estadoAux, caracterDev)

                if tipoToken is not None:

                    if tipoToken == "Error léxico":
                        print(">>> Error léxico(línea:" + str(fila) + ",posición:" + str(columna - 1 - devolver) + ")")
                        bucleInterno = False
                        break

                    devueltos, fila, columna, buffer = definirToken(devolver, tipoToken, devueltos, fila, columna, buffer)

            devueltos = ""


cod1 = '''var z:num;
z := 0;
while (z < 10)
  {
  z := z + 1;
  print z;
  }
end
# salida: 1 2 3 4 5 6 7 8 9 10'''

cod2 = '''## función min(x, y)
function @min:num (x:num, y:num)
  {
  when ((x < y) == true) do return x;
  return y;
  }

## función max(x, y)
function @max:num (x:num, y:num)
  {
  if ((x < y) == false) do
    {
    return x;
    }
  else
    {
    return y;
    }
  }

print @min(1,2);
print @max(1,2);
a := 10;
a %= 2;
end'''

cod3 = "2.5598055while3!=88¬56.a"

cod4 = "_print"

analizarLexico(cod4)

# lineasSeparadas = sys.stdin.readlines()
# lineas = ""
# for linea in lineasSeparadas:
#     lineas += linea
#
# analizarLexico(lineas)