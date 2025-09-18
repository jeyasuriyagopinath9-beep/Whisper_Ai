from fastapi import FastAPI, UploadFile, File
import whisper
import uvicorn
import os

app = FastAPI(title="Whisper AI API")

# Load Whisper model (small model, change if you want larger)
model = whisper.load_model("small")

@app.post("/transcribe")
async def transcribe(file: UploadFile = File(...)):
    file_path = f"/tmp/{file.filename}"
    
    # Save uploaded file
    with open(file_path, "wb") as f:
        f.write(await file.read())
    
    # Run transcription
    result = model.transcribe(file_path)
    
    # Delete file after processing
    os.remove(file_path)
    
    return {"transcript": result["text"]}

# Run server if executed directly
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
