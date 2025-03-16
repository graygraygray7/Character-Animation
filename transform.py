import cv2, json
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
while capture.isOpened() and frame_index < total:
    capture.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
    ret, frame = capture.read()

    if ret:
        stretched_frame = cv2.resize(frame, (0, 0), fx=0.141, fy=0.0625 )  # 裁切
        gray_frame = cv2.cvtColor(stretched_frame, cv2.COLOR_BGR2GRAY)    # 灰度

        frame = np.array(gray_frame)
        frame  = frame // 32
        data =  list([0] for _ in range(30))
        for i in range(30):
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

    else:
        break