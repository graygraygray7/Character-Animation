import cv2, json
import pandas as pd
import numpy as np

json_path = "control.json"
with open(json_path) as file:
    control = json.load(file)
    csv_path = control["csv_path"]
    media_path = control["media_path"]
    target_width, target_height = control["pixel"]

cap = cv2.VideoCapture(media_path)

if cap.isOpened() is False:
    print("Error opening video stream or file")

frame_index = 0
print("Starting in frame: '{}'".format(frame_index))

total = cap.get(cv2.CAP_PROP_FRAME_COUNT)
width = float(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = float(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(total)
while cap.isOpened() and frame_index < total:
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
    ret, frame = cap.read()

    if ret:
        stretched_frame = cv2.resize(frame, (0, 0), fx=target_width/width, fy=target_height/height )  # 裁切
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)  # 色彩转化
        frame = frame // 84
        # frame  = np.where(frame > 12,frame - 12 , 0)

        data =  list([0] for _ in range(30))
        for i in range(30):
            # print(frame[i])
            for j in frame[i]:
                if 120*j < data[i][-1] < 120*(j+1)+1:
                    data[i][-1] += 1
                else:
                    data[i].append(120*j+1)

        data.append([-1])
        df = pd.DataFrame(data)
        df.fillna(0, inplace=True)
        df.astype(int)
        df.to_csv(csv_path, mode='a', index=False, header=False)
        frame_index += 1

        print("Complete: ",  frame_index, "/", total)
        # x = input()

    else:
        break