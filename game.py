import random
from typing import Optional
import arcade
from arcade import Texture 
class Spaceship(arcade.Sprite):
    def __init__(self, Background):
        super().__init__(':resources:images/space_shooter/playerShip1_blue.png')
        self.center_x = Background.width //2
        self.center_y=100
        self.width=56
        self.height=56


class Enemy(arcade.Sprite):
    def __init__(self, Background):
        super().__init__(':resources:images/space_shooter/playerShip1_orange.png')
        self.width = 69
        self.height = 69
        self.center_x = random.randint(40, Background.width-40)
        self.center_y = Background.height -30
        self.angle= 180
        

class Background(arcade.Window):
    def __init__(self):
        super().__init__(width=900, height=700, title='spaceship game')
        arcade.set_background_color(arcade.color.BLACK)
        self.background = arcade.load_texture(':resources:images/backgrounds/stars.png')
        self.spaceship = Spaceship(self)
        self.enemy = Enemy(self)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.spaceship.draw()
        self.enemy.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == 97:
            self.spaceship.center_x = self.spaceship.center_x -10
        if symbol == 100:
            self.spaceship.center_x = self.spaceship.center_x + 10
    def on_update(self, delta_time: float):
        self.enemy.center_y -= 3


Window=Background()
arcade.run()
 