decisao = 0
arquivo = open('C:\\cotacao.txt' , 'a') # w escrever

while decisao != 2:
    decisao = int(input('Digite:\n 1 - Cadastrar \n 2 - Sair\n'))

    if decisao == 1:
        empresa =(str(input('Empresa: ')))
        data_hora = (str(input('Data/Hora: ')))
        val_acao = (str(input('Valor da ação: ')))
        desc = (str(input('Descrição: ')))
        arquivo.write('Empresa: {}| Data/hora: {}| Valor Cotação: {}| Descrição: {}\n'.format(empresa,data_hora,val_acao,desc) )


arquivo.close()


arquivo = open('C:\\cotacao.txt' , 'r')
print(arquivo.read())