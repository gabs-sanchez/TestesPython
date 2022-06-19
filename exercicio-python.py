# exercicio 5 - lista 7
"""
def exercicio5():
  nota=input('Informe sua 1º nota:\n');
  nota2=input('Informe sua 2º nota:\n');

  nota=int(nota);
  nota2=int(nota2);

  media=(nota+nota2)/2

  if media>=6:
      print('Parabéns,aprovado!'); 
  else:
      print('Tente outra vez...');

exercicio5();
"""

#exercicio 9 - lista 7
"""
def exercicio9(escolha2):
  
  print('\n------------------------------------');
  print('   Escolha uma espécie\n');
  print(' 1. Ovíparo ');
  print(' 2. Mamíferos');
  print('------------------------------------');
  
  escolha1=input('\n');
  escolha1=int(escolha1);
  
  if escolha1==1:
   print('\n------------------------------------');
   print('   Escolha um Ovíparo \n');
   print(' 1. Galinha ');
   print(' 2. Peixe');
   print(' 3. Tartaruga');
   print('------------------------------------');
  
   escolha2=input('\n');

  else:
   
   print('\n------------------------------------');
   print('   Escolha um Mamífero \n');
   print(' 1. Elefante ');
   print(' 2. Porco');
   print(' 3. Coelho');
   print('------------------------------------');
  
   escolha3=input('\n');

  print('------------------------------------');
  print('Valor de compra do animal');
  print('------------------------------------');
  
  valor=input('\n');
  valor= int(valor);
  
  if escolha2 != 0:
      resultado= valor/0.95;
      resultadoRound= round(resultado,2);

      print('\n------------------------------------');
      print(f'O imposto será de {resultadoRound}');
      print('------------------------------------');
  else:
      resultado2= valor/0.9;
      resultadoRound2= round(resultado2,2);

      print('\n------------------------------------');
      print(f'O imposto será de {resultadoRound2}');
      print('------------------------------------');
      
exercicio9(0);
"""
#exercicio8 - lista 16
"""
def exercicio8():
  lista=[];
  i=0;
  LoopPrint=1;
  x='------------------------------------';
  print(f'\n{x}');
  print('   Digite a qtnd de alunos')
  print(f'{x}');

  valorAluno =input('\n');
  valorAluno =int(valorAluno);
  
  while i < valorAluno :
    aluno=input(f'Digite o nome do {i+1}º aluno\n');
    lista.append(aluno);
    i+=1;

  print('\n');

  while LoopPrint<=valorAluno:
    print(f'aluno/aluna {lista[-LoopPrint]}');
    LoopPrint+=1;
exercicio8();
"""
#exercicio - lista 16
