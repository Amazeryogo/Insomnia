import random

import pygame
import json

with open('config.json', 'r') as f:
    xsf = json.load(f)


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
        self.inventory = []
        self.saber = False

    def get_inventory(self):
        return self.inventory

    def add_item_to_inventory(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        self.inventory.remove(item)

    def is_item_in_inventory(self, item):
        return item in self.inventory

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

    def attack(self, enemy):
        if self.saber == True:
            enemy.remove_health()


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
        self.health = 3

    def add_health(self):
        if self.health < 2: self.health += 1

    def remove_health(self): self.health -= 1

    def movement(self):
        self.rect.x += self.speed
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def get_rect(self):
        return self.rect


def draw_hearts(screen, x, y, obj, image):
    if obj.health == 3:
        life1 = pygame.image.load(image)
        life1 = pygame.transform.scale(life1, (50, 50))
        life1_rect = life1.get_rect()
        life1_rect.x = x
        life1_rect.y = y
        screen.blit(life1, life1_rect)
        life2 = pygame.image.load(image)
        life2 = pygame.transform.scale(life2, (50, 50))
        life2_rect = life2.get_rect()
        life2_rect.x = x + 50
        life2_rect.y = y
        screen.blit(life2, life2_rect)
        life3 = pygame.image.load(image)
        life3 = pygame.transform.scale(life3, (50, 50))
        life3_rect = life3.get_rect()
        life3_rect.x = x + 100
        life3_rect.y = y
        screen.blit(life3, life3_rect)
    if obj.health == 2:
        life1 = pygame.image.load(image)
        life1 = pygame.transform.scale(life1, (50, 50))
        life1_rect = life1.get_rect()
        life1_rect.x = x
        life1_rect.y = y
        screen.blit(life1, life1_rect)
        life2 = pygame.image.load(image)
        life2 = pygame.transform.scale(life2, (50, 50))
        life2_rect = life2.get_rect()
        life2_rect.x = x + 50
        life2_rect.y = y
        screen.blit(life2, life2_rect)
    if obj.health == 1:
        life1 = pygame.image.load(image)
        life1 = pygame.transform.scale(life1, (50, 50))
        life1_rect = life1.get_rect()
        life1_rect.x = x
        life1_rect.y = y
        screen.blit(life1, life1_rect)
    if obj.health == 0:
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

    def draw(self, screen): screen.blit(self.image, self.rect)

    def get_rect(self): return self.rect


class HealthPoints(StaticObject):
    def __init__(self, x, y, image, screen):
        super().__init__(x, y, image)
        self.health = 3
        self.speed = 0
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.x += self.speed
        self.rect.y += self.speed
        self.draw(screen)

    def movement(self):
        self.rect.x += self.speed
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def get_rect(self):
        return self.rect


class Key(StaticObject):
    def __init__(self, x, y, image, screen):
        super().__init__(x, y, image)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.draw(screen)

    def draw(self, screen): screen.blit(self.image, self.rect)

    def get_rect(self): return self.rect


class Saber(StaticObject):
    def __init__(self, x, y, image, screen):
        super().__init__(x, y, image)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.draw(screen)
        self.acquired = False

    def draw(self, screen): screen.blit(self.image, self.rect)

    def get_rect(self): return self.rect


class Textbox:
    def __init__(self, x, y, x1, y1, font):
        self.rect = None
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.font = font

    def add_text(self, text, screen,x,y):
        screen.blit(self.font.render(text, True, (255, 255, 255)), (x,y))


# general functions to make the main file less bloated. named after the admiral general of the marines
class Sakazuki:
    def __init__(self):
        pass

    @staticmethod
    def check_collision(obj1, obj2):
        if obj1.rect.colliderect(obj2.rect):
            return True
        else:
            return False

    @staticmethod
    def overflow(x, y, obj):
        if obj.rect.x > x:
            obj.rect.x = 0
        elif obj.rect.y > y:
            obj.rect.y = 0
        elif obj.rect.x < 0:
            obj.rect.x = 0
        elif obj.rect.y < 0:
            obj.rect.y = 0
