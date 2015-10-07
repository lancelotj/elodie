#!/usr/bin/env python

import os
import shutil
import sys

from elodie import arguments
from elodie.media.video import Video
from elodie.filesystem import FileSystem

def main(argv):
    
    args = arguments.parse(argv, None, ['source=','destination='], './import.py --source=<source directory> -destination=<destination directory>')

    source = args['source']
    destination = args['destination']

    filesystem = FileSystem()

    for video_file in filesystem.get_all_files(source, Video.get_valid_extensions()):
        video = Video(video_file)

        filesystem.set_date_from_path_video(video)

        metadata = video.get_metadata()

        directory_name = filesystem.get_folder_name_by_date(metadata['date_taken'])
        dest_directory = '%s/%s' % (destination, directory_name)
        # TODO remove the day prefix of the file that was there prior to the crawl
        file_name = filesystem.get_file_name_for_video(video)
        dest_path = '%s/%s' % (dest_directory, file_name)

        filesystem.create_directory(dest_directory)

        print '%s -> %s' % (video_file, dest_path)
        shutil.copy2(video_file, dest_path)

if __name__ == '__main__':
    main(sys.argv[1:])