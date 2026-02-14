import pygame
from object import Object


class Duck(Object):

    def quack(self):
        print('Quack Quack!')
        self.quack_text_size = 18
        self.quack_color = ("yellow")  # yellow color for quack text
        self.quack_text = 'Quack Quack!' 
        self.quack_timer = 500  # Display for 1/2 second (in milliseconds)