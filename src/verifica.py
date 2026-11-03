from difflib import SequenceMatcher
import json

def carregar_redes_oficiais():
    with open("../data/redes_oficiais.json", "r", encoding="utf-8") as arquivo:
        redes = json.load(arquivo)
    return redes

redes_oficiais = carregar_redes_oficiais()

print("AQUI \n")
print(redes_oficiais) # é uma lista de dicionarios

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
    return "diferente"




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

    for ponto in rede["Pontos de acesso"]:
        for indice, info in ponto.items():
            print(f"{indice}: {info}")
            bssid_rede_encontrada = info["BSSID"]

            for rede_oficial in redes_oficiais:
                for oficial in rede_oficial["Pontos de acesso"]:
                    for valor in oficial.values(): # valor é um dicionario com BSSID e Canal
                        bssid_oficial_atual = valor["BSSID"]
                        if bssid_oficial_atual == bssid_rede_encontrada:
                            return "igual"
    return "diferente"


'''

def verificar_criptografia(rede):
       
           
           for rede_oficial in redes_oficiais:
               crip_oficial = rede_oficial["Criptografia"]
               crip_rede = c["Criptografia"]
           
           
    
       '''








def verificar_rede_suspeita(rede_wifi): # rede wifi é a lista de redes Wi-Fi obtida pelo get_wifi_networks(), lista de dicionarios

    cont = 0
    # suspeitas, desconhecidas ou possivelmente legítimas
    for rede in rede_wifi:
        
        if verificar_nome_similar(rede["SSID"]) == "suspeito":
            cont = 10;
            
            if verificar_bssid_similar(rede) == "diferente":
                # alto risco
                cont = cont + 10
                #if verificar_criptografia(rede) == "suspeito":
               #     cont = cont + 10

           # else: 
                # "baixo risco - possivel rede oficial"
               # if verificar_criptografia(rede) == "igual"

        elif verificar_nome_similar(rede["SSID"]) == "diferente":
            return "não suspeito"
