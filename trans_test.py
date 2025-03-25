import cv2, json
import time
import pandas as pd
import numpy as np

json_path = "control.json"
with open(json_path) as file:
    control = json.load(file)
    csv_path = control["csv_path"]
    media_path = control["media_path"]

capture = cv2.VideoCapture(media_path)

if capture.isOpened() is False:
    print("Error opening video stream or file")

frame_index = 0
print("Starting in frame: '{}'".format(frame_index))

total = capture.get(cv2.CAP_PROP_FRAME_COUNT)
print(total)

fps = 24
frame_interval = 1.0/fps
prev_time = 0.0

while capture.isOpened() and frame_index < total:
    start_time = time.time()
    if start_time - prev_time >= frame_interval:
        capture.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        ret, frame = capture.read()

        if ret:
            div = 128
            # stretched_frame = cv2.resize(frame, (0, 0), fx = 0.141, fy=0.0625)  # 裁切
            stretched_frame = cv2.resize(frame, (0, 0), fx=0.225, fy=0.1)  # 裁切
            gray_frame = cv2.cvtColor(stretched_frame, cv2.COLOR_BGR2GRAY)   # 灰度
            gray_frame = gray_frame//32 * 32
            # frame = frame // div *div

            cv2.imshow("railgun", gray_frame)
            prev_time = start_time

            print("Complete: ",  frame_index, "/", total)
            frame_index += 1
            # x = input()

            if cv2.waitKey(1) & 0xFF == ord('q'):  # 按 'q' 退出
                break

        else:
            break

capture.release()