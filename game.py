import random
from pygame import Rect

WIDTH = 800
HEIGHT = 450
TITLE = "Err@ 410"

GRAVITY = 0.8
JUMP_FORCE = -12
MOVE_SPEED = 3

GAME_MENU = "menu"
GAME_PLAYING = "playing"
GAME_GAME_OVER = "game_over"
GAME_WIN = "win"

game_state = GAME_MENU
sound_on = True

# MUSICA
current_music = None
def play_music(name):
    global current_music
    if not sound_on:
        music.stop()
        current_music = None
        return

    if current_music != name:
        music.stop()
        music.play(name)
        current_music = name


# BOTOES
retry_button = Rect((WIDTH//2 - 100, HEIGHT//2 + 50), (200, 50))
menu_back = Rect((WIDTH//2 - 100, HEIGHT//2 + 50), (200, 50))
sound_button = Rect((WIDTH - 80, 10), (50, 50))



# ================= ANIMATION =================

class SpriteAnimation:
    def __init__(self, frames, speed):
        self.frames = frames
        self.speed = speed
        self.timer = 0
        self.index = 0

    def update(self):
        self.timer += 1
        if self.timer >= self.speed:
            self.timer = 0
            self.index = (self.index + 1) % len(self.frames)

    def get_frame(self):
        return self.frames[self.index]


# HEROI
class Hero:
    def __init__(self, pos):
        self.actor = Actor("hero_idle_0", pos)
        self.velocity_y = 0
        self.on_ground = False
        self.has_key = False
        self.spawn_protection = 30

        self.jump_sprite = "hero_jump"
        self.idle_animation = SpriteAnimation(["hero_idle_0", "hero_idle_1"], 150)
        self.walk_animation = SpriteAnimation(["hero_walk_0", "hero_walk_1"], 10)
        self.facing_right = True

        # Footstep com delay
        self.footstep_cooldown = 0
        self.footstep_delay = 15  # frames

    def update(self, platforms):
        moving = False

        if keyboard.left:
            self.actor.x -= MOVE_SPEED
            moving = True
            self.facing_right = False
        if keyboard.right:
            self.actor.x += MOVE_SPEED
            moving = True
            self.facing_right = True

        self.apply_gravity(platforms)

        if not self.on_ground:
            self.actor.image = self.jump_sprite
        else:
            if moving:
                self.walk_animation.update()
                self.actor.image = self.walk_animation.get_frame()
                if self.footstep_cooldown == 0 and sound_on:
                    sounds.footstep.play()
                    self.footstep_cooldown = self.footstep_delay
            else:
                self.idle_animation.update()
                self.actor.image = self.idle_animation.get_frame()

        if self.footstep_cooldown > 0:
            self.footstep_cooldown -= 1

        self.actor.flip_h = not self.facing_right

        if self.spawn_protection > 0:
            self.spawn_protection -= 1

    def apply_gravity(self, platforms):
        self.velocity_y += GRAVITY
        self.actor.y += self.velocity_y
        self.on_ground = False

        for platform in platforms:
            rect = platform["rect"]
            if self.actor.colliderect(rect) and self.velocity_y > 0:
                self.actor.bottom = rect.top
                self.velocity_y = 0
                self.on_ground = True

    def jump(self):
        if self.on_ground:
            self.velocity_y = JUMP_FORCE




# INIMIGOS
class Enemy:
    def __init__(self, left_limit, right_limit, y):
        self.left_limit = left_limit
        self.right_limit = right_limit

        start_x = (left_limit + right_limit) // 2
        self.actor = Actor("enemy_idle_1", (start_x, y))

        self.speed = random.choice([-2, 2])
        self.active = False

        self.idle_animation = SpriteAnimation(["enemy_idle_1", "enemy_idle_0"], 150)
        self.walk_animation = SpriteAnimation(["enemy_walk_0", "enemy_walk_1"], 12)

    def update(self, hero):
        if not self.active:
            if self.left_limit - 10 <= hero.actor.x <= self.right_limit + 10:
                self.active = True
            else:
                self.idle_animation.update()
                self.actor.image = self.idle_animation.get_frame()
                return

        self.actor.x += self.speed

        if self.actor.centerx <= self.left_limit:
            self.actor.centerx = self.left_limit
            self.speed = abs(self.speed)
        elif self.actor.centerx >= self.right_limit:
            self.actor.centerx = self.right_limit
            self.speed = -abs(self.speed)

        self.walk_animation.update()
        self.actor.image = self.walk_animation.get_frame()


class FlyingEnemy:
    def __init__(self, x, top_limit, bottom_limit):
        self.actor = Actor("enemy_flying_0", (x, top_limit))
        self.top_limit = top_limit
        self.bottom_limit = bottom_limit
        self.speed = 1
        self.direction = 1

        self.animation = SpriteAnimation(
            ["enemy_flying_0", "enemy_flying_1"], 12
        )

    def update(self):
        self.actor.y += self.speed * self.direction

        if self.actor.y <= self.top_limit:
            self.actor.y = self.top_limit
            self.direction = 1
        elif self.actor.y >= self.bottom_limit:
            self.actor.y = self.bottom_limit
            self.direction = -1

        self.animation.update()
        self.actor.image = self.animation.get_frame()



# ENTIDADES
hero = Hero((100, 300))

platforms = [
    {"rect": Rect((30, 400), (730, 20)), "sprite": "platform_0"}, # CHÃO
    {"rect": Rect((220, 320), (170, 20)), "sprite": "platform_1"}, # PLAT1
    {"rect": Rect((450, 250), (150, 20)), "sprite": "platform_1"}, # PLAT2 (BAU)
    {"rect": Rect((190, 180), (200, 20)), "sprite": "platform_1"}, # PLAT3
    {"rect": Rect((20, 110), (120, 20)), "sprite": "platform_1"}, # PLAT 4 (CHAVE)
]

enemies = [
    Enemy(180, 700, 390), # NO CHÃO
    Enemy(200, 380, 170) # NA PLAT 3
]

flying_enemies = [
    FlyingEnemy(420, 100, 250), # ENTRE PLAT1 E 2
    FlyingEnemy(170, 60, 170) # ENTRE PLAT3 E 4
]

spikes = [
    Actor("spike", (270, 310)), # NA PLAT1
    Actor("spike", (350, 310)), # NA PLAT1
    Actor("spike", (100, 100)) # NA PLAT4
]

key = Actor("key", (40, 100))
key_collected = False
chest = Actor("chest", (580, 240))

buttons = {
    "Iniciar": Rect((300, 180), (200, 50)),
    "Sair": Rect((300, 260), (200, 50)),
}



# RENDERIZAR
def draw_platform(platform):
    sprite_name = platform["sprite"]
    rect = platform["rect"]

    sprite_image = getattr(images, sprite_name)
    tile_w = sprite_image.get_width()
    y = rect.top

    for x in range(rect.left, rect.right, tile_w):
        screen.blit(sprite_name, (x, y))

def draw():
    screen.clear()

    if game_state == GAME_MENU:
        draw_menu()
    elif game_state == GAME_PLAYING:
        draw_game()
    elif game_state == GAME_GAME_OVER:
        draw_center_text("Aniquilado!", "red")
        screen.draw.filled_rect(retry_button, (60, 60, 60))
        screen.draw.text("Tentar novamente", center=retry_button.center, fontsize=25)
    elif game_state == GAME_WIN:
        draw_center_text("Erro concertado!", "green")
        screen.draw.filled_rect(menu_back, (60, 60, 60))
        screen.draw.text("Voltar ao menu", center=menu_back.center, fontsize=25)

    if sound_on:
        screen.draw.text("Som: on", center=sound_button.center, fontsize=30)
    else:
        screen.draw.text("Som: off", center=sound_button.center, fontsize=30)



def draw_menu():
    screen.draw.text("Err@ 410", center=(WIDTH // 2, 100), fontsize=60)
    for name, rect in buttons.items():
        screen.draw.filled_rect(rect, (60, 60, 60))
        screen.draw.text(name.upper(), center=rect.center, fontsize=30)


def draw_game():
    for platform in platforms:
        draw_platform(platform)

    if not key_collected:
        screen.draw.text("PEGUE A CHAVE", center=(WIDTH // 2, 40), fontsize=30, color="yellow")
    if hero.has_key:
        screen.draw.text("ABRA O BAU", center=(WIDTH // 2, 40), fontsize=30, color="green")

    screen.draw.text("SETAS: Mover  |  ESPACO: Pular", center=(WIDTH // 2, 20), fontsize=20, color="white")

    if not key_collected:
        key.draw()
    chest.draw()
    hero.actor.draw()

    for enemy in enemies:
        enemy.actor.draw()
    for fe in flying_enemies:
        fe.actor.draw()
    for spike in spikes:
        spike.draw()

    if sound_on:
        screen.draw.text("Som: on", center=sound_button.center, fontsize=30)
    else:
        screen.draw.text("Som: off", center=sound_button.center, fontsize=30)


def draw_center_text(text, color):
    screen.draw.text(text, center=(WIDTH // 2, HEIGHT // 2), fontsize=60, color=color)



# UPDATES
def update():
    global game_state, key_collected, current_music  # Adicionado current_music aqui

    if game_state == GAME_MENU:
        play_music("menu_music")
        return  # Retorna aqui para não executar o resto do update no menu

    elif game_state == GAME_PLAYING:
        # Apenas toca música do jogo se não estiver tocando
        if current_music != "game_music" and sound_on:
            play_music("game_music")
        
        # Resto da lógica do jogo...
        hero.update(platforms)
        
        if hero.actor.y > HEIGHT:
            if sound_on: sounds.defeat.play()
            game_state = GAME_GAME_OVER

        for enemy in enemies:
            enemy.update(hero)
            if hero.spawn_protection == 0 and hero.actor.colliderect(enemy.actor):
                if sound_on: sounds.defeat.play()
                game_state = GAME_GAME_OVER

        for fe in flying_enemies:
            fe.update()
            if hero.spawn_protection == 0 and hero.actor.colliderect(fe.actor):
                if sound_on: sounds.defeat.play()
                game_state = GAME_GAME_OVER

        for spike in spikes:
            if hero.actor.colliderect(spike):
                if sound_on: sounds.defeat.play()
                game_state = GAME_GAME_OVER

        if not key_collected and hero.actor.colliderect(key):
            if sound_on: sounds.key.play()
            key_collected = True
            hero.has_key = True

        if hero.has_key and hero.actor.colliderect(chest):
            if sound_on: sounds.chest.play()
            if sound_on: sounds.win.play()
            game_state = GAME_WIN
        
    elif game_state == GAME_GAME_OVER or game_state == GAME_WIN:
        # Para a música nas telas de fim
        if current_music is not None:
            music.stop()
            current_music = None


# INPUTS
def on_key_down(key):
    if game_state == GAME_PLAYING and key == keys.SPACE:
        hero.jump()


def on_mouse_down(pos):
    global game_state, sound_on, current_music
    
    if sound_button.collidepoint(pos):
        sound_on = not sound_on
        if not sound_on:
            music.stop()
            current_music = None
        else:
            # Se ligou o som e está no menu, toca música do menu
            if game_state == GAME_MENU:
                play_music("menu_music")
        return

    if game_state == GAME_MENU:
        if buttons["Iniciar"].collidepoint(pos):
            if sound_on: sounds.start.play()
            game_state = GAME_PLAYING
        elif buttons["Sair"].collidepoint(pos):
            if sound_on: sounds.click.play()
            exit()
    elif game_state == GAME_GAME_OVER:
        if retry_button.collidepoint(pos):
            if sound_on: sounds.start.play()
            restart_game()
    elif game_state == GAME_WIN:
        if menu_back.collidepoint(pos):
            if sound_on: sounds.click.play()
            game_state = GAME_MENU


# RESTART
def restart_game():
    global game_state, key_collected, current_music

    hero.actor.pos = (100, 300)
    hero.velocity_y = 0
    hero.on_ground = False
    hero.has_key = False
    hero.spawn_protection = 30
    hero.footstep_cooldown = 0

    key.pos = (40, 100)
    key_collected = False
    chest.pos = (580, 240)

    for e in enemies:
        e.actor.x = (e.left_limit + e.right_limit) // 2
        e.active = False

    for fe in flying_enemies:
        fe.actor.y = fe.top_limit
        fe.direction = 1

    game_state = GAME_PLAYING
    # Força a música do jogo a tocar
    if sound_on:
        music.stop()
        music.play("game_music")
        current_music = "game_music"