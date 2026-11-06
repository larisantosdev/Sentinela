
# 🛡️ Sentinela


## 💡 Origem e inspiração

O Sentinela surgiu a partir de uma dinâmica em grupo que abordava um problema relacionado à segurança de redes. Durante a atividade, foi discutida a possibilidade de desenvolver uma solução preventiva capaz de identificar redes Wi-Fi potencialmente suspeitas.

A ideia despertou meu interesse em transformar a proposta em uma aplicação real, colocando em prática meus conhecimentos de programação, lógica e análise de dados.

O projeto também representa uma oportunidade de explorar como a coleta e a interpretação de dados podem contribuir para a identificação de padrões, avaliação de riscos e, futuramente, aplicações de análise preditiva.


**Sistema de identificação e análise de redes Wi-Fi potencialmente suspeitas.**

O Sentinela é um projeto desenvolvido em Python com o objetivo de monitorar redes Wi-Fi próximas, coletar informações sobre os pontos de acesso e identificar possíveis comportamentos suspeitos.

A proposta é desenvolver uma ferramenta que auxilie equipes de infraestrutura na identificação de redes desconhecidas ou que apresentem características potencialmente perigosas.

> O sistema tem caráter preventivo e investigativo. A identificação de um indicador suspeito não significa, necessariamente, que uma rede seja maliciosa.

---


---

## 🧠 Lógica de análise e árvore de decisão

O Sentinela utiliza uma lógica de análise baseada em múltiplos critérios para identificar possíveis redes Wi-Fi que tentam se passar por redes oficiais.

O processo começa pela comparação do SSID da rede detectada com os nomes das redes oficiais cadastradas.

A partir dessa comparação, o sistema segue diferentes caminhos:

1. **SSID sem similaridade significativa:** a rede é classificada como desconhecida e recebe uma pontuação inicial de baixo risco, sem necessidade de realizar as demais verificações.
2. **SSID semelhante ao de uma rede oficial:** o sistema inicia uma investigação mais detalhada das características técnicas.
3. **Verificação dos pontos de acesso:** são analisados BSSID, criptografia, autenticação e canal, buscando identificar divergências em relação ao cadastro oficial.
4. **Identificação de divergências:** possíveis inconsistências são registradas e podem gerar alertas para investigação.
5. **Compatibilidade com o cadastro:** quando todas as características são compatíveis com uma mesma rede oficial, ela pode ser reconhecida como legítima.

A lógica de análise está representada na árvore de decisão abaixo:

<p align="center">
  <img src="docs/arvore-decisao.png" alt="Árvore de decisão do Sentinela" width="750">
</p>

*A árvore representa a lógica de classificação proposta para o sistema e poderá ser atualizada conforme o desenvolvimento for avançando.*

---


## 🎯 Objetivos

- Detectar redes Wi-Fi próximas ao dispositivo.
- Coletar informações sobre SSID, BSSID, autenticação, criptografia e canal.
- Identificar redes conhecidas e desconhecidas.
- Analisar possíveis indicadores de comportamento suspeito.
- Classificar o nível de suspeita das redes identificadas.
- Desenvolver um mecanismo de alerta para a equipe de infraestrutura.

---

## ⚙️ Tecnologias utilizadas

- **Python:** linguagem principal do projeto.
- **Subprocess:** execução de comandos do sistema operacional.
- **Netsh:** ferramenta nativa do Windows utilizada para consultar redes Wi-Fi próximas.

---

## 📡 Informações coletadas

O sistema utiliza o comando:

```powershell
netsh wlan show networks mode=bssid
```

As informações extraídas são:

| Informação | Descrição |
|---|---|
| SSID | Nome da rede Wi-Fi. |
| BSSID | Endereço MAC do ponto de acesso. |
| Autenticação | Método de autenticação utilizado. |
| Criptografia | Tipo de criptografia informado. |
| Canal | Canal de operação do ponto de acesso. |

O projeto organiza os dados em listas e dicionários, agrupando os pontos de acesso de acordo com suas respectivas redes.

---

## 🧩 Etapas de desenvolvimento

O desenvolvimento está dividido em cinco etapas:

- [x] **1. Coleta de dados:** obtenção das redes Wi-Fi próximas utilizando o Netsh.
- [ ] **2. Extração e organização:** estruturação e tratamento das informações coletadas.
- [ ] **3. Análise de indicadores:** identificação de características potencialmente suspeitas.
- [ ] **4. Classificação de risco:** atribuição de pontuações e níveis de suspeita.
- [ ] **5. Sistema de alertas:** desenvolvimento de notificações para a equipe de infraestrutura.

*As etapas serão atualizadas conforme a implementação do projeto avançar.*

---

## 🔍 Indicadores que serão investigados

Entre os comportamentos que poderão ser analisados nas próximas etapas:

- Redes com nomes semelhantes aos de redes oficiais.
- Pontos de acesso desconhecidos.
- Múltiplos BSSIDs associados a um mesmo SSID.
- Configurações de autenticação e criptografia potencialmente inseguras.
- Alterações nas características observadas durante diferentes varreduras.

A análise será baseada em múltiplos indicadores, evitando classificar uma rede como maliciosa com base em apenas uma característica isolada.

---

## 💻 Como executar

### Pré-requisitos

- Windows 10 ou superior.
- Python 3 instalado.
- Adaptador Wi-Fi habilitado.


### Execução

Clone o repositório:

```bash
git clone https://github.com/larisantosdev/Sentinela.git
```

Entre na pasta:

```bash
cd Sentinel
```

Execute o programa:

```bash
python main.py
```

*O nome do arquivo de execução poderá variar conforme a organização final do projeto.*

---

## 📌 Status do projeto

<kbd>Em desenvolvimento</kbd>

Atualmente, o projeto está na fase inicial de coleta e organização das informações das redes Wi-Fi detectadas.

As próximas implementações serão voltadas à análise dos dados coletados e à criação de mecanismos de identificação de possíveis ameaças.

---


## 👩‍💻 Autora

**Larissa Santos**

Estudante de Ciência da Computação na UFRRJ.

Tenho interesse em Inteligência Artificial, Ciência de Dados e Análise Preditiva, especialmente no desenvolvimento de soluções que utilizem dados para identificar padrões, antecipar possíveis problemas e apoiar a tomada de decisões.

GitHub: [@larisantosdev](https://github.com/larisantosdev)
