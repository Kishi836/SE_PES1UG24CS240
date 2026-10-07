import pygame
from game.player import Player
from game.world import generate_platforms, update_crumbling, draw_platform, draw_lava

WIDTH,HEIGHT=500,640
FPS=60
BG=(20,15,30)
GROUND_Y=HEIGHT+200
WARN_DIST=200      # 20m (score is px//10)
SURGE_EVERY=720    # a surge every 12s...
SURGE_LEN=120      # ...lasting 2s
SURGE_MULT=3
MAX_LAVA_SPEED=1.2*SURGE_MULT

class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Lava Escape")
        self.clock=pygame.time.Clock()
        self.font=pygame.font.SysFont("monospace",24,bold=True)
        self.big_font=pygame.font.SysFont("monospace",42,bold=True)
        self.reset()

    def reset(self):
        self.platforms=generate_platforms(WIDTH,GROUND_Y)
        self.player=Player(WIDTH//2-16,GROUND_Y-50)
        self.cam_y=GROUND_Y+20-HEIGHT  # ground sits at the bottom of the screen
        self.lava_y=GROUND_Y+WARN_DIST+20  # start just outside the warning range
        self.lava_rise=0.4
        self.lava_speed=self.lava_rise
        self.surging=False
        self.score=0
        self.game_over=False
        self.won=False
        self.top_y=self.platforms[-1].y
        self.frame=0
        self.start_ticks=pygame.time.get_ticks()
        self.elapsed_ms=0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT: return False
            if event.type==pygame.KEYDOWN and event.key==pygame.K_r: self.reset()
        return True

    def update(self):
        if self.game_over or self.won: return
        keys=pygame.key.get_pressed()
        self.player.update(keys,self.platforms,WIDTH)
        self.platforms=update_crumbling(self.platforms,self.player.standing_on,self.frame)
        target=self.player.rect.centery-HEIGHT//2
        if target<self.cam_y: self.cam_y=target
        self.surging=self.frame%SURGE_EVERY>=SURGE_EVERY-SURGE_LEN
        self.lava_speed=self.lava_rise*(SURGE_MULT if self.surging else 1)
        self.lava_y-=self.lava_speed
        self.lava_rise=min(1.2,self.lava_rise+0.0003)
        self.score=max(0,(GROUND_Y-self.player.rect.y)//10)
        self.frame+=1
        self.elapsed_ms=pygame.time.get_ticks()-self.start_ticks  # frozen once the run ends
        if self.player.rect.bottom>=self.lava_y:
            self.game_over=True
        if self.player.rect.top<=self.top_y-20:
            self.won=True

    def draw(self):
        self.screen.fill(BG)
        for p in self.platforms:
            draw_platform(self.screen,p,self.cam_y,self.frame)
        self.player.draw(self.screen,self.cam_y)
        draw_lava(self.screen,self.lava_y,self.cam_y,WIDTH,HEIGHT,self.frame)
        sc=self.font.render(f"Height: {self.score}m  R=Restart",True,(220,200,180))
        self.screen.blit(sc,(8,10))
        ms=self.elapsed_ms
        tm=self.font.render(f"{ms//60000:02}:{ms//1000%60:02}:{ms%1000:03}",True,(220,200,180))
        self.screen.blit(tm,(WIDTH-tm.get_width()-8,10))
        self._danger_meter()
        if not self.game_over and self.lava_y-self.player.rect.bottom<=WARN_DIST:
            self._warning()
        if self.game_over:
            self._msg("LAVA GOT YOU!",(220,80,40))
        if self.won:
            self._msg("ESCAPED!",(80,220,100))
        pygame.display.flip()

    def _danger_meter(self):
        color=(255,40,20) if self.surging else (255,150,0)
        self.screen.blit(self.font.render("LAVA",True,(220,200,180)),(8,40))
        pygame.draw.rect(self.screen,(60,50,60),(72,46,150,16),border_radius=3)
        fill=int(150*min(1,self.lava_speed/MAX_LAVA_SPEED))
        pygame.draw.rect(self.screen,color,(72,46,fill,16),border_radius=3)
        if self.surging:
            self.screen.blit(self.font.render("SURGE!",True,color),(232,40))

    def _warning(self):
        # translucent so the player stays visible behind it
        color=(255,220,0) if (self.frame//15)%2 else (230,40,20)
        s=pygame.Surface((120,105),pygame.SRCALPHA)
        pygame.draw.polygon(s,(*color,190),[(60,0),(120,104),(0,104)])
        ex=self.big_font.render("!",True,(0,0,0))
        s.blit(ex,(60-ex.get_width()//2,62-ex.get_height()//2))
        self.screen.blit(s,(WIDTH//2-60,HEIGHT//2-52))

    def _msg(self,text,color):
        ov=pygame.Surface((WIDTH,HEIGHT),pygame.SRCALPHA)
        ov.fill((0,0,0,150))
        self.screen.blit(ov,(0,0))
        m=self.big_font.render(text,True,color)
        s=self.font.render("Press R to Play Again",True,(200,200,200))
        self.screen.blit(m,(WIDTH//2-m.get_width()//2,HEIGHT//2-40))
        self.screen.blit(s,(WIDTH//2-s.get_width()//2,HEIGHT//2+20))

    def run(self):
        running=True
        while running:
            running=self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
