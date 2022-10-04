# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário,
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar
valores = input(
    "Por gentileza. Digite o tempo gasto na viagem em horas e logo em seguida a velocidade média durante a mesma em km por hora.").split()
#valores = input().split()

tempo_gasto_horas = int(valores[0])
velocidade_media_kmh = int(valores[1])

# Cálculo da quantidade de litros necessária para realizar a viagem
calculo_qtd_litros = float((tempo_gasto_horas * velocidade_media_kmh)/12)

# Impressão com TRÊS dígitos após o ponto decimal
print(f"{calculo_qtd_litros:.3f}")
