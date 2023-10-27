from fastapi import FastAPI, HTTPException
from src.logger import logging
from src.api import request
from fastapi.responses import JSONResponse
from src import config
from src.video_analysis import analyze_video as get_analysis
from src.healthckeck import healthcheck as get_healthcheck

logging = logging.getLogger(__name__)
logging.info("App initialization...")

app = FastAPI()


@app.get("/")
def root():
    return {"msg": "Hello World"}


@app.post("/healthcheck", status_code=200)
def healthcheck(request: request.HealthcheckRequest):
    status, msg = get_healthcheck(request.video_path)
    return JSONResponse(content={"status": msg}, status_code=status)


@app.post("/analyze_video", status_code=201)
def analyze_video(request: request.AnalyzeRequest):
    if request.max_x is None:
        max_x = config.RESOLUTION_WIDTH
    else:
        max_x = request.max_x
    try:
        spotted_points = get_analysis(path=request.video_path, max_x=max_x)
    except Exception as e:
        msg = f"Error during analyzing video, full info: {e}"
        logging.error(msg)
        raise HTTPException(status_code=500, detail=msg)
    return JSONResponse(content={"Percentage Points": spotted_points}, status_code=201)
