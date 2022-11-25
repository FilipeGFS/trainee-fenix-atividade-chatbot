class ProdutoDaLoja:
    def __init__(self,nome, preco):
        self.nome = nome
        self.preco = preco



class CarrinhoDeCompras:
    def __init__(self):
        self.lista_carrinho = []
        self.preco_total = 0


    def inserir_ao_carrinho(self,produto,qtd):
       for i in range(1,qtd+1):
           self.lista_carrinho.append([produto.nome,produto.preco])
           self.preco_total+=produto.preco

    def remover(self,produto):
        x =self.lista_carrinho.count([produto.nome,produto.preco])
        for i in range(1,x+1):
            self.lista_carrinho.remove([produto.nome,produto.preco])
            self.preco_total -=produto.preco

    def tamanho_do_carrinho(self):
        return len(self.lista_carrinho)

    def retornar_lista(self):
        return self.lista_carrinho

    def contar_produto(self,valor):
        return self.lista_carrinho.count(valor)

    def gerar_conta(self):
        return self.preco_total




