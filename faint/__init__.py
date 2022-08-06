import pygame


class UserControlledObject:
    def __init__(self, x, y, speed, image_a, points, health, image_b=None):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load(image_a)
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.points = points
        self.health = health

    def move_forward(self):
        self.rect.x += self.speed

    def move_backward(self):
        self.rect.x -= self.speed

    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def add_point(self):
        self.points += 1

    def remove_health(self):
        self.health -= 1

    def remove_points(self):
        self.points -= 1

    def get_points(self):
        return self.points

    def add_health(self):
        if self.health < 3: self.health += 1

    def get_health(self):
        return self.health


class NonUserControlledObject:
    def __init__(self, x, y, speed, image_a, image_b=None):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load(image_a)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def movement(self):
        self.rect.x += self.speed
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def get_rect(self):
        return self.rect


def draw_hearts(screen, x, y, main_character,image):
    if main_character.health == 3:
        life1 = pygame.image.load(image)
        life1 = pygame.transform.scale(life1, (50, 50))
        life1_rect = life1.get_rect()
        life1_rect.x = 0
        life1_rect.y = 0
        screen.blit(life1, life1_rect)
        life2 = pygame.image.load(image)
        life2 = pygame.transform.scale(life2, (50, 50))
        life2_rect = life2.get_rect()
        life2_rect.x = 50
        life2_rect.y = 0
        screen.blit(life2, life2_rect)
        life3 = pygame.image.load(image)
        life3 = pygame.transform.scale(life3, (50, 50))
        life3_rect = life3.get_rect()
        life3_rect.x = 100
        life3_rect.y = 0
        screen.blit(life3, life3_rect)
    if main_character.health == 2:
        life1 = pygame.image.load(image)
        life1 = pygame.transform.scale(life1, (50, 50))
        life1_rect = life1.get_rect()
        life1_rect.x = 0
        life1_rect.y = 0
        screen.blit(life1, life1_rect)
        life2 = pygame.image.load(image)
        life2 = pygame.transform.scale(life2, (50, 50))
        life2_rect = life2.get_rect()
        life2_rect.x = 50
        life2_rect.y = 0
        screen.blit(life2, life2_rect)
    if main_character.health == 1:
        life1 = pygame.image.load(image)
        life1 = pygame.transform.scale(life1, (50, 50))
        life1_rect = life1.get_rect()
        life1_rect.x = 0
        life1_rect.y = 0
        screen.blit(life1, life1_rect)
    if main_character.health == 0:
        pass

class StaticObject:
    def __init__(self, x, y, image_a, image_b=None):
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_a)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def get_rect(self):
        return self.rect
