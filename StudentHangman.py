from hangman_helpers import *
import pygame

# CREATE GAME WINDOW/SCREEN
# HINT: use a function from the list
screen=setup_game()

# NAME THE GAME
game_title="hangman"

# LOAD GAME PICTURES
# HINT: use a function from the list
image=load_images()

# CREATE LIST OF AT LEAST 10 WORDS
words=["apple","game","mango","sushi","antmantony","joolibee","weeble","jojojjoojjojojojojojojojo","goober","glazing"] 

# PICK A RANDOM WORD
# HINT: use a function from the list
pick=pick_word(words)
# KEEP TRACK OF GAME
# What are two variables we can use to keep track of our progress in the game

mistakes = 0
letters=[]

# PLAY UNTIL WE TELL IT TO STOP
playing = True

while playing == True:
    # WHAT DO WE SEE ON THE SCREEN
    # HINT: use a function from the list
    draw_game(screen,game_title,image,mistakes,pick,letters)

    for event in pygame.event.get():
        # CLOSE THE GAME
        # IF WINDOW IS CLOSED
        if event.type == pygame.QUIT:
            # STOP PLAYING
            playing = False

        # DETECT KEY
        if event.type == pygame.KEYDOWN:
            key = event.unicode.lower() # Grab unicode of pressed key

            # IF THE KEY PRESSED HAS NOT BEEN TRIED BEFORE
            if key not in letters:
                # ADD IT TO THE LIST OF GUESSED KEYS
                letters.append(key)
            

                #IF THAT KEY WAS WRONG
                if key not in pick:

                    # INCREASE THE COUNT ON THE AMOUNT OF MISTAKES
                    mistakes+=1

    # CHECK FOR WIN
    # HINT: use a function from the list
    win=check_win(pick,letters)


    # IF WE WON:
    if win == True:

        # CELEBRATION MESSAGE (HINT: use a function from the list)
        show_result(screen, "YOU WIN!!!!!!!!!!!!!!!!!!!", "purple")
        # STOP PLAYING


    # IF WE DID NOT WIN AND WE RAN OUT OF GUESSES (We only have 6)
    if mistakes==6 and win==False:
        # TELL PLAYER THEY LOST (HINT: use a function from the list)
        show_result(screen,"YOU LOST!!!","red")
        # STOP PLAYING
        playing=False


pygame.quit()
