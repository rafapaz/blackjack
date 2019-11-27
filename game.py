
from blackjack import BlackJack

if __name__ == "__main__":
    while True:
        bj = BlackJack()
        bj.show_table()

        if not bj.hit():
            if bj.continue_game():
                continue
            else:
                break            

        bj.show_table()
        bj.dealer_plays()
        bj.show_table()
        bj.final_result()
        if not bj.continue_game():
            break
