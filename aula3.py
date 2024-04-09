#bool - tipo de dado boolean
#ao questionar algo em um programa, só existem duas possibilidades
#true ou false
# existem varios operadores que "questionam o programa"
# o == checa se uma coisa é igual a outra
print( 10 == 10) #sim => verdadeiro True
print( 10 == 8 ) #não => falso False
print( type(10 == 8) ) #type- tipo dos números
print( type(True) )
print( type(False) )

##############################################################
#CONVERSÃO DE TIPOS, COERÇÃO
# type convertion
# typecasting
#coercion
#tipos imutáveis e primitivos 
# str (uma string vazia é considerada falsa )
# int
# float
# bool
print(1+1) #=>  ( aqui é int + int)
print('a'+'b')# => junta os caracteres
#print('1' + 1) # => nao funciona porque str nao soma nem junta com int
print( int('1'), type (int('1'))) # mostra o numero inteiro e seu tipo class int
print (float('1')+ 1) # consegue somar com a variavel e adiciona .0 no final 
print (type(float ('1') + 1))
print (bool (' '))
