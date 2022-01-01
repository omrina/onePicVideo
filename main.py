from moviepy.editor import *
from os import listdir
from os.path import isfile, join


def create_video_clip(image_clip, audio):
    image_clip.duration = audio.duration
    image_clip.audio = audio

    return image_clip


def create_video_name(name):
    return os.path.join(os.getcwd(), "final_videos", name[:-4] + ".mp4")


pic_path = r'./Pic.jpeg'
music_folder = os.path.join(os.getcwd(), 'music files')

audio_file_paths = [join(music_folder, f) for f in listdir(music_folder) if isfile(join(music_folder, f))]
clip = ImageClip(pic_path)

for audio_path in audio_file_paths:
    audio_name = os.path.basename(audio_path)
    audio_clip = AudioFileClip(audio_path)

    video_clip = create_video_clip(clip, audio_clip)
    video_clip.write_videofile(create_video_name(audio_name), fps=24)
