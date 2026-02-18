import random
import string

caracteres = string.ascii_letters + string.digits + string.punctuation

def gerar_senha(tamanho):
    senha = random.choices(caracteres, k=tamanho)
    senha = "".join(senha)
    return senha

print("=== Gerador de Senhas ===")

while True:
    try:
        tamanho = int(input("\nQual o tamanho da senha? "))
        if tamanho < 1:
            print("O tamanho precisa ser maior que zero!")
        else:
            quantidade = int(input("Quantas senhas você quer gerar? "))
            if quantidade < 1:
                print("A quantidade precisa ser maior que zero!")
            else:
                print("\nSuas senhas são:")
                for i in range(quantidade):
                    senha_gerada = gerar_senha(tamanho)
                    print(f"  {i+1}. {senha_gerada}")

    except ValueError:
        print("Digite apenas números inteiros!")
    continuar = input("\nGerar outra senha? (s/n): ")
    if continuar.lower() != "s":
        print("Até mais!")
        break

#fazer esse código foi mais dificil do que parece mas achei 10
