import subprocess 



def verificar_rede(rede_wifi): # rede_wifi é a lista de redes Wi-Fi obtida pelo get_wifi_networks()
    for rede in rede_wifi:
        if verificar_nome_similar(rede['SSID']) == "suspeito":
            print(f"A rede '{rede['SSID']}' é suspeita")
        
        
        
        else:
            print(f"A rede '{rede['SSID']}' não é suspeita.")








def main():
    print("\n")

    dados_redes = get_wifi_networks()

    if dados_redes:
        # print(dados_redes)  # Exibe as redes Wi-Fi encontradas no terminal
        for rede in dados_redes:
            verificar_nome_similar(rede['SSID'])

    else:
        print("Não foi possível obter as redes Wi-Fi.")

    
    


main()