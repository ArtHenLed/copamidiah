# main.py

# Estes são os dados que vamos substituir no HTML. 
# Numa próxima etapa, o Python vai buscar isto à internet sozinho.
dados_jogos = {
    "{{BANDEIRA_CASA_1}}": "https://flagcdn.com/w160/qa.png",
    "{{SIGLA_CASA_1}}": "CAT",
    "{{PLACAR_CASA_1}}": "0",
    "{{PLACAR_FORA_1}}": "2",
    "{{SIGLA_FORA_1}}": "HOL",
    "{{BANDEIRA_FORA_1}}": "https://flagcdn.com/w160/nl.png",

    "{{BANDEIRA_CASA_2}}": "https://flagcdn.com/w160/sn.png",
    "{{SIGLA_CASA_2}}": "SEN",
    "{{PLACAR_CASA_2}}": "1",
    "{{PLACAR_FORA_2}}": "2",
    "{{SIGLA_FORA_2}}": "EQU",
    "{{BANDEIRA_FORA_2}}": "https://flagcdn.com/w160/ec.png",

    "{{BANDEIRA_CASA_3}}": "https://flagcdn.com/w160/nl.png",
    "{{SIGLA_CASA_3}}": "HOL",
    "{{DATA_JOGO}}": "HOJE",
    "{{HORA_JOGO}}": "16:00",
    "{{SIGLA_FORA_3}}": "ARG",
    "{{BANDEIRA_FORA_3}}": "https://flagcdn.com/w160/ar.png"
}

# 1. Abre o arquivo molde que você criou
with open("template.html", "r", encoding="utf-8") as arquivo_molde:
    html = arquivo_molde.read()

# 2. Substitui as chaves pelos dados reais
for etiqueta, valor in dados_jogos.items():
    html = html.replace(etiqueta, valor)

# 3. Salva o resultado final num novo arquivo chamado index.html
with open("index.html", "w", encoding="utf-8") as arquivo_final:
    arquivo_final.write(html)

print("Painel atualizado com sucesso!")
