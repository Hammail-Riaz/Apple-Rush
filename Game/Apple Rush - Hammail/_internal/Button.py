# Importing the required Modules
import pygame

pygame.init()

class Click_Button:
    
    def __init__(
        self, surface, normal_img, hover_img, click_sound, cordinate_to_place, normal_img_size, hover_img_size,  command, bg_color = (255, 255, 255) 
        ):
        
        self.normal_img = normal_img
        self.hover_img = hover_img
        self.click_sound = click_sound
        self.cordinate_to_place = cordinate_to_place
        self.normal_img_size = normal_img_size
        self.hover_img_size = hover_img_size
        self.bg_color = bg_color
        self.command = command
        
        normal_img = pygame.transform.scale(pygame.image.load(normal_img), normal_img_size)
        normal_img.set_colorkey(bg_color)
        
        hover_img = pygame.transform.scale(pygame.image.load(hover_img), hover_img_size )
        hover_img.set_colorkey(bg_color)
        
        surface.blit(normal_img , self.cordinate_to_place)
        
        pos = pygame.mouse.get_pos()
        
        x = pos[0]
        y = pos[1]
        
        r_x = cordinate_to_place[0]
        r_y = cordinate_to_place[1]
        
        w = normal_img_size[0]
        h = normal_img_size[1]
        
        if (x < ( r_x + w )  and x > (r_x)) and (y < (r_y + h)  and y > (r_y)):
             
            surface.blit(hover_img, cordinate_to_place)
            
            b1_pressed = pygame.mouse.get_pressed()[0]
            if b1_pressed:                
                pygame.mixer.music.load(self.click_sound)
                pygame.mixer.music.play()
                command()
            #     return True
            # return False
        
        
       
            
            

# white = (255,255,255)
# win = pygame.display.set_mode((500, 500))
# pygame.display.set_caption("main menu of the game")

# run = True
# def hammail():
#     pygame.init()
#     r = True
#     pygame.display.set_caption("game is playing - hammail")
#     while r:
#         win.fill((,,0))    
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 r = False
#         pygame.display.flip()
        
#     pygame.quit()
              
# def main():
#     global run
#     pygame.init()
#     while run:
#         b1 = Click_Button(win, "play_normal.png", "play_click.png", "MOUSE CLICK.mp3",(10, 10), (200, 80),(200, 80),  white)
#         # Button.Click_Button(win, img, c_img, (100,100), (200, 80),white,  command= hammail)
        
#         # win.blit(img, (100, 100))
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
                
#             if b1.check_input():
#                 print("this is maded sucessfully congrats... i am so happy so what i have to do now i am very good in typing now so i really wants to type extra therefore i am typing this extra text ...")
#                 hammail()
        
#         pygame.display.flip()
            
#     pygame.quit()    
# main()