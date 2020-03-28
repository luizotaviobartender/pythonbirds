class Pessoa:
    def __init__(self,nome=None):
        self.name = nome

    def cumprimenta(self):
        return f'olá {id(self)}'

if __name__=='__main__':
    p = Pessoa('luiz')
    print(Pessoa.cumprimenta(p))
    print(id(p))
    print(p.cumprimenta())
    print(p.nome)
    p.nome='otavio'
    print(p.nome)
