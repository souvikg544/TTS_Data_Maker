from pytube import YouTube
import os
import argparse

parser = argparse.ArgumentParser(description='Add the following arguments')
parser.add_argument("--video_link", help="Prints the supplied argument.", default="None")
parser.add_argument("--speaker_name", help="Prints the supplied argument.", default="None")
args = parser.parse_args()
link=args.video_link.strip()
speaker=args.speaker_name.strip()


if not os.path.exists("main_audio"):
    os.makedirs("main_audio")
try:
    yt=YouTube(link)
    t=yt.streams.filter(only_audio=True)
    print(t)
    output=t[0].download(output_path="main_audio",filename=f"{speaker}.mp4")
    print(f"Audio saved to {output}")
except Exception as exception:
    print(f"Failed with the following exception : {exception.__class__.__name__ }")
