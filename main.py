import sqlite3

banco = sqlite3.connect('banco1.db')
cursor= banco.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS  aluno (id integer primary key autoincrement  , nome text , idade integer, ano integer , sere text, nota1 integer, nota2 integer, nota3 integer, nota4 integer)')

while True:
  print("""
---- ESCOLA IDIOMAS UPTALK ----
1. INSERIR
2. ALTERAR
3. EXCLUIR
4. LISTAR ALUNOS
5. BOLETIM
6. SAIR
""")
  op = int(input('---- Informe a ação desejada: '))
  if op ==1:
    print('----inserindo novo aluno----')
    
    nome = input('digite o nome: ')
    idade = int(input('digite a idade: '))
    ano = int(input('digite o ano: '))
    sere = input('digite a sere: ')
    nota1 = int(input('digite a nota1: '))
    nota2 = int(input('digite a nota2: '))
    nota3 = int(input('digite a nota3: '))
    nota4 = int(input('digite a nota4: '))
    
    cursor.execute("INSERT INTO aluno (nome, idade, ano, sere , nota1, nota2 , nota3 , nota4 ) VALUES('{}',{},{},'{}',{},{},{},{})".format(nome,idade,ano,sere,nota1,nota2,nota3,nota4))
    banco.commit()
    
  
  if op ==2:
    print('----alterando dados----')
    cursor.execute('SELECT id FROM  aluno')
    id = cursor.fetchall()
    boletin = int(input('total={}. digite um id: '.format(id[-1][0])))
    if boletin <=0 or boletin > id[-1][0]:
      print('opção invalida !!!. programa encerrando...')
      break
    else:
      cursor.execute('SELECT * FROM aluno WHERE id = {}'.format(boletin))
      a = cursor.fetchall()
      print(a)
      print('''
      NOME: {}
      IDADE: {}
      ANO LETIVO: {}
      SÉRIE: {}
      NOTA1 = {}
      NOTA2 = {}
      NOTA3 = {}
      NOTA4 = {}'''.format(a[0][1],a[0][2],a[0][3],a[0][4],a[0][5],a[0][6],a[0][7],a[0][8]))
      print('-------------------------------')
      idade = int(input('digite a idade: '))
      ano = int(input('digite o ano: '))
      sere = input('digite a sere: ')
      nota1 = int(input('digite a nota1: '))
      nota2 = int(input('digite a nota2: '))
      nota3 = int(input('digite a nota3: '))
      nota4 = int(input('digite a nota4: '))
      cursor.execute("UPDATE aluno SET idade = {} ,ano = {} , sere = '{}' , nota1 = {} , nota2 = {} , nota3 = {} , nota4 = {} WHERE id = {}".format(idade,ano,sere,nota1,nota2,nota3,nota4,boletin))
      print('-------------------------------')
      banco.commit()
      print('update feito com sucesso')



  if op ==3:
    boletin =0
    cursor.execute('SELECT id FROM  aluno')
    id = cursor.fetchall()
    
    print('----excluindo dados----')
    boletin = int(input('total={}. digite um id: '.format(len(id))))
    if boletin <=0 or boletin > id[-1][0]:
      print('opção invalida !!!. programa encerrando...')
      break
    else:
      cursor.execute('SELECT * FROM aluno WHERE id = {}'.format(boletin))
      a = cursor.fetchall()
      print('''
      NOME      : {}
      IDADE     : {}
      ANO LETIVO: {}
      SÉRIE     : {}
      NOTA1     = {}
      NOTA2     = {}
      NOTA3     = {}
      NOTA4     = {}'''.format(a[0][1],a[0][2],a[0][3],a[0][4],a[0][5],a[0][6],a[0][7],a[0][8]))
      print('-------------------------------')
      deletar = input('Deseja excluir o registro? (S/N) ')
      if deletar =='s':
        idd =a[0][0]
        print(idd-1)
       
        iddfinal= a[-1][0]
        print(iddfinal *10)
        cursor.execute('DELETE FROM aluno WHERE id = {}'.format(idd))
        banco.commit()
        print('registro excluido com sucesso !!!')
        
        




  if op ==4:
    idd=cursor.execute('SELECT id FROM  aluno')
    id = idd.fetchall()
    print('-----listagem de alunos-----')
    print('id.|idade.|sere.| nome')
    num=0
    for x in range(len(id)):
      cursor.execute('SELECT * FROM aluno')
      a = cursor.fetchall()
      print('{}  |{}   |{}   | {}'.format(a[num][0],a[num][2],a[num][4],a[num][1]))
      num +=1

      


  if op ==5:
    cursor.execute('SELECT id FROM  aluno')
    id = cursor.fetchall()
    boletin = int(input('total={}. digite um id: '.format(id[-1][0])))
    if boletin <=0 or boletin > id[-1][0]:
      print('opção invalida !!!. programa encerrando...')
      break
    else:
      cursor.execute('SELECT * FROM aluno WHERE id = {}'.format(boletin))
      a = cursor.fetchall()
      

      print('''
      NOME      : {}
      IDADE     : {}
      ANO LETIVO: {}
      SÉRIE     : {}
      NOTA1     = {}
      NOTA2     = {}
      NOTA3     = {}
      NOTA4     = {}'''.format(a[0][1],a[0][2],a[0][3],a[0][4],a[0][5],a[0][6],a[0][7],a[0][8]))
      print('-------------------------------')
      media = a[0][5]+a[0][6]+a[0][7]+a[0][8]
      print('MEDIA = {}'.format(media/4))

  if op==6:
    break