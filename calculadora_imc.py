def calcular_imc(peso, altura_cm):
    """
    Calcula o IMC dado o peso (em kg) e a altura (em centímetros).
    Retorna o valor do IMC e a categoria correspondente.
    """
    altura_m = altura_cm / 100  # Convertendo a altura de centímetros para metros
    imc = peso / (altura_m ** 2)
    
    if imc < 18.5:
        categoria = "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        categoria = "Peso normal"
    elif 25 <= imc < 29.9:
        categoria = "Sobrepeso"
    elif 30 <= imc < 34.9:
        categoria = "Obesidade Grau 1"
    elif 35 <= imc < 39.9:
        categoria = "Obesidade Grau 2"
    else:
        categoria = "Obesidade Grau 3"
    
    return imc, categoria

def main():
    try:
        peso = float(input("Digite o seu peso (em kg): "))
        altura_cm = float(input("Digite a sua altura (em centímetros): "))
        imc, categoria = calcular_imc(peso, altura_cm)
        
        print(f"\nSeu IMC é: {imc:.2f}")
        print(f"Categoria: {categoria}")
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

if _name_ == "_main_":
    main()