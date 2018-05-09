#!/usr/bin/env python
from samplebase import SampleBase
from rgbmatrix import graphics
import time
import numpy as np

# sudo python music-note.py --led-rows=16 --led-show-refresh --led-pwm-lsb-nanoseconds 500

#   Music Cheat Sheet
#   0   1   2   3   4   5   6   7   8   9   10  11
#   1   1+  2   2+  3   4   4+  5   5+  6   6+  7
def note_to_piano_key(note):
    mapping_look_up_table = {'1': 0, '1+': 1, '2': 2, '2+': 3, '3': 4, '4': 5,
                             '4+': 6, '5': 7, '5+': 8, '6': 9, '6+': 10, '7': 11}
    return mapping_look_up_table[note]

key_to_led_position = [1, 4, 6, 8, 11, 15, 17, 20, 22, 24, 27, 30]
black_key_position = [key_to_led_position[key] for key in [1, 3, 6, 8, 10]]
LED_HEIGHT = 16
huan_le_song_simple_note = ['3', '3', '4', '5',
                            '5', '4', '3', '2',
                            '1', '1', '2', '3',
                            '3', '2', '2',
                            '3', '3', '4', '5',
                            '5', '4', '3', '2',
                            '1', '1', '2', '3',
                            '2', '1', '1',
                            '2', '2', '3', '1',
                            '2', '3', '4', '3', '1',
                            '2', '3', '4', '3', '2',
                            '1', '2', '5',
                            '3', '3', '4', '5',
                            '5', '4', '3', '2',
                            '1', '1', '2', '3',
                            '2', '1', '1']

huan_le_song_note_duration =    [1, 1, 1, 1,
                                 1, 1, 1, 1,
                                 1, 1, 1, 1,
                                 1.5, 0.5, 2,
                                 1, 1, 1, 1,
                                 1, 1, 1, 1,
                                 1, 1, 1, 1,
                                 1.5, 0.5, 2,
                                 1, 1, 1, 1,
                                 1, 0.5, 0.5, 1, 1,
                                 1, 0.5, 0.5, 1, 1,
                                 1, 1, 1,
                                 1, 1, 1, 1,
                                 1, 1, 1, 1,
                                 1, 1, 1, 1,
                                 1.5, 0.5, 2,
                                 ]

sample_song = [note_to_piano_key(note) for note in huan_le_song_simple_note]
sample_song_duration = np.array(huan_le_song_note_duration) * 4


color_intensity = 128
white_intensity = 32

class MusicTest(SampleBase):
    def __init__(self, *args, **kwargs):
        super(MusicTest, self).__init__(*args, **kwargs)

    def within_display(self, x, y):
        if x >= 0 and x <= 32 and y >= 0 and y <= 15:
            return True
        return False

    def run(self):
        canvas = self.matrix
        sample_song_length = int((np.sum(sample_song_duration)))
        while True:
            for i in range(32):
                    for j in range(16):
                        canvas.SetPixel(i, j,
                                        white_intensity, white_intensity, white_intensity)

            for offset in range(-sample_song_length, LED_HEIGHT):
                time.sleep(0.14)
                for i in range(len(sample_song)):

                    # head
                    if key_to_led_position[sample_song[i]] in black_key_position:
                        canvas.SetPixel(key_to_led_position[sample_song[i]],
                                        offset + int(sum(sample_song_duration[i:])),
                                        color_intensity, 0, color_intensity)
                    else:
                        canvas.SetPixel(key_to_led_position[sample_song[i]],
                                        offset + int(sum(sample_song_duration[i:])),
                                        color_intensity, color_intensity, 0)
                    # tail head
                    canvas.SetPixel(key_to_led_position[sample_song[i]],
                                    offset + int(sum(sample_song_duration[i:])) - 1,
                                    color_intensity, 0, 0)
                    # tail
                    canvas.SetPixel(key_to_led_position[sample_song[i]],

                                    offset + int(sum(sample_song_duration[i:])) - sample_song_duration[i],
                                    white_intensity, white_intensity, white_intensity)


# Main function
if __name__ == "__main__":
    music_test = MusicTest()
    if (not music_test.process()):
        music_test.print_help()
