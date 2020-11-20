# De quem é a responsabilidade?


#### Autor: Leonardo Donderi Rodrigues.

## SOLID

O princípio que será tratado neste artigo, junto com outros 4 foram identificados por Robert C. Martin, por volta do ano 2000 e agrupados no acrônimo SOLID por Michael Feathers, após observar que os cinco princípios poderiam se encaixar nesta palavra.

        S — Single Responsiblity Principle (Princípio da responsabilidade única)
        O — Open-Closed Principle (Princípio Aberto-Fechado)
        L — Liskov Substitution Principle (Princípio da substituição de Liskov)
        I — Interface Segregation Principle (Princípio da Segregação da Interface)
        D — Dependency Inversion Principle (Princípio da inversão da dependência)
    
Esses princípios quando bem aplicados evitam uma série de problemas:

        Dificuldade na testabilidade / criação de testes de unidade;
        Código macarrônico, sem estrutura ou padrão;
        Dificuldades de isolar funcionalidades;
        Duplicação de código, uma alteração precisa ser feita em N pontos;
        Fragilidade, o código quebra facilmente em vários pontos após alguma mudança.

## Principio da responsabilidade Única

Contrariando o conceito de classe "faz tudo" (comumente chamada de God Class), o príncipio da responsabilidade única tem como base que todas as classes devem possuir uma e somente uma responsabilidade, ou seguindo a definição:

        "Uma classe deve ter um, e somente um, motivo para mudar."

Códigos que fogem a esse princípio podem funcionar perfeitamente, mas por existir uma intersecção de responsabilidades, ao fazer uma alteração de algum parâmetro ou função há sempre a possibilidade de comprometer outra parte da aplicação ou alterar essa mesma parte em diversas outras partes do código, prejudicando muito as manutenções e alterações rotineiras.

Imagine o seguinte cenário, uma academia possui um sistema que controla a quantidade de alunos na academia (inserção e remoção de alunos) e calcula o lucro bruto com base na quantidade de alunos matriculados.

Sem pensar nos principios SOLID, criamos uma [God Class](https://medium.com/@carlos.ariel.mamani/the-god-object-or-god-class-anti-pattern-bfb8c15eb513):

```py     

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
 
```

Note que a classe possue metodos que executam as funções descritas anteriormente.

* __init__ : Construtor da classe, recebe o nome da academia e a constrói com lucro = 0 e um dicionário de alunos vazio.
* adiciona_aluno(): Método que adiciona um aluno com nome e idade a academia e recalcula o lucro da academia (metodo calcula_lucro)
* lista_alunos(): Método que imprime todos os alunos da academia, definida na classe Aluno.
* remove_aluno(): Método que remove um aluno usando seu nome e recalcula o lucro da academia (metodo calcula_lucro).
* calcula_lucro(): Método que calcula o lucro bruto com a operação: (quantidade de alunos * preço da mensalidade)
* exibe_lucro(): Método que exibe o lucro previamente calculado.

Podemos identificar o princípio da responsabilidade única quando pessoas com áreas de conhecimento diferentes ou outros colaboradores utilizam o software  com demandas diferentes. No exemplo dado, temos que os responsáveis pela gestão dos alunos e os responsáveis pelas finanças dessa academia, possuem seus métodos na mesma classe.

Assim, identificamos duas responsabilidades na classe Academia:

* Gerenciamento de pessoas
* Gerenciamento de finanças 

Com isso, podemos criar um novo código, aplicando o SRP e resolvendo o possível conflito causado por uma classe que viola esse princípio.

```py
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
```

Agora conseguimos observar que cada classe possui um e apenas um motivo de existência/alteração, portanto, uma responsabilidade. Respeitando assim, o princípio da responsabilidade única.

Mas, o que ganhamos respeitando esse princípio?

* A manutenção se torna mais simples, já que estamos com um código mais limpo e bem dividido.
* As atualizações, melhorias e novos recursos podem ser alocados na classe correta, sem correr o risco de quebrar toda a aplicação (ortogonalidade)
* As classes bem definidas podem ser reutilizadas de forma simples.

Por fim, esse príncipio não traz benefícios visíveis na aplicação como talvez uma redução no tempo de carregamento ou compilação, porém, é de extrema importância para gerar um código de alto nível e legível para outros programadores que terão responsabilidades em cima dele (melhorias/manutenção)



### Fontes

* [O que é SOLID: O guia completo para você entender os 5 princípios da POO](https://medium.com/desenvolvendo-com-paixao/o-que-%C3%A9-solid-o-guia-completo-para-voc%C3%AA-entender-os-5-princ%C3%ADpios-da-poo-2b937b3fc530)
* [The God Object Or The God Class Anti-Pattern](https://medium.com/@carlos.ariel.mamani/the-god-object-or-god-class-anti-pattern-bfb8c15eb513)
* [Solid — S.R.P — Single Responsibility Principle](https://medium.com/@tbaragao/solid-s-r-p-single-responsibility-principle-2760ff4a7edc)
* [Princípios SOLID na programação orientada a objetos - Princípio da Responsabilidade Única](https://www.youtube.com/watch?v=wwg-gWTuB1o)



