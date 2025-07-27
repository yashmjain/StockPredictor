
import yt_dlp

def download_video(url):
    ydl_opts = {
        'format': 'bestzScZXczX',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == '__main__':
    download_video('https://www.youtube.com/watch?v=fAFBdvdx494')
