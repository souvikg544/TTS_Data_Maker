import speech_recognition as sr
import os
import csv
#filename = "audio_split\\1.wav"

class text_extraction():

    def __init__(self,audio_Split_directory):
        self.directory=audio_Split_directory


    def extract(self,foldername,output_name):
        r = sr.Recognizer()
        
        if(foldername is None):
            pth="metadata.txt"
            pth1="metadata.csv"
        else:
            pth=os.path.join(foldername,output_name)
            pth1=os.path.join(foldername,"metadata.csv")
        #print("Path to the output file is : ", pth)
        f=open(pth,"w+")
        c = open(pth1, 'w+')
        writer = csv.writer(c)
        data=[]
        for file in sorted(os.listdir(self.directory)):
            filename = os.fsdecode(file)
            if filename.endswith(".wav"):
                with sr.AudioFile(os.path.join(self.directory, filename)) as source:
                    # listen for the data (load audio to memory)
                    audio_data = r.record(source)
                    # recognize (convert from speech to text)
                    try:
                        text = r.recognize_google(audio_data,language = 'en-IN')
                        name=str(filename).split(".")[0]
                        f.write(f"{name}|{text}|{text}\n")
                        #row.append(f"{name}|{text}")
                        #writer.writerows(f"{name}|{text}")
                        data.append([f"{name}|{text}|{text}"])
                        print(f"Extracted text from {filename}")
                    except:
                        os.remove(os.path.join(self.directory, filename))
                        print(f"Could not extract from {filename}")

                        
                    #print(filename)

        writer.writerows(data)         
        c.close()          
        print("Text file saved in path : ",pth)
        print("Csv file saved in path : ",pth1)
        f.close()
        
if __name__=="__main__":
    et=text_extraction("audio_split")
    et.extract("D:\whilter\TTS_Data_Maker\main_audio","metadata.txt")

                    
