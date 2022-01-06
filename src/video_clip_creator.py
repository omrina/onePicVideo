from os import listdir
from os.path import isfile, join, abspath, basename, splitext
from configs import video_fps, output_folder_path
from moviepy.editor import *


def create_videos(music_folder_path, image_path):
    audio_file_paths = get_audio_file_paths(music_folder_path)

    for audio_path in audio_file_paths:
        create_video(audio_path, image_path)


def get_audio_file_paths(music_folder_path):
    return [join(music_folder_path, file) for file in listdir(music_folder_path) if
            isfile(join(music_folder_path, file))]


def create_video(audio_path, image_path):
    audio_name = basename(audio_path)

    video_clip = build_video_clip(audio_path, image_path)
    video_clip.write_videofile(create_video_name(audio_name), fps=video_fps)


def build_video_clip(audio_path, image_path):
    audio_clip = AudioFileClip(audio_path)
    image_clip = ImageClip(image_path)

    image_clip.duration = audio_clip.duration
    image_clip.audio = audio_clip

    return image_clip
    

def create_video_name(name):
    return abspath(join(output_folder_path, splitext(name)[0] + ".mp4"))
