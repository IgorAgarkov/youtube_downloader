from pytube import YouTube
def download(link):
    youtube_object = YouTube(link)
    youtube_object = youtube_object.streams.get_highest_resolution()
    try:
        youtube_object.download()
    except:
        print('Ошибка скачивания')
    print("Скачивание успешно завершено")
link = input("Ссылка на ролик Youtube: ")
download(link)