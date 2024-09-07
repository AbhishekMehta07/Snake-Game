from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle, Color
from kivy.clock import Clock
from kivy.core.window import Window
import random

# Set the window size
Window.size = (1080, 720)

class SnakeGame(Widget):
    def __init__(self, **kwargs):
        super(SnakeGame, self).__init__(**kwargs)
        self.snake_block = 10
        self.snake_speed = 15
        self.snake_list = []
        self.length_of_snake = 1
        self.foodx = random.randint(0, Window.width - self.snake_block)
        self.foody = random.randint(0, Window.height - self.snake_block)
        self.x1 = Window.width / 2
        self.y1 = Window.height / 2
        self.x1_change = 0
        self.y1_change = 0

        with self.canvas:
            self.snake_color = Color(0, 0, 0, 1)
            self.snake = Rectangle(size=(self.snake_block, self.snake_block), pos=(self.x1, self.y1))
            self.food_color = Color(0, 1, 0, 1)
            self.food = Rectangle(size=(self.snake_block, self.snake_block), pos=(self.foodx, self.foody))

        Clock.schedule_interval(self.update, 1.0 / 15.0)
        Window.bind(on_key_down=self.on_key_down)

    def update(self, dt):
        self.x1 += self.x1_change
        self.y1 += self.y1_change
        self.snake.pos = (self.x1, self.y1)

        if self.x1 == self.foodx and self.y1 == self.foody:
            self.foodx = random.randint(0, Window.width - self.snake_block)
            self.foody = random.randint(0, Window.height - self.snake_block)
            self.food.pos = (self.foodx, self.foody)
            self.length_of_snake += 1

        if self.x1 < 0 or self.x1 >= Window.width or self.y1 < 0 or self.y1 >= Window.height:
            self.reset_game()

    def on_key_down(self, window, keycode, *args):
        if keycode[1] == 'left':
            self.x1_change = -self.snake_block
            self.y1_change = 0
        elif keycode[1] == 'right':
            self.x1_change = self.snake_block
            self.y1_change = 0
        elif keycode[1] == 'up':
            self.y1_change = self.snake_block
            self.x1_change = 0
        elif keycode[1] == 'down':
            self.y1_change = -self.snake_block
            self.x1_change = 0

    def reset_game(self):
        self.x1 = Window.width / 2
        self.y1 = Window.height / 2
        self.x1_change = 0
        self.y1_change = 0

class SnakeApp(App):
    def build(self):
        return SnakeGame()

if __name__ == "__main__":
    SnakeApp().run()
