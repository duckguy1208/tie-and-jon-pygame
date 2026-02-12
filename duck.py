from object import Object

class Duck(Object):
    vel = 100
    x = 0
    y = 0
    x_min = 0
    y_min = 0
    x_max = 0
    y_max = 0

    def quack():
        print('Quack, quack')

    def run(self):
        self.x += self.vel
        if self.x > self.x_max:
            self.x = self.x_max
        if self.x < self.x_min:
            self.x = self.x_min

    def jump(self):
        self.y -= self.vel
        if self.y < self.y_min:
            self.y = self.y_min
            