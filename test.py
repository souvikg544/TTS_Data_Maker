from extract_segment import SplitWavAudioMubin
from extract_text import text_extraction

download_folder="main_audio"
video_filename="got.mp4"
output_folder="audio_split"
duration=30

spliter=SplitWavAudioMubin(download_folder,video_filename,output_folder)
spliter.multiple_split(duration)




path_to_audio_split="audio_split"
path_to_output_folder=None # Implies will write a text file to the same folder
output_folder_name="metadata.txt"



et=et=text_extraction(path_to_audio_split)
et.extract(path_to_output_folder,output_folder_name)