from os import listdir
from os.path import isfile, join, abspath, basename, splitext
from configs import is_single_image, video_fps, output_folder_path
from moviepy.editor import *


def create_videos(music_folder_path, images_folder_path):
    audio_to_image_paths = get_image_to_audio_paths(music_folder_path, images_folder_path)

    for audio_path, image_path in audio_to_image_paths:
        create_video(audio_path, image_path)


def get_image_to_audio_paths(music_folder_path, images_folder_path):
    audio_file_paths = get_folder_file_paths(music_folder_path)
    images_file_paths = get_folder_file_paths(images_folder_path)

    if is_single_image:
        images_file_paths = [images_file_paths[0] for _ in range(len(audio_file_paths))]

    return zip(sorted(audio_file_paths), sorted(images_file_paths))


def get_folder_file_paths(folder_path):
    return [join(folder_path, file) for file in listdir(folder_path) if
            isfile(join(folder_path, file))]


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
