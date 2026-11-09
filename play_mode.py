import game_framework
import title_mode
from pico2d import *
import game_world
from boy import Boy
from grass import Grass


paused = False
pause_image = None


def handle_events():
    global boy, paused

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
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
    global boy, paused, pause_image

    game_world.clear()
    paused = False
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
    update_canvas()

def finish():
    global pause_image
    game_world.clear()
    del pause_image
