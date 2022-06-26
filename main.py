import requests
import json
import telebot
from secrets import api_Key_tempo, api_telegram

bot = telebot.TeleBot(
    api_telegram
)

@bot.message_handler(commands=["mandarabraco"])
def verprevisao(mensagem):
    bot.send_message(mensagem.chat.id,
                     'O Chico agradece o abraço. Tenha um bom dia!')
    
@bot.message_handler(commands=["verprevisaolavras"])
def verprevisao(mensagem):
    url = f'https://api.hgbrasil.com/weather?key={api_Key_tempo}&city_name=Lavras,MG'
    response = requests.get(url=url)
    dados_consulta = response.json()
    texto_base = ''
    for i in range(len(dados_consulta["results"]["forecast"])):
        texto_base = texto_base + '>> Dia: '+ str(dados_consulta["results"]["forecast"][i]['date'])+ ' - Dia da semana: '+ dados_consulta["results"]["forecast"][i]['weekday'] + '\n'
        texto_base = texto_base + ('Temperatura máxima: '+str(dados_consulta["results"]["forecast"][i]['max']) + ' °C \n'+
                                     'Temperatura mínima: '+str(dados_consulta["results"]["forecast"][i]['min'] )+' °C\n')
        texto_base = texto_base + ' Condição do tempo: '+ dados_consulta["results"]["forecast"][i]['description']+'\n\n'

    bot.send_message(mensagem.chat.id, 
                     f"""
-- Seguem as informações solicitadas:

Dia de referência: {dados_consulta['results']['date']}  
Dia da semana: {dados_consulta["results"]["forecast"][0]["weekday"]} 
Horário de referência: {dados_consulta['results']['time']}

Cidade referência: { dados_consulta['results']['city']}
Temperatura atual: { dados_consulta['results']['temp']} °C
Condição atual: { dados_consulta['results']['description']}
Humidade relativa do ar: { dados_consulta['results']['humidity']}
Velocidade do vento: { dados_consulta['results']['wind_speedy']}

-- Previsão para os próximos dias -- 
                     
{texto_base}
                    """)
@bot.message_handler(commands=["verprevisaosalinas"])
def verprevisao(mensagem):
    url = f'https://api.hgbrasil.com/weather?key={api_Key_tempo}&city_name=Salinas,MG'
    response = requests.get(url=url)
    dados_consulta = response.json()
    texto_base = ''
    for i in range(len(dados_consulta["results"]["forecast"])):
        texto_base = texto_base + '>> Dia: '+ str(dados_consulta["results"]["forecast"][i]['date'])+ ' - Dia da semana: '+ dados_consulta["results"]["forecast"][i]['weekday'] + '\n'
        texto_base = texto_base + ('Temperatura máxima: '+str(dados_consulta["results"]["forecast"][i]['max']) + ' °C \n'+
                                     'Temperatura mínima: '+str(dados_consulta["results"]["forecast"][i]['min'] )+' °C\n')
        texto_base = texto_base + ' Condição do tempo: '+ dados_consulta["results"]["forecast"][i]['description']+'\n\n'

    bot.send_message(mensagem.chat.id, 
                     f"""
-- Seguem as informações solicitadas:

Dia de referência: {dados_consulta['results']['date']}  
Dia da semana: {dados_consulta["results"]["forecast"][0]["weekday"]} 
Horário de referência: {dados_consulta['results']['time']}

Cidade referência: { dados_consulta['results']['city']}
Temperatura atual: { dados_consulta['results']['temp']} °C
Condição atual: { dados_consulta['results']['description']}
Humidade relativa do ar: { dados_consulta['results']['humidity']}
Velocidade do vento: { dados_consulta['results']['wind_speedy']}

-- Previsão para os próximos dias -- 
                     
{texto_base}
                    """)
def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
Olá, seja bem-vindo(a).

Eu sou um bot que retorna a previsão de tempo nos municípios de Salinas/MG e Lavras/MG.

Fui criado apenas com a finalidade de aprendizado do meu criador.

Clique em uma das opções abaixo:

/verprevisaolavras - Ver previsão do tempo em Lavras/MG
/verprevisaosalinas - Ver previsão do tempo em Salinas/MG
/mandarabraco - Mandar um abraço para o criador (Chico).
    
    """
    bot.reply_to(mensagem,
                 texto)

bot.polling()