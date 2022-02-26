from os.path import isdir
from os import listdir, mkdir
from video_clip_creator import create_videos
from configs import music_folder_path, image_folder, output_folder_path, is_single_image


def ensure_file_system_nodes():
    if not isdir(music_folder_path):
        print("cant find your music folder: %s" % music_folder_path)
        exit(1)

    if not isdir(image_folder) or len(listdir(image_folder)) == 0:
        print("need image folder at: %s , and at least 1 picture" % image_folder)
        exit(1)

    if not listdir(music_folder_path):
        print("your music folder is empty: %s" % music_folder_path)
        exit(1)

    if not is_single_image and len(listdir(music_folder_path)) != len(listdir(image_folder)):
        print("in multiple image mode you need the same number of images and mp3 files")
        exit(1)

    if not isdir(output_folder_path):
        mkdir(output_folder_path)


ensure_file_system_nodes()
print("starting the creation")
create_videos(music_folder_path, image_folder)
print("finished successfully")
