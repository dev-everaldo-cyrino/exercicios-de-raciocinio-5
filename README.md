# exercicios-de-raciocinio-5
 exercicios que medem a capacidade do aluno/entrevistado

Construa um pequeno aplicativo SHELL do Python,
usando os requisitos abaixo citados:
Requisitos de Usuário
Na ultima elicitação, o cliente expos suas preferencias
acerca de como o sistema deveria agir para sua melhor
comodidade, definindo os seguintes requisitos:



RU001. O usuário deseja guardar as informações
referentes aos dados escolares de seus alunos
em uma tabela de banco de dados.
RU002. O usuário deseja obter o BOLETIM impresso do
aluno.



RU003. Os alunos devem ser identificados com um
número único.



RU004. O usuário acha muito necessário uma listagem
apenas com os nomes dos alunos para
conferencia.



RU005. O usuário pediu que, quando for alterar os dados
do aluno, ele primeiro consiga enxergar os dados
numa linha superior e depois, alterar os dados
depois de uma linha tracejada.



RU006. Na listagem do sistema, o usuário necessita
apenas do cabeçalho com o ano letivo, a série e,
uma lista contendo o ID, NOME e IDADE, como
também um espaço para assinatura.
Requisitos de Sistema
O gerente de projeto definiu uma série de requisitos de
sistema para orientação de seus programadores



RS001. Os dados armazenados devem ser o NOME,
IDADE, ANOLETIVO, SERIE, NOTA1, NOTA2,
NOTA3, NOTA4.



RS002. Os dados dos alunos devem ser armazenados
em modo DB, num arquivo identificado por
ALUNOS.DB usando a biblioteca SQLite3 do
próprio Python (recurso nativo)



RS003. O sistema deve criar o banco de dados quando
não existir o arquivo na pasta de trabalho.



RS004. O usuário optou por ter na interface do programa,
um menu com as opções do sistema, acessível
por digitação numérica. Deve constar:

    ---- ESCOLA IDIOMAS UPTALK ----
    1. INSERIR
    2. ALTERAR
    3. EXCLUIR
    4. LISTAR ALUNOS
    5. BOLETIM
    6. SAIR
    ---- Informe a ação desejada:

RS005. Ao inserir os dados, o sistema deve sair da tela
de MENU para a de INSERÇÃO, sendo necessário
apenas a digitação do NOME, IDADE, NOTA1,
NOTA2, NOTA3, NOTA4 e ANOLETIVO.


RS006. Para alterar os dados, o usuário optou por
mostrar a tela com as seguintes opções:


    Informe o ID do aluno: 1
    NOME: FULANO DE TAL, 23
    ANO LETIVO: 2018
    SÉRIE: 1ANO
    NOTA1 = 7.5
    NOTA2 = 8.7
    NOTA3 = 8.2
    NOTA4 = 7.8
    -------------------------------
    Digite o nome:
    Digite o Ano Letivo:
    Digite a Série:
    Digite a Nota1:
    Digite a Nota2:
    Digite a Nota3:
    Digite a Nota4:

RS007. A exclusão do aluno deve ser feita mediante
solicitação do código deste (ID) e posteriormente,
deve pedir confirmação.

    Informe o ID do aluno: 1
    NOME: FULANO DE TAL, 23
    ANO LETIVO: 2018
    SÉRIE: 1ANO
    NOTA1 = 7.5
    NOTA2 = 8.7
    NOTA3 = 8.2
    NOTA4 = 7.8
    -------------------------------
    Deseja excluir o registro? (S/N)

RS008. Na listagem, deve constar os dados abaixo:

    ---- ESCOLA IDIOMAS UPTALK ----
    Ano Letivo: 2018 Série: 1ANO
    LISTA PRESENÇA
    ID | ALUNO | IDADE | ASSINATURA
    -------------------------------------
    1 |FULANO | 23 | __________


RS009. O boletim deve constar basicamente os dados
do aluno com a média aritmética das quatro notas e
o STATUS: APROVADO ou REPROVADO. Nas
informações abaixo, segue o modelo de boletim


    sugerido pelo usuário:
    Informe o ID do aluno: 1
    ----------------------------
    BOLETIM ESCOLAR
    NOME: FULANO DE TAL, 23
    ANO LETIVO: 2018
    SÉRIE: 1ANO
    NOTA1 = 7.5
    NOTA2 = 8.7
    NOTA3 = 8.2
    NOTA4 = 7.8
    ----------------------------
    MEDIA = 8.0 STATUS: APROVADO