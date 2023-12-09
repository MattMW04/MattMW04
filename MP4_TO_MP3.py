from moviepy.editor import *

def convert(input_file_path, output_file):

    video = VideoFileClip(input_file_path)
    audio = video.audio
    audio.write_audiofile(output_file, codec='mp3')
    audio.close()
    video.close()


def convert_with_time(input_file_path, output_file, start_time, end_time= None):

    video = VideoFileClip(input_file_path)
    audio = video.audio.subclip(start_time, end_time)
    audio.write_audiofile(output_file, codec='mp3')
    audio.close()
    video.close()

mp4 = "videos/Monday left me broken cat (1).mp4"
mp3 = "videos/Monday.mp3"

mp5 = "videos/sweatshirt.mp4"
mp6 = "videos/sweatshirt.mp3"
start = 43


convert_with_time(mp5, mp6, start)
