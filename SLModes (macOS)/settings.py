# SLModes - Music Software    Copyright (C) 2018-2023  Sinewave Lab
# email: https://sinewavelab.com/contact/
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# Read GNU GPL 3.0 license here: https://www.gnu.org/licenses/gpl-3.0.html

import configparser
import os
import sys
import pygame.midi # Pygame uses a GNU LESSER GENERAL PUBLIC LICENSE that can be found at the folder Third-Party Library Licenses
from MN_Scales import Chord


midi_port = 0
midi_ports_list = []
midi_ports_list_index = []
midi_no_ports = ["No MIDI Port available"]

composer_tempo = 100
is_play_stopped = True
is_playing = False
negative_harmony_display_options = ["Determined by Negative Chord", "Determined by Negative Root Note"]
negative_harmony_display_selected  = "Determined by Negative Chord"

fretboardy = 120
fretboardx = 195
x0 = 3
y0 = 8

color = "white"
greencolor = '#5bff94'
redcolor = "#f96c44"
listbox_color = "#eaeaea"
darkgrey= "#3A3A3A"

font_01 = ("ansi", 12)
font_01_bold = ("ansi", 12, "bold")
font_01_bold_02 = ("ansi", 12, "bold")

usersettingspath = os.path.abspath(os.path.expanduser("~/SLModes Settings/2_5_0/usersettings_2_5_0.ini"))
partialusersettingspath = os.path.abspath(os.path.expanduser("~/SLModes Settings/2_5_0"))
tmpcomposerpath = os.path.abspath(os.path.expanduser("~/SLModes Settings/2_5_0/tmp_composer.txt"))

def create_settings():

    config = configparser.ConfigParser()

    config['usersettings'] = {
                                'flat': "0",

                                'negative_display': "Determined by Negative Chord",
                                'tempo': "100",

                                'play_style': "Scale",
                                'circle_of_notes_left': "Circle of Fifths",
                                'circle_of_notes_right': "Circle of Fifths",

                                'major': "1",
                                'melodic_minor': "0",
                                'harmonic_minor': "0",
                                'harmonic_major': "0",
                                'double_harmonic_major': "0",
                                'neapolitan_major': "0",
                                'neapolitan_minor': "0",
                                'hungarian_major': "0",
                                'romanian_major': "0",
                                'maj': "1",
                                'majadd2': "0",
                                'majadd4': "0",
                                'majadd6': "0",
                                'maj7': "1",
                                'm': "1",
                                'madd2': "0",
                                'madd4': "0",
                                'madd6': "0",
                                'm7': "1",
                                '7': "1",
                                '7sus2': "0",
                                '7sus4': "0",
                                '+': "1",
                                'dim': "1",
                                'dim7': "0",
                                'maj7b5': "0",
                                'maj7#5': "0",
                                'm7b5': "0",
                                'm7#5': "0",
                                '7b5': "0",
                                '7#5': "0",
                                'mM7': "1",
                                'sus2': "0",
                                'sus4': "0",

                                'sixth_string': "E",
                                'fifth_string': "A",
                                'fourth_string': "D",
                                'third_string': "G",
                                'second_string': "B",
                                'first_string': "E"
                              }

    with open(os.path.abspath(os.path.expanduser(usersettingspath)), 'w') as f:
        config.write(f)

    empty_text = ""

    with open(os.path.abspath(os.path.expanduser(tmpcomposerpath)), 'w') as tc:
        tc.write(empty_text)

scales_list = []

chord_progression_list = []

first_string_notes = []
second_string_notes = []
third_string_notes = []
fourth_string_notes = []
fifth_string_notes = []
sixth_string_notes = []

other_more_chords = []
fretboard_height = fretboardy - y0
fretboard_width = fretboardx - x0
x_displacement = 4
y_displacement = 8
fcanvaswidth = fretboardx + x_displacement
fcanvasheight = fretboardy + y_displacement

major_names = ('Ionian', 'Dorian', 'Phrygian', 'Lydian', 'Mixolydian', 'Aeolian', 'Locrian'); # these are tuplets...
melodic_minor_names = ('Melodic Minor', 'Dorian b2', 'Lydian Augmented', 'Lydian Dominant', 'Mixolydian b6', 'Locrian #2', 'Altered');
harmonic_minor_names = ('Harmonic Minor', 'Locrian 6', 'Ionian #5', 'Dorian #4', 'Phrygian Major', 'Lydian #2', 'Ultralocrian');
harmonic_major_names = ('Harmonic Major', 'Dorian b5', 'Phrygian b4', 'Lydian Minor', 'Mixolydian b2', 'Lydian Augmented #2', 'Locrian bb7');
double_harmonic_major_names = ('Double Harmonic Major', 'Lydian #2 #6', 'Ultraphrygian', 'Hungarian Minor', 'Oriental', 'Ionian #2 #5', 'Locrian bb3 bb7');
neapolitan_major_names = ('Neapolitan Major', 'Leading Whole Tone', 'Lydian Augmented Dominant', 'Lydian Dominant b6', 'Major Locrian', 'Half-Diminished b4', 'Altered Dominant bb3');
neapolitan_minor_names = ('Neapolitan Minor', 'Lydian #6', 'Mixolydian Augmented', 'Romani Minor', 'Locrian Dominant', 'Ionian #2', 'Ultralocrian bb3');
hungarian_major_names = ('Hungarian Major', 'Ultralocrian bb6', 'Harmonic Minor b5', 'Superlocrian ♮6', 'Jazz Minor #5', 'Dorian b2 #4', 'Lydian Augmented #3');
romanian_major_names = ('Romanian Major', 'Superlydian Augmented ♮6', 'Locrian ♮2 bb7', 'Blues Phrygian b4', 'Jazz Minor b5', 'Superphrygian ♮6', 'Lydian Augmented b3');

scales_names = tuple() # scales_names is a string, not a list

white_key_height = 80
offset = 7
white_key_width = 14.28
black_key_height = 50
black_key_width = 14.28

pianokeyXYDict = {'C4': [white_key_width * 1 - offset, white_key_height],
                  'D4': [white_key_width * 2 - offset, white_key_height],
                  'E4': [white_key_width * 3 - offset, white_key_height],
                  'F4': [white_key_width * 4 - offset, white_key_height],
                  'G4': [white_key_width * 5 - offset, white_key_height],
                  'A4': [white_key_width * 6 - offset, white_key_height],
                  'B4': [white_key_width * 7 - offset, white_key_height],
                  'C5': [white_key_width * 8 - offset, white_key_height],
                  'D5': [white_key_width * 9 - offset - 1, white_key_height],
                  'E5': [white_key_width * 10 - offset, white_key_height],
                  'F5': [white_key_width * 11 - offset, white_key_height],
                  'G5': [white_key_width * 12 - offset, white_key_height],
                  'A5': [white_key_width * 13 - offset, white_key_height],
                  'B5': [white_key_width * 14 - offset, white_key_height],
                  'C#4': [black_key_width * 1 - 1, black_key_height],
                  'Db4': [black_key_width * 1 - 1, black_key_height],
                  'D#4': [black_key_width * 2 + 1, black_key_height],
                  'Eb4': [black_key_width * 2 + 1, black_key_height],
                  'F#4': [black_key_width * 4 - 1, black_key_height],
                  'Gb4': [black_key_width * 4 - 1, black_key_height],
                  'G#4': [black_key_width * 5 + 1, black_key_height],
                  'Ab4': [black_key_width * 5 + 1, black_key_height],
                  'A#4': [black_key_width * 6 + 2, black_key_height],
                  'Bb4': [black_key_width * 6 + 2, black_key_height],
                  'C#5': [black_key_width * 8 - 1, black_key_height],
                  'Db5': [black_key_width * 8 - 1, black_key_height],
                  'D#5': [black_key_width * 9 + 1, black_key_height],
                  'Eb5': [black_key_width * 9 + 1, black_key_height],
                  'F#5': [black_key_width * 11 - 2, black_key_height],
                  'Gb5': [black_key_width * 11 - 2, black_key_height],
                  'G#5': [black_key_width * 12, black_key_height],
                  'Ab5': [black_key_width * 12, black_key_height],
                  'A#5': [black_key_width * 13 + 1, black_key_height],
                  'Bb5': [black_key_width * 13 + 1, black_key_height],
                  }

guitar_modes_shapes = {
    # Major modes:
    'Ionian': [  # 6string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Dorian': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)
    ],
    'Phrygian': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Lydian': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Mixolydian': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Aeolian': [

        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Locrian': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    # Melodic Minor modes:
    'Melodic Minor': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Dorian b2': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Lydian Augmented': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Lydian Dominant': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Mixolydian b6': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Locrian #2': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Altered': [
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    # Harmonic Minor modes:
    'Harmonic Minor': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Locrian 6': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Ionian #5': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Dorian #4': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Phrygian Major': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Lydian #2': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Ultralocrian': [
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    # Harmonic Major modes:
    'Harmonic Major': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Dorian b5': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Phrygian b4': [
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Lydian Minor': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Mixolydian b2': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Lydian Augmented #2': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Locrian bb7': [
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 12.5)],
    # Double Harmonic Major modes:
    'Double Harmonic Major': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Lydian #2 #6': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Ultraphrygian': [
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Hungarian Minor': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Oriental': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Ionian #2 #5': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Locrian bb3 bb7': [
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Neapolitan Major': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Leading Whole Tone': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Lydian Augmented Dominant': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Lydian Dominant b6': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Major Locrian': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Half-Diminished b4': [
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Altered Dominant bb3': [
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Neapolitan Minor': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Lydian #6': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Mixolydian Augmented': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Romani Minor': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Locrian Dominant': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Ionian #2': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Ultralocrian bb3': [
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Hungarian Major': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Ultralocrian bb6': [
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Harmonic Minor b5': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Superlocrian ♮6': [
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Jazz Minor #5': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Dorian b2 #4': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Lydian Augmented #3': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Romanian Major': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Superlydian Augmented ♮6': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Locrian ♮2 bb7': [
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Blues Phrygian b4': [
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Jazz Minor b5': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Superphrygian ♮6': [
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 12.5)],
    'Lydian Augmented b3': [
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 1.4),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 1.4),
        # 5string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 3.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 3.5),
        # 4string
        x0 + ((fretboard_width / 14) * 3), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 5.8),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 5.8),
        # 3string
        x0 + ((fretboard_width / 14) * 1), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 8),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 8),
        # 2string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 9), fretboardy - ((fretboard_height / 13) * 10.5),
        x0 + ((fretboard_width / 14) * 11), fretboardy - ((fretboard_height / 13) * 10.5),
        # 1string
        x0 + ((fretboard_width / 14) * 5), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 7), fretboardy - ((fretboard_height / 13) * 12.5),
        x0 + ((fretboard_width / 14) * 13), fretboardy - ((fretboard_height / 13) * 12.5)],
}

sixth_string_coordinates  = [    [ 32 ,  171.0 ],
                                                         [ 64 ,  171.0 ],
                                                         [ 118 ,  171.0 ],
                                                         [ 171 ,  171.0 ],
                                                         [ 222 ,  171.0 ],
                                                         [ 274 ,  171.0 ],
                                                         [ 321 ,  171.0 ],
                                                         [ 366 ,  171.0 ],
                                                         [ 405 ,  171.0 ],
                                                         [ 441 ,  171.0 ],
                                                         [ 478 ,  171.0 ],
                                                         [ 514 ,  171.0 ],
                                                         [ 555 ,  171.0 ],
                                                         [ 598 ,  171.0 ],
                                                         [ 633 ,  171.0 ],
                                                         [ 667 ,  171.0 ],
                                                         [ 700 ,  171.0 ],
                                                         [ 735 ,  171.0 ],
                                                         [ 767 ,  171.0 ],
                                                         [ 801 ,  171.0 ],
                                                         [ 833 ,  171.0 ],
                                                         [ 861 ,  171.0 ],
                                                         [ 887 ,  171.0 ],
                                                         [ 911 ,  171.0 ],
                                                         [ 933 ,  171.0 ]]

fifth_string_coordinates  = [         [ 32 ,  145.5 ],
                                                         [ 64 ,  145.5 ],
                                                         [ 118 ,  145.5 ],
                                                         [ 171 ,  145.5 ],
                                                         [ 222 ,  145.5 ],
                                                         [ 274 ,  145.5 ],
                                                         [ 321 ,  145.5 ],
                                                         [ 366 ,  145.5 ],
                                                         [ 405 ,  145.5 ],
                                                         [ 441 ,  145.5 ],
                                                         [ 478 ,  145.5 ],
                                                         [ 514 ,  145.5 ],
                                                         [ 555 ,  145.5 ],
                                                         [ 598 ,  145.5 ],
                                                         [ 633 ,  145.5 ],
                                                         [ 667 ,  145.5 ],
                                                         [ 700 ,  145.5 ],
                                                         [ 735 ,  145.5 ],
                                                         [ 767 ,  145.5 ],
                                                         [ 801 ,  145.5 ],
                                                         [ 833 ,  145.5 ],
                                                         [ 861 ,  145.5 ],
                                                         [ 887 ,  145.5 ],
                                                         [ 911 ,  145.5 ],
                                                         [ 933 ,  145.5 ]]

fourth_string_coordinates  = [        [ 32 ,  118.0 ],
                                                                 [ 64 ,  118.0 ],
                                                                 [ 118 ,  118.0 ],
                                                                 [ 171 ,  118.0 ],
                                                                 [ 222 ,  118.0 ],
                                                                 [ 274 ,  118.0 ],
                                                                 [ 321 ,  118.0 ],
                                                                 [ 366 ,  118.0 ],
                                                                 [ 405 ,  118.0 ],
                                                                 [ 441 ,  118.0 ],
                                                                 [ 478 ,  118.0 ],
                                                                 [ 514 ,  118.0 ],
                                                                 [ 555 ,  118.0 ],
                                                                 [ 598 ,  118.0 ],
                                                                 [ 633 ,  118.0 ],
                                                                 [ 667 ,  118.0 ],
                                                                 [ 700 ,  118.0 ],
                                                                 [ 735 ,  118.0 ],
                                                                 [ 767 ,  118.0 ],
                                                                 [ 801 ,  118.0 ],
                                                                 [ 833 ,  118.0 ],
                                                                 [ 861 ,  118.0 ],
                                                                 [ 887 ,  118.0 ],
                                                                 [ 911 ,  118.0 ],
                                                                 [ 933 ,  118.0 ]]

third_string_coordinates  = [         [ 32 ,  90.5 ],
                                                             [ 64 ,  90.5 ],
                                                             [ 118 ,  90.5 ],
                                                             [ 171 ,  90.5 ],
                                                             [ 222 ,  90.5 ],
                                                             [ 274 ,  90.5 ],
                                                             [ 321 ,  90.5 ],
                                                             [ 366 ,  90.5 ],
                                                             [ 405 ,  90.5 ],
                                                             [ 441 ,  90.5 ],
                                                             [ 478 ,  90.5 ],
                                                             [ 514 ,  90.5 ],
                                                             [ 555 ,  90.5 ],
                                                             [ 598 ,  90.5 ],
                                                             [ 633 ,  90.5 ],
                                                             [ 667 ,  90.5 ],
                                                             [ 700 ,  90.5 ],
                                                             [ 735 ,  90.5 ],
                                                             [ 767 ,  90.5 ],
                                                             [ 801 ,  90.5 ],
                                                             [ 833 ,  90.5 ],
                                                             [ 861 ,  90.5 ],
                                                             [ 887 ,  90.5 ],
                                                             [ 911 ,  90.5 ],
                                                             [ 933 ,  90.5 ]]

second_string_coordinates  = [         [ 32 ,  63.0 ],
                                                                 [ 64 ,  63.0 ],
                                                                 [ 118 ,  63.0 ],
                                                                 [ 171 ,  63.0 ],
                                                                 [ 222 ,  63.0 ],
                                                                 [ 274 ,  63.0 ],
                                                                 [ 321 ,  63.0 ],
                                                                 [ 366 ,  63.0 ],
                                                                 [ 405 ,  63.0 ],
                                                                 [ 441 ,  63.0 ],
                                                                 [ 478 ,  63.0 ],
                                                                 [ 514 ,  63.0 ],
                                                                 [ 555 ,  63.0 ],
                                                                 [ 598 ,  63.0 ],
                                                                 [ 633 ,  63.0 ],
                                                                 [ 667 ,  63.0 ],
                                                                 [ 700 ,  63.0 ],
                                                                 [ 735 ,  63.0 ],
                                                                 [ 767 ,  63.0 ],
                                                                 [ 801 ,  63.0 ],
                                                                 [ 833 ,  63.0 ],
                                                                 [ 861 ,  63.0 ],
                                                                 [ 887 ,  63.0 ],
                                                                 [ 911 ,  63.0 ],
                                                                 [ 933 ,  63.0 ]]

first_string_coordinates  = [        [32 ,  35.5],
                                                            [64 ,  35.5],
                                                            [118 ,  35.5],
                                                            [171 ,  35.5],
                                                            [222 ,  35.5],
                                                            [274 ,  35.5],
                                                            [321 ,  35.5],
                                                            [366 ,  35.5],
                                                            [405 ,  35.5],
                                                            [441 ,  35.5],
                                                            [478 ,  35.5],
                                                            [514 ,  35.5],
                                                            [555 ,  35.5],
                                                            [598 ,  35.5],
                                                            [633 ,  35.5],
                                                            [667 ,  35.5],
                                                            [700 ,  35.5],
                                                            [735 ,  35.5],
                                                            [767 ,  35.5],
                                                            [801 ,  35.5],
                                                            [833 ,  35.5],
                                                            [861 ,  35.5],
                                                            [887 ,  35.5],
                                                            [911 ,  35.5],
                                                            [933 ,  35.5]]
