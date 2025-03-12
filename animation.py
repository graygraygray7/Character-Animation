import time,os,pandas
import curses

def clear_screen():
    os.system('cls')

def animate(data):
    while True:
        clear_screen()
        for index, row in data.iterrows():
            for i in row:
                if i>100:
                    print("*"*(i%100), end="")
                else:
                    print(" "*i, end="")
            print("\n", end="")
        time.sleep(0.04)

def main(stdscr):
    curses.curs_set(0)  # 隐藏光标
    stdscr.nodelay(1)   # 非阻塞输入
    stdscr.timeout(100) # 每100毫秒刷新一次
    file_path = r"D:\py\birthday0502\animation.csv"
    data = pandas.read_csv(file_path, dtype=int, header=None)

    while True:
        #一帧以内
        x, y = 0, 0
        stdscr.clear()

        for index, row in data.iterrows():
            #一行以内
            x = 0
            for i in row:
                if i>100:
                    for j in range(i%100):
                        stdscr.addstr(y, x+j, "*")
                else:
                    for j in range(i%100):
                        stdscr.addstr(y, x+j, " ")
                x += (i%100)
            y+=1
        stdscr.refresh()


if __name__ == "__main__":
    try:
        curses.wrapper(main)

    except KeyboardInterrupt:
        print("\nAnimation stopped.")
        x = input()