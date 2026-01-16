print('Olá seja Bem-vindo a Entrevista,irei fazer algumas perguntas simples.')
print()

resposta = input('Ok?')
if resposta >= 'ok'+'sim':
  print('Ok,então vamos prosseguir com a entrevista.')
else:
  print('Ok tenha um bom dia!')

nome = input('Qual o seu nome?')
print()

idade = int(input('Qual a sua idade?'))
print()

comida = input('Qual sua comida favorita?')
print()

lazer = input('O que você gosta de fazer no tempo livre?')
print()

local = input('Que lugar você sonha em ir?')
print()

trabalho = input('Qual seu trabalho do sonhos?')
print()

salario = int(input('Qual  seu salário dos sonhos?'))
print()
print('Ok,vou ler uma breve resumo das suas repostas e você no final me diz se tá certo.')
alternativa = input('Ok?')
if alternativa >= 'ok'+ 'sim':
  print('Então vamos lá.')
else:
  print('Não entendi!')

print('Seu nome é {}'.format(nome))
print()

print('Você tem {} anos'.format(idade))
print()

print('A sua comida favorita é {}'.format(comida))
print()

print('Você gosta {} no seu tempo livre'.format(lazer))
print()

print('Você tem um sonho de ir para {}'.format(local))
print()

print('O seu trabalho do sonhos é {}'.format(trabalho))
print()

print('O seu salário dos sonhos é {}$'.format(salario))
print()

resumo = input('Tudo que eu disse está correto?')
if resumo >= 'sim':
  print('Ok,obrigado pela sua atenção para a entrevista,Até mais!')
else:
  print('Desculpe,você poderá enviar a correção pelo email no nosso site.')
