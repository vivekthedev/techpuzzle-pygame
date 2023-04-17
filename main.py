import pygame
from levels import SortTheDate, GetTheColor, CeaserCipher, ThinkBinary, ThinkAscii
from settings import *
class Game:
    def __init__(self):
        pygame.init()
        self.width, self.height = WIDTH, HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.image.load('assets/Background.png').convert()
        self.start_button_background = pygame.image.load('assets/btn-back.png').convert_alpha()
        self.background = pygame.transform.scale(self.background, (self.screen.get_width(), self.screen.get_height()))
        self.title = "TechPuzzle"
        pygame.display.set_caption(self.title.upper())
        self.font = pygame.font.Font(MAIN_FONT, 60)
        self.start_button = pygame.Rect((self.width / 2) - 100, (self.height / 2) - 25, 200, 50)
        self.current_level = None
        self.signal = False
        self.end_screen = pygame.image.load('assets/end_screen.png')
        self.finished = False
        pygame.mixer.music.load(BG_MUSIC)

    def run(self):
        pygame.mixer.music.play(-1)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if self.current_level:
                    self.signal = self.current_level.update(event, self.screen)
                else:    
                    if not self.finished:
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            mouse_pos = pygame.mouse.get_pos()
                            if self.btn_back_rect.collidepoint(mouse_pos):
                                self.start_game()
                # if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                #     # print(pygame.mouse.get_pos())
            if not self.finished:
                if self.signal:
                    self.start_game()

            if self.current_level:
                self.current_level.run(self.screen)
            else:
                if not self.finished:
                    self.screen.blit(self.background, (0, 0))
                    self.draw_title()
                    self.draw_start_button()
            pygame.display.update()

    def draw_title(self):
        text = self.font.render(self.title, True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.width / 2, 50))
        self.screen.blit(text, text_rect)

    def draw_start_button(self):
        text = self.font.render("Start", True, (255, 255, 255))
        text_rect = text.get_rect(center=self.start_button.center)
        self.btn_back_rect = self.start_button_background.get_rect(center=self.start_button.center)
        self.screen.blit(self.start_button_background, self.btn_back_rect)
        self.screen.blit(text, text_rect)

    def start_game(self):
        if self.current_level is None:
            self.load_levels()
            self.level_gen = self.get_level()
        
        try:
            self.signal = False
            self.current_level = next(self.level_gen)
        except:
            self.game_finished()

    
    def load_levels(self):
        self.levels = [SortTheDate(), GetTheColor(), CeaserCipher(), ThinkBinary(), ThinkAscii()]
        # self.levels = [ThinkAscii()]
            
    def get_level(self):
        for level in self.levels:
            yield level
        
    def game_finished(self):
        self.screen.fill(('#e76f51'))
        self.screen.blit(self.end_screen, (100,50))
        self.finished = True
        self.current_level = None
        print("Congratulations")
    


if __name__ == '__main__':
    game = Game()
    game.run()
