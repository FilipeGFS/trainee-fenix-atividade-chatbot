from arquivo_de_classes import ProdutoDaLoja, CarrinhoDeCompras

prods_precos_qtds = [['Fone de Ouvido',60.00,50],['Carregador',50.00,30],['Pen Drive',40.00,45],['SmartWatch',150.00,25],
                          ['Iphone',5000.00,40], ['Mouse',40.00,50],['Teclado',120.00,40]]
#                   [item,preço unitário,quantidade em estoque]

p1 = ProdutoDaLoja(prods_precos_qtds[0][0],prods_precos_qtds[0][1])
p2 = ProdutoDaLoja(prods_precos_qtds[1][0],prods_precos_qtds[1][1])
p3 = ProdutoDaLoja(prods_precos_qtds[2][0],prods_precos_qtds[2][1])
p4 = ProdutoDaLoja(prods_precos_qtds[3][0],prods_precos_qtds[3][1])
p5 = ProdutoDaLoja(prods_precos_qtds[4][0],prods_precos_qtds[4][1])
p6 = ProdutoDaLoja(prods_precos_qtds[5][0],prods_precos_qtds[5][1])
p7 = ProdutoDaLoja(prods_precos_qtds[6][0],prods_precos_qtds[6][1])

lista_produtos_disponiveis = [p1, p2, p3, p4, p5, p6, p7]
carrinho = CarrinhoDeCompras()
adicionados_ao_carrinho = []
registro_de_comando_encerrar = [0]

print('Olá! Seja bem vindo ao nosso chatbot de atendimento :)\n')
print('Lista de operações:\n(1)Adicionar item\n(2)Remover item\n'
      '(3)Mostrar carrinho\n(4)Fechar carrinho\n')
while not registro_de_comando_encerrar[-1]==4:
    comando = input('Digite o índice da ação desejada: ')
    while not comando.isnumeric() or not int(comando) in range(1,5):
        comando = input('Você deve digitar um comando válido: ')

    if comando=='1':
        print('\nItens disponíveis:')
        for indice, item in enumerate(prods_precos_qtds):
            print(f'({indice+1}) Produto: {item[0]} | Preço: R${item[1]} | Quantidade disponível: {item[2]}')

        comando2=input('Digite o número do item que deseja adicionar ao carrinho: ')

        while not comando2.isnumeric() or not int(comando2) in range(1,8):
            comando2= input('Você deve digitar um valor válido: ')
        comando2 = int(comando2)
        if prods_precos_qtds[comando2-1][2]==0:
            print(f'Não há mais {prods_precos_qtds[comando2-1][0]} disponível.')

        else:
            qtd = input(f'Digite a quantidade de {prods_precos_qtds[comando2-1][0]} que deseja inserir ao carrinho: ')
            qtd_limite = prods_precos_qtds[comando2 - 1][2]

            while not qtd.isnumeric() or not int(qtd) <= qtd_limite:
                qtd= input('Você deve digitar um valor válido dentro da quantidade disponível: ')
            qtd= int(qtd)

            carrinho.inserir_ao_carrinho(lista_produtos_disponiveis[comando2-1],qtd)
            prods_precos_qtds[comando2 - 1][2] -=qtd
            prod_preco = [prods_precos_qtds[comando2-1][0],prods_precos_qtds[comando2-1][1]]
            if prod_preco  not in adicionados_ao_carrinho:
                adicionados_ao_carrinho.append(prod_preco)
            print(f'{qtd} unidades de {prod_preco[0]} inseridas com sucesso!')



    if comando=='2':
        if carrinho.tamanho_do_carrinho()==0:
            print('Não é possível remover itens de um carrinho vazio.')
        else:
            comando3= input('Digite o índice do produto que deseja remover do carrinho: ')
            while not comando3.isnumeric() or not int(comando3) in range(1,8):
                comando3=input('Você deve inserir um valor válido: ')
            comando3= int(comando3)
            n= comando3-1
            if [prods_precos_qtds[n][0],prods_precos_qtds[n][1]] not in carrinho.retornar_lista():
                print('Não é possível remover um item que não está no carrinho.')

            else:
                carrinho.remover(lista_produtos_disponiveis[comando3-1])
                adicionados_ao_carrinho.remove([prods_precos_qtds[n][0],prods_precos_qtds[n][1]])
                print(f'{prods_precos_qtds[comando3-1][0]} removido do carrinho com sucesso!')

    if comando=='3':
        if carrinho.tamanho_do_carrinho()==0:
            print('O carrinho está vazio.')
        else:
            print('Itens do carrinho:')
             for indice,item in enumerate(adicionados_ao_carrinho):
                z = carrinho.contar_produto(item)
                print(f'Produto: {adicionados_ao_carrinho[indice][0]} | Quantidade no carrinho: {z}')

    if comando=='4':
        registro_de_comando_encerrar.append(4)
print(f'Valor total da compra: R${carrinho.gerar_conta()}0')
print('Operação finalizada. Agradecemos a preferência! :)')


