#!/usr/bin/env python
from pytube import YouTube
import os

def progress_Check(stream = None, chunk = None, file_handle = None, remaining = None):
	#retorna o percentual do arquivo baixado
	percent = (100*(tamanho_arquivo - remaining))/tamanho_arquivo
	print("{:00.0f}% baixado..".format(percent))

#retorna o local de download padrao do sistema
def caminho_arquivo():
	home = os.path.expanduser('~')
	local_download = os.path.join(home, 'Downloads')
	return local_download

def inicia_download_audio():
	youtube_link = input("[AUDIO] Por favor, informe a URL do video (YouTube): ")
	print('Verificando URL..')
	audio = YouTube(youtube_link, on_progress_callback=progress_Check)
	print('Vídeo localizando, processando..')
	configuracao_audio = audio.streams.filter(only_audio=True).first()
	global tamanho_arquivo
	tamanho_arquivo = configuracao_audio.filesize
	titulo_video = audio.title
	print(titulo_video)
	configuracao_audio.download(caminho_arquivo())
	print('Download concluido! Seu arquivo está salvo na pasta: {}'.format(caminho_arquivo()))

inicia_download_audio()