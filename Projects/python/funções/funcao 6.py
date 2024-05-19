def converter_24_para_12(horas, minutos, periodo):
    if periodo.upper() == 'A':
        periodo_str = 'A.M.'
    elif periodo.upper() == 'P':
        periodo_str = 'P.M.'
    else:
        return "Período inválido. Use 'A' para A.M. ou 'P' para P.M."


    if horas > 12:
        horas -= 12
    elif horas == 0:
        horas = 12


    return f"{horas}:{minutos:02d} {periodo_str}"

def main():
    while True:
        try:
            horas = int(input("Digite a hora (0-23): "))
            minutos = int(input("Digite os minutos (0-59): "))
            periodo = input("Digite 'A' para A.M. ou 'P' para P.M.: ")

            hora_convertida = converter_24_para_12(horas, minutos, periodo)
            print(f"Hora convertida: {hora_convertida}")

            continuar = input("Deseja converter outra hora? (S/N): ")
            if continuar.upper() != 'S':
                break
        except ValueError:
            print("Entrada inválida. Certifique-se de digitar números para horas e minutos.")


main()
