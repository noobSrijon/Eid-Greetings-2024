import pygame
import random
import math

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
COLORS = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (128, 0, 128)]


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Eid Mubarak Animation")

font = pygame.font.Font('ubuntu.ttf', 80)
text_surface = font.render("Eid Mubarak", True, WHITE)
black = (0, 0, 0)
gray = (200, 200, 200)

class Firecracker:

    def __init__(self):
        self.x = random.randint(100, SCREEN_WIDTH - 100)
        self.y = SCREEN_HEIGHT
        self.color = random.choice(COLORS)
        self.speed = random.uniform(10, 15)
        self.size = random.randint(3, 5)

    def move(self):
        self.y -= self.speed

    def explode(self):
        particles = []
        num_particles = random.randint(30, 50)
        for _ in range(num_particles):
            angle = random.uniform(0, 2 * math.pi)
            speed = random.uniform(2, 5)
            particle = {
                'x': self.x,
                'y': self.y,
                'vx': speed * math.cos(angle),
                'vy': speed * math.sin(angle),
                'radius': random.randint(2, 4),
                'color': self.color,
                'life': random.randint(20, 40)
            }
            particles.append(particle)
        return particles

class Star:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.size = random.randint(1, 3)
        self.color = WHITE

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.size)


class Moon:
    def __init__(self):
        self.x = 600  
        self.y = 150  
        self.radius = 80
        self.color = GREY

    def draw(self):
        moon_center = (self.x, self.y)
        moon_radius = self.radius
        tilt_angle = math.radians(45) 

        
        outer_center = (self.x, self.y)
        inner_center = (moon_center[0] - moon_radius * math.cos(tilt_angle),
                        moon_center[1] - moon_radius * math.sin(tilt_angle))

        pygame.draw.circle(screen, gray, outer_center, moon_radius)

        inner_radius = moon_radius * 0.6  


        pygame.draw.circle(screen, black, inner_center, self.radius)

    


firecrackers = []
stars = [Star() for _ in range(50)]  
moon = Moon() 

particles = []


clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill(BLACK)


    for star in stars:
        star.draw()
    moon.draw()


    for i in range(len("Eid Mubarak")):

        color = random.choice(COLORS)
        text = font.render("Eid Mubarak"[i], True, color)

        text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        text_rect.x += (i - len("Eid Mubarak") / 2) * 40

    
        screen.blit(text, text_rect)

    if random.random() < 0.02:
        firecracker = Firecracker()
        firecrackers.append(firecracker)


    for firecracker in firecrackers:
        firecracker.move()
        pygame.draw.circle(screen, firecracker.color, (firecracker.x, int(firecracker.y)), firecracker.size)
        if firecracker.y <= random.randint(100, 200):
            particles.extend(firecracker.explode())
            firecrackers.remove(firecracker)


    for particle in particles:
        pygame.draw.circle(screen, particle['color'], (int(particle['x']), int(particle['y'])), particle['radius'])
        particle['x'] += particle['vx']
        particle['y'] += particle['vy']
        particle['life'] -= 1
        if particle['life'] <= 0:
            particles.remove(particle)


    pygame.display.flip()

    clock.tick(30)  


pygame.quit()
