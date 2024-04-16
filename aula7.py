# 1. (n + n) primeira coisa executada são os parenteses (sempre os mais internos / de dentro para fora)
# 2. ** potenciação / exponenciaçã
# 3. * / // %  multiplicação, divisao, divisao inteira e modulo
# 4. + - adição e subtração
#esquerda p direita

conta_1 = 1 + 1 ** 5 + 5 #7
print(conta_1)
print ( conta_1 == 7) #bool
#se a variavel não mudar de nome, o ultimo valor escrito será executado
conta_2 = 2 + 5 / 2
