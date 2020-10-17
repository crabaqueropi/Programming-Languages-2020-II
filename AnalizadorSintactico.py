# Cristian Adolfo Baquero Pico

import sys

flagSintaxis = False
finArchivo = False

recursive_calls = []
tokens = []
indexToken = 0
tokenActual = None


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

diccionarioTokens = {
    "tk_mayor": ">",
    "tk_mayor_igual": ">=",
    "tk_menor": "<",
    "tk_menor_igual": "<=",
    "tk_sum_asig": "+=",
    "tk_mas": "+",
    "tk_incremento": "++",
    "tk_res_asig": "-=",
    "tk_menos": "-",
    "tk_decremento": "--",
    "tk_mul_asig": "*=",
    "tk_mul": "*",
    "tk_div_asig": "/=",
    "tk_div": "/",
    "tk_mod_asig": "%=",
    "tk_mod": "%",
    "tk_dospuntos": ":",
    "tk_asignacion": ":=",
    "tk_igualdad": "==",
    "tk_diferente": "!=",
    "tk_llave_izq": "{",
    "tk_llave_der": "}",
    "tk_par_izq": "(",
    "tk_par_der": ")",
    "tk_coma": ",",
    "tk_puntoycoma": ";"
}

noTerminales = ["prog", "var_decl", "var_decl_mas", "tipoDato", "fn_decl_list", "var_locales",
                "stmt_block", "stm_mas", "stmt", "stmt_do_next", "stmt_while", "stmt_until",
                "stmt_id_next", "lexpr", "nexpr_mas", "nexpr_mas_and", "nexpr_mas_or", "nexpr",
                "rexpr", "rexpr_mas", "simple_expr", "simple_expr_mas", "term", "term_mas", "factor",
                "factor_mas", "incr_decr", "argu", "argu_mas", "main_prog"]

gramatica = {
    "prog": [["fn_decl_list", "main_prog"]],
    "var_decl": [["id", "tk_dospuntos", "tipoDato", "var_decl_mas"]],
    "var_decl_mas": [["tk_coma", "id", "tk_dospuntos", "tipoDato", "var_decl_mas"],
                     [""]],
    "tipoDato": [["bool"],
                 ["num"]],
    "fn_decl_list": [
        ["function", "fid", "tk_dospuntos", "tipoDato", "tk_par_izq", "var_decl", "tk_par_der", "var_locales",
         "stmt_block", "fn_decl_list"],
        [""]],
    "var_locales": [["var", "var_decl", "tk_puntoycoma"],
                    [""]],
    "stmt_block": [["tk_llave_izq", "stm_mas", "tk_llave_der"],
                   ["stmt"]],
    "stm_mas": [["stmt", "stm_mas"],
                [""]],
    "stmt": [["print", "lexpr", "tk_puntoycoma"],
             ["input", "id", "tk_puntoycoma"],
             ["when", "tk_par_izq", "lexpr", "tk_par_der", "do", "stmt_block"],
             ["if", "tk_par_izq", "lexpr", "tk_par_der", "do", "stmt_block", "else", "stmt_block"],
             ["unless", "tk_par_izq", "lexpr", "tk_par_der", "do", "stmt_block"],
             ["stmt_while", "do", "stmt_block"],
             ["return", "lexpr", "tk_puntoycoma"],
             ["stmt_until", "do", "stmt_block"],
             ["loop", "stmt_block"],
             ["do", "stmt_block", "stmt_do_next"],
             ["repeat", "tk_num", "tk_dospuntos", "stmt_block"],
             ["for", "tk_par_izq", "lexpr", "tk_puntoycoma", "lexpr", "tk_puntoycoma", "lexpr", "tk_par_der", "do",
              "stmt_block"],
             ["next", "tk_puntoycoma"],
             ["break", "tk_puntoycoma"],
             ["id", "stmt_id_next"],
             ["tk_decremento", "id", "tk_puntoycoma"],
             ["tk_incremento", "id", "tk_puntoycoma"]],
    "stmt_do_next": [["stmt_while"],
                     ["stmt_until"]],
    "stmt_while": [["while", "tk_par_izq", "lexpr", "tk_par_der"]],
    "stmt_until": [["until", "tk_par_izq", "lexpr", "tk_par_der"]],
    "stmt_id_next": [["tk_asignacion", "lexpr", "tk_puntoycoma"],
                     ["tk_sum_asig", "lexpr", "tk_puntoycoma"],
                     ["tk_res_asig", "lexpr", "tk_puntoycoma"],
                     ["tk_mul_asig", "lexpr", "tk_puntoycoma"],
                     ["tk_div_asig", "lexpr", "tk_puntoycoma"],
                     ["tk_mod_asig", "lexpr", "tk_puntoycoma"],
                     ["tk_incremento", "tk_puntoycoma"],
                     ["tk_decremento", "tk_puntoycoma"]],
    "lexpr": [["nexpr", "nexpr_mas"]],
    "nexpr_mas": [["and", "nexpr", "nexpr_mas_and"],
                  ["or", "nexpr", "nexpr_mas_or"],
                  [""]],
    "nexpr_mas_and": [["and", "nexpr", "nexpr_mas_and"],
                      [""]],
    "nexpr_mas_or": [["or", "nexpr", "nexpr_mas_or"],
                     [""]],
    "nexpr": [["not", "tk_par_izq", "lexpr", "tk_par_der"],
              ["rexpr"]],
    "rexpr": [["simple_expr", "rexpr_mas"]],
    "rexpr_mas": [["tk_menor", "simple_expr"],
                  ["tk_igualdad", "simple_expr"],
                  ["tk_menor_igual", "simple_expr"],
                  ["tk_mayor", "simple_expr"],
                  ["tk_mayor_igual", "simple_expr"],
                  ["tk_diferente", "simple_expr"],
                  [""]],
    "simple_expr": [["term", "simple_expr_mas"]],
    "simple_expr_mas": [["tk_mas", "term", "simple_expr_mas"],
                        ["tk_menos", "term", "simple_expr_mas"],
                        [""]],
    "term": [["factor", "term_mas"]],
    "term_mas": [["tk_mul", "factor", "term_mas"],
                 ["tk_div", "factor", "term_mas"],
                 ["tk_mod", "factor", "term_mas"],
                 [""]],
    "factor": [["tk_num"],
               ["true"],
               ["false"],
               ["id", "factor_mas"],
               ["incr_decr", "id"],
               ["tk_par_izq", "lexpr", "tk_par_der"],
               ["fid", "tk_par_izq", "argu", "tk_par_der"]],
    "factor_mas": [["incr_decr"],
                   [""]],
    "incr_decr": [["tk_incremento"],
                  ["tk_decremento"]],
    "argu": [["lexpr", "argu_mas"],
             [""]],
    "argu_mas": [["tk_coma", "lexpr", "argu_mas"],
                 [""]],
    "main_prog": [["var_locales", "stm_mas", "end"]]
}

reglasPediccion = {}

for k in gramatica.keys():
    reglasPediccion[k] = []


def log(s, debug=0):
    if debug:
        print(s)


def PRIMEROS(alpha, debug=0):
    alpha = [alpha] if type(alpha) is str else alpha

    primeros = set()
    if alpha[0] == "":  # 1. Si alpha == epsilon
        primeros = primeros.union([""])
        return primeros

    if alpha[0] not in noTerminales:  # 2a. a_1 es un terminal

        primeros = primeros.union([alpha[0]])
        return primeros

    else:
        if alpha[0] != alpha[0]:
            primeros = primeros.union(PRIMEROS(alpha[0], debug))

            if "" in primeros:
                if len(alpha) == 1:
                    pass
                else:
                    try:
                        primeros.remove("")
                    except KeyError:
                        pass

                    primeros = primeros.union(PRIMEROS(alpha[1:], debug))

            return primeros

        else:
            for regla in gramatica[alpha[0]]:
                primeros = primeros.union(PRIMEROS(regla, debug))
                if "" in primeros:
                    if len(alpha) == 1:
                        pass
                    else:
                        try:
                            primeros.remove("")
                        except KeyError:
                            pass

                        primeros = primeros.union(PRIMEROS(alpha[1:], debug))

            log("PRIMEROS( " + alpha[0] + " ) = { " + str(
                primeros) + " }", debug)
            pass

    return primeros


def SIGUIENTES(no_terminal):
    global recursive_calls
    set_siguientes = set()
    if no_terminal == "prog":
        set_siguientes = set_siguientes.union(set("$"))

    for noTerm, reglas in gramatica.items():
        for regla in reglas:
            try:
                index = regla.index(no_terminal)
                if index == len(regla) - 1:
                    beta = ""
                else:
                    beta = regla[index + 1:]

                if type(beta) == str:
                    beta = [beta]

                primeros_beta = PRIMEROS(beta)
                set_siguientes = set_siguientes.union(primeros_beta)
                set_siguientes.remove("")

                if "" in primeros_beta or beta == "":
                    if noTerm not in recursive_calls:
                        recursive_calls.append(no_terminal)
                        set_siguientes = set_siguientes.union(SIGUIENTES(noTerm))
            except ValueError:
                pass
            except KeyError:
                pass

    return set_siguientes


def PRED(noTerminal):
    for regla in gramatica[noTerminal]:
        set_prediccion = set()
        primeros_alpha = PRIMEROS(regla)

        if "" in primeros_alpha:
            set_prediccion = set_prediccion.union(primeros_alpha)
            set_prediccion.remove("")
            recursive_calls = []  # para que pueda iniciar bien SIGUIENTES
            siguientesDeNoTerm = SIGUIENTES(noTerminal)
            set_prediccion = set_prediccion.union(siguientesDeNoTerm)

        else:
            set_prediccion = set_prediccion.union(primeros_alpha)

        lst_tmp = []
        for i in set_prediccion:
            lst_tmp.append(i)

        reglasPediccion[noTerminal].append(lst_tmp)


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

    token = None
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
            # print(token)
        else:
            if tipoToken == "REVISAR":
                token = Token("id", nuevoBuffer, fila, (columna - len(nuevoBuffer)))
                # print(token)
            elif tipoToken == "tk_num" or tipoToken == "fid":
                token = Token(tipoToken, nuevoBuffer, fila, (columna - len(nuevoBuffer)))
                # print(token)
            else:
                token = Token(tipoToken, nuevoBuffer, fila, (columna - len(nuevoBuffer)))
                # print(token)

    return devueltos, fila, columna, buffer, token


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

            devueltos, fila, columna, buffer, token = definirToken(devolver, tipoToken, devueltos, fila, columna,
                                                                   buffer)
            if token != None:
                tokens.append(token)

            for caracterDev in devueltos:
                buffer += caracterDev
                columna += 1
                estadoAux, devolver, tipoToken = delta(estadoAux, caracterDev)

                if tipoToken is not None:

                    if tipoToken == "Error léxico":
                        print(">>> Error léxico(línea:" + str(fila) + ",posición:" + str(columna - 1 - devolver) + ")")
                        bucleInterno = False
                        break

                    devueltos, fila, columna, buffer, token = definirToken(devolver, tipoToken, devueltos, fila,
                                                                           columna, buffer)
                    if token != None:
                        tokens.append(token)

            devueltos = ""


def getNextToken():
    global indexToken, tokenActual, finArchivo
    if indexToken == len(tokens):
        finArchivo = True
    else:
        tokenActual = tokens[indexToken]
    indexToken += 1


def errorSintaxis(lista_tokens_Esperados):
    global tokenActual, flagSintaxis
    flagSintaxis = True
    # if i == -2 and j == -2:
    #     return
    str_tmp = ""
    for pred in lista_tokens_Esperados:
        for token_esperado in pred:
            try:
                str_tmp += "'" + diccionarioTokens[token_esperado] + "', "
            except KeyError:
                str_tmp += "'" + token_esperado + "', "
    token_found = str(tokenActual.tipo)
    try:
        token_found = diccionarioTokens[str(tokenActual.tipo)]
    except KeyError:
        pass
    print(
        "<" + str(tokenActual.fila) + "," + str(
            tokenActual.columna) + ">" + " Error sintactico: se encontró: '" + token_found + "' y se esperaba " + str(
            str_tmp[:-2]) + ".")


def emparejar(token, token_esperado):
    # Emparejar No Terminales
    if token == token_esperado:
        getNextToken()
    else:
        errorSintaxis([[token_esperado]])


def nonTerminal(N):
    global tokenActual
    for idx, pd in enumerate(reglasPediccion[N]):
        if flagSintaxis:
            return
        if tokenActual.tipo in pd:
            for symbol in gramatica[N][idx]:
                if flagSintaxis:
                    return
                if symbol in noTerminales:
                    nonTerminal(symbol)
                    if flagSintaxis:
                        return
                elif symbol == "":
                    if flagSintaxis:
                        return
                else:
                    emparejar(tokenActual.tipo, symbol)
                    # if i == -1 and j == -1:  # Fin de archivo
                    #     token = ("$", i, j)
                    # if i == -2 and j == -2:  # Error lexico
                    #     flagSintaxis == True
                    if flagSintaxis:
                        return

            return
    tokensEsperados = []
    for k in reglasPediccion[N]:
        tokensEsperados.append(k)
    errorSintaxis(tokensEsperados)
    return


def main():
    global tokenActual, recursive_calls, finArchivo

    for nt in noTerminales:
        recursive_calls = []
        PRED(nt)

    # lineasSeparadas = sys.stdin.readlines()
    # lineas = ""
    # for linea in lineasSeparadas:
    #     lineas += linea


    lineas = cod4

    analizarLexico(lineas)  # Llenar lista de tokens

    getNextToken()
    nonTerminal("prog")
    if not flagSintaxis:
        if finArchivo:
            print("El analisis sintactico ha finalizado exitosamente.")
        else:
            errorSintaxis(["No se esperaba este token"])
            # print(token)


cod1 = '''## función min(x, y)
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
end
'''

cod2 = '''## función min(x, y)
function @min:num (x:num, y:num)
var menor:num, flag:bool;     # Las variables locales van antes del bloque
  {
  when ((x < y) == true) do return x;
  return y;
  }

## función max(x, y) El bloque debe tener, como mínimo, una sentencia
function @max:num (x:num, y:num)
  {
    print x+y;
  }

## función asignar(x, y) puede haber funciones de una única instrucción
function @asignar:num (x:num, y:num)
  x := y;

end
'''

cod3 = '''## función retornay(x, y)
function @retornay: (x:num, y:num)
  {
  return y;
  }
end
'''

cod4 = '''variable := 1;
variable;
end
'''

main()

# print("****")
# for i in tokens:
#     print(i.tipo)

# print(SIGUIENTES("lexpr"))

# for keys, values in reglasPediccion.items():
    #     print(keys)
    #     print(values)
