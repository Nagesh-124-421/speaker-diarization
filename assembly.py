# Start by making sure the `assemblyai` package is installed.
# If not, you can install it by running the following command:
# pip install -U assemblyai
#
# Note: Some macOS users may need to use `pip3` instead of `pip`.
import time
    
import assemblyai as aai
import os


def processAudio(file_url):
    try:
        start_time = time.time()
        print("process started at:", time.ctime(start_time))
            



        # Replace with your API key
        aai.settings.api_key = "ff5858599e3c4979a626c7cf463688d5"

        # URL of the file to transcribe
        FILE_URL = file_url

        # You can also transcribe a local file by passing in a file path
        # FILE_URL = './path/to/file.mp3'

        config = aai.TranscriptionConfig(speaker_labels=True)

        transcriber = aai.Transcriber()

        transcript = transcriber.transcribe(
        FILE_URL,
        config=config
        )

        data=[]
            
        for utterance in transcript.utterances:
        
            data.append({
                f"Speaker {utterance.speaker}: {utterance.text}"
            })


        # Print finish time
        end_time = time.time()
        print("Code finished at:", time.ctime(end_time))


        # Calculate and print the total elapsed time
        elapsed_time = end_time - start_time
        print("Total elapsed time:", elapsed_time, "seconds")
        
        # Delete the file
        os.remove(file_url)
        
        return data
    except Exception as e:
        print(e)
        print('Errror while processing audio')
        return 'something went wrong'
