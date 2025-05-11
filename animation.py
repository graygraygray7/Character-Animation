import _curses
import csv, time, curses, json

def main(stdscr):
    curses.curs_set(0)  # 隐藏光标
    stdscr.nodelay(1)  # 非阻塞输入
    # frame_rate = 24  # 帧率
    frame_delay = 1.0 / frame_rate  # 每帧的延迟时间

    # 记录当前帧率
    frame = 0
    with open(file_path) as file:

        data = csv.reader(file)
        # 一帧以内
        start_time = time.time()
        global x
        global y
        x, y = 0, 0
        stdscr.clear()

        for row in data:
            row = ["0" if i == '' else i for i in row]
            row = list(map(int, map(float, row)))
            #一行以内
            if row[0] == -1:
                #
                # stdscr.addstr(0, 0, str(frame))
                stdscr.refresh()

                # 动态控制延时，稳定刷新率
                elapsed_time = time.time() - start_time
                if elapsed_time < frame_delay:
                    time.sleep(frame_delay - elapsed_time)

                start_time = time.time()
                x, y = 0, 0
                stdscr.clear()
                frame += 1

                print("over")
                continue

            for i in row:
                i = int(i)

                if i != 0 and i%120 == 0:
                    for j in range(0, 120, 1):
                        try:
                            stdscr.addstr(y, x + j, characters[(i - 1) // 120])
                        except _curses.error:
                            pass

                for j in range(0, i % 120, 1):
                    try:
                        stdscr.addstr(y, x + j, characters[(i-1)//120])
                    except _curses.error:
                        pass

                # if i > 600:
                #     for j in range(i % 200):
                #         try:
                #             stdscr.addstr(y, x + j, '#')
                #         except _curses.error:
                #             pass
                # elif i > 400:
                #     for j in range(i % 200):
                #         try:
                #             stdscr.addstr(y, x + j, '*')
                #         except _curses.error:
                #             pass
                # elif i > 200:
                #     for j in range(i % 200):
                #         try:
                #             stdscr.addstr(y, x + j, '·')
                #         except _curses.error:
                #             pass
                # else:
                #     for j in range(i % 200):
                #         try:
                #             stdscr.addstr(y, x + j, ' ')
                #         except _curses.error:
                #             # 功勋代码，舍不得删
                #             # print(y, x+j)
                #             # print(curses.LINES, curses.COLS)
                #             # time.sleep(0.5)
                #             # raise ValueError(y, x+j)
                #             # x = input("d")
                #             pass

                x += (i % 120)
            y += 1
            x = 0

if __name__ == "__main__":
    try:
        json_path = "control.json"
        with open(json_path, encoding="UTF-8") as file:
            control = json.load(file)
            file_path = control["file_path"]
            frame_rate = control["frame_rate"]
            characters = control["characters"]

        curses.wrapper(main)

    except KeyboardInterrupt:
        print("\nAnimation stopped.")
        x = input()
