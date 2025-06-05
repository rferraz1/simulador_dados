import random

def rolar_dado(lados, quantidade):
    return [random.randint(1, lados) for _ in range(quantidade)]

def main():
    print("Simulador de Dados de RPG")
    tipos = {4, 6, 8, 10, 12, 20, 100}
    lados = int(input(f"Escolha o dado ({tipos}): "))
    if lados not in tipos:
        print("Tipo de dado inválido.")
        return
    quantidade = int(input("Quantos dados deseja rolar? "))
    resultados = rolar_dado(lados, quantidade)
    print(f"Resultados: {resultados}")

if __name__ == "__main__":
    main()
