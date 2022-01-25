from time import time

def defineOrdemLista(dados): #Organiza os itens em ordem decrescente de "preciosidade" (interesse/peso)
    dados.sort(key=lambda info: info[0]/info[1], reverse=True)

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com secesso!')

def escreverArquivo(nome, tempo, MelhorRamo, MaiorInteresse, CapacidadeMelhorRamo, qtdRamos, sucesso=0, podaFolha=0):
    try:
        a = open(nome, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{tempo};{MelhorRamo};{MaiorInteresse};{CapacidadeMelhorRamo};{qtdRamos};{sucesso};{podaFolha}\n')
        except:
            print('Houve um erro na hora de escrever os dados.')
        else:
            print(f'NOVO REGISTRO ADICIONADO COM SUCESSO!')
            a.close() 

def calculaLimitante(lista, indice, capacidade, interesseParcial, pesoParcial):
    print(f'interesseParcial: {interesseParcial}\n(lista[indice+1][0] / lista[indice+1][1]): {(lista[indice+1][0] / lista[indice+1][1])}')
    print(f'(capacidade - pesoParcial): {(capacidade - pesoParcial)}')
    S = float(interesseParcial + ((lista[indice+1][0] / lista[indice+1][1]) * (capacidade - pesoParcial)))
    
    return S

def solucionaProblemaMochila(lista, C, saida):
    limiteTempo = 5
    hora_inicial = time()
    print(f'Lista inicial: {lista}')
    defineOrdemLista(lista)
    print(f'Lista ordenada: {lista}')
    melhorRamo = list()
    ramoAtual = list()

    for i in range(0, len(lista)):
        melhorRamo.append(int(0))
        ramoAtual.append(int(0))
    
    contador = 0
    inicio = 0
    maiorInteresse = 0
    maiorCapacidade = 0
    sucesso = 1
    auxiliar = 0
    U = 0
    P = 0
    podaFolha = 0

    while True:         
        auxiliarCapacidade = C - P

        for i in range(inicio, len(lista)):            
            ramoAtual[i] = int(auxiliarCapacidade // lista[i][1])
            auxiliarCapacidade -= (ramoAtual[i] * lista[i][1])
            U += ramoAtual[i] * lista[i][0] #interesse do ramo atual
            P += ramoAtual[i] * lista[i][1] #peso do ramo atual
        
        if (contador == 0) or (U > maiorInteresse):
            melhorRamo = ramoAtual[:]
            maiorInteresse = U
            maiorCapacidade = P
        
        contador += 1
        print(60*"=")
        print(f'ramo atual: {ramoAtual}\ninteresse do ramo atual: {U}\npeso do ramo atual: {P}')

        indiceFolha = len(lista) - 1
        if ramoAtual[indiceFolha] > 0:
            podaFolha += ramoAtual[indiceFolha]
            U -= ramoAtual[indiceFolha] * lista[indiceFolha][0]
            P -= ramoAtual[indiceFolha] * lista[indiceFolha][1]
            print(f'\033[1;32mVAMOS PODAR {ramoAtual[indiceFolha]} FOLHA(S)\033[m')
            ramoAtual[indiceFolha] = 0

        auxiliar = 0
        for i in range(len(lista) - 2, -1, -1):
            if ramoAtual[i] > 0:
                ramoAtual[i] -= 1
                P -= lista[i][1]
                U -= lista[i][0]
                inicio = i + 1
                limitante = calculaLimitante(lista, i, C, U, P)

                print(f'limitante: {limitante}\n maior interesse: {maiorInteresse}')
                if limitante < float(maiorInteresse):
                    print(f'\033[1;36mVAMOS PODAR {ramoAtual[i] + 1} UNIDADE(S) DO ELEMENTO {i}\033[m')
                    P -= ramoAtual[i] * lista[i][1]
                    U -= ramoAtual[i] * lista[i][0]
                    ramoAtual[i] = 0
                    continue
                else:
                    break
            elif i != len(lista) - 1:
                auxiliar += 1
        
        if auxiliar == len(lista) - 1:
            break

        tempo_total = time() - hora_inicial
        if tempo_total >= limiteTempo:
            sucesso = 0
            print(f'Execução interrompida ({limiteTempo} segundos)')
            break

    contador -= 1
    print(60*"=")
    print(f'\033[4;31mMelhor ramo: {melhorRamo}\nMaior interesse: {maiorInteresse}\nMaior capacidade: {maiorCapacidade}\nQuantidade de verificações: {contador}\033[m')
    print(f'\033[1;32mPodas de folhas: {podaFolha}\033[m')
    print(60*"=")

    arquivoResultados = saida + 'resultadosLimitante.txt'
    print(arquivoResultados)
    if not arquivoExiste(arquivoResultados):
        criarArquivo(arquivoResultados)
    escreverArquivo(arquivoResultados, tempo_total, melhorRamo, maiorInteresse, maiorCapacidade, contador, sucesso, podaFolha)

#Leitura dos diretórios de entrada e saída de dados

print(f'\n\033[1;35m{40*"="} Solucionador de Problemas da Mochila {40*"="}\033[m\n')
caminho = str(input("Informe o caminho completamente qualificado do arquivo de testes: "))
saida = str(input("Informe a pasta de saída (com uma barra no final): "))

#Leitura dos parâmetros: quantidade de variáveis, capacidade e interesse e peso de cada item

print(f'O caminho inserido é: {caminho}')
arquivoTestes = open(caminho, 'rt')
contador = -1
nx = 0
itens = list()

for linha in arquivoTestes:
    if contador == -1:
        nx = int(linha)
        itens = list()
    else:
        if contador == 0:
            capacidade = float(linha)
            if capacidade.is_integer():
                capacidade = int(capacidade)
        else:
            dado = linha.split(' ')
            dado[1] = int(dado[1].replace('\n', ''))
            dado[0] = int(dado[0])
            itens.append(dado) #Adicionando um item [interesse, peso]
    contador += 1      
    if len(itens) == nx:
        print(f'Lista: {itens}')
        print(f'Capacidade: {capacidade}')
        solucionaProblemaMochila(itens, capacidade, saida)
        contador = -1

arquivoTestes.close()
