import view 
import model
import logger

def run_prog():
    win = model.run_game(view.choose_game())
    logger.log_win(win)
    return win