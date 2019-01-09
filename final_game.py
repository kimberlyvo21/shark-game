#Julie Nguyen (jqn5xk) and Kimberly Vo (kv3nw)

import pygame
import gamebox
import random

#OVERALL GAME IDEA:
# There will be a swimmer that is controlled by the user.
# He will be horizontally stationary but can move vertically, up and down the screen.
# Goal is to collect stars to gain points.
# Game ends if shark eats the swimmer.



camera = gamebox.Camera(800, 600)
background = gamebox.from_image(400, 300, 'https://cdn.dribbble.com/users/375867/screenshots/2841681/creepy-deep-sea-ocean-monster-game-background.png')

start_screen = gamebox.from_image(400,300,'https://images.wallpaperscraft.com/image/shark_art_background_protruding_tongue_98694_800x600.jpg')

start_text = gamebox.from_text(250, 475, 'SHOO-SHOO SHARK',50, 'white')
how_to_start = gamebox.from_text(630, 425, 'Press the SPACE BAR to start', 25, 'black')
controls = gamebox.from_text(630, 450, 'Use UP and DOWN keys to control', 25, 'black')
instructions1 = gamebox.from_text(400, 50, 'Collect stars to gain points and avoid incoming sharks. Every 5 points you collect,',25, 'black')
instructions2 = gamebox.from_text(400, 75, 'your speed increases and you move on to the next level.', 25, 'black')
tip = gamebox.from_text(400, 100, 'Tip: Collecting crabs will cause you to lose points.', 25, 'black')
names = gamebox.from_text(300, 550, 'Created By: Kimberly Vo (kv2nw) and Julie Nguyen (jqn5xk)', 25, 'black')

topborder = gamebox.from_color(0, 0, 'black', 800, 2)
bottomborder = gamebox.from_color(0, 600, 'black', 800, 2)

swimmer_sheet = gamebox.load_sprite_sheet('https://66.media.tumblr.com/57bcb2eecadb04ddec1c7be43e378411/tumblr_pjdyfk6TP31qkemqxo1_540.png', 2, 4)
swimmer = gamebox.from_image(400, 400, swimmer_sheet[3])
swimmer.scale_by(0.8)

shark = gamebox.from_color(1300, 400, 'orange', 40, 30)
shark_sheet = gamebox.load_sprite_sheet('https://orig00.deviantart.net/bd28/f/2014/048/4/b/pating_triangle_by_ottojoy-d76ywd4.png', 2, 2)
shark = gamebox.from_image(shark.x, shark.y, shark_sheet[1])
shark.scale_by(0.7)

crab = gamebox.from_color(800, 300, 'red', 40, 30)
crab_sheet = gamebox.load_sprite_sheet('https://d3tv7e6jdw6zbr.cloudfront.net/items/2012-12-06/npc_crab__x1_walk_png_1354831183.png', 4, 6)
crab = gamebox.from_image(crab.x, crab.y, crab_sheet[1])
crab.scale_by(0.5)

star = gamebox.from_circle(1050, 100, 'yellow', 10)
star_sheet = gamebox.load_sprite_sheet('http://3.bp.blogspot.com/-eo9bbSi5gmo/Uz6ylKl5hUI/AAAAAAAAAjo/OhG0bdh9xSo/s1600/Ster+animatie.png', 3, 8)
star = gamebox.from_image(star.x, star.y, star_sheet[3])
star.scale_by(0.8)

start = False
score = 0
count_tick = 0
speed = 3
lvl = 1

def random_boosts():
    """
    Randomizes the location of the star each time it goes off screen, making it appear in different places each time.
    """
    star.y = random.randint(100, 500)
    star.x = random.randint((camera.x + 400), (camera.x + 800))

def random_shark():
    """
    Randomizes the location of the shark each time it goes off screen, making it appear in different places each time.
    """
    shark.y = random.randint(100, 500)
    shark.x = random.randint((camera.x + 400), (camera.x + 800))

def random_crab():
    """
    Randomizes the location of the crab each time it goes off screen, making it appear in different places each time.
    """
    crab.y = random.randint(100, 500)
    crab.x = random.randint((camera.x + 400), (camera.x + 800))

def tick(keys):
    """
    Controls everything in the game. Draws the backgeound and objects/characters, allows movement of the swimmer through inputs, animates sprite sheets, keeps track of score/speed/level while displaying on screen, and detects collisions between objects. Clearly defines a start and end to the game as well.
    """
    global score
    global start
    global count_tick
    global speed
    global lvl

    # ---------- INPUT ------------
    # Up and down arrow keys will be used to move the player vertically across the screen.
    # This is fulfilling the Input feature.

    if pygame.K_SPACE in keys:
        start = True

    if pygame.K_UP in keys:
        swimmer.y -= 20
    if pygame.K_DOWN in keys:
        swimmer.y += 20

    swimmer.x = camera.x - 180
    background.x = camera.x
    topborder.x = camera.x
    bottomborder.x = camera.x

    swimmer.move_to_stop_overlapping(topborder)  # Hardcoded borders to avoid swimmer going off screen
    swimmer.move_to_stop_overlapping(bottomborder)

    if star.right < camera.left:
        random_boosts()
    if shark.right < camera.left:
        random_shark()
    if crab.right < camera.left:
        random_crab()

    # ----------- DRAW -------------
    #Where all the gameboxes will be drawn
    #This fulfills the graphics/images feature. We will make sure to have appropriate images fitting a swimmer and sharks.
    # The screen will also be a scrolling level. There will be collectibles off screen that will appear randomly as screen scrolls.
    #We will have a start screen with the game name and basic instructions.
    #This fulfills the Scrolling Level
    if start is True:
        camera.draw(background)
        camera.draw(swimmer)
        camera.draw(star)
        camera.draw(shark)
        camera.draw(crab)
        camera.move(speed, 0)
        count_tick += 0.5

        # --------- ANIMATION -----------
        # Shark, swimmer, star, and crab will be moving.
        # This fulfills the Animation feature.
        swimmer.image = swimmer_sheet[int(count_tick) % len(swimmer_sheet)]
        shark.image = shark_sheet[int(count_tick) % len(shark_sheet)]
        star.image = star_sheet[int(count_tick) % len(star_sheet)]
        crab.image = crab_sheet[int(count_tick) % len(crab_sheet)]

        # ---------- SCORE -------------
        # When the player collects stars, score will increase by 1.
        # Score will be displayed throughout whole game.
        scoreboard = gamebox.from_text(camera.x, 50, 'SCORE: ' + str(score), 30, 'black')
        camera.draw(scoreboard)

        # ---------- LEVELS -----------
        #Each level is defined by how fast the speed is. Higher the level, faster the speed.
        #This fulfills the Levels feature.
        lvl = (score//5) + 1
        speed = 3 + 2*lvl
        camera.move(speed, 0)

        swim_fast = gamebox.from_text(camera.x - 200, 50, 'SPEED: ' + str(int(speed)) + ' m/s', 30, 'black')
        levels = gamebox.from_text(camera.x + 200, 50, 'LEVEL: ' + str(lvl), 30, 'black')
        camera.draw(levels)
        camera.draw(swim_fast)

        # ----- COLLISION DETECTION -----
        # First collision: Animated sharks will be used to chase the player across the screen.
        # When collision is detected, game will end.
        # Second collision: Player will be able to collect stars that randomly appear on the screen.
        # Every time player collects five  stars, his speed will increase and a point will be added to the score.
        # Third collision: Player will be able to collect crabs but will lose one point each time.
        # This will fulfill the Enemies and Collectibles features.

        if swimmer.touches(star, -70, -70) is True:
            random_boosts()
            score += 1

        if swimmer.touches(shark, -70, -55) is True:
            end_game = gamebox.from_text(camera.x, 200, 'GAME OVER', 100, 'white')
            camera.draw(end_game)
            gamebox.pause()

        if swimmer.touches(crab, -50, -55) is True:
            random_crab()
            if score > 0:
                score -= 1

    # --------- START SCREEN ----------
    # Draws everything on the beginning screen before game starts.
    # This fulfills the Start Screen feature.
    else:
        camera.draw(start_screen)
        camera.draw(start_text)
        camera.draw(instructions1)
        camera.draw(instructions2)
        camera.draw(tip)
        camera.draw(how_to_start)
        camera.draw(controls)
        camera.draw(names)


    camera.display()

gamebox.timer_loop(30, tick)