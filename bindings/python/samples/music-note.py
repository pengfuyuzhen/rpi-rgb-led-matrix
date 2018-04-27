#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
import time


class MusicTest(SampleBase):
    def __init__(self, *args, **kwargs):
        super(MusicTest, self).__init__(*args, **kwargs)

    def run(self):
        canvas = self.matrix
        # font = graphics.Font()
        # font.LoadFont("../../../fonts/7x13.bdf")

        red = graphics.Color(255, 0, 0)
        green = graphics.Color(0, 255, 0)
        blue = graphics.Color(0, 0, 255)



        for offset in range(32):
            canvas.offsetTop(offset)
            time.sleep(0.25)
            graphics.DrawLine(canvas, 1, 1, 1, 5, red)

# Main function
if __name__ == "__main__":
    music_test = MusicTest()
    if (not music_test.process()):
        music_test.print_help()
