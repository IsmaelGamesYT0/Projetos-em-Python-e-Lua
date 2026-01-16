print('Registro.') # Inicío do código.
print()   # Espaço.

# Armazenamento do nome.
nome = input('Digite seu nome:')  
while nome == '':
    nome = input('Nome não pode ser vazio. Digite seu nome:')  # Verificação do nome,
                                                               #caso o usúario não insira nada.
# Armazenamento da idade.
idade = input('Digite sua idade:')   
while idade == '':
    idade = input('Você precisa inserir sua idade para continuar!')  # Verificação da idade,
                                                                     # caso o usúario não insira nada.
# Conversão da idade para número inteiro.
idade = int(idade) 

# Entrada permitida apenas se a idade miníma for alcançada.
if idade >= 18:
  print('Entrada Permitida!') 
  print()                     
else:
   print('Entrada Bloqueada!')           # Entrada Bloqueada caso o usúario,
print('Seja Bem-vindo! {}'.format(nome)) # não tenha a idade miníma.
acao = input('O que você gostaria de fazer agora?')  # Acão a ser executada.
if acao.lower() == 'Nada':
    print('Ok,Até mais.')
else:
    print('Ok,até mais!')

# Encerramento do Programa.
quit()  
