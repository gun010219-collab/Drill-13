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
item_select_image = None


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
        elif inventory_open and event.type == SDL_KEYDOWN and event.key in (
                SDLK_0, SDLK_1, SDLK_2):
            boy.ball_size = event.key - SDLK_0
            continue
        elif paused:
            if event.type == SDL_KEYUP:
                boy.handle_event(event)
            continue
        else:
            boy.handle_event(event)



def init():
    global boy, paused, pause_image, inventory_open, inventory_key_down
    global item_select_image

    game_world.clear()
    paused = False
    inventory_open = False
    inventory_key_down = False
    pause_image = load_image('pause.png')
    item_select_image = load_image('item_select.png')
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
    item_select_image.draw(655, 300, 220, 171)

    choice_y = {0: 352, 1: 301, 2: 250}[boy.ball_size]
    draw_rectangle(542, choice_y - 15, 768, choice_y + 15,
                   75, 195, 205, 255)


def finish():
    global pause_image, item_select_image
    game_world.clear()
    del pause_image
    del item_select_image
