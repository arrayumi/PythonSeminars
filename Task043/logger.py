from datetime import datetime as dt

def log_win (win):
    time = dt.now().strftime('%Y-%m-%d %H:%M:%S')
    file = open('Task043/win.txt', 'a+')
    file.write('{} Winner -> {}\n'.format(time, win))
    file.close()