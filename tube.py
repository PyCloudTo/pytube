
from pytube import YouTube

#URL do video que você deseja baixar
url = "DIGITE AQUI A URL DO VIDEO"

#Crie um objeto YouTube
yt = YouTube(url)

#Escolha a melhor qualidade disponivel
video_stream = yt.streams.get_highest_resolution()

#Baixar o video para o dirtorio atual
video_stream.download()

print("Download completo!")