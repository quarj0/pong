from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.properties import (
NumericProperty, ReferenceListProperty,ObjectProperty)
from kivy.vector import Vector
from random import randint


""" Pong game made with python kivy which
can be played on desktop and mobile """

class PongPaddle(Widget):
    score  = NumericProperty(0)
    
    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            speedup = 1.1
            # sx,sy = ball.speed
            offset  = 0.02 * Vector(0,ball.center_y - self.center_y)
            ball.speed = speedup * (offset - ball.speed)
            

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
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    
    def serve_ball(self, spel=(4,0)):
       self.ball.speed = Vector(4,0).rotate(randint(0,360))
    
    def update(self, dt):
        # calling the ball and making updates
        self.ball.move()
        
        # bounce the ball off the top and bottom
        if (self.ball.y < 0) or (self.ball.y > self.height -50):
            self.ball.speed_y *= -1
            
           # bounce off to left
        if self.ball.x < 0:
            self.ball.speed_x *= -1
            self.player1.score +=1
           # bounce off to right     
        if self.ball.x > self.width - 50:
            self.ball.speed_x *= -1
            self.player2.score +=1
            
            # paddle bounce
        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)
            
            
    def on_touch_move(self, touch):
        if touch.x < self.width / 3:
            self.player1.center_y = touch.y
        if touch.x > self.width - self.width / 3:
            self.player2.center_y = touch.y


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game

if __name__ == '__main__':
    PongApp().run()
