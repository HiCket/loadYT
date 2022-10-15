import tldextract
from pytube import YouTube


def Download_audio(video_list):
    for url in video_list:
        youtube = YouTube(url.strip())
        youtube.streams.filter(only_audio=True, subtype='webm', abr='160kbps').first().download()
        print(f'The video - {youtube.title} - was downloaded.')

def Download_video(video_list):
    for url in video_list:
        youtube = YouTube(url.strip())
        youtube.streams.get_highest_resolution().download()
        print(f'The video - {youtube.title} - was downloaded.') 


video_list = []

run = True

while run == True:
        link = str(input("Enter a YouTube URL or press D/Da to download the video(s)/audio(s): "))
        domain_name = tldextract.extract(link).domain
        if link.lower() == 'd':
            Download_video(video_list)
            run = False
        elif link.lower() == 'da':
            Download_audio(video_list)
            run = False
        elif domain_name == 'youtube':
            video_list.append(link)
        else:
            print("Invalid youtube URL.")