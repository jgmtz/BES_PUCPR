def verificar_quadrado_magico(quadrado):
    return (quadrado[0] + quadrado[1] + quadrado[2] == 15 and
            quadrado[3] + quadrado[4] + quadrado[5] == 15 and
            quadrado[6] + quadrado[7] + quadrado[8] == 15 and
            quadrado[0] + quadrado[3] + quadrado[6] == 15 and
            quadrado[1] + quadrado[4] + quadrado[7] == 15 and
            quadrado[2] + quadrado[5] + quadrado[8] == 15 and
            quadrado[0] + quadrado[4] + quadrado[8] == 15 and
            quadrado[2] + quadrado[4] + quadrado[6] == 15)

def identificar_quadrados_magicos():
    quadrados_magicos = []
    for a in range(1, 10):
        for b in range(1, 10):
            if b == a:
                continue
            for c in range(1, 10):
                if c == a or c == b:
                    continue
                for d in range(1, 10):
                    if d == a or d == b or d == c:
                        continue
                    for e in range(1, 10):
                        if e == a or e == b or e == c or e == d:
                            continue
                        for f in range(1, 10):
                            if f == a or f == b or f == c or f == d or f == e:
                                continue
                            for g in range(1, 10):
                                if g == a or g == b or g == c or g == d or g == e or g == f:
                                    continue
                                for h in range(1, 10):
                                    if h == a or h == b or h == c or h == d or h == e or h == f or h == g:
                                        continue
                                    for i in range(1, 10):
                                        if i == a or i == b or i == c or i == d or i == e or i == f or i == g or i == h:
                                            continue
                                        quadrado = [a, b, c, d, e, f, g, h, i]
                                        if verificar_quadrado_magico(quadrado):
                                            quadrados_magicos.append(quadrado)

    return quadrados_magicos
def mostrar_quadrados_magicos():
    quadrados = identificar_quadrados_magicos()

    if quadrados:
        print("Quadrados Mágicos:")
        for quadrado in quadrados:
            print(f"{quadrado[0]} {quadrado[1]} {quadrado[2]}\n"
                  f"{quadrado[3]} {quadrado[4]} {quadrado[5]}\n"
                  f"{quadrado[6]} {quadrado[7]} {quadrado[8]}\n")
    else:
        print("Nenhum quadrado mágico encontrado.")
mostrar_quadrados_magicos()
