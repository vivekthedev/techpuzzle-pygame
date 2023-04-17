import pygame
from random import randint
from settings import *

class Level:
    def __init__(self):
        self.background = pygame.image.load('assets/level-bg.png').convert_alpha()
        self.font = pygame.font.Font(LEVEL_FONT, 45)
        self.small_font = pygame.font.Font(LEVEL_FONT, 20)
        self.med_font = pygame.font.Font(MEDIEVAL_FONT, 150)
        self.seg_font = pygame.font.Font(SEGMENT_FONT, 90)
        self.input = pygame.image.load('assets/text-bg.png').convert_alpha()
        self.submit = pygame.image.load('assets/go-btn.png').convert_alpha()
        self.submit_rect = self.submit.get_rect(topleft=((620,610)))
        self.wrong = pygame.image.load('assets/wrong.png').convert_alpha()
        self.wrong = pygame.transform.scale(self.wrong, (OBJECT_WIDTH-80, OBJECT_HEIGHT-80))
        self.next_lvl = pygame.image.load('assets/next-lvl.png').convert_alpha()
        self.next_lvl_rect = self.next_lvl.get_rect(topleft= (110, 290))
        self.key_sound = pygame.mixer.Sound(KEYBOARD_SOUND)
        self.wrong_sound = pygame.mixer.Sound(WRONG_SOUND)
        self.correct_sound = pygame.mixer.Sound(CORRECT_SOUND)
        self.completed = False

    def run(self, screen):
        screen.blit(self.background, (110,100))
        screen.blit(self.input, (336,600))
        screen.blit(self.submit, self.submit_rect)
        
    def update(self, event, screen):
        screen.blit(self.input, (336,600))
        screen.blit(self.submit, (620,610))
        
class SortTheDate(Level):
    def __init__(self):
        super().__init__()
        self.objects = [pygame.image.load('assets/cup.png').convert_alpha(),
                        pygame.image.load('assets/elephant.png').convert_alpha(),
                        pygame.image.load('assets/ring.png').convert_alpha(),
                        pygame.image.load('assets/snake.png').convert_alpha(),
                        ]

        self.objects = [pygame.transform.scale(_, (OBJECT_WIDTH, OBJECT_HEIGHT)) for _ in self.objects]
        self.codes = [32,53,75,15]
        self.codes = [self.small_font.render(str(_), False, (255,255,255)) for _ in self.codes]
        self.clue = [self.small_font.render(text, True, (0, 0, 0)) for text in ['To solve this riddle,','you must arrange,','key is the father,','when he first breathe,']]
        self.objects_rendered = False
        self.message = 'PASSCODE'
        self.user_text = self.small_font.render(self.message, True, (0,0,0))
        self.instruction = self.small_font.render("Enter the passcode below then press submit button", True, (0,0,0))

    def run(self, screen):
        if self.objects_rendered is False:
            super().run(screen)
            screen.blit(self.user_text, (359,658))
            y = 110
            for c in self.clue:
                screen.blit(c, (338,y))
                y+=25
                
            cordinates = ((205,237), (353,430), (512,273), (706,331))
            for object, coordinate, code in zip(self.objects, cordinates, self.codes):
                screen.blit(object, coordinate)
                screen.blit(code, (coordinate[0]+90, coordinate[1]+75))

            screen.blit(self.instruction, (280,220))
            self.objects_rendered = True
       

    
    def update(self, event, screen):
        if not self.completed:
            if event.type == pygame.KEYDOWN:
                channel = self.key_sound.play()
                channel.fadeout(300)
                if event.key == pygame.K_BACKSPACE:
                    self.message = self.message[:-1]
                else:
                    if len(self.message) <= 8 and event.unicode.isnumeric(): self.message += event.unicode
                super().update(event, screen)
                self.user_text = self.small_font.render(self.message, True, (0,0,0))
                screen.blit(self.user_text, (359,658))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if self.submit_rect.collidepoint(pos):self.check_win(screen)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.completed:
            pos = pygame.mouse.get_pos()
            if self.next_lvl_rect.collidepoint(pos): return True
        return False

    def check_win(self, screen):
        if self.message == '32157553': 
            screen.blit(self.next_lvl, self.next_lvl_rect)
            self.completed = True
            self.correct_sound.play()
        else:
            screen.blit(self.wrong, (730,170)) 
            self.wrong_sound.play()
    
class GetTheColor(Level):
    def __init__(self):
        super().__init__()

        self.objects = [
            pygame.Surface((50,50)) for i in range(5) ]

        for i, color in enumerate([ (255,255,255),(0,0,255), (255,0,0), (0,255,0), (0,0,0)]):
            self.objects[i].fill(color)

        switch_on = pygame.image.load('assets/on.png')
        switch_off = pygame.image.load('assets/off.png')
        self.switch_on = pygame.transform.scale(switch_on, (45,45))
        self.switch_off = pygame.transform.scale(switch_off, (45,45))
        self.swich_board = pygame.Rect((340, 250), (150*3,70*5))
        self.grid = [[False for _ in range(3)] for _ in range(5)]
        self.objects_rendered = False
        self.clue = [self.small_font.render(text, True, (0, 0, 0)) for text in ['To solve this riddle,','think about color,','only two values,','max and min,']]
        self.instruction = self.small_font.render("Tap on the switch to toggle ", True, (0,0,0))

    def run(self, screen):
        if self.objects_rendered is False:
            super().run(screen)
            self.draw_switches(screen)
            for object, y in zip(self.objects, range(250, 250+(70*5), 70)):
                screen.blit(object, (220, y))                
            y = 110
            for c in self.clue:
                screen.blit(c, (338,y))
                y+=25
            screen.blit(self.instruction, (280,220))
            self.objects_rendered = True

    def draw_switches(self, screen):
        for i in range(5):
            y = (self.swich_board.y) + (i*70)
            for j in range(3):
                x = (self.swich_board.x) + (j*150)
                screen.blit(self.switch_off, (x,y))

    def update(self, event, screen):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.completed:
            pos = pygame.mouse.get_pos()
            if self.next_lvl_rect.collidepoint(pos): return True
        if not self.completed:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                x,y = (pos[0] - 340) // 150 , (pos[1] - 250) // 70
                if x in range(3) and y in range(5):
                    self.grid[y][x] = not self.grid[y][x]
                    pos_x, pos_y = 340 + (x*150), 250 + (y*70)
                    if self.grid[y][x]:
                        screen.blit(self.switch_on, (pos_x, pos_y))
                    else:
                        screen.blit(self.switch_off, (pos_x, pos_y))
                self.check_win(screen)
        return False
                
    def check_win(self, screen):
        valid = [[True, True, True], [False, False, True], [True, False, False], [False, True, False], [False, False, False]]
        if self.grid == valid: 
            screen.blit(self.next_lvl, self.next_lvl_rect)
            self.completed = True
            self.correct_sound.play()

class CeaserCipher(Level):
    def __init__(self):
        super().__init__()
        self.coded_msg = self.med_font.render("BRX ZRQ", True, ("#252422"))
        self.message = "DECRYPT MESSAGE HERE"
        self.user_text = self.small_font.render(self.message, True, (0,0,0))
        self.instruction = self.small_font.render("Think and Decrypt", True, (0,0,0))
        self.clue = [self.small_font.render(text, True, (0, 0, 0)) for text in ['A famous cryptography,','back in time,','when friend stabbed']]
        self.objects_rendered = False
        self.completed = False

    def run(self, screen):
        if not self.objects_rendered:
            super().run(screen)
            y = 110
            for c in self.clue:
                screen.blit(c, (338,y))
                y+=25
            screen.blit(self.instruction, (280,220))
            screen.blit(self.coded_msg, (180, 360))
            screen.blit(self.user_text, (370,650))
            self.objects_rendered = True

    def update(self, event, screen):
        if not self.completed:
            if event.type == pygame.KEYDOWN:
                self.key_sound.play()
                if event.key == pygame.K_BACKSPACE:
                    self.message = self.message[:-1]
                else:
                    if len(self.message) < 8 and not event.unicode.isnumeric(): self.message += event.unicode.upper()
                super().update(event, screen)
                self.user_text = self.small_font.render(self.message, True, (0,0,0))
                screen.blit(self.user_text, (370,650))
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if self.submit_rect.collidepoint(pos):self.check_win(screen)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.completed:
            pos = pygame.mouse.get_pos()
            if self.next_lvl_rect.collidepoint(pos): return True
        return False

    def check_win(self, screen):
        if self.message == 'YOU WON': 
            screen.blit(self.next_lvl, self.next_lvl_rect)
            self.completed = True
            self.correct_sound.play()
        else:
            screen.blit(self.wrong, (730,170))
            self.wrong_sound.play()  

class ThinkBinary(Level):
    def __init__(self):
        super().__init__()
        switch_on = pygame.image.load('assets/on.png')
        self.switch_on = pygame.transform.scale(switch_on, (60,60))
        switch_off = pygame.image.load('assets/off.png')
        self.switch_off = pygame.transform.scale(switch_off, (60,60))
        self.swich_board = pygame.Rect((190, 260), (80*8,80*4))
        self.grid = [[False for _ in range(8)] for i in range(4)]
        self.objects_rendered = False
        self.completed = False
        self.instruction = self.small_font.render("Flip Switches to solve.", True, (0,0,0))
        self.clue = [self.small_font.render(text, True, (0, 0, 0)) for text in ['answEr is simple,','each rOw is a letter,','coNvert the letter','to approPriate form,']]

    
    def run(self, screen):
        if not self.objects_rendered:
            super().run(screen)
            self.draw_switches(screen)
            screen.blit(self.instruction, (280,220))
            y = 110
            for c in self.clue:
                screen.blit(c, (338,y))
                y+=25
            self.objects_rendered = True

            
    
    def draw_switches(self, screen):
        for i in range(4):
            y = (self.swich_board.y) + (i*80)
            for j in range(8):
                x = (self.swich_board.x) + (j*80)
                screen.blit(self.switch_off, (x,y))
    
    def update(self, event, screen):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.completed:
            pos = pygame.mouse.get_pos()
            if self.next_lvl_rect.collidepoint(pos): return True
        if not self.completed:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                x,y = (pos[0] - 190) // 80 , (pos[1] - 260) // 80
                if x in range(8) and y in range(4):
                    self.grid[y][x] = not self.grid[y][x]
                    pos_x, pos_y = 190 + (x*80), 260 + (y*80)
                    if self.grid[y][x]:
                        screen.blit(self.switch_on, (pos_x, pos_y))
                    else:
                        screen.blit(self.switch_off, (pos_x, pos_y))
                self.check_win(screen)
        return False    
    
    def check_win(self, screen):
        valid = [
            [False, True, False, False, True, True, True, True],
            [False, True, False, True, False, False, False, False],
            [False, True, False, False, False, True, False, True],
            [False, True, False, False, True, True, True, False]
        ]
        if self.grid == valid:
            screen.blit(self.next_lvl, self.next_lvl_rect)
            self.completed = True
            self.correct_sound.play()
            
class ThinkAscii(Level):
    def __init__(self):
        super().__init__()
        self.nums = self.seg_font.render("0 1 2 3 4 5 6 7 8 9", True, (200,0,0))
        num_rect = self.nums.get_rect()
        num_rect.inflate_ip(20, 20)
        self.bg_surf = pygame.Surface((num_rect.width, num_rect.height))
        print(num_rect.width, num_rect.height)
        self.bg_surf.fill((0,0,0))
        self.mover = pygame.image.load("assets/Dragon.png")
        self.completed = False
        self.instruction = self.small_font.render("Use Left-Right Arrows to move and Space to select", True, (0,0,0))
        self.clue = [self.small_font.render(text, True, (0, 0, 0)) for text in ['answEr is simple,','each rOw is a letter,','coNvert the letter','to approPriate form,']]
        self.objects_rendered = False
        self.mover_rect = self.mover.get_rect()
        self.text = ""
    
    def run(self, screen):
        if not self.objects_rendered:
            super().run(screen)

            screen.blit(self.bg_surf, (180, 340))
            screen.blit(self.nums, (190,350))
            screen.blit(self.instruction, (280,220))
            screen.blit(self.mover, (180,380))

            self.objects_rendered = True
        pass
    def update(self, event, screen):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.completed:
            pos = pygame.mouse.get_pos()
            if self.next_lvl_rect.collidepoint(pos): return True
        if not self.completed:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and self.mover_rect.x > 247:
                    print("Das")
                    screen.blit(self.mover, (self.mover_rect.x + 67, 380))                
                if event.key == pygame.K_LEFT:
                    print("Dass")

                    screen.blit(self.mover, (self.mover_rect.x - 67, 380))
        return False

    def check_win(self):
        pass   



