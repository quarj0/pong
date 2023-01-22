from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import (
NumericProperty, ReferenceListProperty,ObjectProperty)
from kivy.vector import Vector
from random import randint

""" Pong game made with python kivy which
can be played on desktop and mobile """

class PongBall(Widget):
    
    # speed of the ball on x and y
    speed_x = NumericProperty(0)
    speed_y = NumericProperty(0)
    
    # using reference list property to use ball.speed as shorthand, 
    # just like using w.pos for w.x and w.y
    speed = ReferenceListProperty(speed_x,speed_y)
    
    # move function to move a step. It would be called in equal
    # intervals to animate the ball
    def move(self):
        self.pos = Vector(*self.speed) + self.pos


class PongGame(Widget):
    ball = ObjectProperty(None)
    
    def serve_ball(self):
        self.ball.center = self.center
        self.ball.speed = Vector(4,0).rotate(randint(0,360))
    
    def update(self, dt):
        # calling the ball and making updates
        self.ball.move()
        
        # bounce the ball off the top and bottom
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.speed_y *= -1
            
        # bounce the ball off the left and right
        if (self.ball.x < 0) or (self.ball.right > self.width):
            self.ball.speed_x *= -1


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == '__main__':
    PongApp().run()
