#if / elif        / else
#se / se não se  / senao
entrada= input ('Você quer "entrar" ou "sair"? ')

if entrada=='entrar':
   print('Você entrou no sistema')
# se essa condição for verdadeira ele vai executar o codigo 
elif entrada == 'sair':
    print('Você saiu do sistema ')
else:
    print('Você não digitou nem entrar nem sair!!')
    print('DIGITE NOVAMENTE')
