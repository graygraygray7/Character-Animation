import pandas,time, curses
from itertools import islice

def main(stdscr):
    curses.curs_set(0)  # 隐藏光标
    stdscr.nodelay(1)   # 非阻塞输入
    frame_rate = 10  # 帧率
    frame_delay = 1.0 / frame_rate  # 每帧的延迟时间

    index = -1
    while True:
        # 一帧以内
        start_time = time.time()
        x, y = 0, 0
        stdscr.clear()

        for cur_index, row in islice( data.iterrows(), index+1, None ):
            #一行以内
            x = 0
            index = cur_index
            if row[0]==-1:
                print("over")
                break

            for i in row:
                i = int(i)
                if i>100:
                    for j in range(i%100):
                        stdscr.addstr(y, x+j, "*")
                else:
                    for j in range(i%100):
                        stdscr.addstr(y, x+j, " ")
                x += (i%100)
            y+=1
        stdscr.refresh()

        # 动态控制延时，稳定刷新率
        elapsed_time = time.time() - start_time
        if elapsed_time < frame_delay:
            time.sleep(frame_delay - elapsed_time)

if __name__ == "__main__":
    try:
        file_path = r"D:\py\Character-Animation\animation.csv"
        data = pandas.read_csv(file_path, dtype=float, header=None)
        curses.wrapper(main)

    except KeyboardInterrupt:
        print("\nAnimation stopped.")
        x = input()