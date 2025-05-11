import cv2
import numpy as np

frame: list = list(list([180, 24, 128] for _ in range(500)) for _ in range(500))
frame = np.array(frame)
frame = frame.astype(np.uint8)
# print(frame)
frame = cv2.cvtColor(frame, cv2.COLOR_LAB2BGR)
print(frame)

while True:
    cv2.imshow("railgun", frame)

    if cv2.waitKey(24) & 0xFF == ord('q'):  # 按 'q' 退出
        break
