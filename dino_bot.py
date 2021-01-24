from PIL import ImageGrab, ImageOps
import pyautogui
import time
import numpy as np

class Bot:
    def __init__(self):
        self.restart_coords = (641, 366)
        self.dino_coords = (161, 410)
        self.box_coords = (self.dino_coords[0] + 50, self.dino_coords[1], self.dino_coords[0] + 275, self.dino_coords[1] + 50)
        self.pause = 0.6

    def change_speed(self, x, t):
        self.box_coords = (self.dino_coords[0] + 50, self.dino_coords[1], self.dino_coords[0] + 295 + x, self.dino_coords[1] + 50)
        self.pause = t

    def restart(self):
        pyautogui.click(self.restart_coords)

    def jump(self):
        pyautogui.keyDown('space')
        time.sleep(self.pause)
        pyautogui.keyUp('space')

    def detection_area(self):
        image = ImageGrab.grab(self.box_coords)
        gray_img = ImageOps.grayscale(image)
        arr = np.array(gray_img.getcolors())
        # print(arr.mean())
        return arr.mean()

    def main(self):
        startTime = time.time()
        self.restart()

        while True:
            currTime = time.time() - startTime

            if currTime < 30:
                self.change_speed(-40, 0.5)
                if self.detection_area() < 5141:
                    self.jump()

            elif currTime < 65:
                self.change_speed(30, 0.3)
                if self.detection_area() < 6141:
                    self.jump()

            elif 65 <= currTime < 78:
                self.change_speed(147, 0.3)
                if self.detection_area() < 5516:
                    self.jump()

            elif 78 <= currTime < 110:
                self.change_speed(140, 0.005)
                if self.detection_area() < 5516:
                    self.jump()

            else:
                self.change_speed(360, 0.05)
                if self.detection_area() < 5516:
                    self.jump()

bot = Bot()
bot.main()
