# Importing the required modules
import pygame as pg
import os 
import time
import Button
import random

pg.init() # initializing the pygame module
pg.mixer.init()

# generating the txt file for presistence of high score out side the game
if not os.path.exists(os.path.join("assets","high score.txt")):
    with open(os.path.join("assets","high score.txt"), "w") as file:
        file.write("0")
        
# generating the read me txt file for the basic instruction and for credits
if not os.path.exists(os.path.join("assets","read_me.txt")):
    with open(os.path.join("assets","read_me.txt"), "w") as file:
        file.write("This Game is made By Hammail in Python programming language using the Pygame module.\nNote:\n\tPlease not edit any file in the assets folder.\n\tlike renaming , deleting, changing the location of the file.\n\tIf you do any change in the assets folder so it can crash the Game...")

# Reading the high score form the high score txt file
with open(os.path.join("assets","high score.txt")) as file:
    h_s = file.read()
    h_s = int(h_s) #converting in intger for mathematical and comparisonal operation

# color definition
white = (255 ,255 ,255)
black = (0, 0, 0)

# Game specfic variables
screen_width , screen_height = 800 , 800
button_width , button_height = 150 , 60
font = pg.font.SysFont(None, 50)
fps = 60
vel = 15
basket_height , basket_width = 150, 100
font_c = pg.font.SysFont(None, 45)

# Clock Definition
clock = pg.time.Clock()

# SFX Loading
apple_hit = pg.mixer.Sound(os.path.join("assets", "sound_elements", "apple_collection_sound.mp3"))
bomb_hit = pg.mixer.Sound(os.path.join("assets", "sound_elements", "EXPLOSION.mp3"))

# Loading the sounds from the assets folder
click_sound = os.path.join("assets", "sound_elements", "MOUSE CLICK.mp3")

# Loading the GUI assets form the folder
menu_bg = pg.transform.scale(pg.image.load(os.path.join("assets","gui_assets","bg_.jpg")), (screen_width , screen_height))
menu_frame = pg.transform.scale(pg.image.load(os.path.join("assets", "gui_assets", "button_frame.png")),(screen_width // 1.5 , screen_height // 1.5))
menu_frame.set_colorkey(white)
game_tag = pg.transform.scale(pg.image.load(os.path.join("assets", "gui_assets", "game_tag.png")), (screen_width // 1.5, screen_height // 4))
game_tag.set_colorkey(white)
others_frame = pg.transform.scale(pg.image.load(os.path.join("assets", "gui_assets", "menu_frame.png")),(screen_width // 1.5, screen_height // 1.5))
others_frame.set_colorkey(white)

# Path for the button from the assets folder
play_normal = os.path.join("assets", "gui_assets", "play_normal.png")
play_click = os.path.join("assets", "gui_assets", "play_click.png")
hg_normal = os.path.join("assets", "gui_assets", "hg_normal.png")
hg_click = os.path.join("assets", "gui_assets", "hg_click.png")
credits_normal = os.path.join("assets", "gui_assets", "credits_normal.png")
credits_click = os.path.join("assets", "gui_assets", "credits_click.png")
quit_normal = os.path.join("assets", "gui_assets" , "quit_normal.png")
quit_click = os.path.join("assets", "gui_assets" , "quit_click.png")
back_normal = os.path.join("assets", "gui_assets" , "back_normal.png")
back_click = os.path.join("assets", "gui_assets" , "back_click.png")

# game assets loading from the assets folder
bg_sky = pg.transform.scale(pg.image.load(os.path.join("assets", "game_elements", "bg_sky.jpg")), (screen_width, screen_height))
basket_img = pg.transform.scale(
    pg.image.load(os.path.join("assets", "game_elements", "basket.png")), (basket_width, basket_height)
    )
basket_img.set_colorkey(white)

# creating the game window
window = pg.display.set_mode(
    (screen_width, screen_height)
    )
icon = pg.image.load("icon.ico")
pg.display.set_icon(icon)
pg.display.set_caption("Apple Rush - Hammail")

# Game main important variables
# creating the rect of the game elements
basket = pg.Rect( screen_width // 2 , screen_height - 150 , basket_width, basket_height)



def quit_game():
    """Function for the quit button in the main menu"""
    pg.quit()
    
def main_menu():
    """Main menu of the game"""
    pg.init()    
    
    # Loading and playing the back groung music
    pg.mixer.music.load(os.path.join("assets", "sound_elements", "bg_music.mp3"))
    pg.mixer.music.play()
    
    
    # Main loop of the main menu    
    run_menu = True
    f = pg.font.SysFont(None, 25)
    while run_menu:
        try:
    
            pg.mixer.music.set_volume(0.5)
            
            clock.tick(fps)
                
            # Adding the bg of the menu
            window.blit(menu_bg, (0, 0))
            
            # adding the menu frame
            window.blit(menu_frame , (screen_width // 6 , screen_height // 3.5 ))        
            
         
            # adding the button on the menu frame
            Button.Click_Button(window, play_normal, play_click , click_sound, (screen_width // 2.5 , screen_height // 3 ), (button_width , button_height), (button_width , button_height), play)
            
            Button.Click_Button(window, hg_normal, hg_click, click_sound, (screen_width // 2.5 , screen_height // 2.2 ), (button_width , button_height), (button_width , button_height),high_score)
            
            Button.Click_Button(window, credits_normal , credits_click, click_sound, (screen_width // 2.5 , screen_height // 1.75), (button_width, button_height),(button_width , button_height), game_credits  )
            
            Button.Click_Button(window, quit_normal  , quit_click, click_sound, (screen_width // 2.5 , screen_height // 1.45), (button_width, button_height),(button_width , button_height), quit_game  )
            
            # adding the tag of the game
            window.blit(game_tag , (screen_width // 6 , 50))

        
            # Event Handler for the main_menu
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run_menu = False
            text7 = f.render("'Apple Rush 2.o' is Coming Soon", 1 , "black")
            window.blit(text7, (screen_width // 4 , screen_height // 1.2))
                    
            pg.display.flip()
            
        except:
            pass 
            # handling the suspicious error on closing the game by excepting them nothing
                
    pg.quit()
                

def game_credits():
    '''function for the credits button on the main menu'''
    pg.display.set_caption("Credits - Hamamil")
    
    # Credits text 
    texts = [
    "Developer:",
    "Hammail Riaz.",
    
    "Copy Right:",
    "All Right are Reserved.",
    
    "Graphics & Sounds Designer:",
    "Hammail Riaz.",


        ]
    
    # Main loop of the game credits window
   
    run_credits_win = True
    while run_credits_win:
        
        window.fill(black)
        window.blit(menu_bg , (0, 0))
        window.blit(others_frame, (screen_width // 6 , screen_height // 6))
        
        
        text1 = font_c.render(texts[0], 1 , "black")
        window.blit(text1, (screen_width // 4.7 , screen_height // 4))
        
        text2 = font_c.render(texts[1], 1 , "black")
        window.blit(text2, (screen_width // 4.5 , screen_height // 3.2))
        
        text3 = font_c.render(texts[2], 1 , "black")
        window.blit(text3, (screen_width // 4.5 , screen_height // 2.5))
        
        text4 = font_c.render(texts[3], 1 , "black")
        window.blit(text4, (screen_width // 4.5 , screen_height // 2.1))
        
        text5 = font_c.render(texts[4], 1 , "black")
        window.blit(text5, (screen_width // 4.5 , screen_height // 1.7))
        
        text6 = font_c.render(texts[5], 1 , "black")
        window.blit(text6, (screen_width // 4 , screen_height // 1.5))
        

        
    
                
        # event handler for the stats
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run_credits_win = False

        Button.Click_Button(window, back_normal, back_click, click_sound, (15, 15), (50, 50), (50, 50),main_menu)
        
        
        pg.display.flip()
                
    pg.quit()
                
                

def high_score():
    """Fuction for the high score button on the main menu"""
    pg.display.set_caption("High Score - Hammail")
    run_hs_win = True
    
    # Main loop of the high score window
    while run_hs_win:
        # event handler for the stats
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run_hs_win = False
        
        window.fill(black)
        window.blit(menu_bg , (0, 0))
        window.blit(others_frame, (screen_width // 6 , screen_height // 6))
        
        hg_text = font.render(f"High Score: {h_s}", 1, "black")
        window.blit(hg_text, (screen_width // 3 , screen_height // 2.2))
        
        Button.Click_Button(window, back_normal, back_click,click_sound, (15, 15), (50, 50), (50, 50),main_menu)

        pg.display.flip()
                
    pg.quit()
                
                
                

def play():
    """Function for the play button on the menu"""
    pg.display.set_caption("Apple Rush - Hammail")

    # Apples specific variables
    apple_spawn_interval = 1500
    apple_timer = 0
    apples = []
    apple_width, apple_height = 40, 50
    apple_vel = 5
    score = 0
    apple_img = pg.transform.scale(pg.image.load(os.path.join("assets", "game_elements", "falling_apples.jpeg")), (apple_width, apple_height))
    apple_img.set_colorkey(white)

    

    # Creating the rect of the bomb
    bomb_img = pg.transform.scale(pg.image.load(os.path.join("assets", "game_elements",  "bomb.png")), (apple_width + 5, apple_height + 5))
    
    # Bomb specific variables
    bomb_img.set_colorkey(white)
    bombs = []
    start_time = time.time()
    elasped_time = 0
    # Main loop of the game
    run_game = True
    while run_game:
        apple_timer += clock.tick(fps)
        elasped_time = round(time.time() - start_time, 1)
 
        window.fill(black)
        
        # adding the sky of the game
        window.blit(bg_sky, (0, 0))
        
        # adding the basket on the screen
        window.blit(basket_img, (basket.x, basket.y))

        key_pressed = pg.key.get_pressed()
        
        if len(apples) < 15 and apple_timer >= apple_spawn_interval:
            for _ in range(2):
                apple_x = random.randint(0 , screen_width - apple_width)
                apples.append(pg.Rect(apple_x, - apple_height, apple_width, apple_height))
            
            bomb_x = random.randint(0, screen_width - apple_width)
            bombs.append(pg.Rect(bomb_x, - apple_height, apple_width, apple_height))
            apple_spawn_interval = max(100, apple_spawn_interval - 20)
            apple_timer = 0
            
                       
        # Event handler for the game
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run_game = False 
        
        if key_pressed[pg.K_RIGHT] and basket.x < 705:
            basket.x += vel
                                    
        elif key_pressed[pg.K_LEFT] and basket.x >= 10:
            basket.x -= vel

        time_text = font.render(f"Time : {elasped_time} s", 1, "black")   
        window.blit(time_text,  (screen_width - 250 , 20))
        
        score_text = font.render(f"Score : {score}", 1, "black")
        window.blit(score_text, (20, 20))
        for apple in apples[:]:
            
            apple.y += apple_vel
            if apple.y > screen_height:
                apples.remove(apple)
                
            if apple.colliderect(basket):
                apple_hit.play()
                pg.mixer.music.set_volume(1.0)
                score += 5
                apples.remove(apple)
                break
        
        for bomb in bombs[:]:
            
            bomb.y += apple_vel + 5
            if bomb.y > screen_height:
                bombs.remove(bomb)
                
            if bomb.colliderect(basket):
                bomb_hit.play()
                pg.mixer.music.set_volume(1.0)
                score -= 10
                if score <= 0:
                    score = 0
                    
                bombs.remove(bomb)
                break
        
        for apple in apples:
            window.blit(apple_img, (apple.x, apple.y))
        for bomb in bombs:
            window.blit(bomb_img, (bomb.x, bomb.y))
        
        if score > h_s:
            with open(os.path.join("assets", "high score.txt"), "w") as file:
                file.write(str(score))
            
        pg.display.flip()
        
    

    
# Checks that we are directly running over script form the scrip as we are not importing it
if __name__ == "__main__":
    main_menu()
