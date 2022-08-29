from pydub import AudioSegment
import math
import os
import ffmpeg

class SplitWavAudioMubin():
    def __init__(self, folder, filename,output_folder):
        self.folder = folder
        self.filename = filename
        #self.filepath = folder + "\\" + filename
        self.output_folder=output_folder
        self.filepath = os.path.join(folder, filename)
        
        #self.audio = AudioSegment.from_wav(self.filepath)
        try:
            self.audio = AudioSegment.from_file(self.filepath,"mp4")
        except:
            print("No such file exists as : ",self.filepath)
    
    def get_duration(self):
        return self.audio.duration_seconds
    
    def single_split(self, from_min, to_min, split_filename):
        #t1 = from_min * 60 * 1000
        #t2 = to_min * 60 * 1000
        t1=from_min* 1000
        t2=to_min* 1000
        split_audio = self.audio[t1:t2]
        output= os.path.join(self.output_folder, split_filename)
        split_audio.export(output, format="wav")
        
    def multiple_split(self, min_per_split):

        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)
        #total_mins = math.ceil(self.get_duration() / 60)
        

        total_seconds=self.get_duration()
        print("Length of the video is :",total_seconds)
        j=1
        
        for i in range(0,int(total_seconds)-min_per_split, min_per_split):
            #split_fn = str(i) + '_' + self.filename
            split_fn=f"audio{j}.wav"
            j+=1
            self.single_split(i, i+min_per_split, split_fn)
            print(split_fn + ' Done')
            #if i == total_seconds - min_per_split:
        print('All splited successfully')

if __name__=="__main__":
    sp=SplitWavAudioMubin("main_audio","got.mp4","audio_split")
    sp.multiple_split(20)
