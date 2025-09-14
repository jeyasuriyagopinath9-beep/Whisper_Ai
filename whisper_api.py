from fastapi import FastAPI, UploadFile, File
import whisper
import uvicorn
import os

app = FastAPI()

# Load the small model (good balance between speed and accuracy for CPU)
model = whisper.load_model("small")

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    file_location = f"/tmp/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())
    result = model.transcribe(file_location)
    os.remove(file_location)  # clean up temp file
    return {"transcription": result["text"]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
