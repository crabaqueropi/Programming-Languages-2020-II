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
                return "<" + str(self.tipo) + "," + str(self.lexema) + "," + str(self.fila) + "," + str(self.columna) + ">"
            elif self.tipo == "tk_num" or self.tipo == "fid":
                return "<" + str(self.tipo) + "," + str(self.lexema) + "," + str(self.fila) + "," + str(self.columna) + ">"
            else:
                return "<" + str(self.tipo) + "," + str(self.fila) + "," + str(self.columna) + ">"


palabrasReservadas = ("and", "bool", "break", "do", "else", "end", "false",
                      "for", "function", "if", "input", "loop", "next", "num",
                      "or", "print", "repeat", "return", "true", "unless",
                      "until", "var", "when", "while")

cod = '''var z:num;
z := 0;
while (z < 10)
  {
  z := z + 1;
  print z;
  }
end
# salida: 1 2 3 4 5 6 7 8 9 10'''

cod2 ='''## función min(x, y)
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

cod3 = '''2.5598055while3!=88¬56.a'''


def delta(est, c):
    # est = estado; c = caracter

    if est == 0:
        if c == ">":
            return (1, 0, None)
        elif c == "<":
            return (4, 0, None)
        elif c == "<":
            return (4, 0, None)
        elif c == "+":
            return (7, 0, None)
        elif c == "-":
            return (11, 0, None)
        elif c == "*":
            return (15, 0, None)
        elif c == "/":
            return (18, 0, None)
        elif c == "%":
            return (21, 0, None)
        elif c == ":":
            return (24, 0, None)
        elif c == "=":
            return (27, 0, None)
        elif c == "!":
            return (30, 0, None)
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
        elif c.isalpha():
            return (38, 0, None)
        elif c == "@":
            return (42, 0, None)
        elif c.isdigit():
            return (45, 0, None)
        elif c == "#":
            return (51, 0, None)
        elif c == " ":
            return (0, 0, "espacio")
        elif c == "\n":
            return (0, 0, "saltoLinea")
        else:
            return (29, 0, "Error léxico")

    elif est == 1:
        if c == "=":
            return (0, 0, "tk_mayor_igual")
        else:
            return (0, 1, "tk_mayor")
    # elif est == 2:
    #     return -1
    # elif est == 3:
    #     return -1
    elif est == 4:
        if c == "=":
            return (0, 0, "tk_menor_igual")
        else:
            return (0, 1, "tk_menor")
    # elif est == 5:
    #     return -1
    # elif est == 6:
    #     return -1
    elif est == 7:
        if c == "=":
            return (0, 0, "tk_sum_asig")
        elif c == "+":
            return (0, 0, "tk_incremento")
        else:
            return (0, 1, "tk_mas")
    # elif est == 8:
    #     return -1
    # elif est == 9:
    #     return -1
    # elif est == 10:
    #     return -1
    elif est == 11:
        if c == "=":
            return (0, 0, "tk_res_asig")
        elif c == "+":
            return (0, 0, "tk_decremento")
        else:
            return (0, 1, "tk_menos")
    # elif est == 12:
    #     return -1
    # elif est == 13:
    #     return -1
    # elif est == 14:
    #     return -1
    elif est == 15:
        if c == "=":
            return (0, 0, "tk_mul_asig")
        else:
            return (0, 1, "tk_mul")
    # elif est == 16:
    #     return -1
    # elif est == 17:
    #     return -1
    elif est == 18:
        if c == "=":
            return (0, 0, "tk_div_asig")
        else:
            return (0, 1, "tk_div")
    # elif est == 19:
    #     return -1
    # elif est == 20:
    #     return -1
    elif est == 21:
        if c == "=":
            return (0, 0, "tk_mod_asig")
        else:
            return (0, 1, "tk_mod")
    # elif est == 22:
    #     return -1
    # elif est == 23:
    #     return -1
    elif est == 24:
        if c == "=":
            return (0, 0, "tk_asignacion")
        else:
            return (0, 1, "tk_dospuntos")
    # elif est == 25:
    #     return -1
    # elif est == 26:
    #     return -1
    elif est == 27:
        if c == "=":
            return (0, 0, "tk_igualdad")
        else:
            return (29, 0, "Error léxico")
    # elif est == 28:
    #     return -1
    # elif est == 29:
    #     pass
    elif est == 30:
        if c == "=":
            return (0, 0, "tk_diferente")
        else:
            return (29, 0, "Error léxico")
    # elif est == 31:
    #     return -1
    # elif est == 32:
    #     return -1
    # elif est == 33:
    #     return -1
    # elif est == 34:
    #     return -1
    # elif est == 35:
    #     return -1
    # elif est == 36:
    #     return -1
    # elif est == 37:
    #     return -1
    elif est == 38:
        if c.isalpha():
            return (38, 0, None)
        elif c.isdigit():
            return (40, 0, None)
        else:
            return (0, 1, "REVISAR")
    # elif est == 39:
    #     return -1
    elif est == 40:
        if c.isalnum():
            return (40, 0, None)
        else:
            return (0, 1, "id")
    # elif est == 41:
    #     return -1
    elif est == 42:
        if c.isalpha():
            return (43, 0, None)
        else:
            return (0, 0, "Error léxico")
    elif est == 43:
        if c.isalnum():
            return (43, 0, None)
        else:
            return (0, 1, "fid")
    # elif est == 44:
    #     return -1
    elif est == 45:
        if c.isdigit():
            return (45, 0, None)
        elif c == ".":
            return (46, 0, None)
        else:
            return (0, 1, "tk_num")
    elif est == 46:
        if c.isdigit():
            return (49, 0, None)
        else:
            return (0, 2, "tk_num")
    # elif est == 47:
    #     return -1
    # elif est == 48:
    #     return -1
    elif est == 49:
        if c.isdigit():
            return (49, 0, None)
        else:
            return (0, 1, "tk_num")
    # elif est == 50:
    #     return -1
    elif est == 51:
        if c == "\n":
            return (0, 0, "comentario")
        else:
            return (51, 0, None)
    # elif est == 52:
    #     pass
    # elif est == 53:
    #     if c == " ":
    #         return (53, 0, None)
    #     else:
    #         return (0, 1, "espacios")
    # elif est == 54:
    #     pass
    # elif est == 55:
    #     return -1
    else:
        print("errorEnEstados")


def analizarLexico(codigo):
    codigo += " "
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
                print("Error léxico(línea:" + str(fila) + ",posición:" + str(columna-1) + ")")
                break

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
            elif tipoToken == "espacio":
                pass
            else:
                if nuevoBuffer in palabrasReservadas:
                    token = Token(nuevoBuffer, nuevoBuffer, fila, (columna - len(nuevoBuffer)))
                    # print(nuevoBuffer, fila, (columna - len(nuevoBuffer)))
                    print(token)
                else:
                    if tipoToken == "REVISAR":
                        #print("id", nuevoBuffer, fila, (columna - len(nuevoBuffer)))
                        token = Token("id", nuevoBuffer, fila, (columna - len(nuevoBuffer)))
                        print(token)
                    elif tipoToken == "tk_num" or tipoToken == "fid":
                        #print(tipoToken, nuevoBuffer, fila, (columna - len(nuevoBuffer)))
                        token = Token(tipoToken, nuevoBuffer, fila, (columna - len(nuevoBuffer)))
                        print(token)
                    else:
                        #print(tipoToken, fila, (columna - len(nuevoBuffer)))
                        token = Token(tipoToken, nuevoBuffer, fila, (columna - len(nuevoBuffer)))
                        print(token)

            for caracterDev in devueltos:
                buffer += caracterDev
                columna += 1
                estadoAux, devolver, tipoToken = delta(estadoAux, caracter)

                if tipoToken is not None:

                    if tipoToken == "Error léxico":
                        print("Error léxico(línea:" + str(fila) + ",posición:" + str(columna-1) + ")")
                        bucleInterno = False
                        break

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
                    elif tipoToken == "espacio":
                        pass
                    else:
                        if nuevoBuffer in palabrasReservadas:
                            token = Token(nuevoBuffer, nuevoBuffer, fila, (columna - len(nuevoBuffer)))
                            # print(nuevoBuffer, fila, (columna - len(nuevoBuffer)))
                            print(token)
                        else:
                            if tipoToken == "REVISAR":
                                # print("id", nuevoBuffer, fila, (columna - len(nuevoBuffer)))
                                token = Token("id", nuevoBuffer, fila, (columna - len(nuevoBuffer)))
                                print(token)
                            elif tipoToken == "tk_num" or tipoToken == "fid":
                                # print(tipoToken, nuevoBuffer, fila, (columna - len(nuevoBuffer)))
                                token = Token(tipoToken, nuevoBuffer, fila, (columna - len(nuevoBuffer)))
                                print(token)
                            else:
                                # print(tipoToken, fila, (columna - len(nuevoBuffer)))
                                token = Token(tipoToken, nuevoBuffer, fila, (columna - len(nuevoBuffer)))
                                print(token)
            devueltos = ""


analizarLexico(cod3)
# mensaje9 = "Hola Mundo"
# endLoc = len(mensaje9)
# startLoc = endLoc - 2
# mensaje9b = mensaje9[startLoc: endLoc]
# mensaje9c = mensaje9[0: startLoc]
# print(mensaje9b)
# print(mensaje9c)
