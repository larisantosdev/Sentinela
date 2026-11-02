import subprocess

def get_wifi_networks():

    redes = []  # Lista para armazenar as redes Wi-Fi encontradas
    ssid_atual = None
    bssid_atual = None
    canal = None
    indice = None
    num_bssid = None
    ponto_de_acesso = None

    

    command = ["netsh", "wlan", "show", "networks", "mode=bssid"]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )









    if result.returncode != 0:
        print("Erro ao executar o comando:", result.stderr)
        return None

    dados = result.stdout

    # ATRIBUINDO VALORES AOS 5 ATRIBUTOS PRINCIPAIS DE CADA REDE ENCONTRADA
    # OS ATRIBUTOS SÃO: SSID, BSSID, CANAL, AUTENTICAÇÃO E CRIPTOGRAFIA

    for line in dados.splitlines(): # .splitlines() divide a string em uma lista de linhas
        line = line.strip() # .strip() remove espaços em branco no início e no final da linha

        if line.startswith("SSID"): # .startswith() verifica se a linha começa com "SSID"
            num = int(line.split()[1])
            indice = num - 1

            ssid_atual = line.split(":", 1)[1].strip()

            ponto_de_acesso = {}  # Dicionário para armazenar os dados do ponto de acesso atual           
            redes.append({"SSID": ssid_atual, 
                          "Pontos de acesso": [], 
                          "Criptografia": None, 
                          "Autenticacao": None})

            

        elif line.startswith("BSSID"):
            num_bssid = int(line.split()[1]) # numero do BSSID atual
            bssid_atual = line.split(":",1)[1].strip() # valor do BSSID atual
 
            ponto_de_acesso = { num_bssid: { "BSSID": bssid_atual,
                                             "Canal": None } }

            redes[indice]["Pontos de acesso"].append(ponto_de_acesso)

        elif line.startswith("Autenticação"):
           
            redes[indice]["Autenticacao"] = line.split(":", 1)[1].strip()

        elif line.startswith("Criptografia"):
            
            redes[indice]["Criptografia"] = line.split(":", 1)[1].strip()

        elif line.startswith("Canal"):
             
             canal = line.split(":", 1)[1].strip()
             ponto_de_acesso[num_bssid]["Canal"] = canal
        
        else:
            continue    
    
        
    return redes

# return dados
# (use return dados quando quiser ver as redes Wi-fi encontradas no terminal e return redes quando quiser ver as redes em formato de dicionário)