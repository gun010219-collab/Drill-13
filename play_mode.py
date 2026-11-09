import game_framework
import title_mode
from pico2d import *
import game_world
from boy import Boy
from grass import Grass


paused = False
pause_image = None
inventory_open = False
inventory_key_down = False


def handle_events():
    global boy, paused, inventory_open, inventory_key_down

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            if not inventory_key_down:
                inventory_open = not inventory_open
                inventory_key_down = True
            continue
        elif event.type == SDL_KEYUP and event.key == SDLK_i:
            inventory_key_down = False
            continue
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
            return
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            paused = not paused
            return
        elif paused:
            if event.type == SDL_KEYUP:
                boy.handle_event(event)
            continue
        else:
            boy.handle_event(event)



def init():
    global boy, paused, pause_image, inventory_open, inventory_key_down

    game_world.clear()
    paused = False
    inventory_open = False
    inventory_key_down = False
    pause_image = load_image('pause.png')
    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)



def update():
    if not paused:
        game_world.update()


def render():
    clear_canvas()
    game_world.render()
    if paused:
        pause_image.draw(400, 300)
    if inventory_open:
        draw_inventory()
    update_canvas()


def draw_inventory():
    draw_rectangle(530, 120, 780, 480, 20, 32, 52, 255, True)
    draw_rectangle(530, 120, 780, 480, 75, 195, 205, 255)
    draw_rectangle(545, 410, 765, 450, 33, 54, 75, 255, True)
    draw_rectangle(545, 400, 765, 402, 75, 195, 205, 255, True)

    for row in range(3):
        for column in range(3):
            left = 555 + column * 70
            bottom = 175 + row * 70
            draw_rectangle(left, bottom, left + 58, bottom + 58,
                           38, 58, 78, 255, True)
            draw_rectangle(left, bottom, left + 58, bottom + 58,
                           100, 145, 160, 255)


def finish():
    global pause_image
    game_world.clear()
    del pause_image
