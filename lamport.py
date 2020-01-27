def atualizar_processo(numero_processo, processo, processos):
    if numero_processo in processos:
        processos[numero_processo] = processo


def verificar_processo(proc, processos):
    if proc in processos:
        return True
    else:
        return False

def verificar_tempo(processo, tempo_infor, processos):
    contador = 0
    for c in processos[processo]:
        contador +=1
        if tempo_infor == c:
            return True
            break
        if contador == len(processos[processo]):
            return False

def pegar_posicao_tempo(emissor, tempo_e, receptor, tempo_r, tempo, processos, comunicacoes):
    emissor_p = processos[emissor]
    receptor_p = processos[receptor]
    posicao_tempo = 0
    contadorPosi = 0
    posicaoTempoReceptor = 0
    contadorPosi2 = 0

    for c in emissor_p:
        contadorPosi += 1
        if c == tempo_e:
            posicao_tempo = contadorPosi - 1
    for y in receptor_p:
        contadorPosi2 += 1
        if y == tempo_r:
            posicaoTempoReceptor = contadorPosi2 -1
    tupla = (posicao_tempo, posicaoTempoReceptor)
    return   tupla

def fazer_comunicacoes(comunicacoes):
    contador = 0
    for c in comunicacoes:
        e = comunicacoes[c]
        p_emissor = e[1]
        p_receptor = e[2]
        comunicacao = e[0]
        emissor = processos[p_emissor]
        receptor = processos[p_receptor]
        if emissor[comunicacao[0]] <= receptor[comunicacao[1]]:
            contador += 1

            pass
        elif emissor[comunicacao[0]] > receptor[comunicacao[1]]:
            receptor[comunicacao[1]] = emissor[comunicacao[0]] + 1
            for u in range(len(receptor)):
                if u > (comunicacao[1]):
                    receptor[u] = receptor[u -1] + tempo[p_receptor]
            atualizar_processo(p_receptor, receptor, processos)
        if contador >= 1:
            print(f"          \033[1;36m Etapa {c} não ouve alteracoes!\033[m")
        else:
            print(f"          \033[1;34m Etapa {c} os tempos sofreu alteracoes\033[m")
        for y in processos:
            print(f"Processo {y} : " + str(processos[y]).strip('[]'))
        contador = 0
        del receptor

def intervalos_tempo(intervalo, lista, processos, tempo, chave):
    numero = intervalo
    lista.append(numero)
    while True:
        if len(lista) == tempo:
            break
        else:
            numero = numero + intervalo
            lista.append(numero)

    processos[chave] = lista
    del lista

def impressao(processos):
    for c in processos:
        print(f"Processo {c} : "+str(processos[c]).strip('[]'))

def todas_comunicacoes(comunicacoes):
    for c in comunicacoes:
        comunicao = comunicacoes[c]
        t = comunicao['tempos']
        print(f"Processo emissor {comunicao['emissor']} : tempo {t[0]} | Processo receptor {comunicao['receptor']} : tempo {t[1]}")

def espacoPrint():
    print("-"*65)



espacoPrint()
print("                      \033[1;36m Trabalho SD\033[m")
espacoPrint()
while True:
    comunicacao = {}
    emissor = 0
    tempo_e = 0
    receptor = 0
    tempo_r = 0
    processos = {}
    tempo = {}
    comunicacoes = {}
    chave = 0
    quantidade = int(input("Informe a quantidades de processos :"))
    espacoPrint()
    print("\033[1mA Quantidade de tempos informado a baixo vai comecar a partir do 0!\033[m")
    espacoPrint()
    quant_tempo = int(input("Informe a quantidade de tempo :"))
    espacoPrint()
    print("           \033[1;36m Intervalo de tempo de cada processo\033[m")
    for g in range(quantidade):
        lista = [0]
        intervalo = int(input(f"Informe o intervalo de tempo para o processo {g+1} :"))
        espacoPrint()
        chave += 1
        tempo[chave] = intervalo
        intervalos_tempo(intervalo, lista, processos,quant_tempo, chave)

    
    print("                     \033[1;36m Seus processos \033[m")
    impressao(processos)
    espacoPrint()
    contador_c = 0
    contador = 0
    op = ""
    print("               \033[1;36m Vamos para as comunicacoes agora!\033[m")
    while True:
        contador_c +=1
        if contador_c == 1:
            emissor = int(input("Informe o processo emissor :"))
            espacoPrint()
            if verificar_processo(emissor, processos) == True:
                tempo_e = int(input("Informe o tempo de envio :"))
                espacoPrint()
                if verificar_tempo(emissor, tempo_e, processos) == True:
                    receptor = int(input("Informe o processo receptor :"))
                    espacoPrint()
                    if verificar_processo(receptor, processos) == True:
                        tempo_r = int(input("Informe o tempo de chegada :"))
                        espacoPrint()
                        if verificar_tempo(receptor, tempo_r, processos) == True:
                            posicao = pegar_posicao_tempo(emissor, tempo_e, receptor, tempo_r, tempo, processos, comunicacoes)
                            contador +=1
                            comunicacoes[contador] = posicao, emissor, receptor
                            comunicacao[contador]= {"tempos":(tempo_e, tempo_r), "emissor":emissor, "receptor":receptor}
                            op = input("\033[1mDeseja fazer outra comunicacao(S/N) ?\033[m")
                            espacoPrint()
                            if op == "s":
                                contador_c = 0
                            elif op == "n":
                                break
                            else:
                                pass
                        else:
                            contador_c = 0
                            print("\033[1;31mNão existe! Ops, terá que recomeçar!\033[m")
                            espacoPrint()
                    else:
                        contador_c = 0
                        print("\033[1;31mNão existe! Ops, terá que recomeçar!\033[m")
                        espacoPrint()
                else:
                    contador_c = 0
                    print("\033[1;31mNão existe! Ops, terá que recomeçar!\033[m")
                    espacoPrint()
            else:
                contador_c = 0
                print("\033[1;31mNão existe! Ops, terá que recomeçar!\033[m")
                espacoPrint()
    print("                  \033[1;36mComunicaçãoes  solicitadas!\033[m")
    todas_comunicacoes(comunicacao)
    espacoPrint()
    fazer_comunicacoes(comunicacoes)
    espacoPrint()
    print("                  \033[1;36m Resultado final!\033[m")
    impressao(processos)
    espacoPrint()
