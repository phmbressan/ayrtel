import cv2
import json
import numpy as np

from extractor import extract_text_from_region
from tqdm import tqdm


def extract_all_values(frame, boxes):
    return [extract_text_from_region(frame, box) for box in boxes]


def process_video(video_path, header_boxes):
    cap = cv2.VideoCapture(video_path)
    data_log = []

    cap = cv2.VideoCapture(video_path)
    actual_total = 0
    while True:
        ret, _ = cap.read()
        if not ret:
            break
        actual_total += 1
    cap.release()

    cap = cv2.VideoCapture(video_path)
    pbar = tqdm(total=actual_total, desc="Processing frames")
    data_log = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        current_extract = [extract_text_from_region(frame, box) for box in header_boxes]
        if current_extract[0] != "" and (
            len(data_log) == 0 or current_extract[0] != data_log[-1][0]
        ):
            data_log.append(current_extract)

        pbar.update(1)

    cap.release()
    pbar.close()
    return data_log


if __name__ == "__main__":
    try:
        with open("data/header_boxes.json", "r") as f:
            header_boxes = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(
            "header_boxes.json not found. Please run the header marker script first."
        )

    data = np.array(process_video("data/ayr_cut.mp4", header_boxes), dtype=str)
    header = [
        "Time (s)",
        "Space (m)",
        "Stgpr (psi)",
        "Stgtgt (psi)",
        "Stgstn (m/m2)",
        "Stgact (psi)",
        "Pedal 1 (%)",
        "Gear (-)",
        "Clutch (mm)",
        "Pedal 2 (%)",
        "Potd (%)",
        "N (Rpm)",
        "Rodsp (km/h)",
        "Rearsp (km/h)",
        "Lat Acc (g)",
        "Lon Acc (g)",
    ]

    np.savetxt(
        "data/ayr_data.csv",
        data,
        header=";".join(header),
        delimiter=";",
        fmt="%s",
    )
