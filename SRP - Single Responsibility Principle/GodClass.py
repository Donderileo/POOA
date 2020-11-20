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
        self.calcula_lucro()

    def remove_aluno (self, aluno):
        self.alunos.pop(aluno)
        self.calcula_lucro()

    def lista_alunos(self):
        for aluno in self.alunos.values():
            aluno.imprime()

    def calcula_lucro(self):
        self.lucro = len(self.alunos) * self.preco_mensal
 
    def exibe_lucro(self):
        print(f'Lucro bruto:  {self.lucro}')

    



smart_fit = Academia("Smart Fit", 13)


smart_fit.calcula_lucro()
print("Lucro: " + str(smart_fit.lucro) + "\n")

smart_fit.adiciona_aluno(Aluno("Joao", 17))
smart_fit.lista_alunos()

smart_fit.adiciona_aluno(Aluno("Pedro", 20))
smart_fit.lista_alunos()

smart_fit.calcula_lucro()
print("Lucro: " + str(smart_fit.lucro) + "\n")


smart_fit.remove_aluno("Pedro")
smart_fit.lista_alunos()

smart_fit.calcula_lucro()
print("Lucro: " + str(smart_fit.lucro) + "\n")


