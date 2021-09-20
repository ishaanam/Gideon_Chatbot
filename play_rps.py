#another simple game I made back when I started programming
import random

player = " "

def play_rps():
    choices = ['r', 'p', 's']
    playing = True
    player_score = 0
    gideon_score = 0
    while playing == True:
        print('\n')
        player_choice = input("enter: ")
        gideon_choice = random.choice(choices)
        print(player + ': ' + player_choice)
        print('Gideon: ' + gideon_choice)
        result = player_choice + gideon_choice
        #quit
        if player_choice == 'q':
            playing = False
            print('\n')
            print('Final:')
            print(player +': ' + str(player_score))
            print('Gideon: ' + str(gideon_score))
        elif result == 'ss' or result == 'pp' or result == 'rr':
            print('tie!')
            print(player +': ' + str(player_score))
            print('Gideon: ' + str(gideon_score))
        #lose
        elif result == 'rp' or result =='ps' or result == 'sr':
            print('you lost the match!')
            gideon_score = gideon_score + 1
            print(player +': ' + str(player_score))
            print('Gideon: ' + str(gideon_score))
        #win
        elif result =='rs' or result =='pr' or result == 'sp':
            print('you won the match!')
            player_score = player_score + 1
            print(player +': ' + str(player_score))
            print('Gideon: ' + str(gideon_score))







