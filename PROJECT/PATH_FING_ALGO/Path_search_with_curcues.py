import curses
from curses import wrapper

import Path_Search_Algo


def main(stdscr):
    maxy = Path_Search_Algo.maz
    s = Path_Search_Algo.path()
    curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    c1 = curses.color_pair(1)
    c2 = curses.color_pair(2)
    s.find_path(maxy,stdscr,c1,c2,K=True)
    # stdscr.clear()
    # stdscr.addstr('jj')
    stdscr.getch()
if __name__ == '__main__':
    wrapper(main)
