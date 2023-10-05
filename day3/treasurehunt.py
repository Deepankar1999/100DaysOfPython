DragonWelcome="""
                                __+__
            _,-------_,       _/  +  \_     /~~>'
         _-~          |      (O   +   O)   |  /
      _-~              \      \       /   /  |
   _-~                  |      \     /   |  /
  ~ ~~~~-_               \     |( " )|  /  |
          \               |    | \./ | |  / |~~\ |~~\  /~\  /~\  /~\ |   | /~\
    |\     |               \ _/      |/  |  |   ||   ||   ||   ||   ||\  ||___
    | |    |   __         _-~         \_/   |   ||--< |---|| -- |   || \ |
   /  /   / _-~  ~~--_ _-~              \   |__/ |   \|   | \_/  \_/ |  \| \_/
  |  |   /-~        _-~                  \
 /   /           _-~  __        \  \     \\                               
|   |__         / _-~  ~-_       \  \     \\                              
|      ~~--__--~ /  _     \       \  |    | |                             
 \               _-~       |      //|\    ||\          ___                
  ~~--__        /         / ___          /--__        / /^\
        ~~--___/       _-~ / /^\        /    ~~~-----~ /___
         _____/     _-~---~ /___       /| _        ~~--~~ /^\
      /^<  ___         ~~--~~ /^\   _-~/ / ~--__   ~~--~~~\
         ~~   ~~--__   ~~--~~~\---~~  | /       ~~--___--~~\
                    ~~--___--~~\       V

------------------------------------------------
Welcome TO Treasure Hunt

"""

DragonKilled="""
<~>
 \ \,_____
       ___`\
       \('>\`-__
         ~      ~~~--__            **              ***
               ______  (@\   *******  ****    *******    ******
              /******~~~~\|**********************************
      \       `--____******************************************
     / ~~~--_____    ~~~/ ***************************************
                 `~~~~~         ******************************
                                      ****    **************
                                        ***       ***********
                                                        ********          

------------------------------------------------
Dragon Killed You Better Luck Next Time
"""

treasureShip="""              |    |    |
             )_)  )_)  )_)
            )___))___))___)\
           )____)____)_____)\\
         _____|____|____|____\\\__
---------\                   /---------
  ^^^^^ ^^^^^^^^^^^^^^^^^^^^^
    ^^^^      ^^^^     ^^^    ^^
         ^^^^      ^^^

------------------------------------------------
Congratulions You Found A Treasure Ship..... 
GAME OVER
"""

start=input("Press y to Start the game  ")
if start=='y':
    print(DragonWelcome)
    choice1=input("Your boat was destroyed by stroms and you are stranded in an Island. Press l to go left and r to go right   " )
    if choice1=='r':
        choice2=input("You Stumbled Upon two caves.One leads to ocean and other leads to mountain. Press o for ocean and m for mountain   ")
        if choice2=='o':
            print(treasureShip)
        else:
            print(DragonKilled)

    else:
        print(DragonKilled)
        print("GAME OVER")

else:
    print("Bye Have A Great Day")
    print("GAME OVER")




