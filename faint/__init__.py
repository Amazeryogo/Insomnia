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
        self.inventory = []

    def get_inventory(self): return self.inventory

    def add_item_to_inventory(self, item): self.inventory.append(item)

    def remove_item(self, item): self.inventory.remove(item)

    def is_item_in_inventory(self, item): return item in self.inventory

    def move_forward(self): self.rect.x += self.speed

    def move_backward(self): self.rect.x -= self.speed

    def move_up(self): self.rect.y -= self.speed

    def move_down(self): self.rect.y += self.speed

    def draw(self, screen): screen.blit(self.image, self.rect)

    def add_point(self): self.points += 1

    def remove_health(self): self.health -= 1

    def remove_points(self): self.points -= 1

    def get_points(self): return self.points

    def add_health(self):
        if self.health < 3: self.health += 1

    def get_health(self): return self.health


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


def draw_hearts(screen, x, y, main_character, image):
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

    def add_in_user_inventory(self, main_character): main_character.add_item(self)


class Ghost(NonUserControlledObject):
    def __init__(self, image, screen):
        super().__init__(0, 0, 0, image)
        self.speed = 0
        self.image = pygame.image.load("ghost.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.x += self.speed
        self.rect.y += self.speed
        self.draw(screen)
        self.health = 3
        self.getting_damage = False

    def movement(self):
        self.rect.x += self.speed
        self.rect.y += self.speed

    def speak(self, screen, text):
        font = pygame.font.SysFont("comicsansms", 30)
        text = font.render(text, True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (self.rect.x + 25, self.rect.y + 25)
        screen.blit(text, text_rect)

    def attack(self, main_character):
        if 50 > main_character.rect.x - self.rect.x > -50 and self.getting_damage == False:
            if 50 > main_character.rect.y - self.rect.y > -50 and self.getting_damage == False:
                main_character.health -= 1