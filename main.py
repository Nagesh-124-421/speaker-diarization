from fastapi import FastAPI, File, UploadFile
import os
from pathlib import Path
from assembly import processAudio


app = FastAPI()

@app.post("/upload-audio/")
async def create_upload_file(file: UploadFile = File(...)):
    try:
        # Save the file locally
        file_location = f"temp/{file.filename}"
        os.makedirs(os.path.dirname(file_location), exist_ok=True)
        with open(file_location, "wb+") as file_object:
            file_object.write(await file.read())
            
        

        # Process the file
        return processAudio(file_location)
    except Exception as e:
        print(e)
        return 'something went wrong'

    


# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)
