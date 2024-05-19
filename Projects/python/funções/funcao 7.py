def valorPagamento(valor_prestacao, dias_atraso):
    if dias_atraso <= 0:
        return valor_prestacao
    else:
        multa = valor_prestacao * 0.03
        juros = valor_prestacao * (0.001 * dias_atraso)
        return valor_prestacao + multa + juros


def main():
    total_prestacoes = 0
    total_valor_pago = 0

    while True:
        valor_prestacao = float(input("Digite o valor da prestação (ou 0 para sair): "))
        if valor_prestacao == 0:
            break

        dias_atraso = int(input("Digite o número de dias em atraso: "))
        valor_pago = valorPagamento(valor_prestacao, dias_atraso)

        print(f"Valor a ser pago: R$ {valor_pago:.2f}")

        total_prestacoes += 1
        total_valor_pago += valor_pago

    print(f"\nRelatório do dia:")
    print(f"Quantidade de prestações pagas: {total_prestacoes}")
    print(f"Valor total pago: R$ {total_valor_pago:.2f}")


if __name__ == "__main__":
    main()
