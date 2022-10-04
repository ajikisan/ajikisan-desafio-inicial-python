# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário,
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar
valores = input(
    "Por gentileza. Digite o número total de cachorros-quentes consumidos e o número total de participantes na competição.").split()

#valores = input().split()
cachorros_quentes = int(valores[0])
total_participantes = int(valores[1])

# Cálculo da média de cachorros quentes consumidas por participante e impresso o valor com DUAS casas decimais.
print(f"{cachorros_quentes/total_participantes:.2f}")
