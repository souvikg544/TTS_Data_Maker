import speech_recognition as sr
import os

#filename = "audio_split\\1.wav"

class text_extraction():

    def __init__(self,audio_Split_directory):
        self.directory=audio_Split_directory


    def extract(self,foldername=None,output_name="metadata.txt"):
        r = sr.Recognizer()
        
        if(foldername is None):
            pth="metadata.txt"
        else:
            pth=os.path.join(foldername,output_name)
        f=open(pth,"w+")
        for file in sorted(os.listdir(self.directory)):
            filename = os.fsdecode(file)
            if filename.endswith(".wav"):
                with sr.AudioFile(os.path.join(self.directory, filename)) as source:
                    # listen for the data (load audio to memory)
                    audio_data = r.record(source)
                    # recognize (convert from speech to text)
                    text = r.recognize_google(audio_data)
                    #print(filename)
                    name=str(filename).split(".")[0]
                    f.write(f"{name}|{text}\n")
                    #print(text)
        print("Text folder saved in path : ",pth)
        f.close()
if __name__=="__main__":
    et=text_extraction("audio_split")
    et.extract()

                    
