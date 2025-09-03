from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
import test as t  
app = FastAPI()

@app.post("/start")
def start_inference():
    started = t.start_pipeline()
    if not started:
        return {"status": "already running"}
    return {"status": "pipeline started"}

@app.post("/stop")
def stop_inference():
    stopped = t.stop_pipeline()
    if not stopped:
        return {"status": "not running"}

    return FileResponse(
        "predictions.json",
        media_type="application/json",
        filename="predictions.json"
    )

@app.get("/results")
def get_results():
    return t.get_results()

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
