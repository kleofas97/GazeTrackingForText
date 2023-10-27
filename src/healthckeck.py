from src.gaze_tracking import GazeTracking
from src.config import *
import cv2
from src.logger import logging
import time


def healthcheck(path):
    start = time.time()
    logging.info('Healthcheck started.')
    gaze = GazeTracking()
    cap = cv2.VideoCapture(path)
    error_counter = 0
    total_frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 3
    while cap.isOpened():  # if too slow on better computer, perhaps need to apply multithread
        ret, frame = cap.read()
        if ret:
            gaze.refresh(frame)
            if (gaze.eye_left is None) or (gaze.eye_right is None):
                error_counter += 1
        else:
            break
    cap.release()
    hc_time = time.time() - start
    logging.info(f'Healthcheck analysis took: {hc_time:.02}')
    error_rate = error_counter / total_frame_count
    if error_rate >= THRESHOLD_HEALTHCHECK:
        msg = f"Threshold in healthcheck exceeded. Current value: {error_rate}, threshold: {THRESHOLD_HEALTHCHECK}"
        logging.error(msg)
        return 422, msg
    else:
        msg = f"Error rate: {error_rate}. Healthcheck ok."
        return 200, msg
