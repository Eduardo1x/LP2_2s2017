# coding:utf-8
#arquivoABS = open('C:/Users/1700576/Downloads/tweets.txt')
#arquivoREL = open("twitter/tweets.txt")



#conteudo = arquivoABS.read()
#conteudo = arquivoREL.read()
#print(conteudo)

#arquivoREL.seek(1000)
#conteudo = arquivoREL.read()
#print('\n\n\nSegunda leitura')
#print(conteudo)

#print(arquivoREL.tell())

#print(arquivoREL.closed)

#if arquivoREL.closed == False:
#    arquivoREL.close()
#print(arquivoREL.closed)


#with open('twitter/tweets.txt') as arquivo:
#    conteudo = arquivo.read()
#    print(conteudo)
#    print(arquivo.tell())
#    arquivo.seek(0)
#    for linha in arquivo:
#        print(linha.rstrip())


#with open('twitter/teste.txt', 'w') as arquivo:
#    arquivo.write('Sua mãe\r\n')
#    arquivo.write('é minha\r\n')

#with open('twitter/teste.txt') as arquivo:
#    print(arquivo.read())


# ler arquivo e fechar ao finalizar
dic = {}
with open('twitter/teste.txt') as arquivo:
    # para cada linha do arquivo
    for linha in arquivo:
        # remove \n do final da linha
        linha = linha.rstrip()
        # separar a linha por espaços
        palavras = linha.split(' ')
        # percorrer palavras para contar
        for palavra in palavras:
            if palavra in dic.keys():
                dic[palavra] = dic[palavra] + 1
            else:
                dic[palavra] = 1
with open('twitter/saida.txt', 'w') as arquivo:
    for chave, valor in dic.items():
        arquivo.write(chave+": "+str(valor)+"\n")
