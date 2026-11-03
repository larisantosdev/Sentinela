from difflib import SequenceMatcher
import json

def carregar_redes_oficiais():
    with open("../data/redes_oficiais.json", "r", encoding="utf-8") as arquivo:
        redes = json.load(arquivo)
    return redes

redes_oficiais = carregar_redes_oficiais()

#print("AQUI \n")
#print(redes_oficiais) # é uma lista de dicionarios

# FUNÇÃO QUE VERIFICA A SIMILARIDADE DO NOME DA REDE (SSID) COM AS REDES OFICIAIS


def verificar_nome_similar(nome_rede): # nome_rede é o SSID da rede Wi-Fi

    for rede_oficial in redes_oficiais:
        ssid_oficial = rede_oficial["SSID"]
        similaridade = SequenceMatcher(None,
                                       nome_rede.lower(),
                                       ssid_oficial.lower()).ratio()
        if similaridade > 0.7 :
            print(f"A rede '{nome_rede}' é suspeita ou oficial")
            return "suspeito"
    print(f"A rede '{nome_rede}' apresenta BAIXO RISCO.")
    return "diferente"




# FUNÇÃO BSSID SIMILARIDADE
       
def verificar_bssid_similar(rede): # redes detectadas 

    encontrou_igualdade = False

    for ponto in rede["Pontos de acesso"]:
        for indice, info in ponto.items():
            #print(f"{indice}: {info}")
            bssid_rede_encontrada = info["BSSID"]

            for rede_oficial in redes_oficiais: # pego o primeiro dicionario e passo pra rede_oficial
                for oficial in rede_oficial["Pontos de acesso"]: # pego a lista de dicionarios do campo pontos de acesso e passo pra oficial {BSSID, CANAL} {BSSID, CANAL} {BSSID, CANAL}
                    for valor in oficial.values(): # valor é um dicionario com BSSID e Canal -> {BSSID, CANAL} 
                        bssid_oficial_atual = valor["BSSID"]
                        if bssid_oficial_atual == bssid_rede_encontrada:
                            encontrou_igualdade = True

    if encontrou_igualdade:
        return "igual"
    else:
        return "diferente"


# FUNÇÃO VERIFICA CANAL


def verificar_canal(rede):

    encontrou_igualdade = False

    ponto = rede["Pontos de acesso"] # ponto é uma lista
    for acesso in ponto: # acesso é cada dicionário dentro da lista ponto (2 dicionarios)
        for valor in acesso.values(): # valor é um dicionário interno que contém BSSID e Canal
            canal_rede_wifi = valor["Canal"] # canal recebe o número do canal daquele ponto de acesso

            for rede_oficial in redes_oficiais:
                for oficial in rede_oficial["Pontos de acesso"]:
                    for dados in oficial.values(): # acesso é cada dicionário dentro da lista
                        canal_oficial = dados["Canal"] # canal_oficial recebe o número do canal do ponto de acesso oficial
                        if canal_oficial == canal_rede_wifi:
                            encontrou_igualdade = True

    if encontrou_igualdade:
        return "igual"
    else:
        return "diferente"







# FUNÇÃO VERIFICA CRIPTOGRAFIA

def verificar_criptografia(rede):

    crip_rede_wifi = rede["Criptografia"]
    encontrou_igualdade = False

    for rede_oficial in redes_oficiais:
        crip_oficial = rede_oficial["Criptografia"]
        if crip_oficial == crip_rede_wifi:
            encontrou_igualdade = True

    if encontrou_igualdade:
        return "igual"
    else:
        return "diferente"

           
           
# FUNÇÃO VERIFICA AUTENTICAÇÃO

def verificar_autenticacao(rede):
    aut = rede["Autenticacao"]
    encontrou_igualdade = False

    for rede_oficial in redes_oficiais: # são 2
        aut_rede_oficial = rede_oficial["Autenticacao"]
        if aut_rede_oficial == aut:
            encontrou_igualdade = True

    if encontrou_igualdade:
        return "igual"
    else:
        return "diferente"


            





# FUNÇÃO PRINCIPAL/GERAL


def verificar_rede_suspeita(rede_wifi): # rede wifi é a lista de redes Wi-Fi obtida pelo get_wifi_networks(), lista de dicionarios

    
    # suspeitas, desconhecidas ou possivelmente legítimas
    for rede in rede_wifi:
        cont = 0

        # SSID

        resultado_nome = verificar_nome_similar(rede["SSID"])

        match resultado_nome:
            case "suspeito":
                cont += 10;
            case "diferente":
                cont = 10

                print(f"\nRede analisada: {rede['SSID']}")
                print(f"Pontuação de risco: {cont} \n")
                print(f"CLASSIFICAÇÃO: RISCO BAIXO")
                print("-" * 45)
                # return "rede não é suspeita"

                continue

        # BSSID

        resultado_bssid = verificar_bssid_similar(rede)

        match resultado_bssid:
            case "diferente":
                cont += 10
            case "igual":
                cont += 0
    
        # CRIPTOGRAFIA

        resultado_criptografia = verificar_criptografia(rede)

        match resultado_criptografia:
            case "diferente":
                cont += 10
            case "igual":
                cont += 0


        # AUTENTICAÇÃO

        resultado_autenticacao = verificar_autenticacao(rede)

        match resultado_autenticacao:
            case "diferente":
                cont += 10
            case "igual":
                cont += 0


        # CANAL

        resultado_canal = verificar_canal(rede)

        match resultado_canal:
            case "diferente":
                cont += 10
            case "igual":
                cont += 0
                    
        print(f"\nRede analisada: {rede['SSID']}")
        print(f"Pontuação de risco: {cont} \n")
        if cont >= 40:
            print(f"CLASSIFICAÇÃO: RISCO CRÍTICO")
        elif cont >= 30:
            print(f"CLASSIFICAÇÃO: RISCO MODERADO")
        elif cont <= 20:
            print(f"CLASSIFICAÇÃO: RISCO BAIXO")
        print("-" * 45)


# FAZENDO UM TESTE AQUI

with open("../data/redes_experimento.json", "r", encoding="utf-8") as arq:
    wifi = json.load(arq)

verificar_rede_suspeita(wifi)




















        