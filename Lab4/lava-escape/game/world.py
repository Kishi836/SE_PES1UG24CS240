import pygame
import random

PLATFORM_COLOR = (100,80,50)
CRUMBLE_COLOR = (165,140,105)
SPRING_COLOR = (25,45,130)
LAVA_COLOR = (220,60,20)
MAX_EDGE_GAP = 80
CRACK_START = 60          # frames (1s) before cracks appear

class Platform(pygame.Rect):
    kind = "normal"
    touched = None        # frame the player first landed on it
    life = 0              # frames from first landing until it breaks

def generate_platforms(width, base_y, count=30):
    plats = [Platform(0, base_y, width, 20)]  # ground
    y = base_y - 110
    for i in range(count):
        w = random.randint(80,200)
        # keep the next platform within jump reach (max jump ~135px up, ~128px across at 115px up)
        prev = plats[-1]
        x = random.randint(max(0, prev.left-w-MAX_EDGE_GAP), min(width-w, prev.right+MAX_EDGE_GAP))
        p = Platform(x, y, w, 16)
        r = random.random()
        if i < count-1 and r < 0.25:  # top platform stays solid
            p.kind = "crumble"
            # 3s at the bottom, shrinking linearly to 1.8s at the top
            p.life = int(60 * (3.0 - 1.2 * i / (count-1)))
        elif i < count-1 and r < 0.37:
            p.kind = "spring"
        plats.append(p)
        y -= random.randint(80,115)
    return plats

def update_crumbling(platforms, standing_on, frame):
    if standing_on is not None and standing_on.kind == "crumble" and standing_on.touched is None:
        standing_on.touched = frame
    return [p for p in platforms if p.touched is None or frame - p.touched < p.life]

def draw_platform(screen, p, cam_y, frame):
    dr = p.move(0, -int(cam_y))
    if p.kind == "spring":
        pygame.draw.rect(screen, SPRING_COLOR, dr, border_radius=4)
        cx = dr.centerx
        coil = [(cx + (8 if k % 2 else -8), dr.top - 3 - k*3) for k in range(6)]
        pygame.draw.lines(screen, (255,255,255), False, [(cx, dr.top)] + coil + [(cx, dr.top-20)], 2)
        pygame.draw.rect(screen, (150,150,155), (cx-14, dr.top-24, 28, 5), border_radius=2)
        return
    if p.kind != "crumble":
        pygame.draw.rect(screen, PLATFORM_COLOR, dr, border_radius=4)
        return
    elapsed = 0 if p.touched is None else frame - p.touched
    if elapsed < CRACK_START:
        pygame.draw.rect(screen, CRUMBLE_COLOR, dr, border_radius=4)
        return
    progress = (elapsed - CRACK_START) / max(1, p.life - CRACK_START)
    dr.x += random.randint(-2, 2)  # shake
    pygame.draw.rect(screen, CRUMBLE_COLOR, dr, border_radius=4)
    for k in range(1 + int(progress * 4)):  # more cracks as it nears breaking
        cx = dr.x + dr.width * (k*2+1) // 10
        pygame.draw.lines(screen, (40,30,20), False,
                          [(cx, dr.top), (cx+7, dr.top+5), (cx-6, dr.top+10), (cx+3, dr.bottom)], 3)

def draw_lava(screen, lava_y, cam_y, width, height, frame):
    import math
    ly = int(lava_y - cam_y)
    if ly < height:
        # lava surface wave
        pts=[(0,ly)]
        for x in range(0,width+20,20):
            pts.append((x, ly + int(math.sin(x*0.08+frame*0.1)*8)))
        pts.append((width,height)); pts.append((0,height))
        pygame.draw.polygon(screen,LAVA_COLOR,pts)
        # glow
        s=pygame.Surface((width,30),pygame.SRCALPHA)
        for i in range(15):
            pygame.draw.line(s,(255,100,0,max(0,60-i*4)),(0,i),(width,i),1)
        screen.blit(s,(0,ly-15))
