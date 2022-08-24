# Text To Speech Dataset Maker

### This repository offers a way to make personalized dataset for model creation using the famous TTS text to speech github repo.

Link to TTS repository - https://github.com/coqui-ai/TTS

Link to TTS pypi - https://pypi.org/project/TTS/#description

## Steps to build your Dataset

### 1. Clone the repository
```
git clone https://github.com/souvikg544/TTS_Data_Maker.git
```
```
cd TTS_Data_Maker
pip install -r requirements.txt
```

### 2. Download a audio
To download a audio from YouTube cd into the TTS_Data_Maker directory and use audio_download.py
Below is a sample command for downloading a GOT video :) .A mp4 file will be downloaded in the main_audio directory.
```
python audio_download.py --video_link https://www.youtube.com/watch?v=-B8IkMj6d1E --speaker_name got

```


### 3.Split the audio into small parts.
To split the downloaded audio into smaller parts use the extract_segment.py file of the repository.

```
from extract_segment import SplitWavAudioMubin
download_folder="main_audio"
video_filename="got.mp4"
output_folder="audio_split"
duration=20

spliter=SplitWavAudioMubin(download_folder,video_filename,output_folder)
spliter.multiple_split(duration)

```
## Note: 
pydub module uses ffmpeg to process wav files. Hence if
running on a local machine it requires ffmpeg to be downloaded and the bin folder must be added to path.

Link - https://ffmpeg.org/download.html

Download from *Get packages & executable files* section on the above link.


### Audio to speech 

For Audio to speech we will choose over many text to speech engine including those of Google and IBM.


### Final Dataset

