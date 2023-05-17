from pytube import YouTube

link = input('Enter your link: ')
yt = YouTube(link)

# print('Title: ', yt.title)
# print('Views: ', yt.views )

# Here you can change the resolution, for example: 'get_highes_resolution'
yd = yt.streams.get_lowest_resolution()
# Here you copy a path to where the video is going to download to
yd.download("D:\PythonProjects\pythonProject10")
