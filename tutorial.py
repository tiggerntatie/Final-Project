error = " "

slideNumber = 1
def tutorial1():
    global error
    st = input('{0} Welcome to Survival. You are the grey sprite, everyone else is trying to kill you. 4 hits and you die. WASD move you, with W always moving you in the direction of the arrow. Press the "w" key when you understand.'.format(error))
    if st != 'w':
        error = "ERROR, TRY AGAIN"
        tutorial1()
    else:
        slideNumber=2
def tutorial2():
    global error
    nd = input('{0}Q and E rotate you. J is a short ranged melee attack that kills stuff. K is a bullet. You have 4 shots before you have to use R to reload. Press the "r" key if you understand'.format(error))
    if nd != 'r':
        error = "ERROR, TRY AGAIN"
        tutorial2()
def tutorial3():
    global error
    nd = input('{0}L is a shield with a turn two cooldown. Speaking of turns, you have a limited number of moves 4. Rotating is free. Moving is one move, as is melee attacking. Shooting and reloading is 3 moves, while shielding is 2. Press Space to get your moves back and have the enemies attack. Press the "space" key if you understand'.format(error))
    if nd != ' ':
        error = "ERROR, TRY AGAIN"
        tutorial3()
    
def tutorial():
    global error
    error = " "
    tutorial1()
    error = " "
    tutorial2()
    error = " "
    tutorial3()
    input("There are some othering things, but I'm sure you'll figure them out. Good Luck.")
controlAsset= 0
def controls():
    print("""CONTROLS:
        WASD TO MOVE (1 move per)
        J: short range attack (1 move per)
        K: long range attack (3 move per)
        SPACE: end turn
        L: shield (2 move per and 2 turn cooldown)
        R: reload (3 move per)
        Q/E: rotate""")
    global controlAsset
    controlAsset= """CONTROLS:
        WASD TO MOVE (1 move per)
        J: short range attack (1 move per)
        K: long range attack (3 move per)
        SPACE: end turn
        L: shield (2 move per and 2 turn cooldown)
        R: reload (3 move per)
        Q/E: rotate"""
