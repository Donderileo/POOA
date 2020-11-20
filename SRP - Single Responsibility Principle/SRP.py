class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def imprime(self):
        print('Aluno:')
        print(f'  Nome: {self.nome}')
        print(f'  Idade: {self.idade} \n')
        

class Academia:
    def	__init__(self, nome, preco):
        self.nome = nome
        self.lucro = 0
        self.alunos = {}
        self.preco_mensal = preco

    def adiciona_aluno(self, aluno):
        self.alunos[aluno.nome] = aluno
        x.calcula_lucro(self)
    
    def remove_aluno (self, aluno):
        self.alunos.pop(aluno)
        x.calcula_lucro(self)
    
    def lista_alunos(self):
        for aluno in self.alunos.values():
            aluno.imprime()

class Financeiro:
    def calcula_lucro(self, academia):
        academia.lucro = len(academia.alunos) * academia.preco_mensal
        
    def exibe_lucro(self, academia):
        print(f'Lucro bruto:  {academia.lucro}')



smart_fit = Academia("Smart Fit", 100)

x = Financeiro()

x.calcula_lucro(smart_fit)
x.exibe_lucro(smart_fit)

smart_fit.adiciona_aluno(Aluno("Joao", 17))
smart_fit.adiciona_aluno(Aluno("Pedro", 20))
smart_fit.lista_alunos()


x.calcula_lucro(smart_fit)
x.exibe_lucro(smart_fit)


smart_fit.remove_aluno("Pedro")
smart_fit.lista_alunos()

x.calcula_lucro(smart_fit)
x.exibe_lucro(smart_fit)

 

    
