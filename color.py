import curses

def main(stdscr):
    """ Use to see the color codes
    """
    curses.start_color()
    curses.use_default_colors()
    for i in range(1, curses.COLORS):
        curses.init_pair(i, i, -1)
    try:
        for i in range(1, 255):
            stdscr.addstr(f"{str(i)} ", curses.color_pair(i))
    except curses.ERR:
        # End of screen reached
        pass
    stdscr.getch()

curses.wrapper(main)