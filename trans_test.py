import cv2, json
import time
import _curses

import pandas as pd
import numpy as np

json_path = "control.json"
with open(json_path) as file:
    control = json.load(file)
    csv_path = control["csv_path"]
    media_path = control["media_path"]

cap = cv2.VideoCapture(media_path)

if cap.isOpened() is False:
    print("Error opening video stream or file")

frame_index = 0
print("Starting in frame: '{}'".format(frame_index))

total = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(total)

fps = 24
frame_interval = 1.0/fps
width = float(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = float(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
prev_time = 0.0
cha = False

print(width, height)
while cap.isOpened() and frame_index < total:
    start_time = time.time()
    if start_time - prev_time >= frame_interval:
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        ret, frame = cap.read()

        if ret:
            div = 128
            # stretched_frame = cv2.resize(frame, (0, 0), fx = 0.141, fy=0.0625)  # 裁切
            stretched_frame = cv2.resize(frame, (0, 0), fx=120.0/width, fy=30.0/height)  # 裁切
            stretched_frame = cv2.resize(stretched_frame, (0, 0), fx=width/120, fy=height/30.0)  # 裁切
            gray_frame = cv2.cvtColor(stretched_frame, cv2.COLOR_BGR2GRAY)   # 灰度
            gray_frame = gray_frame//32 * 32
            # frame = gray_frame
            frame = stretched_frame // div *div

            if not cha:
                cv2.imshow("railgun", frame)
                prev_time = start_time

                print("Complete: ",  frame_index, "/", total)
                frame_index += 1
                # x = input()

                if cv2.waitKey(1) & 0xFF == ord('q'):  # 按 'q' 退出
                    break

        else:
            break

cap.release()