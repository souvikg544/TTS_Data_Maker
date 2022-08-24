from extract_segment import SplitWavAudioMubin
download_folder="main_audio"
video_filename="got.mp4"
output_folder="audio_split"
duration=20

spliter=SplitWavAudioMubin(download_folder,video_filename,output_folder)
spliter.multiple_split(duration)