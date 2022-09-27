# Text To Speech Dataset Maker

![data_maker](https://user-images.githubusercontent.com/63863911/192467194-ef6cce26-1ece-44be-9fff-5cd65b043280.png)


### This repository offers a way to make personalized dataset for model creation using the famous TTS text to speech github repo.

Link to TTS repository - https://github.com/coqui-ai/TTS

Link to TTS in pypi - https://pypi.org/project/TTS/#description

## Steps to build your Dataset
If you have want to use an audio file of your own skip step 2 . If you want to use audio from a wide range of speakers available from youtube step 2 is for you.

### 1. Clone the repository
```
git clone https://github.com/souvikg544/TTS_Data_Maker.git
```
```
cd TTS_Data_Maker
pip install -r requirements.txt
```

### 2. Download a speech
To download an audio from YouTube video cd into the TTS_Data_Maker directory and use audio_download.py
Below is a sample command for downloading a GOT video :) .A mp4 file will be downloaded in the main_audio directory.
It is required to give the video_link and speaker/video name as arguments to the below python file.
```
python audio_download.py --video_link https://www.youtube.com/watch?v=-B8IkMj6d1E --speaker_name got

```


### 3.Split the audio into small parts.
To split the downloaded audio into smaller parts use the extract_segment.py file of the repository.

```
from extract_segment import SplitWavAudioMubin
download_folder="main_audio"                      #folder in which audio file is stored
video_filename="got.mp4"                          # Filename of the audio
output_folder="/content/sample_tts_dataset/wavs"  #Output folder that will have segments of audio 
duration=20                                       # Duration of each split in seconds

spliter=SplitWavAudioMubin(download_folder,video_filename,output_folder)
spliter.multiple_split(duration)

```

### Audio to speech 

For Audio to speech we will choose over many text to speech engine including those of Google and IBM. Run the below code snippet 
to extract text from the audio snippets.

```
from extract_text import text_extraction

path_to_audio_split="/content/sample_tts_dataset/wavs"  # As the name suggests use the same folder as output folder before
output_folder="/content/sample_tts_dataset"             # Output folder having the text file
output_file= "metadata.txt"                             # Name of the text file.

et=text_extraction(path_to_audio_split)
et.extract(output_folder,output_file)
```


### Final Dataset
The final dataset will have metadata.txt and audio_split folder having all the audio files like 1.wav , 2.wav , 3.wav and soon
metadata.txt file will look like this
```
metadata.txt-
audio1|Hey how are you
audio2|I hope you are fine
audio3|Lets meet at dinner
```
The wav folder containing all the audio files will look like this
```
wav
-audio1.wav
-audio2.wav
-audio3.wav
```
In the end, we should have the following folder structure:
```
/MyTTSDataset
 |
 | -> metadata.txt
 | -> /wavs
  | -> audio1.wav
  | -> audio2.wav
  | ...
```
## Implementation

- Implementing from github readmes is always a pain.
To make things easier,the entire process has been implemented in Google collab -
[![Collab for tts data maker](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1F2lxFNIHxvNcAhzSoxDl_W4nX5tnu6nr?usp=sharing)

- The dataset creation must be followed by creating a model using TTS. Details of the same can be found from this notebook -
[![Collab for TTS](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1F8mdG6Vm7kAigyLZhc37_vTQBnh7wgk2?usp=sharing)





## Note:
*Please ignore if running on collab or cloud.*

pydub module used extensively in this repository uses ffmpeg to process wav files. Hence if
running on a local machine it requires ffmpeg to be downloaded and the bin folder must be added to path.

Link - https://ffmpeg.org/download.html

Download from *Get packages & executable files* section on the above link.
