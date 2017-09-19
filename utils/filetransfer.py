#!/usr/bin/env python3

import sys
import socket
import time
import subprocess



RSYNC_PASSWORD = "Aileron24"
# UPLOADADDR = "rsync@rsync.rrp.local"
UPLOADADDR = "rsync@rsync.racereplay.co"
hostname = socket.gethostname()

# vid_output_file=$HOSTNAME-vidtest-$(date +%s)


def transfer_video(video_fn):
    subprocess.call(["rsync ", "-avz ", "-R ",
                     "--progress ",
                     "--password-file=./password",
                     "--remove-source-files",
                     "*.mp4",
                     "{0}::rrp/{1}/" .format(UPLOADADDR, hostname),
                     "{filename}.mp4" .format(filename=video_fn)])
    return


def transfer_image():
    subprocess.call(["rsync", "-avz", "-R", "--remove-source-files",
                     "--progress" "*.jpg",
                     "$UPLOADADDR::rrp/$HOSTNAME/",
                     "{filename}.jpg" .format(filename=video_fn)])
    return


def transfer_log():
    return


def transfer_file():
    return

transfer_video(testfile)
