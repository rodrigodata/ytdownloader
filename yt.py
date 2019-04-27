#!/usr/bin/env python3
from pytube import YouTube
import os

# Este script funciona tanto na versao python 2.x quanto 3.x
#retorna o local de download padrao do sistema
def caminho_arquivo():
	home = os.path.expanduser('~')
	local_download = os.path.join(home, 'Downloads')
	return local_download

def inicia_download_audio():
	youtube_link = input("[AUDIO] Por favor, informe a URL do video (YouTube): ")
	print('Verificando URL..')
	print(youtube_link)
	try:
			audio = YouTube(youtube_link)
	except:
			print('[ERRO] Por favor, verifique sua conexao ou a URL informada.')
			a = inicia_download_audio()

	configuracao_audio = audio.streams.filter(only_audio=True).first()
	titulo_video = audio.title
	configuracao_audio.download(caminho_arquivo())

inicia = inicia_download_audio()