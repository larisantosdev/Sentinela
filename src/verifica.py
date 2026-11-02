from difflib import SequenceMatcher
import json

def carregar_redes_oficiais():
    with open("../data/redes_oficiais.json", "r", encoding="utf-8") as arquivo:
        redes = json.load(arquivo)
    return redes

redes_oficiais = carregar_redes_oficiais()

# FUNÇÃO QUE VERIFICA A SIMILARIDADE DO NOME DA REDE (SSID) COM AS REDES OFICIAIS


def verificar_nome_similar(nome_rede): # nome_rede é o SSID da rede Wi-Fi

    for rede_oficial in redes_oficiais:
        ssid_oficial = rede_oficial["SSID"]
        similaridade = SequenceMatcher(None,
                                       nome_rede.lower(),
                                       ssid_oficial.lower()).ratio()
        if similaridade > 0.7 :
            print(f"A rede '{nome_rede}' é suspeita")
            return "suspeito"
    print(f"A rede '{nome_rede}' é desconhecida.")
    return True




# PONTOS DE ACESSO INFORMAÇÕES
quantidade = 0

"""

for rede in redes_oficiais:
    for ponto in rede["Pontos de acesso"]:

        quantidade = quantidade + len(ponto.keys())

        for indice, info in ponto.items():
            print(f"SSID: {rede['SSID']}")
            print(f"  {indice}: {info}")

print(f"Quantidade de chaves: {quantidade}")

"""

# FUNÇÃO BSSID SIMILARIDADE
       
def verificar_bssid_similar(rede): # redes detectadas

    for r in rede:
        for ponto in r["Pontos de acesso"]:
            for indice, info in ponto.items():
                print(f"{indice}: {info}")
                bssid_rede_encontrada = info
                quantidade = quantidade + len(ponto.keys())

                for rede_oficial in redes_oficiais:
                    for oficial in rede_oficial["Pontos de acesso"]:
                        for valor in oficial.items():
                            bssid_oficial_atual = valor
                            if bssid_oficial_atual == bssid_rede_encontrada:
                                return True
                            else: 
                                return "suspeito"

def verificar_criptografia(rede):
    rede 
    
       
# preciso de um contador que vai contar a quantidade de chaves de um dicionario antes de adicionar seus valores 


# construindo um
# preciso de um contador para df









def verificar_rede_suspeita(rede_wifi): # rede wifi é a lista de redes Wi-Fi obtida pelo get_wifi_networks()
    for rede in rede_wifi:
        
        if verificar_nome_similar(rede["SSID"]) == "suspeito":
            
            if verificar_bssid_similar(rede) == "suspeito":
                # alto risco
                if verificar_criptografia(rede) == ""
            else: 
                # "baixo risco"
                if verificar_criptografia(rede) == "suspeito"
        else:
            return "não suspeito"
