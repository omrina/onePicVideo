from os.path import isdir, isfile
from os import listdir, mkdir
from video_clip_creator import create_videos
from configs import music_folder_path, image_path, output_folder_path


def ensure_file_system_nodes():
    if not isdir(music_folder_path):
        print("cant find your music folder: %s" % music_folder_path)
        exit(1)

    if not isfile(image_path):
        print("cant find your image file: %s" % image_path)
        exit(1)

    if not listdir(music_folder_path):
        print("your music folder is empty: %s" % music_folder_path)
        exit(1)

    if not isdir(output_folder_path):
        mkdir(output_folder_path)


ensure_file_system_nodes()
create_videos(music_folder_path, image_path)
