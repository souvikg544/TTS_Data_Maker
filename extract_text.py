import speech_recognition as sr
import os

#filename = "audio_split\\1.wav"

class text_extraction():

    def __init__(self,audio_Split_directory):
        self.directory=audio_Split_directory


    def extract(self,foldername,output_name):
        r = sr.Recognizer()
        
        if(foldername is None):
            pth="metadata.txt"
        else:
            pth=os.path.join(foldername,output_name)
        #print("Path to the output file is : ", pth)
        f=open(pth,"w+")
        for file in sorted(os.listdir(self.directory)):
            filename = os.fsdecode(file)
            if filename.endswith(".wav"):
                with sr.AudioFile(os.path.join(self.directory, filename)) as source:
                    # listen for the data (load audio to memory)
                    audio_data = r.record(source)
                    # recognize (convert from speech to text)
                    try:
                        text = r.recognize_google(audio_data,language = 'en-IN')
                    except:
                        text="Music"
                    #print(filename)
                    name=str(filename).split(".")[0]
                    f.write(f"{name}|{text}\n")
                    print(f"Extracted text from {filename}")
        print("Text folder saved in path : ",pth)
        f.close()
if __name__=="__main__":
    et=text_extraction("audio_split")
    et.extract("D:\whilter\TTS_Data_Maker\main_audio","metadata.txt")

                    
