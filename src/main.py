from logger import logging
import uvicorn

if __name__ == "__main__":
    logging = logging.getLogger(__name__)
    logging.info("Starting the application...")
    uvicorn.run("src.api.endpoints:app", host="0.0.0.0", port=8000, reload=True)