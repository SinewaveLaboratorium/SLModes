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

import threading
import time
import webbrowser
from configparser import ConfigParser
from tkinter import *
from tkinter import ttk
from os import path
import tk as tk
import MN_AUDIO
import MN_Draw
import settings
from MN_Scales import *
from settings import *
from PIL import ImageTk, Image
from tkinter import filedialog as fd
import modes_7, modes_6, modes_5, modes_4, modes_3, modes_2, chords
import Negative_Harmony_utils
import Composer_Mode_utils

pygame.mixer.init(channels=1) # covers all files # Pygame uses a GNU LESSER GENERAL PUBLIC LICENSE that can be found at the folder Third-Party Library Licenses
pygame.mixer.set_num_channels(44)

if not os.path.exists(os.path.abspath(os.path.expanduser("~/SLModes Settings"))): #if file doesn't exist, create.
    os.mkdir(os.path.abspath(os.path.expanduser("~/SLModes Settings")))

if not os.path.exists(partialusersettingspath):  # if file doesn't exist, create.
    os.mkdir(partialusersettingspath)
    settings.create_settings()  # create usersettings.ini

def find_data_file(filename):
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        datadir = os.path.dirname(sys.executable)
    else:
        datadir = path.dirname(__file__)
    return path.join(datadir, filename)


pianopath = find_data_file("piano.png")
backgroundpath = find_data_file("Background01.png")
settingsbackgroundpath = find_data_file("Settings.png")
fretboardpath = find_data_file("fretboard.png")
fretboardnotepath = find_data_file("fretnote.png")
composerbackgroundpath = find_data_file("composer_background.png")
fretboarddpathlarge = find_data_file("LargeNote.png")
fretboarddpathrootnote = find_data_file("Root_Note.png")
fretboarddpathopenlarge = find_data_file("OpenFret.png")
fretboarddchordnote = find_data_file("Chord_Note.png")
extendedfretboardpath = find_data_file("extended_fretboard.png")




negativeharmonybackgroundpath = find_data_file("negative_harmony_background.png")
negativeharmonybackgroundpath_pos_1 = find_data_file("negative_harmony_pos_1.png")
negativeharmonybackgroundpath_pos_1_pos_1 = find_data_file("negative_harmony_pos_1_pos_1.png")
negativeharmonybackgroundpath_pos_1_pos_2 = find_data_file("negative_harmony_pos_1_pos_2.png")
negativeharmonybackgroundpath_pos_1_pos_3 = find_data_file("negative_harmony_pos_1_pos_3.png")
negativeharmonybackgroundpath_pos_1_pos_4 = find_data_file("negative_harmony_pos_1_pos_4.png")
negativeharmonybackgroundpath_pos_1_pos_5 = find_data_file("negative_harmony_pos_1_pos_5.png")
negativeharmonybackgroundpath_pos_1_pos_6 = find_data_file("negative_harmony_pos_1_pos_6.png")
negativeharmonybackgroundpath_pos_2 = find_data_file("negative_harmony_pos_2.png")
negativeharmonybackgroundpath_pos_2_pos_1 = find_data_file("negative_harmony_pos_2_pos_1.png")
negativeharmonybackgroundpath_pos_2_pos_2 = find_data_file("negative_harmony_pos_2_pos_2.png")
negativeharmonybackgroundpath_pos_2_pos_3 = find_data_file("negative_harmony_pos_2_pos_3.png")
negativeharmonybackgroundpath_pos_2_pos_4 = find_data_file("negative_harmony_pos_2_pos_4.png")
negativeharmonybackgroundpath_pos_2_pos_5 = find_data_file("negative_harmony_pos_2_pos_5.png")
negativeharmonybackgroundpath_pos_2_pos_6 = find_data_file("negative_harmony_pos_2_pos_6.png")
negativeharmonybackgroundpath_pos_3 = find_data_file("negative_harmony_pos_3.png")
negativeharmonybackgroundpath_pos_3_pos_1 = find_data_file("negative_harmony_pos_3_pos_1.png")
negativeharmonybackgroundpath_pos_3_pos_2 = find_data_file("negative_harmony_pos_3_pos_2.png")
negativeharmonybackgroundpath_pos_3_pos_3 = find_data_file("negative_harmony_pos_3_pos_3.png")
negativeharmonybackgroundpath_pos_3_pos_4 = find_data_file("negative_harmony_pos_3_pos_4.png")
negativeharmonybackgroundpath_pos_3_pos_5 = find_data_file("negative_harmony_pos_3_pos_5.png")
negativeharmonybackgroundpath_pos_3_pos_6 = find_data_file("negative_harmony_pos_3_pos_6.png")
negativeharmonybackgroundpath_pos_4 = find_data_file("negative_harmony_pos_4.png")
negativeharmonybackgroundpath_pos_4_pos_1 = find_data_file("negative_harmony_pos_4_pos_1.png")
negativeharmonybackgroundpath_pos_4_pos_2 = find_data_file("negative_harmony_pos_4_pos_2.png")
negativeharmonybackgroundpath_pos_4_pos_3 = find_data_file("negative_harmony_pos_4_pos_3.png")
negativeharmonybackgroundpath_pos_4_pos_4 = find_data_file("negative_harmony_pos_4_pos_4.png")
negativeharmonybackgroundpath_pos_4_pos_5 = find_data_file("negative_harmony_pos_4_pos_5.png")
negativeharmonybackgroundpath_pos_4_pos_6 = find_data_file("negative_harmony_pos_4_pos_6.png")
negativeharmonybackgroundpath_pos_5 = find_data_file("negative_harmony_pos_5.png")
negativeharmonybackgroundpath_pos_5_pos_1 = find_data_file("negative_harmony_pos_5_pos_1.png")
negativeharmonybackgroundpath_pos_5_pos_2 = find_data_file("negative_harmony_pos_5_pos_2.png")
negativeharmonybackgroundpath_pos_5_pos_3 = find_data_file("negative_harmony_pos_5_pos_3.png")
negativeharmonybackgroundpath_pos_5_pos_4 = find_data_file("negative_harmony_pos_5_pos_4.png")
negativeharmonybackgroundpath_pos_5_pos_5 = find_data_file("negative_harmony_pos_5_pos_5.png")
negativeharmonybackgroundpath_pos_5_pos_6 = find_data_file("negative_harmony_pos_5_pos_6.png")
negativeharmonybackgroundpath_pos_6 = find_data_file("negative_harmony_pos_6.png")
negativeharmonybackgroundpath_pos_6_pos_1 = find_data_file("negative_harmony_pos_6_pos_1.png")
negativeharmonybackgroundpath_pos_6_pos_2 = find_data_file("negative_harmony_pos_6_pos_2.png")
negativeharmonybackgroundpath_pos_6_pos_3 = find_data_file("negative_harmony_pos_6_pos_3.png")
negativeharmonybackgroundpath_pos_6_pos_4 = find_data_file("negative_harmony_pos_6_pos_4.png")
negativeharmonybackgroundpath_pos_6_pos_5 = find_data_file("negative_harmony_pos_6_pos_5.png")
negativeharmonybackgroundpath_pos_6_pos_6 = find_data_file("negative_harmony_pos_6_pos_6.png")


#### INITIALIZE SETTINGS ####
parser = ConfigParser()
parser.read(usersettingspath)
composer_parser = ConfigParser()

settings.composer_tempo = int(parser.get('usersettings', 'tempo'))
FLAT_SETTING = parser.getint('usersettings', 'flat') #reads ok
MAJOR_SETTING = int(parser.get('usersettings', 'major'))
MELODIC_MINOR_SETTING = int(parser.get('usersettings', 'melodic_minor'))
HARMONIC_MINOR_SETTING = int(parser.get('usersettings', 'harmonic_minor'))
HARMONIC_MAJOR_SETTING = int(parser.get('usersettings', 'harmonic_major'))
DOUBLE_HARMONIC_MAJOR_SETTING = int(parser.get('usersettings', 'double_harmonic_major'))
NEAPOLITAN_MAJOR_SETTING = int(parser.get('usersettings', 'neapolitan_major'))
NEAPOLITAN_MINOR_SETTING = int(parser.get('usersettings', 'neapolitan_minor'))
HUNGARIAN_MAJOR_SETTING = int(parser.get('usersettings', 'hungarian_major'))
ROMANIAN_MAJOR_SETTING = int(parser.get('usersettings', 'romanian_major'))

MAJ_SETTING = int(parser.get('usersettings', 'maj'))
MAJADD2_SETTING = int(parser.get('usersettings', 'majadd2'))
MAJADD4_SETTING = int(parser.get('usersettings', 'majadd4'))
MAJADD6_SETTING = int(parser.get('usersettings', 'majadd6'))
MAJ7_SETTING = int(parser.get('usersettings', 'maj7'))
M_SETTING = int(parser.get('usersettings', 'm'))
MADD2_SETTING = int(parser.get('usersettings', 'madd2'))
MADD4_SETTING = int(parser.get('usersettings', 'madd4'))
MADD6_SETTING = int(parser.get('usersettings', 'madd6'))
M7_SETTING = int(parser.get('usersettings', 'm7'))
DOM7_SETTING = int(parser.get('usersettings', '7'))
DOM7SUS2_SETTING = int(parser.get('usersettings', '7sus2'))
DOM7SUS4_SETTING = int(parser.get('usersettings', '7sus4'))
AUG_SETTING = int(parser.get('usersettings', '+'))
DIM_SETTING = int(parser.get('usersettings', 'dim'))
DIM7_SETTING = int(parser.get('usersettings', 'dim7'))
MAJ7B5_SETTING = int(parser.get('usersettings', 'maj7b5'))
MAJ7SHARP5_SETTING = int(parser.get('usersettings', 'maj7#5'))
M7B5_SETTING = int(parser.get('usersettings', 'm7b5'))
M7SHARP5_SETTING = int(parser.get('usersettings', 'm7#5'))
DOM7B5_SETTING = int(parser.get('usersettings', '7b5'))
DOM7SHARP5_SETTING = int(parser.get('usersettings', '7#5'))
mM7_SETTING = int(parser.get('usersettings', 'mM7'))
SUS2_SETTING = int(parser.get('usersettings', 'sus2'))
SUS4_SETTING = int(parser.get('usersettings', 'sus4'))

SIXTH_STRING_SETTING = parser.get('usersettings', 'sixth_string')
FIFTH_STRING_SETTING = parser.get('usersettings', 'fifth_string')
FOURTH_STRING_SETTING = parser.get('usersettings', 'fourth_string')
THIRD_STRING_SETTING = parser.get('usersettings', 'third_string')
SECOND_STRING_SETTING = parser.get('usersettings', 'second_string')
FIRST_STRING_SETTING = parser.get('usersettings', 'first_string')

PLAY_STYLE_SETTING = parser.get('usersettings', 'play_style')

Negative_Harmony_utils.CIRCLE_OF_NOTES_LEFT_SETTING = parser.get('usersettings', 'circle_of_notes_left')
Negative_Harmony_utils.CIRCLE_OF_NOTES_RIGHT_SETTING = parser.get('usersettings', 'circle_of_notes_right')

NEGATIVE_HARMONY_DISPLAY_SETTING = parser.get('usersettings', 'negative_display')
Negative_Harmony_utils.update_negative_display(str(NEGATIVE_HARMONY_DISPLAY_SETTING))

if MAJOR_SETTING == 1:
        settings.scales_names = settings.scales_names + settings.major_names
if MELODIC_MINOR_SETTING == 1:
        settings.scales_names = settings.scales_names + settings.melodic_minor_names
if HARMONIC_MINOR_SETTING == 1:
        settings.scales_names = settings.scales_names + settings.harmonic_minor_names
if HARMONIC_MAJOR_SETTING == 1:
        settings.scales_names = settings.scales_names + settings.harmonic_major_names
if DOUBLE_HARMONIC_MAJOR_SETTING == 1:
        settings.scales_names = settings.scales_names + settings.double_harmonic_major_names
if NEAPOLITAN_MAJOR_SETTING == 1:
        settings.scales_names = settings.scales_names + settings.neapolitan_major_names
if NEAPOLITAN_MINOR_SETTING == 1:
        settings.scales_names = settings.scales_names + settings.neapolitan_minor_names
if HUNGARIAN_MAJOR_SETTING == 1:
        settings.scales_names = settings.scales_names + settings.hungarian_major_names
if ROMANIAN_MAJOR_SETTING == 1:
        settings.scales_names = settings.scales_names + settings.romanian_major_names

if (MAJOR_SETTING+MELODIC_MINOR_SETTING+HARMONIC_MINOR_SETTING+HARMONIC_MAJOR_SETTING+DOUBLE_HARMONIC_MAJOR_SETTING+
    NEAPOLITAN_MAJOR_SETTING+NEAPOLITAN_MINOR_SETTING+HUNGARIAN_MAJOR_SETTING+ROMANIAN_MAJOR_SETTING)==0:
    settings.scales_names = settings.scales_names + settings.major_names
    parser.set('usersettings', 'major', "1")
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)
    MAJOR_SETTING = 1

if (MAJ_SETTING+MAJADD2_SETTING+MAJADD4_SETTING+MAJADD6_SETTING+MAJ7_SETTING+M_SETTING+MADD2_SETTING+MADD4_SETTING+
        MADD6_SETTING+M7_SETTING+DOM7_SETTING+DOM7SUS2_SETTING+DOM7SUS4_SETTING+AUG_SETTING+DIM_SETTING+DIM7_SETTING+
        MAJ7B5_SETTING+MAJ7SHARP5_SETTING+M7B5_SETTING+M7SHARP5_SETTING+DOM7B5_SETTING+DOM7SHARP5_SETTING+mM7_SETTING+
        SUS2_SETTING+SUS4_SETTING)==0:
    parser.set('usersettings', 'maj', "1")
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)
    MAJ_SETTING = 1

window = Tk()
window.title("SLModes 2.5.0 - Sinewave Lab")
window.geometry("980x527+300+300")
window.resizable(False, False)



backgroundimgfile = ImageTk.PhotoImage(Image.open(backgroundpath))
background = Label(window, image=backgroundimgfile)
background.place(x=-3, y=-15)
fretboardfile = ImageTk.PhotoImage(Image.open(fretboardpath))
pianofile = ImageTk.PhotoImage(Image.open(pianopath))
notefile = ImageTk.PhotoImage(Image.open(fretboardnotepath))
largenotefile = PhotoImage(file=fretboarddpathlarge)
largerootnotefile = PhotoImage(file=fretboarddpathrootnote)
largechordnotefile = PhotoImage(file=fretboarddchordnote)
extendedfretboardfile = PhotoImage(file=extendedfretboardpath)
composerbackgroundfile = PhotoImage(file=composerbackgroundpath)
negativeharmonybackgroundfile = PhotoImage(file=negativeharmonybackgroundpath)

negativeharmonybackgroundfile_pos_1 = PhotoImage(file=negativeharmonybackgroundpath_pos_1)
negativeharmonybackgroundfile_pos_1_pos_1 = PhotoImage(file=negativeharmonybackgroundpath_pos_1_pos_1)
negativeharmonybackgroundfile_pos_1_pos_2= PhotoImage(file=negativeharmonybackgroundpath_pos_1_pos_2)
negativeharmonybackgroundfile_pos_1_pos_3= PhotoImage(file=negativeharmonybackgroundpath_pos_1_pos_3)
negativeharmonybackgroundfile_pos_1_pos_4= PhotoImage(file=negativeharmonybackgroundpath_pos_1_pos_4)
negativeharmonybackgroundfile_pos_1_pos_5= PhotoImage(file=negativeharmonybackgroundpath_pos_1_pos_5)
negativeharmonybackgroundfile_pos_1_pos_6= PhotoImage(file=negativeharmonybackgroundpath_pos_1_pos_6)

negativeharmonybackgroundfile_pos_2 = PhotoImage(file=negativeharmonybackgroundpath_pos_2)
negativeharmonybackgroundfile_pos_2_pos_1= PhotoImage(file=negativeharmonybackgroundpath_pos_2_pos_1)
negativeharmonybackgroundfile_pos_2_pos_2= PhotoImage(file=negativeharmonybackgroundpath_pos_2_pos_2)
negativeharmonybackgroundfile_pos_2_pos_3= PhotoImage(file=negativeharmonybackgroundpath_pos_2_pos_3)
negativeharmonybackgroundfile_pos_2_pos_4= PhotoImage(file=negativeharmonybackgroundpath_pos_2_pos_4)
negativeharmonybackgroundfile_pos_2_pos_5= PhotoImage(file=negativeharmonybackgroundpath_pos_2_pos_5)
negativeharmonybackgroundfile_pos_2_pos_6= PhotoImage(file=negativeharmonybackgroundpath_pos_2_pos_6)

negativeharmonybackgroundfile_pos_3 = PhotoImage(file=negativeharmonybackgroundpath_pos_3)
negativeharmonybackgroundfile_pos_3_pos_1= PhotoImage(file=negativeharmonybackgroundpath_pos_3_pos_1)
negativeharmonybackgroundfile_pos_3_pos_2= PhotoImage(file=negativeharmonybackgroundpath_pos_3_pos_2)
negativeharmonybackgroundfile_pos_3_pos_3= PhotoImage(file=negativeharmonybackgroundpath_pos_3_pos_3)
negativeharmonybackgroundfile_pos_3_pos_4= PhotoImage(file=negativeharmonybackgroundpath_pos_3_pos_4)
negativeharmonybackgroundfile_pos_3_pos_5= PhotoImage(file=negativeharmonybackgroundpath_pos_3_pos_5)
negativeharmonybackgroundfile_pos_3_pos_6= PhotoImage(file=negativeharmonybackgroundpath_pos_3_pos_6)

negativeharmonybackgroundfile_pos_4 = PhotoImage(file=negativeharmonybackgroundpath_pos_4)
negativeharmonybackgroundfile_pos_4_pos_1= PhotoImage(file=negativeharmonybackgroundpath_pos_4_pos_1)
negativeharmonybackgroundfile_pos_4_pos_2= PhotoImage(file=negativeharmonybackgroundpath_pos_4_pos_2)
negativeharmonybackgroundfile_pos_4_pos_3= PhotoImage(file=negativeharmonybackgroundpath_pos_4_pos_3)
negativeharmonybackgroundfile_pos_4_pos_4= PhotoImage(file=negativeharmonybackgroundpath_pos_4_pos_4)
negativeharmonybackgroundfile_pos_4_pos_5= PhotoImage(file=negativeharmonybackgroundpath_pos_4_pos_5)
negativeharmonybackgroundfile_pos_4_pos_6= PhotoImage(file=negativeharmonybackgroundpath_pos_4_pos_6)

negativeharmonybackgroundfile_pos_5 = PhotoImage(file=negativeharmonybackgroundpath_pos_5)
negativeharmonybackgroundfile_pos_5_pos_1= PhotoImage(file=negativeharmonybackgroundpath_pos_5_pos_1)
negativeharmonybackgroundfile_pos_5_pos_2= PhotoImage(file=negativeharmonybackgroundpath_pos_5_pos_2)
negativeharmonybackgroundfile_pos_5_pos_3= PhotoImage(file=negativeharmonybackgroundpath_pos_5_pos_3)
negativeharmonybackgroundfile_pos_5_pos_4= PhotoImage(file=negativeharmonybackgroundpath_pos_5_pos_4)
negativeharmonybackgroundfile_pos_5_pos_5= PhotoImage(file=negativeharmonybackgroundpath_pos_5_pos_5)
negativeharmonybackgroundfile_pos_5_pos_6= PhotoImage(file=negativeharmonybackgroundpath_pos_5_pos_6)

negativeharmonybackgroundfile_pos_6 = PhotoImage(file=negativeharmonybackgroundpath_pos_6)
negativeharmonybackgroundfile_pos_6_pos_1= PhotoImage(file=negativeharmonybackgroundpath_pos_6_pos_1)
negativeharmonybackgroundfile_pos_6_pos_2= PhotoImage(file=negativeharmonybackgroundpath_pos_6_pos_2)
negativeharmonybackgroundfile_pos_6_pos_3= PhotoImage(file=negativeharmonybackgroundpath_pos_6_pos_3)
negativeharmonybackgroundfile_pos_6_pos_4= PhotoImage(file=negativeharmonybackgroundpath_pos_6_pos_4)
negativeharmonybackgroundfile_pos_6_pos_5= PhotoImage(file=negativeharmonybackgroundpath_pos_6_pos_5)
negativeharmonybackgroundfile_pos_6_pos_6= PhotoImage(file=negativeharmonybackgroundpath_pos_6_pos_6)

fretboard01_canvas = Canvas(window, height=114, width=194, bg="black", highlightthickness=0, highlightbackground=color)
fretboard01_canvas.place(x=290, y=33)
fretboard01_canvas.create_image(97, 57, image=fretboardfile)
fretboard02_canvas = Canvas(window, height=114, width=194, bg="black", highlightthickness=0, highlightbackground=color)
fretboard02_canvas.place(x=775, y=33)
fretboard02_canvas.create_image(97, 57, image=fretboardfile)
piano01_canvas = Canvas(window, height=100, width=201, highlightthickness=0, highlightbackground=color)
piano01_canvas.place(x=285, y=155)
piano01_canvas.create_image(100, 50, image=pianofile)
piano02_canvas = Canvas(window, height=100, width=201, highlightthickness=0, highlightbackground=color)
piano02_canvas.place(x=770, y=155)
piano02_canvas.create_image(100, 50, image=pianofile)

window.option_add('*TCombobox*Listbox.font', font_01)

style = ttk.Style()

style.theme_create('combostyle', parent='alt', settings={'TCombobox': {
    'configure': {'selectbackground': listbox_color, 'fieldbackground': listbox_color, 'selectforeground': "black"}}})
style.theme_use('combostyle')

Root_in = None
Root_in_2 = None
Scale_in = None
Scale_in_2 = None
N_Notes_in = 7

is_extended_fretboard_open = False
is_composer_mode_open = False
enable_second_fretboard_drawing = False

UserScale = None

all_notes = []

circle_of_notes_options = ['Chromatic', 'Circle of Fourths', 'Circle of Fifths']

circle_of_notes_left = StringVar()
circle_of_notes_left.set(Negative_Harmony_utils.CIRCLE_OF_NOTES_LEFT_SETTING)

circle_of_notes_right = StringVar()
circle_of_notes_right.set(Negative_Harmony_utils.CIRCLE_OF_NOTES_RIGHT_SETTING)

# GUI VARIABLES

tempo = StringVar()
tempo.set(settings.composer_tempo)
checkbox = FLAT_SETTING
cb = IntVar()
cb.set(FLAT_SETTING)
maj_scale = IntVar()
maj_scale.set(MAJOR_SETTING)
melmin = IntVar()
melmin.set(MELODIC_MINOR_SETTING)
harmin = IntVar()
harmin.set(HARMONIC_MINOR_SETTING)
harmaj = IntVar()
harmaj.set(HARMONIC_MAJOR_SETTING)
dblharmaj = IntVar()
dblharmaj.set(DOUBLE_HARMONIC_MAJOR_SETTING)
neapmaj = IntVar()
neapmaj.set(NEAPOLITAN_MAJOR_SETTING)
neapmin = IntVar()
neapmin.set(NEAPOLITAN_MINOR_SETTING)
hunmaj = IntVar()
hunmaj.set(HUNGARIAN_MAJOR_SETTING)
romaj = IntVar()
romaj.set(ROMANIAN_MAJOR_SETTING)
maj_chord = IntVar()
maj_chord.set(MAJ_SETTING)
majadd2_chord = IntVar()
majadd2_chord.set(MAJADD2_SETTING)
majadd4_chord = IntVar()
majadd4_chord.set(MAJADD4_SETTING)
majadd6_chord = IntVar()
majadd6_chord.set(MAJADD6_SETTING)
maj7_chord = IntVar()
maj7_chord.set(MAJ7_SETTING)
m_chord = IntVar()
m_chord.set(M_SETTING)
madd2_chord = IntVar()
madd2_chord.set(MADD2_SETTING)
madd4_chord = IntVar()
madd4_chord.set(MADD4_SETTING)
madd6_chord = IntVar()
madd6_chord.set(MADD6_SETTING)
m7_chord = IntVar()
m7_chord.set(M7_SETTING)
dom7_chord = IntVar()
dom7_chord.set(DOM7_SETTING)
dom7sus2_chord = IntVar()
dom7sus2_chord.set(DOM7SUS2_SETTING)
dom7sus4_chord = IntVar()
dom7sus4_chord.set(DOM7SUS4_SETTING)
aug_chord = IntVar()
aug_chord.set(AUG_SETTING)
dim_chord = IntVar()
dim_chord.set(DIM_SETTING)
dim7_chord = IntVar()
dim7_chord.set(DIM7_SETTING)
maj7b5_chord = IntVar()
maj7b5_chord.set(MAJ7B5_SETTING)
maj7sharp5_chord = IntVar()
maj7sharp5_chord.set(MAJ7SHARP5_SETTING)
m7b5_chord = IntVar()
m7b5_chord.set(M7B5_SETTING)
m7sharp5_chord = IntVar()
m7sharp5_chord.set(M7SHARP5_SETTING)
dom7b5_chord = IntVar()
dom7b5_chord.set(DOM7B5_SETTING)
dom7sharp5_chord = IntVar()
dom7sharp5_chord.set(DOM7SHARP5_SETTING)
mM7_chord = IntVar()
mM7_chord.set(mM7_SETTING)
sus2_chord = IntVar()
sus2_chord.set(SUS2_SETTING)
sus4_chord = IntVar()
sus4_chord.set(SUS4_SETTING)

v = StringVar()  # a string variable to hold user selection
x = StringVar()
y = IntVar()
z = StringVar()

six_string_tuning = StringVar()
six_string_tuning.set(SIXTH_STRING_SETTING)
five_string_tuning = StringVar()
five_string_tuning.set(FIFTH_STRING_SETTING)
four_string_tuning = StringVar()
four_string_tuning.set(FOURTH_STRING_SETTING)
three_string_tuning = StringVar()
three_string_tuning.set(THIRD_STRING_SETTING)
two_string_tuning = StringVar()
two_string_tuning.set(SECOND_STRING_SETTING)
one_string_tuning = StringVar()
one_string_tuning.set(FIRST_STRING_SETTING)

play_style = StringVar()
play_style.set(PLAY_STYLE_SETTING)

hidden_more_chords = [True, True]
chord_label1 = ttk.Label()
chord_label2 = ttk.Label()
chord_label3 = ttk.Label()
chord_label4 = ttk.Label()
midivar = StringVar()

neg_var = StringVar()

show_chords = False

current_selected_chord_left = "Nothing Here"
current_selected_chord_right = "Nothing Here"

if MAJOR_SETTING == 1:
        UserScale = Scale(Note('C'), "Ionian")
elif MELODIC_MINOR_SETTING == 1:
        UserScale = Scale(Note('C'), "Melodic Minor")
        Scale_in = "Melodic Minor"
elif HARMONIC_MINOR_SETTING == 1:
        UserScale = Scale(Note('C'), "Harmonic Minor")
        Scale_in = "Harmonic Minor"
elif HARMONIC_MAJOR_SETTING == 1:
        UserScale = Scale(Note('C'), "Harmonic Major")
        Scale_in = "Harmonic Major"
elif DOUBLE_HARMONIC_MAJOR_SETTING == 1:
        UserScale = Scale(Note('C'), "Double Harmonic Major")
        Scale_in = "Double Harmonic Major"
elif NEAPOLITAN_MAJOR_SETTING == 1:
        UserScale = Scale(Note('C'), "Neapolitan Major")
        Scale_in = "Neapolitan Major"
elif NEAPOLITAN_MINOR_SETTING == 1:
        UserScale = Scale(Note('C'), "Neapolitan Minor")
        Scale_in = "Neapolitan Minor"
elif HUNGARIAN_MAJOR_SETTING == 1:
        UserScale = Scale(Note('C'), "Hungarian Major")
        Scale_in = "Hungarian Major"
elif ROMANIAN_MAJOR_SETTING == 1:
        UserScale = Scale(Note('C'), "Romanian Major")
        Scale_in = "Romanian Major"

UserScaleBox02 = None
CurrentMatchedScaleIndex = 0
CurrentChord02 = 0  # Actual Chord, Not Index
CurrentChord1Index = -1
CurrentChord2Index = -1
CurrentChord3Index = -1
CurrentChord4Index = -1
common_notes_list = [2, 3, 4, 5, 6, 7]
user_common_notes = []
seven_notes = []
other_seven_notes = []


def update_root_in():
    global all_notes, Root_in
    current = Root_in_box.index(Root_in_box.curselection())
    Root_in_box.delete(0, END)
    counter_root = 0
    for note in all_notes:
        Root_in_box.insert(counter_root, note)
        counter_root = counter_root + 1
    Root_in_box.select_set(current)
    Root_in = Root_in_box.get(current)
    Root_in_box.update_idletasks()


def check_checkbox():
    global all_notes
    if checkbox == 0:
        all_notes = ('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B')
    else:
        all_notes = ('C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B')


def initialize_scales():
    global scales_list
    for i in all_notes:
        for j in settings.scales_names:
            scales_list.append(Scale(i, j))



def update_checkbox():
    global checkbox, Matched_Scales, CurrentMatchedScaleIndex, FLAT_SETTING
    checkbox = (cb.get())

    parser.set('usersettings', 'flat', str(cb.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    check_checkbox()
    update_root_in()

    global scales_list
    scales_list = []
    for i in all_notes:
        for j in settings.scales_names:
            scales_list.append(Scale(i, j))  ### update matched scales list with new # or b name

    if FLAT_SETTING == 0:
        FLAT_SETTING = 1
    else:
        FLAT_SETTING = 0

    try:
        process_matched_scales_right_side()
    except:
        pass

    if Negative_Harmony_utils.is_negative_harmony_open == True:
        Negative_Harmony_utils.update_accidental()
    
def update_SixthString(event):
    global SIXTH_STRING_SETTING
    parser.set('usersettings', 'sixth_string', str(six_string_tuning.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)
        SIXTH_STRING_SETTING = six_string_tuning.get()

        if is_extended_fretboard_open == True:
            global extended_fretboard_canvas
            extended_fretboard_canvas.delete("all")
            extended_fretboard_canvas.create_image(490, 215, image=extendedfretboardfile)
            update_guitar_notes_array()
            MN_Draw.drawExtendedFretboard(UserScale, UserScaleBox02, Root_in, Root_in_2,  extended_fretboard_canvas, show_chords, current_selected_chord_right, current_selected_chord_left, enable_second_fretboard_drawing, largenotefile, largerootnotefile, largechordnotefile)

def update_FifthString(event):
    global FIFTH_STRING_SETTING
    parser.set('usersettings', 'fifth_string', str(five_string_tuning.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)
        FIFTH_STRING_SETTING = five_string_tuning.get()

        if is_extended_fretboard_open == True:
            global extended_fretboard_canvas
            extended_fretboard_canvas.delete("all")
            extended_fretboard_canvas.create_image(490, 215, image=extendedfretboardfile)
            update_guitar_notes_array()
            MN_Draw.drawExtendedFretboard(UserScale, UserScaleBox02, Root_in, Root_in_2,  extended_fretboard_canvas, show_chords, current_selected_chord_right, current_selected_chord_left, enable_second_fretboard_drawing, largenotefile, largerootnotefile, largechordnotefile)

def update_FourthString(event):
    global FOURTH_STRING_SETTING
    parser.set('usersettings', 'fourth_string', str(four_string_tuning.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)
        FOURTH_STRING_SETTING = four_string_tuning.get()

        if is_extended_fretboard_open == True:
            global extended_fretboard_canvas
            extended_fretboard_canvas.delete("all")
            extended_fretboard_canvas.create_image(490, 215, image=extendedfretboardfile)
            update_guitar_notes_array()
            MN_Draw.drawExtendedFretboard(UserScale, UserScaleBox02, Root_in, Root_in_2,  extended_fretboard_canvas, show_chords, current_selected_chord_right, current_selected_chord_left, enable_second_fretboard_drawing, largenotefile, largerootnotefile, largechordnotefile)

def update_ThirdString(event):
    global THIRD_STRING_SETTING
    parser.set('usersettings', 'third_string', str(three_string_tuning.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)
        THIRD_STRING_SETTING = three_string_tuning.get()

        if is_extended_fretboard_open == True:
            global extended_fretboard_canvas
            extended_fretboard_canvas.delete("all")
            extended_fretboard_canvas.create_image(490, 215, image=extendedfretboardfile)
            update_guitar_notes_array()
            MN_Draw.drawExtendedFretboard(UserScale, UserScaleBox02, Root_in, Root_in_2,  extended_fretboard_canvas, show_chords, current_selected_chord_right, current_selected_chord_left, enable_second_fretboard_drawing, largenotefile, largerootnotefile, largechordnotefile)

def update_SecondString(event):
    global SECOND_STRING_SETTING
    parser.set('usersettings', 'second_string', str(two_string_tuning.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)
        SECOND_STRING_SETTING = two_string_tuning.get()

        if is_extended_fretboard_open == True:
            global extended_fretboard_canvas
            extended_fretboard_canvas.delete("all")
            extended_fretboard_canvas.create_image(490, 215, image=extendedfretboardfile)
            update_guitar_notes_array()
            MN_Draw.drawExtendedFretboard(UserScale, UserScaleBox02, Root_in, Root_in_2,  extended_fretboard_canvas, show_chords, current_selected_chord_right, current_selected_chord_left, enable_second_fretboard_drawing, largenotefile, largerootnotefile, largechordnotefile)


def update_FirstString(event):
    global FIRST_STRING_SETTING
    parser.set('usersettings', 'first_string', str(one_string_tuning.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)
        FIRST_STRING_SETTING = one_string_tuning.get()

        if is_extended_fretboard_open == True:
            global extended_fretboard_canvas
            extended_fretboard_canvas.delete("all")
            extended_fretboard_canvas.create_image(490, 215, image=extendedfretboardfile)
            update_guitar_notes_array()
            MN_Draw.drawExtendedFretboard(UserScale, UserScaleBox02, Root_in, Root_in_2,  extended_fretboard_canvas, show_chords, current_selected_chord_right, current_selected_chord_left, enable_second_fretboard_drawing, largenotefile, largerootnotefile, largechordnotefile)

def update_major():
    global MAJOR_SETTING
    settings.major = (maj_scale.get())
    parser.set('usersettings', 'major', str(maj_scale.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if MAJOR_SETTING == 0:
        MAJOR_SETTING = 1
    else:
        MAJOR_SETTING = 0


def update_melodic_minor():
    global MELODIC_MINOR_SETTING
    settings.melodic_minor = (melmin.get())
    parser.set('usersettings', 'melodic_minor', str(melmin.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if MELODIC_MINOR_SETTING == 0:
        MELODIC_MINOR_SETTING = 1
    else:
        MELODIC_MINOR_SETTING = 0

def update_harmonic_minor():
    global HARMONIC_MINOR_SETTING

    settings.harmonic_minor = (harmin.get())
    parser.set('usersettings', 'harmonic_minor', str(harmin.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if HARMONIC_MINOR_SETTING == 0:
        HARMONIC_MINOR_SETTING = 1
    else:
        HARMONIC_MINOR_SETTING = 0

def update_harmonic_major():
    global HARMONIC_MAJOR_SETTING

    settings.harmonic_major = (harmaj.get())
    parser.set('usersettings', 'harmonic_major', str(harmaj.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if HARMONIC_MAJOR_SETTING == 0:
        HARMONIC_MAJOR_SETTING = 1
    else:
        HARMONIC_MAJOR_SETTING = 0

def update_double_harmonic_major():
    global DOUBLE_HARMONIC_MAJOR_SETTING

    settings.double_harmonic_major = (dblharmaj.get())
    parser.set('usersettings', 'double_harmonic_major', str(dblharmaj.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if DOUBLE_HARMONIC_MAJOR_SETTING == 0:
        DOUBLE_HARMONIC_MAJOR_SETTING = 1
    else:
        DOUBLE_HARMONIC_MAJOR_SETTING = 0

def update_neapolitan_major():
    global NEAPOLITAN_MAJOR_SETTING

    settings.neapolitan_major = (neapmaj.get())
    parser.set('usersettings', 'neapolitan_major', str(neapmaj.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if NEAPOLITAN_MAJOR_SETTING == 0:
        NEAPOLITAN_MAJOR_SETTING = 1
    else:
        NEAPOLITAN_MAJOR_SETTING = 0

def update_neapolitan_minor():
    global NEAPOLITAN_MINOR_SETTING

    settings.neapolitan_minor = (neapmin.get())
    parser.set('usersettings', 'neapolitan_minor', str(neapmin.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if NEAPOLITAN_MINOR_SETTING == 0:
        NEAPOLITAN_MINOR_SETTING = 1
    else:
        NEAPOLITAN_MINOR_SETTING = 0

def update_hungarian_major():
    global HUNGARIAN_MAJOR_SETTING

    settings.hungarian_major = (hunmaj.get())
    parser.set('usersettings', 'hungarian_major', str(hunmaj.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if HUNGARIAN_MAJOR_SETTING == 0:
        HUNGARIAN_MAJOR_SETTING = 1
    else:
        HUNGARIAN_MAJOR_SETTING = 0

def update_romanian_major():
    global ROMANIAN_MAJOR_SETTING

    settings.romanian_major = (romaj.get())
    parser.set('usersettings', 'romanian_major', str(romaj.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if ROMANIAN_MAJOR_SETTING == 0:
        ROMANIAN_MAJOR_SETTING = 1
    else:
        ROMANIAN_MAJOR_SETTING = 0

def update_maj_chord():
    global MAJ_SETTING
    settings.maj = (maj_chord.get())
    parser.set('usersettings', 'maj', str(maj_chord.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if MAJ_SETTING == 0:
        MAJ_SETTING = 1
    else:
        MAJ_SETTING = 0

def update_majadd2_chord():
    global MAJADD2_SETTING
    settings.majadd2 = (majadd2_chord.get())
    parser.set('usersettings', 'majadd2', str(majadd2_chord.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if MAJADD2_SETTING == 0:
        MAJADD2_SETTING = 1
    else:
        MAJADD2_SETTING = 0

def update_majadd4_chord():
    global MAJADD4_SETTING
    settings.majadd4 = (majadd4_chord.get())
    parser.set('usersettings', 'majadd4', str(majadd4_chord.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if MAJADD4_SETTING == 0:
        MAJADD4_SETTING = 1
    else:
        MAJADD4_SETTING = 0

def update_majadd6_chord():
    global MAJADD6_SETTING
    settings.majadd6 = (majadd6_chord.get())
    parser.set('usersettings', 'majadd6', str(majadd6_chord.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if MAJADD6_SETTING == 0:
        MAJADD6_SETTING = 1
    else:
        MAJADD6_SETTING = 0

def update_maj7_chord():
    global MAJ7_SETTING
    settings.maj7 = (maj7_chord.get())
    parser.set('usersettings', 'maj7', str(maj7_chord.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if MAJ7_SETTING == 0:
        MAJ7_SETTING = 1
    else:
        MAJ7_SETTING = 0

def update_maj7b5_chord():
    global MAJ7B5_SETTING
    settings.maj7b5 = (maj7b5_chord.get())
    parser.set('usersettings', 'maj7b5', str(maj7b5_chord.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if MAJ7B5_SETTING == 0:
        MAJ7B5_SETTING = 1
    else:
        MAJ7B5_SETTING = 0

def update_maj7sharp5_chord():
    global MAJ7SHARP5_SETTING
    settings.maj7sharp5 = (maj7sharp5_chord.get())
    parser.set('usersettings', 'maj7#5', str(maj7sharp5_chord.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if MAJ7SHARP5_SETTING == 0:
        MAJ7SHARP5_SETTING = 1
    else:
        MAJ7SHARP5_SETTING = 0

def update_m_chord():
    global M_SETTING
    settings.m = (m_chord.get())
    parser.set('usersettings', 'm', str(m_chord.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if M_SETTING == 0:
        M_SETTING = 1
    else:
        M_SETTING = 0

def update_madd2_chord():
    global MADD2_SETTING
    settings.madd2 = (madd2_chord.get())
    parser.set('usersettings', 'madd2', str(madd2_chord.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if MADD2_SETTING == 0:
        MADD2_SETTING = 1
    else:
        MADD2_SETTING = 0

def update_madd4_chord():
    global MADD4_SETTING
    settings.madd4 = (madd4_chord.get())
    parser.set('usersettings', 'madd4', str(madd4_chord.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if MADD4_SETTING == 0:
        MADD4_SETTING = 1
    else:
        MADD4_SETTING = 0

def update_madd6_chord():
    global MADD6_SETTING
    settings.madd6 = (madd6_chord.get())
    parser.set('usersettings', 'madd6', str(madd6_chord.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if MADD6_SETTING == 0:
        MADD6_SETTING = 1
    else:
        MADD6_SETTING = 0

def update_m7_chord():
    global M7_SETTING
    settings.m7 = (m7_chord.get())
    parser.set('usersettings', 'm7', str(m7_chord.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if M7_SETTING == 0:
        M7_SETTING = 1
    else:
        M7_SETTING = 0

def update_m7b5_chord():
    global M7B5_SETTING
    settings.m7b5 = (m7b5_chord.get())
    parser.set('usersettings', 'm7b5', str(m7b5_chord.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if M7B5_SETTING == 0:
        M7B5_SETTING = 1
    else:
        M7B5_SETTING = 0

def update_m7sharp5_chord():
    global M7SHARP5_SETTING
    settings.m7sharp5 = (m7sharp5_chord.get())
    parser.set('usersettings', 'm7#5', str(m7sharp5_chord.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if M7SHARP5_SETTING == 0:
        M7SHARP5_SETTING = 1
    else:
        M7SHARP5_SETTING = 0

def update_mM7_chord():
    global mM7_SETTING
    settings.mM7 = (mM7_chord.get())
    parser.set('usersettings', 'mM7', str(mM7_chord.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if mM7_SETTING == 0:
        mM7_SETTING = 1
    else:
        mM7_SETTING = 0

def update_aug_chord():
    global AUG_SETTING
    settings.aug = (aug_chord.get())
    parser.set('usersettings', '+', str(aug_chord.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if AUG_SETTING == 0:
        AUG_SETTING = 1
    else:
        AUG_SETTING = 0

def update_dim_chord():
    global DIM_SETTING
    settings.dim = (dim_chord.get())
    parser.set('usersettings', 'dim', str(dim_chord.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if DIM_SETTING == 0:
        DIM_SETTING = 1
    else:
        DIM_SETTING = 0

def update_dim7_chord():
    global DIM7_SETTING
    settings.dim7 = (dim7_chord.get())
    parser.set('usersettings', 'dim7', str(dim7_chord.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if DIM7_SETTING == 0:
        DIM7_SETTING = 1
    else:
        DIM7_SETTING = 0

def update_dom7_chord():
    global DOM7_SETTING
    settings.dom7 = (dom7_chord.get())
    parser.set('usersettings', '7', str(dom7_chord.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if DOM7_SETTING == 0:
        DOM7_SETTING = 1
    else:
        DOM7_SETTING = 0

def update_dom7b5_chord():
    global DOM7B5_SETTING
    settings.dom7b5 = (dom7b5_chord.get())
    parser.set('usersettings', '7b5', str(dom7b5_chord.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if DOM7B5_SETTING == 0:
        DOM7B5_SETTING = 1
    else:
        DOM7B5_SETTING = 0

def update_dom7sharp5_chord():
    global DOM7SHARP5_SETTING
    settings.dom7sharp5 = (dom7sharp5_chord.get())
    parser.set('usersettings', '7#5', str(dom7sharp5_chord.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if DOM7SHARP5_SETTING == 0:
        DOM7SHARP5_SETTING = 1
    else:
        DOM7SHARP5_SETTING = 0

def update_sus2_chord():
    global SUS2_SETTING
    settings.sus2 = (sus2_chord.get())
    parser.set('usersettings', 'sus2', str(sus2_chord.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if SUS2_SETTING == 0:
        SUS2_SETTING = 1
    else:
        SUS2_SETTING = 0

def update_sus4_chord():
    global SUS4_SETTING
    settings.sus4 = (sus4_chord.get())
    parser.set('usersettings', 'sus4', str(sus4_chord.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if SUS4_SETTING == 0:
        SUS4_SETTING = 1
    else:
        SUS4_SETTING = 0

def update_dom7sus2_chord():
    global DOM7SUS2_SETTING
    settings.dom7sus2 = (dom7sus2_chord.get())
    parser.set('usersettings', '7sus2', str(dom7sus2_chord.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if DOM7SUS2_SETTING == 0:
        DOM7SUS2_SETTING = 1
    else:
        DOM7SUS2_SETTING = 0

def update_dom7sus4_chord():
    global DOM7SUS4_SETTING
    settings.dom7sus4 = (dom7sus4_chord.get())
    parser.set('usersettings', '7sus4', str(dom7sus4_chord.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if DOM7SUS4_SETTING == 0:
        DOM7SUS4_SETTING = 1
    else:
        DOM7SUS4_SETTING = 0

def Exit():
    pygame.mixer.quit()
    
    temp_chord_progression = open(tmpcomposerpath, 'w')
    temp_chord_progression.write("")
    temp_chord_progression.close()

    window.destroy()

def set_negative_display(event):

    settings.negative_harmony_display_selected = str(neg_var.get())
    Negative_Harmony_utils.update_negative_display(str(neg_var.get()))

    parser.set('usersettings', 'negative_display', str(neg_var.get()))
    with open(usersettingspath, 'w') as configfile:
        parser.write(configfile)

    if Negative_Harmony_utils.is_negative_harmony_open == True:

        if (Root_in != None and Scale_in != None):

            list_of_inverted_scale_notes = Negative_Harmony_utils.calculate_inverted_scale_notes(1, Root_in, Scale_in)

            Negative_Harmony_utils.update_scale_labels(Negative_Harmony_utils.InvertedScale(list_of_inverted_scale_notes, Negative_Harmony_utils.Mode_1_Negative_Chords_Listbox_left), Negative_Harmony_utils.Mode2_notes_label_left, 1, settings.darkgrey, font_01)
            Negative_Harmony_utils.Mode_1_Negative_label_left.config(text=(Negative_Harmony_utils.InvertedScale(list_of_inverted_scale_notes, Negative_Harmony_utils.Mode_1_Negative_Chords_Listbox_left)), foreground="white", bg=settings.darkgrey, font=font_01)


        if (Root_in_2 != None and Scale_in_2 != None):

            list_of_inverted_scale_notes = Negative_Harmony_utils.calculate_inverted_scale_notes(2, Root_in_2, Scale_in_2)

            Negative_Harmony_utils.update_scale_labels(Negative_Harmony_utils.InvertedScale(list_of_inverted_scale_notes, Negative_Harmony_utils.Mode_1_Negative_Chords_Listbox_right), Negative_Harmony_utils.Mode2_notes_label_right, 2, settings.darkgrey, font_01)
            Negative_Harmony_utils.Mode_1_Negative_label_right.config(text=(Negative_Harmony_utils.InvertedScale(list_of_inverted_scale_notes, Negative_Harmony_utils.Mode_1_Negative_Chords_Listbox_right)), foreground="white", bg=settings.darkgrey, font=font_01)


def Open_Settings():
    top = Toplevel()
    top.geometry("839x565+550+400")
    top.config(bg=color)
    top.resizable(False, False)

    settingsbackgroundimgfile = PhotoImage(file=settingsbackgroundpath)
    settingsbackground = Label(top, image=settingsbackgroundimgfile)
    settingsbackground.image = settingsbackgroundimgfile
    settingsbackground.place(x=0, y=-0)

    checkbox = Checkbutton(top, variable=cb, command=update_checkbox, bg="white")  # Show flats
    checkbox.bind()
    checkbox.place(x=205, y=65)
    checkbox.config(font=font_01)

    negative_harmony_display = ttk.Combobox(top, textvariable=neg_var, values=negative_harmony_display_options, state='readonly', width=28)
    negative_harmony_display.config(font=font_01)
    cur_neg_idx = settings.negative_harmony_display_options.index(NEGATIVE_HARMONY_DISPLAY_SETTING)
    negative_harmony_display.current(cur_neg_idx)
    negative_harmony_display.bind('<<ComboboxSelected>>', set_negative_display)
    negative_harmony_display.place(x=540, y=69)

    global all_notes, six_string_tuning, five_string_tuning, four_string_tuning, three_string_tuning, two_string_tuning, one_string_tuning

    string_offset = 38

    SixthString = OptionMenu(top, six_string_tuning, *all_notes, command=update_SixthString)
    SixthString.bind()
    SixthString.place(x=460, y=65+string_offset)
    SixthString.config(font=font_01)

    FifthString = OptionMenu(top, five_string_tuning, *all_notes, command=update_FifthString)
    FifthString.bind()
    FifthString.place(x=510, y=65+string_offset)
    FifthString.config(font=font_01)

    FourthString = OptionMenu(top, four_string_tuning, *all_notes, command=update_FourthString)
    FourthString.bind()
    FourthString.place(x=560, y=65+string_offset)
    FourthString.config(font=font_01)

    ThirdString = OptionMenu(top, three_string_tuning, *all_notes, command=update_ThirdString)
    ThirdString.bind()
    ThirdString.place(x=610, y=65+string_offset)
    ThirdString.config(font=font_01)

    SecondString = OptionMenu(top, two_string_tuning, *all_notes, command=update_SecondString)
    SecondString.bind()
    SecondString.place(x=660, y=65+string_offset)
    SecondString.config(font=font_01)

    FirstString = OptionMenu(top, one_string_tuning, *all_notes, command=update_FirstString)
    FirstString.bind()
    FirstString.place(x=710, y=65+string_offset)
    FirstString.config(font=font_01)

    scales_chords_checkbox_offset = 27

    majorcheckbox = Checkbutton(top, variable=maj_scale, command=update_major, bg="white")
    majorcheckbox.bind()
    majorcheckbox.place(x=205, y=148+scales_chords_checkbox_offset)
    majorcheckbox.config(font=font_01)

    melodic_minor_checkbox = Checkbutton(top, variable=melmin, command=update_melodic_minor, bg="white")
    melodic_minor_checkbox.bind()
    melodic_minor_checkbox.place(x=205, y=184+scales_chords_checkbox_offset)
    melodic_minor_checkbox.config(font=font_01)

    harmonic_minor_checkbox = Checkbutton(top, variable=harmin, command=update_harmonic_minor, bg="white")
    harmonic_minor_checkbox.bind()
    harmonic_minor_checkbox.place(x=205, y=221+scales_chords_checkbox_offset) # +37 px
    harmonic_minor_checkbox.config(font=font_01)

    harmonic_major_checkbox = Checkbutton(top, variable=harmaj, command=update_harmonic_major, bg="white")
    harmonic_major_checkbox.bind()
    harmonic_major_checkbox.place(x=205, y=259+scales_chords_checkbox_offset) # +37 px
    harmonic_major_checkbox.config(font=font_01)

    double_harmonic_major_checkbox = Checkbutton(top, variable=dblharmaj, command=update_double_harmonic_major, bg="white")
    double_harmonic_major_checkbox.bind()
    double_harmonic_major_checkbox.place(x=205, y=299+scales_chords_checkbox_offset) # +37 px
    double_harmonic_major_checkbox.config(font=font_01)

    neapolitan_major_checkbox = Checkbutton(top, variable=neapmaj, command=update_neapolitan_major, bg="white")
    neapolitan_major_checkbox.bind()
    neapolitan_major_checkbox.place(x=205, y=339+scales_chords_checkbox_offset) # +37 px
    neapolitan_major_checkbox.config(font=font_01)

    neapolitan_minor_checkbox = Checkbutton(top, variable=neapmin, command=update_neapolitan_minor, bg="white")
    neapolitan_minor_checkbox.bind()
    neapolitan_minor_checkbox.place(x=205, y=377+scales_chords_checkbox_offset) # +37 px
    neapolitan_minor_checkbox.config(font=font_01)

    hungarian_major_checkbox = Checkbutton(top, variable=hunmaj, command=update_hungarian_major, bg="white")
    hungarian_major_checkbox.bind()
    hungarian_major_checkbox.place(x=205, y=414+scales_chords_checkbox_offset) # +37 px
    hungarian_major_checkbox.config(font=font_01)

    romanian_major_checkbox = Checkbutton(top, variable=romaj, command=update_romanian_major, bg="white")
    romanian_major_checkbox.bind()
    romanian_major_checkbox.place(x=205, y=452+scales_chords_checkbox_offset) # +37 px
    romanian_major_checkbox.config(font=font_01)

    maj_checkbox = Checkbutton(top, variable=maj_chord, command=update_maj_chord, bg="white")
    maj_checkbox.bind()
    maj_checkbox.place(x=425, y=148+scales_chords_checkbox_offset)  # +37 px
    maj_checkbox.config(font=font_01)

    majadd2_checkbox = Checkbutton(top, variable=majadd2_chord, command=update_majadd2_chord, bg="white")
    majadd2_checkbox.bind()
    majadd2_checkbox.place(x=425, y=184+scales_chords_checkbox_offset)  # +37 px
    majadd2_checkbox.config(font=font_01)

    majadd4_checkbox = Checkbutton(top, variable=majadd4_chord, command=update_majadd4_chord, bg="white")
    majadd4_checkbox.bind()
    majadd4_checkbox.place(x=425, y=221+scales_chords_checkbox_offset)  # +37 px
    majadd4_checkbox.config(font=font_01)

    majadd6_checkbox = Checkbutton(top, variable=majadd6_chord, command=update_majadd6_chord, bg="white")
    majadd6_checkbox.bind()
    majadd6_checkbox.place(x=425, y=259+scales_chords_checkbox_offset)  # +37 px
    majadd6_checkbox.config(font=font_01)

    maj7_checkbox = Checkbutton(top, variable=maj7_chord, command=update_maj7_chord, bg="white")
    maj7_checkbox.bind()
    maj7_checkbox.place(x=425, y=299+scales_chords_checkbox_offset)  # +37 px
    maj7_checkbox.config(font=font_01)

    maj7b5_checkbox = Checkbutton(top, variable=maj7b5_chord, command=update_maj7b5_chord, bg="white")
    maj7b5_checkbox.bind()
    maj7b5_checkbox.place(x=425, y=339+scales_chords_checkbox_offset)  # +37 px
    maj7b5_checkbox.config(font=font_01)

    maj7sharp5_checkbox = Checkbutton(top, variable=maj7sharp5_chord, command=update_maj7sharp5_chord, bg="white")
    maj7sharp5_checkbox.bind()
    maj7sharp5_checkbox.place(x=425, y=377+scales_chords_checkbox_offset)  # +37 px
    maj7sharp5_checkbox.config(font=font_01)

    m_checkbox = Checkbutton(top, variable=m_chord, command=update_m_chord, bg="white")
    m_checkbox.bind()
    m_checkbox.place(x=550, y=148+scales_chords_checkbox_offset)  # +37 px
    m_checkbox.config(font=font_01)

    madd2_checkbox = Checkbutton(top, variable=madd2_chord, command=update_madd2_chord, bg="white")
    madd2_checkbox.bind()
    madd2_checkbox.place(x=550, y=184+scales_chords_checkbox_offset)  # +37 px
    madd2_checkbox.config(font=font_01)

    madd4_checkbox = Checkbutton(top, variable=madd4_chord, command=update_madd4_chord, bg="white")
    madd4_checkbox.bind()
    madd4_checkbox.place(x=550, y=221+scales_chords_checkbox_offset)  # +37 px
    madd4_checkbox.config(font=font_01)

    madd6_checkbox = Checkbutton(top, variable=madd6_chord, command=update_madd6_chord, bg="white")
    madd6_checkbox.bind()
    madd6_checkbox.place(x=550, y=259+scales_chords_checkbox_offset)  # +37 px
    madd6_checkbox.config(font=font_01)

    m7_checkbox = Checkbutton(top, variable=m7_chord, command=update_m7_chord, bg="white")
    m7_checkbox.bind()
    m7_checkbox.place(x=550, y=299+scales_chords_checkbox_offset)  # +37 px
    m7_checkbox.config(font=font_01)

    m7b5_checkbox = Checkbutton(top, variable=m7b5_chord, command=update_m7b5_chord, bg="white")
    m7b5_checkbox.bind()
    m7b5_checkbox.place(x=550, y=339+scales_chords_checkbox_offset)  # +37 px
    m7b5_checkbox.config(font=font_01)

    m7sharp5_checkbox = Checkbutton(top, variable=m7sharp5_chord, command=update_m7sharp5_chord, bg="white")
    m7sharp5_checkbox.bind()
    m7sharp5_checkbox.place(x=550, y=377+scales_chords_checkbox_offset)  # +37 px
    m7sharp5_checkbox.config(font=font_01)

    mM7_checkbox = Checkbutton(top, variable=mM7_chord, command=update_mM7_chord, bg="white")
    mM7_checkbox.bind()
    mM7_checkbox.place(x=550, y=414+scales_chords_checkbox_offset)  # +37 px
    mM7_checkbox.config(font=font_01)

    aug_checkbox = Checkbutton(top, variable=aug_chord, command=update_aug_chord, bg="white")
    aug_checkbox.bind()
    aug_checkbox.place(x=650, y=148+scales_chords_checkbox_offset)  # +37 px
    aug_checkbox.config(font=font_01)

    dim_checkbox = Checkbutton(top, variable=dim_chord, command=update_dim_chord, bg="white")
    dim_checkbox.bind()
    dim_checkbox.place(x=650, y=184+scales_chords_checkbox_offset)  # +37 px
    dim_checkbox.config(font=font_01)

    dim7_checkbox = Checkbutton(top, variable=dim7_chord, command=update_dim7_chord, bg="white")
    dim7_checkbox.bind()
    dim7_checkbox.place(x=650, y=221+scales_chords_checkbox_offset)  # +37 px
    dim7_checkbox.config(font=font_01)

    dom7_checkbox = Checkbutton(top, variable=dom7_chord, command=update_dom7_chord, bg="white")
    dom7_checkbox.bind()
    dom7_checkbox.place(x=650, y=299+scales_chords_checkbox_offset)  # +37 px
    dom7_checkbox.config(font=font_01)

    dom7_b5_checkbox = Checkbutton(top, variable=dom7b5_chord, command=update_dom7b5_chord, bg="white")
    dom7_b5_checkbox.bind()
    dom7_b5_checkbox.place(x=650, y=339+scales_chords_checkbox_offset)  # +37 px
    dom7_b5_checkbox.config(font=font_01)

    dom7_sharp5_checkbox = Checkbutton(top, variable=dom7sharp5_chord, command=update_dom7sharp5_chord, bg="white")
    dom7_sharp5_checkbox.bind()
    dom7_sharp5_checkbox.place(x=650, y=377+scales_chords_checkbox_offset)  # +37 px
    dom7_sharp5_checkbox.config(font=font_01)

    sus2_checkbox = Checkbutton(top, variable=sus2_chord, command=update_sus2_chord, bg="white")
    sus2_checkbox.bind()
    sus2_checkbox.place(x=785, y=148+scales_chords_checkbox_offset)  # +37 px
    sus2_checkbox.config(font=font_01)

    sus4_checkbox = Checkbutton(top, variable=sus4_chord, command=update_sus4_chord, bg="white")
    sus4_checkbox.bind()
    sus4_checkbox.place(x=785, y=184+scales_chords_checkbox_offset)  # +37 px
    sus4_checkbox.config(font=font_01)

    dom_sus2_checkbox = Checkbutton(top, variable=dom7sus2_chord, command=update_dom7sus2_chord, bg="white")
    dom_sus2_checkbox.bind()
    dom_sus2_checkbox.place(x=785, y=299+scales_chords_checkbox_offset)  # +37 px
    dom_sus2_checkbox.config(font=font_01)

    dom_sus4_checkbox = Checkbutton(top, variable=dom7sus4_chord, command=update_dom7sus4_chord, bg="white")
    dom_sus4_checkbox.bind()
    dom_sus4_checkbox.place(x=785, y=339+scales_chords_checkbox_offset)  # +37 px
    dom_sus4_checkbox.config(font=font_01)

    def process_scales_button(option):

        global MAJOR_SETTING
        global MELODIC_MINOR_SETTING
        global HARMONIC_MINOR_SETTING
        global HARMONIC_MAJOR_SETTING
        global DOUBLE_HARMONIC_MAJOR_SETTING
        global NEAPOLITAN_MAJOR_SETTING
        global NEAPOLITAN_MINOR_SETTING
        global HUNGARIAN_MAJOR_SETTING
        global ROMANIAN_MAJOR_SETTING

        if option == "-":

            parser.set('usersettings', 'major', "1")
            parser.set('usersettings', 'melodic_minor', "0")
            parser.set('usersettings', 'harmonic_minor', "0")
            parser.set('usersettings', 'harmonic_major', "0")
            parser.set('usersettings', 'double_harmonic_major', "0")
            parser.set('usersettings', 'neapolitan_major', "0")
            parser.set('usersettings', 'neapolitan_minor', "0")
            parser.set('usersettings', 'hungarian_major', "0")
            parser.set('usersettings', 'romanian_major', "0")
            with open(usersettingspath, 'w') as configfile:
                parser.write(configfile)

            MAJOR_SETTING = 1
            MELODIC_MINOR_SETTING = 0
            HARMONIC_MINOR_SETTING = 0
            HARMONIC_MAJOR_SETTING = 0
            DOUBLE_HARMONIC_MAJOR_SETTING = 0
            NEAPOLITAN_MAJOR_SETTING = 0
            NEAPOLITAN_MINOR_SETTING = 0
            HUNGARIAN_MAJOR_SETTING = 0
            ROMANIAN_MAJOR_SETTING = 0

            maj_scale.set(1)
            melmin.set(0)
            harmin.set(0)
            harmaj.set(0)
            dblharmaj.set(0)
            neapmaj.set(0)
            neapmin.set(0)
            hunmaj.set(0)
            romaj.set(0)

        elif option == "+":

            parser.set('usersettings', 'major', "1")
            parser.set('usersettings', 'melodic_minor', "1")
            parser.set('usersettings', 'harmonic_minor', "1")
            parser.set('usersettings', 'harmonic_major', "0")
            parser.set('usersettings', 'double_harmonic_major', "0")
            parser.set('usersettings', 'neapolitan_major', "0")
            parser.set('usersettings', 'neapolitan_minor', "0")
            parser.set('usersettings', 'hungarian_major', "0")
            parser.set('usersettings', 'romanian_major', "0")
            with open(usersettingspath, 'w') as configfile:
                parser.write(configfile)

            MAJOR_SETTING = 1
            MELODIC_MINOR_SETTING = 1
            HARMONIC_MINOR_SETTING = 1
            HARMONIC_MAJOR_SETTING = 0
            DOUBLE_HARMONIC_MAJOR_SETTING = 0
            NEAPOLITAN_MAJOR_SETTING = 0
            NEAPOLITAN_MINOR_SETTING = 0
            HUNGARIAN_MAJOR_SETTING = 0
            ROMANIAN_MAJOR_SETTING = 0

            maj_scale.set(1)
            melmin.set(1)
            harmin.set(1)
            harmaj.set(0)
            dblharmaj.set(0)
            neapmaj.set(0)
            neapmin.set(0)
            hunmaj.set(0)
            romaj.set(0)

        elif option == "++":
            parser.set('usersettings', 'major', "1")
            parser.set('usersettings', 'melodic_minor', "1")
            parser.set('usersettings', 'harmonic_minor', "1")
            parser.set('usersettings', 'harmonic_major', "1")
            parser.set('usersettings', 'double_harmonic_major', "1")
            parser.set('usersettings', 'neapolitan_major', "1")
            parser.set('usersettings', 'neapolitan_minor', "1")
            parser.set('usersettings', 'hungarian_major', "1")
            parser.set('usersettings', 'romanian_major', "1")
            with open(usersettingspath, 'w') as configfile:
                parser.write(configfile)

            MAJOR_SETTING = 1
            MELODIC_MINOR_SETTING = 1
            HARMONIC_MINOR_SETTING = 1
            HARMONIC_MAJOR_SETTING = 1
            DOUBLE_HARMONIC_MAJOR_SETTING = 1
            NEAPOLITAN_MAJOR_SETTING = 1
            NEAPOLITAN_MINOR_SETTING = 1
            HUNGARIAN_MAJOR_SETTING = 1
            ROMANIAN_MAJOR_SETTING = 1

            maj_scale.set(1)
            melmin.set(1)
            harmin.set(1)
            harmaj.set(1)
            dblharmaj.set(1)
            neapmaj.set(1)
            neapmin.set(1)
            hunmaj.set(1)
            romaj.set(1)

    button_offset = -30

    basic_scales_button = Button(top, text="-", width=7, highlightthickness=0, command=lambda: process_scales_button("-"))
    basic_scales_button.place(x=80, y=553+button_offset)

    more_scales_button= Button(top, text="+", width=7, highlightthickness=0, command=lambda: process_scales_button("+"))
    more_scales_button.place(x=153, y=553+button_offset)

    all_scales_button= Button(top, text="++", width=7, highlightthickness=0, command=lambda: process_scales_button("++"))
    all_scales_button.place(x=226, y=553+button_offset)

    def process_chords_button(option):

        global MAJ_SETTING
        global MAJADD2_SETTING
        global MAJADD4_SETTING
        global MAJADD6_SETTING
        global MAJ7_SETTING
        global M_SETTING
        global MADD2_SETTING
        global MADD4_SETTING
        global MADD6_SETTING
        global M7_SETTING
        global DOM7_SETTING
        global DOM7SUS2_SETTING
        global DOM7SUS4_SETTING
        global AUG_SETTING
        global DIM_SETTING
        global DIM7_SETTING
        global MAJ7B5_SETTING
        global MAJ7SHARP5_SETTING
        global M7B5_SETTING
        global M7SHARP5_SETTING
        global DOM7B5_SETTING
        global DOM7SHARP5_SETTING
        global mM7_SETTING
        global SUS2_SETTING
        global SUS4_SETTING

        if option == "-":

            parser.set('usersettings', 'maj', "1")
            parser.set('usersettings', 'majadd2', "0")
            parser.set('usersettings', 'majadd4', "0")
            parser.set('usersettings', 'majadd6', "0")
            parser.set('usersettings', 'maj7', "0")
            parser.set('usersettings', 'maj7b5', "0")
            parser.set('usersettings', 'maj7#5', "0")
            parser.set('usersettings', 'm', "1")
            parser.set('usersettings', 'madd2', "0")
            parser.set('usersettings', 'madd4', "0")
            parser.set('usersettings', 'madd6', "0")
            parser.set('usersettings', 'm7', "0")
            parser.set('usersettings', 'm7b5', "0")
            parser.set('usersettings', 'm7#5', "0")
            parser.set('usersettings', 'mM7', "0")
            parser.set('usersettings', '+', "0")
            parser.set('usersettings', 'dim', "1")
            parser.set('usersettings', 'dim7', "0")
            parser.set('usersettings', '7', "1")
            parser.set('usersettings', '7b5', "0")
            parser.set('usersettings', '7#5', "0")
            parser.set('usersettings', 'sus2', "0")
            parser.set('usersettings', 'sus4', "0")
            parser.set('usersettings', '7sus2', "0")
            parser.set('usersettings', '7sus4', "0")
            with open(usersettingspath, 'w') as configfile:
                parser.write(configfile)

            MAJ_SETTING = 1
            MAJADD2_SETTING = 0
            MAJADD4_SETTING = 0
            MAJADD6_SETTING = 0
            MAJ7_SETTING = 0
            MAJ7B5_SETTING = 0
            MAJ7SHARP5_SETTING = 0
            M_SETTING = 1
            MADD2_SETTING = 0
            MADD4_SETTING = 0
            MADD6_SETTING = 0
            M7_SETTING = 0
            M7B5_SETTING = 0
            M7SHARP5_SETTING = 0
            mM7_SETTING = 0
            AUG_SETTING = 0
            DIM_SETTING = 1
            DIM7_SETTING = 0
            DOM7_SETTING = 1
            DOM7B5_SETTING = 0
            DOM7SHARP5_SETTING = 0
            SUS2_SETTING = 0
            SUS4_SETTING = 0
            DOM7SUS2_SETTING = 0
            DOM7SUS4_SETTING = 0

            maj_chord.set(1)
            majadd2_chord.set(0)
            majadd4_chord.set(0)
            majadd6_chord.set(0)
            maj7_chord.set(0)
            maj7b5_chord.set(0)
            maj7sharp5_chord.set(0)
            m_chord.set(1)
            madd2_chord.set(0)
            madd4_chord.set(0)
            madd6_chord.set(0)
            m7_chord.set(0)
            m7b5_chord.set(0)
            m7sharp5_chord.set(0)
            mM7_chord.set(0)
            aug_chord.set(0)
            dim_chord.set(1)
            dim7_chord.set(0)
            dom7_chord.set(1)
            dom7b5_chord.set(0)
            dom7sharp5_chord.set(0)
            sus2_chord.set(0)
            sus4_chord.set(0)
            dom7sus2_chord.set(0)
            dom7sus4_chord.set(0)

        elif option == "+":

            parser.set('usersettings', 'maj', "1")
            parser.set('usersettings', 'majadd2', "0")
            parser.set('usersettings', 'majadd4', "0")
            parser.set('usersettings', 'majadd6', "0")
            parser.set('usersettings', 'maj7', "1")
            parser.set('usersettings', 'maj7b5', "0")
            parser.set('usersettings', 'maj7#5', "0")
            parser.set('usersettings', 'm', "1")
            parser.set('usersettings', 'madd2', "0")
            parser.set('usersettings', 'madd4', "0")
            parser.set('usersettings', 'madd6', "0")
            parser.set('usersettings', 'm7', "1")
            parser.set('usersettings', 'm7b5', "0")
            parser.set('usersettings', 'm7#5', "0")
            parser.set('usersettings', 'mM7', "1")
            parser.set('usersettings', '+', "0")
            parser.set('usersettings', 'dim', "1")
            parser.set('usersettings', 'dim7', "0")
            parser.set('usersettings', '7', "1")
            parser.set('usersettings', '7b5', "0")
            parser.set('usersettings', '7#5', "0")
            parser.set('usersettings', 'sus2', "0")
            parser.set('usersettings', 'sus4', "0")
            parser.set('usersettings', '7sus2', "0")
            parser.set('usersettings', '7sus4', "0")
            with open(usersettingspath, 'w') as configfile:
                parser.write(configfile)

            MAJ_SETTING = 1
            MAJADD2_SETTING = 0
            MAJADD4_SETTING = 0
            MAJADD6_SETTING = 0
            MAJ7_SETTING = 1
            MAJ7B5_SETTING = 0
            MAJ7SHARP5_SETTING = 0
            M_SETTING = 1
            MADD2_SETTING = 0
            MADD4_SETTING = 0
            MADD6_SETTING = 0
            M7_SETTING = 1
            M7B5_SETTING = 0
            M7SHARP5_SETTING = 0
            mM7_SETTING = 1
            AUG_SETTING = 0
            DIM_SETTING = 1
            DIM7_SETTING = 0
            DOM7_SETTING = 1
            DOM7B5_SETTING = 0
            DOM7SHARP5_SETTING = 0
            SUS2_SETTING = 0
            SUS4_SETTING = 0
            DOM7SUS2_SETTING = 0
            DOM7SUS4_SETTING = 0

            maj_chord.set(1)
            majadd2_chord.set(0)
            majadd4_chord.set(0)
            majadd6_chord.set(0)
            maj7_chord.set(1)
            maj7b5_chord.set(0)
            maj7sharp5_chord.set(0)
            m_chord.set(1)
            madd2_chord.set(0)
            madd4_chord.set(0)
            madd6_chord.set(0)
            m7_chord.set(1)
            m7b5_chord.set(0)
            m7sharp5_chord.set(0)
            mM7_chord.set(1)
            aug_chord.set(0)
            dim_chord.set(1)
            dim7_chord.set(0)
            dom7_chord.set(1)
            dom7b5_chord.set(0)
            dom7sharp5_chord.set(0)
            sus2_chord.set(0)
            sus4_chord.set(0)
            dom7sus2_chord.set(0)
            dom7sus4_chord.set(0)

        elif option == "++":

            parser.set('usersettings', 'maj', "1")
            parser.set('usersettings', 'majadd2', "1")
            parser.set('usersettings', 'majadd4', "1")
            parser.set('usersettings', 'majadd6', "1")
            parser.set('usersettings', 'maj7', "1")
            parser.set('usersettings', 'maj7b5', "1")
            parser.set('usersettings', 'maj7#5', "1")
            parser.set('usersettings', 'm', "1")
            parser.set('usersettings', 'madd2', "1")
            parser.set('usersettings', 'madd4', "1")
            parser.set('usersettings', 'madd6', "1")
            parser.set('usersettings', 'm7', "1")
            parser.set('usersettings', 'm7b5', "1")
            parser.set('usersettings', 'm7#5', "1")
            parser.set('usersettings', 'mM7', "1")
            parser.set('usersettings', '+', "1")
            parser.set('usersettings', 'dim', "1")
            parser.set('usersettings', 'dim7', "1")
            parser.set('usersettings', '7', "1")
            parser.set('usersettings', '7b5', "1")
            parser.set('usersettings', '7#5', "1")
            parser.set('usersettings', 'sus2', "1")
            parser.set('usersettings', 'sus4', "1")
            parser.set('usersettings', '7sus2', "1")
            parser.set('usersettings', '7sus4', "1")
            with open(usersettingspath, 'w') as configfile:
                parser.write(configfile)

            MAJ_SETTING = 1
            MAJADD2_SETTING = 1
            MAJADD4_SETTING = 1
            MAJADD6_SETTING = 1
            MAJ7_SETTING = 1
            MAJ7B5_SETTING = 1
            MAJ7SHARP5_SETTING = 1
            M_SETTING = 1
            MADD2_SETTING = 1
            MADD4_SETTING = 1
            MADD6_SETTING = 1
            M7_SETTING = 1
            M7B5_SETTING = 1
            M7SHARP5_SETTING = 1
            mM7_SETTING = 1
            AUG_SETTING = 1
            DIM_SETTING = 1
            DIM7_SETTING = 1
            DOM7_SETTING = 1
            DOM7B5_SETTING = 1
            DOM7SHARP5_SETTING = 1
            SUS2_SETTING = 1
            SUS4_SETTING = 1
            DOM7SUS2_SETTING = 1
            DOM7SUS4_SETTING = 1

            maj_chord.set(1)
            majadd2_chord.set(1)
            majadd4_chord.set(1)
            majadd6_chord.set(1)
            maj7_chord.set(1)
            maj7b5_chord.set(1)
            maj7sharp5_chord.set(1)
            m_chord.set(1)
            madd2_chord.set(1)
            madd4_chord.set(1)
            madd6_chord.set(1)
            m7_chord.set(1)
            m7b5_chord.set(1)
            m7sharp5_chord.set(1)
            mM7_chord.set(1)
            aug_chord.set(1)
            dim_chord.set(1)
            dim7_chord.set(1)
            dom7_chord.set(1)
            dom7b5_chord.set(1)
            dom7sharp5_chord.set(1)
            sus2_chord.set(1)
            sus4_chord.set(1)
            dom7sus2_chord.set(1)
            dom7sus4_chord.set(1)

    basic_chords_button= Button(top, text="-", width=7, highlightthickness=0, command=lambda: process_chords_button("-"))
    basic_chords_button.place(x=487, y=553+button_offset)

    more_chords_button= Button(top, text="+", width=7, highlightthickness=0, command=lambda: process_chords_button("+"))
    more_chords_button.place(x=560, y=553+button_offset)

    all_chords_button= Button(top, text="++", width=7, highlightthickness=0, command=lambda: process_chords_button("++"))
    all_chords_button.place(x=633, y=553+button_offset)
def Share_Your_Music():
    share_window = Toplevel()
    share_window.geometry("420x190+150+150")
    share_window.resizable(False, False)
    share_window.title("Share Your Music")
    share_window.config(bg=listbox_color)
    Text = "\n\nHave you published music online that's inspired by SLModes?\n" \
           "Then use the term #SLModes in the title or description.\n" \
           "This helps promote your music to our other users.\n"
    t = Label(share_window, text=Text, bg=listbox_color, font=(font_01, 13))
    t.place(x=15, y=5)

    def open_YouTube():
        webbrowser.open("https://sinewavelab.com/SLModesHashtag", new=1)

    youtube = Button(share_window, text="SLModes on YouTube", width=19, highlightthickness=0, command=lambda: open_YouTube())
    youtube.place(x = 140, y = 130)

menu = Menu(window)
window.config(menu=menu)
fileMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Settings", command=Open_Settings)
fileMenu.add_command(label="Exit", command=Exit)

moreMenu = Menu(menu, tearoff=0)
menu.add_cascade(label="More", menu=moreMenu)
moreMenu.add_command(label="Share Your Music", command=Share_Your_Music)

def read_root(event):

    global Root_in, Scale_in, UserScale, scale01_notes_label, current_selected_chord_left, enable_second_fretboard_drawing

    current_selected_chord_left = "Nothing Here"

    enable_second_fretboard_drawing = False
    Negative_Harmony_utils.current_selected_negative_chord_1 = None
    Negative_Harmony_utils.current_selected_negative_chord_2 = None

    Root_in = Root_in_box.get(ANCHOR)
    Negative_Harmony_utils.Root_1_temp = Root_in

    if Scale_in_box.get(ANCHOR) != "":
        Scale_in = Scale_in_box.get(ANCHOR)
    else:
        Scale_in = Scale_in_box.get(0)

    try:
        UserScale = Scale(Note(Root_in), Scale_in)
        MN_Draw.drawPianoMode(UserScale, piano01_canvas, notefile, pianofile)
        show_scale_notes(True, scale01_notes_label)
        create_mode_chords_left_up()
        determine_seven_notes()
        threading.Thread(target=process_matched_scales_right_side).start()
        Chords_03_Listbox.delete(0, END)

        if Negative_Harmony_utils.is_negative_harmony_open == True:

            global negativeharmonybackgroundfile_pos_1, negativeharmonybackgroundfile_pos_2, negativeharmonybackgroundfile_pos_3, negativeharmonybackgroundfile_pos_4, negativeharmonybackgroundfile_pos_5, negativeharmonybackgroundfile_pos_6
            global Chords_02_Listbox
            global Root_in_2, Scale_in_2


            Negative_Harmony_utils.clearcolors(1)

            Root_in_2 = None
            Scale_in_2 = None

            Negative_Harmony_utils.cleareverything(2, negativeharmonybackgroundfile_pos_1, negativeharmonybackgroundfile_pos_2, negativeharmonybackgroundfile_pos_3, negativeharmonybackgroundfile_pos_4, negativeharmonybackgroundfile_pos_5, negativeharmonybackgroundfile_pos_6)

            Negative_Harmony_utils.compare_notes_to_circle(1, True, Root_in, Scale_in, settings.greencolor, settings.redcolor, UserScale, negativeharmonybackgroundfile_pos_1, negativeharmonybackgroundfile_pos_2, negativeharmonybackgroundfile_pos_3, negativeharmonybackgroundfile_pos_4, negativeharmonybackgroundfile_pos_5, negativeharmonybackgroundfile_pos_6, negativeharmonybackgroundfile_pos_1_pos_1, negativeharmonybackgroundfile_pos_1_pos_2, negativeharmonybackgroundfile_pos_1_pos_3, negativeharmonybackgroundfile_pos_1_pos_4, negativeharmonybackgroundfile_pos_1_pos_5, negativeharmonybackgroundfile_pos_1_pos_6, negativeharmonybackgroundfile_pos_2_pos_1, negativeharmonybackgroundfile_pos_2_pos_2, negativeharmonybackgroundfile_pos_2_pos_3, negativeharmonybackgroundfile_pos_2_pos_4, negativeharmonybackgroundfile_pos_2_pos_5, negativeharmonybackgroundfile_pos_2_pos_6, negativeharmonybackgroundfile_pos_3_pos_1, negativeharmonybackgroundfile_pos_3_pos_2, negativeharmonybackgroundfile_pos_3_pos_3, negativeharmonybackgroundfile_pos_3_pos_4, negativeharmonybackgroundfile_pos_3_pos_5, negativeharmonybackgroundfile_pos_3_pos_6, negativeharmonybackgroundfile_pos_4_pos_1, negativeharmonybackgroundfile_pos_4_pos_2, negativeharmonybackgroundfile_pos_4_pos_3, negativeharmonybackgroundfile_pos_4_pos_4, negativeharmonybackgroundfile_pos_4_pos_5, negativeharmonybackgroundfile_pos_4_pos_6, negativeharmonybackgroundfile_pos_5_pos_1, negativeharmonybackgroundfile_pos_5_pos_2, negativeharmonybackgroundfile_pos_5_pos_3, negativeharmonybackgroundfile_pos_5_pos_4, negativeharmonybackgroundfile_pos_5_pos_5, negativeharmonybackgroundfile_pos_5_pos_6, negativeharmonybackgroundfile_pos_6_pos_1, negativeharmonybackgroundfile_pos_6_pos_2, negativeharmonybackgroundfile_pos_6_pos_3, negativeharmonybackgroundfile_pos_6_pos_4, negativeharmonybackgroundfile_pos_6_pos_5, negativeharmonybackgroundfile_pos_6_pos_6)

            list_of_inverted_scale_notes = Negative_Harmony_utils.calculate_inverted_scale_notes(1, Root_in, Scale_in)

            if (Root_in != None and Scale_in != None):

                Negative_Harmony_utils.Mode_1_label_left.config(text=((Root_in + " " + Scale_in)), font=font_01, bg=listbox_color)
                Negative_Harmony_utils.update_scale_labels(Scale(Note(Root_in), Scale_in), Negative_Harmony_utils.Mode1_notes_label_left, 1,  listbox_color, font_01)

                Negative_Harmony_utils.Mode_1_Chords_Listbox_left.delete(0, END)

                for c in range(0, Chords_02_Listbox.size()):
                    Negative_Harmony_utils.Mode_1_Chords_Listbox_left.insert(c, Chords_02_Listbox.get(c))

                Negative_Harmony_utils.Mode_1_Negative_Chords_Listbox_left.delete(0, END)

                Negative_Harmony_utils.calculate_inverted_chord_notes(1, Chords_02_Listbox, Negative_Harmony_utils.Mode_1_Negative_Chords_Listbox_left)
                Negative_Harmony_utils.update_scale_labels(Negative_Harmony_utils.InvertedScale(list_of_inverted_scale_notes, Negative_Harmony_utils.Mode_1_Negative_Chords_Listbox_left), Negative_Harmony_utils.Mode2_notes_label_left, 1, settings.darkgrey, font_01)
                Negative_Harmony_utils.Mode_1_Negative_label_left.config(text=(Negative_Harmony_utils.InvertedScale(list_of_inverted_scale_notes, Negative_Harmony_utils.Mode_1_Negative_Chords_Listbox_left)), foreground="white", bg=settings.darkgrey, font=font_01)

                Negative_Harmony_utils.current_selected_negative_mode_1 = Negative_Harmony_utils.Mode_1_Negative_label_left.cget('text')

            Negative_Harmony_utils.negative_harmony_window.lift()

    except:
        pass


    if is_extended_fretboard_open == True:
        global extended_fretboard_canvas
        extended_fretboard_canvas.delete("all")
        extended_fretboard_canvas.create_image(490,215,image=extendedfretboardfile)
        MN_Draw.drawExtendedFretboard(UserScale, UserScaleBox02, Root_in, Root_in_2,  extended_fretboard_canvas, show_chords, current_selected_chord_right, current_selected_chord_left, enable_second_fretboard_drawing, largenotefile, largerootnotefile, largechordnotefile)

def read_scale(event):

    global Scale_in, UserScale, Root_in, scale01_notes_label, current_selected_chord_left, enable_second_fretboard_drawing

    enable_second_fretboard_drawing = False

    Negative_Harmony_utils.current_selected_negative_chord_1 = None
    Negative_Harmony_utils.current_selected_negative_chord_2 = None

    if Root_in == None:
        Root_in = 'C'
        Negative_Harmony_utils.Root_1_temp = Root_in
    current_selected_chord_left = "Nothing Here"
    Scale_in = Scale_in_box.get(ANCHOR)  # access to combobox selected item
    Negative_Harmony_utils.Scale_1_temp = Scale_in
    UserScale = Scale(Note(Root_in), Scale_in)
    MN_Draw.drawModeShape(Scale_in, fretboard01_canvas, notefile, fretboardfile)
    MN_Draw.drawPianoMode(UserScale, piano01_canvas, notefile, pianofile)
    show_scale_notes(True, scale01_notes_label)
    create_mode_chords_left_up() # This wil also create chords left down
    determine_seven_notes()
    threading.Thread(target=process_matched_scales_right_side).start()
    Chords_03_Listbox.delete(0, END)

    if Negative_Harmony_utils.is_negative_harmony_open == True:

        global negativeharmonybackgroundfile_pos_1, negativeharmonybackgroundfile_pos_2, negativeharmonybackgroundfile_pos_3, negativeharmonybackgroundfile_pos_4, negativeharmonybackgroundfile_pos_5, negativeharmonybackgroundfile_pos_6
        global Chords_02_Listbox, Scale_in_2, Root_in_2

        Negative_Harmony_utils.clearcolors(1)

        Scale_in_2 = None
        Root_in_2 = None

        Negative_Harmony_utils.cleareverything(2, negativeharmonybackgroundfile_pos_1, negativeharmonybackgroundfile_pos_2, negativeharmonybackgroundfile_pos_3, negativeharmonybackgroundfile_pos_4, negativeharmonybackgroundfile_pos_5, negativeharmonybackgroundfile_pos_6)

        Negative_Harmony_utils.compare_notes_to_circle(1, True, Root_in, Scale_in, greencolor, redcolor, UserScale, negativeharmonybackgroundfile_pos_1, negativeharmonybackgroundfile_pos_2, negativeharmonybackgroundfile_pos_3, negativeharmonybackgroundfile_pos_4, negativeharmonybackgroundfile_pos_5, negativeharmonybackgroundfile_pos_6, negativeharmonybackgroundfile_pos_1_pos_1, negativeharmonybackgroundfile_pos_1_pos_2, negativeharmonybackgroundfile_pos_1_pos_3, negativeharmonybackgroundfile_pos_1_pos_4, negativeharmonybackgroundfile_pos_1_pos_5, negativeharmonybackgroundfile_pos_1_pos_6, negativeharmonybackgroundfile_pos_2_pos_1, negativeharmonybackgroundfile_pos_2_pos_2, negativeharmonybackgroundfile_pos_2_pos_3, negativeharmonybackgroundfile_pos_2_pos_4, negativeharmonybackgroundfile_pos_2_pos_5, negativeharmonybackgroundfile_pos_2_pos_6, negativeharmonybackgroundfile_pos_3_pos_1, negativeharmonybackgroundfile_pos_3_pos_2, negativeharmonybackgroundfile_pos_3_pos_3, negativeharmonybackgroundfile_pos_3_pos_4, negativeharmonybackgroundfile_pos_3_pos_5, negativeharmonybackgroundfile_pos_3_pos_6, negativeharmonybackgroundfile_pos_4_pos_1, negativeharmonybackgroundfile_pos_4_pos_2, negativeharmonybackgroundfile_pos_4_pos_3, negativeharmonybackgroundfile_pos_4_pos_4, negativeharmonybackgroundfile_pos_4_pos_5, negativeharmonybackgroundfile_pos_4_pos_6, negativeharmonybackgroundfile_pos_5_pos_1, negativeharmonybackgroundfile_pos_5_pos_2, negativeharmonybackgroundfile_pos_5_pos_3, negativeharmonybackgroundfile_pos_5_pos_4, negativeharmonybackgroundfile_pos_5_pos_5, negativeharmonybackgroundfile_pos_5_pos_6, negativeharmonybackgroundfile_pos_6_pos_1, negativeharmonybackgroundfile_pos_6_pos_2, negativeharmonybackgroundfile_pos_6_pos_3, negativeharmonybackgroundfile_pos_6_pos_4, negativeharmonybackgroundfile_pos_6_pos_5, negativeharmonybackgroundfile_pos_6_pos_6)

        list_of_inverted_scale_notes = Negative_Harmony_utils.calculate_inverted_scale_notes(1, Root_in, Scale_in)

        if (Root_in != None and Scale_in != None):

            Negative_Harmony_utils.Mode_1_label_left.config(text=((Root_in + " " + Scale_in)), font=font_01, bg=listbox_color)
            Negative_Harmony_utils.update_scale_labels(Scale(Note(Root_in), Scale_in), Negative_Harmony_utils.Mode1_notes_label_left, 1, listbox_color, font_01)

            Negative_Harmony_utils.Mode_1_Chords_Listbox_left.delete(0, END)

            for c in range(0, Chords_02_Listbox.size()):
                Negative_Harmony_utils.Mode_1_Chords_Listbox_left.insert(c, Chords_02_Listbox.get(c))

            Negative_Harmony_utils.Mode_1_Negative_Chords_Listbox_left.delete(0, END)

            Negative_Harmony_utils.calculate_inverted_chord_notes(1, Chords_02_Listbox, Negative_Harmony_utils.Mode_1_Negative_Chords_Listbox_left)
            Negative_Harmony_utils.update_scale_labels(Negative_Harmony_utils.InvertedScale(list_of_inverted_scale_notes, Negative_Harmony_utils.Mode_1_Negative_Chords_Listbox_left), Negative_Harmony_utils.Mode2_notes_label_left, 1, settings.darkgrey, font_01)
            Negative_Harmony_utils.Mode_1_Negative_label_left.config(text=(Negative_Harmony_utils.InvertedScale(list_of_inverted_scale_notes, Negative_Harmony_utils.Mode_1_Negative_Chords_Listbox_left)), foreground="white", bg=settings.darkgrey, font=font_01)

            Negative_Harmony_utils.current_selected_negative_mode_1 = Negative_Harmony_utils.Mode_1_Negative_label_left.cget('text')

        Negative_Harmony_utils.negative_harmony_window.lift()

    if is_extended_fretboard_open == True:
        global extended_fretboard_canvas
        extended_fretboard_canvas.delete("all")
        extended_fretboard_canvas.create_image(490,215,image=extendedfretboardfile)
        MN_Draw.drawExtendedFretboard(UserScale, UserScaleBox02, Root_in, Root_in_2,  extended_fretboard_canvas, show_chords, current_selected_chord_right, current_selected_chord_left, enable_second_fretboard_drawing, largenotefile, largerootnotefile, largechordnotefile)


def read_number(event):  # function called when '<<ComboboxSelected>>' event is triggered

    Negative_Harmony_utils.current_selected_negative_chord_2 = None
    Negative_Harmony_utils.current_selected_negative_mode_2 = None

    global N_Notes_in, UserScale
    N_Notes_in = int(y.get())  # access to combobox selected item
    process_matched_scales_right_side()

def update_notes_in_common():
    global user_common_notes
    user_common_notes = []

    Common_N = z.get().split()

    for i in Common_N:
        if i.lower() == ("c#"):
            user_common_notes.append("Db")
            user_common_notes.append("C#")
        if i.lower() == ("db"):
            user_common_notes.append("C#")
            user_common_notes.append("Db")
        if i.lower() == ("d#"):
            user_common_notes.append("Eb")
            user_common_notes.append("D#")
        if i.lower() == ("eb"):
            user_common_notes.append("D#")
            user_common_notes.append("Eb")
        if i.lower() == ("f#"):
            user_common_notes.append("Gb")
            user_common_notes.append("F#")
        if i.lower() == ("gb"):
            user_common_notes.append("F#")
            user_common_notes.append("Gb")
        if i.lower() == ("ab"):
            user_common_notes.append("Ab")
            user_common_notes.append("G#")
        if i.lower() == ("g#"):
            user_common_notes.append("Ab")
            user_common_notes.append("G#")
        if i.lower() == ("a#"):
            user_common_notes.append("Bb")
            user_common_notes.append("A#")
        if i.lower() == ("bb"):
            user_common_notes.append("A#")
            user_common_notes.append("Bb")

        if i.lower() == ("c"):
            user_common_notes.append("C")
        if i.lower() == ("d"):
            user_common_notes.append("D")
        if i.lower() == ("e"):
            user_common_notes.append("E")
        if i.lower() == ("f"):
            user_common_notes.append("F")
        if i.lower() == ("g"):
            user_common_notes.append("G")
        if i.lower() == ("a"):
            user_common_notes.append("A")
        if i.lower() == ("b"):
            user_common_notes.append("B")

    process_matched_scales_right_side()

def determine_seven_notes():
    global Root_in, Scale_in, seven_notes, FLAT_SETTING, modes_7, modes_6, modes_5, modes_4, modes_3, modes_2

    seven_notes = []

    scale_string_entry_in_dic = Root_in + " " + Scale_in

    if FLAT_SETTING == 1:
        for a in modes_7.modes_7_flat.get(scale_string_entry_in_dic):
            mode_string = a.split()
            mode_root = mode_string[0]
            mode_name = mode_string[1]
            if mode_string.__len__() > 2:
                for m_n in range(2, mode_string.__len__()):
                    mode_name = mode_name + " " + mode_string[m_n]
            created_mode = Scale(Note(mode_root), mode_name)
            seven_notes.append(created_mode)
    else:
        for a in modes_7.modes_7_sharp[scale_string_entry_in_dic]:
            mode_string = a.split()
            mode_root = mode_string[0]
            mode_name = mode_string[1]
            if mode_string.__len__() > 2:
                for m_n in range(2, mode_string.__len__()):
                    mode_name = mode_name + " " + mode_string[m_n]
            created_mode = Scale(Note(mode_root), mode_name)
            seven_notes.append(created_mode)

def determine_seven_more_notes(scale):
    global Output_Scales, scales_list, other_seven_notes, FLAT_SETTING, modes_7, modes_6, modes_5, modes_4, modes_3, modes_2

    other_seven_notes = []
    Output_Scales = []

    scale_string_entry_in_dic = str(scale.root) + " " + str(scale.name)

    if FLAT_SETTING == 1:
        for a in modes_7.modes_7_flat.get(scale_string_entry_in_dic):
            mode_string = a.split()
            mode_root = mode_string[0]
            mode_name = mode_string[1]
            if mode_string.__len__() > 2:
                for m_n in range(2, mode_string.__len__()):
                    mode_name = mode_name + " " + mode_string[m_n]
            created_mode = Scale(Note(mode_root), mode_name)
            other_seven_notes.append(created_mode)
    else:
        for a in modes_7.modes_7_sharp[scale_string_entry_in_dic]:
            mode_string = a.split()
            mode_root = mode_string[0]
            mode_name = mode_string[1]
            if mode_string.__len__() > 2:
                for m_n in range(2, mode_string.__len__()):
                    mode_name = mode_name + " " + mode_string[m_n]
            created_mode = Scale(Note(mode_root), mode_name)
            other_seven_notes.append(created_mode)

def process_matched_scales_right_side():  # this fucntion will display scales that match to the 3 parameters
    global Root_in, Scale_in, Matched_Scales, user_common_notes, Chords_02_Listbox, N_Notes_in

    Output_Scales = []

    scale_string_entry_in_dic = Root_in + " " + Scale_in

    if N_Notes_in == 7:
        if FLAT_SETTING == 1:
            for a in modes_7.modes_7_flat.get(scale_string_entry_in_dic):
                mode_string = a.split()
                mode_root = mode_string[0]
                mode_name = mode_string[1]
                if mode_string.__len__() > 2:
                    for m_n in range(2, mode_string.__len__()):
                        mode_name = mode_name + " " + mode_string[m_n]
                created_mode = Scale(Note(mode_root), mode_name)
                Output_Scales.append(created_mode)
        else:
            for a in modes_7.modes_7_sharp[scale_string_entry_in_dic]:
                mode_string = a.split()
                mode_root = mode_string[0]
                mode_name = mode_string[1]
                if mode_string.__len__() > 2:
                    for m_n in range(2, mode_string.__len__()):
                        mode_name = mode_name + " " + mode_string[m_n]
                created_mode = Scale(Note(mode_root), mode_name)
                Output_Scales.append(created_mode)
    elif N_Notes_in == 6:
        if FLAT_SETTING == 1:
            for a in modes_6.modes_6_flat.get(scale_string_entry_in_dic):
                mode_string = a.split()
                mode_root = mode_string[0]
                mode_name = mode_string[1]
                if mode_string.__len__() > 2:
                    for m_n in range(2, mode_string.__len__()):
                        mode_name = mode_name + " " + mode_string[m_n]
                if ((MAJOR_SETTING == 1) and (mode_name in settings.major_names)) or ((MELODIC_MINOR_SETTING == 1) and (mode_name in settings.melodic_minor_names)) or ((HARMONIC_MINOR_SETTING == 1) and (mode_name in settings.harmonic_minor_names)) or ((HARMONIC_MAJOR_SETTING == 1) and (mode_name in settings.harmonic_major_names)) or ((DOUBLE_HARMONIC_MAJOR_SETTING == 1) and (mode_name in settings.double_harmonic_major_names)) or ((NEAPOLITAN_MAJOR_SETTING == 1) and (mode_name in settings.neapolitan_major_names)) or ((NEAPOLITAN_MINOR_SETTING == 1) and (mode_name in settings.neapolitan_minor_names)) or ((HUNGARIAN_MAJOR_SETTING == 1) and (mode_name in settings.hungarian_major_names)) or ((ROMANIAN_MAJOR_SETTING == 1) and (mode_name in settings.romanian_major_names)):
                    created_mode = Scale(Note(mode_root), mode_name)
                    Output_Scales.append(created_mode)
        else:
            for a in modes_6.modes_6_sharp[scale_string_entry_in_dic]:
                mode_string = a.split()
                mode_root = mode_string[0]
                mode_name = mode_string[1]
                if mode_string.__len__() > 2:
                    for m_n in range(2, mode_string.__len__()):
                        mode_name = mode_name + " " + mode_string[m_n]
                if ((MAJOR_SETTING == 1) and (mode_name in settings.major_names)) or ((MELODIC_MINOR_SETTING == 1) and (mode_name in settings.melodic_minor_names)) or ((HARMONIC_MINOR_SETTING == 1) and (mode_name in settings.harmonic_minor_names)) or ((HARMONIC_MAJOR_SETTING == 1) and (mode_name in settings.harmonic_major_names)) or ((DOUBLE_HARMONIC_MAJOR_SETTING == 1) and (mode_name in settings.double_harmonic_major_names)) or ((NEAPOLITAN_MAJOR_SETTING == 1) and (mode_name in settings.neapolitan_major_names)) or ((NEAPOLITAN_MINOR_SETTING == 1) and (mode_name in settings.neapolitan_minor_names)) or ((HUNGARIAN_MAJOR_SETTING == 1) and (mode_name in settings.hungarian_major_names)) or ((ROMANIAN_MAJOR_SETTING == 1) and (mode_name in settings.romanian_major_names)):
                    created_mode = Scale(Note(mode_root), mode_name)
                    Output_Scales.append(created_mode)
    elif N_Notes_in == 5:
        if FLAT_SETTING == 1:
            for a in modes_5.modes_5_flat.get(scale_string_entry_in_dic):
                mode_string = a.split()
                mode_root = mode_string[0]
                mode_name = mode_string[1]
                if mode_string.__len__() > 2:
                    for m_n in range(2, mode_string.__len__()):
                        mode_name = mode_name + " " + mode_string[m_n]
                if ((MAJOR_SETTING == 1) and (mode_name in settings.major_names)) or ((MELODIC_MINOR_SETTING == 1) and (mode_name in settings.melodic_minor_names)) or ((HARMONIC_MINOR_SETTING == 1) and (mode_name in settings.harmonic_minor_names)) or ((HARMONIC_MAJOR_SETTING == 1) and (mode_name in settings.harmonic_major_names)) or ((DOUBLE_HARMONIC_MAJOR_SETTING == 1) and (mode_name in settings.double_harmonic_major_names)) or ((NEAPOLITAN_MAJOR_SETTING == 1) and (mode_name in settings.neapolitan_major_names)) or ((NEAPOLITAN_MINOR_SETTING == 1) and (mode_name in settings.neapolitan_minor_names)) or ((HUNGARIAN_MAJOR_SETTING == 1) and (mode_name in settings.hungarian_major_names)) or ((ROMANIAN_MAJOR_SETTING == 1) and (mode_name in settings.romanian_major_names)):
                    created_mode = Scale(Note(mode_root), mode_name)
                    Output_Scales.append(created_mode)
        else:
            for a in modes_5.modes_5_sharp[scale_string_entry_in_dic]:
                mode_string = a.split()
                mode_root = mode_string[0]
                mode_name = mode_string[1]
                if mode_string.__len__() > 2:
                    for m_n in range(2, mode_string.__len__()):
                        mode_name = mode_name + " " + mode_string[m_n]
                if ((MAJOR_SETTING == 1) and (mode_name in settings.major_names)) or ((MELODIC_MINOR_SETTING == 1) and (mode_name in settings.melodic_minor_names)) or ((HARMONIC_MINOR_SETTING == 1) and (mode_name in settings.harmonic_minor_names)) or ((HARMONIC_MAJOR_SETTING == 1) and (mode_name in settings.harmonic_major_names)) or ((DOUBLE_HARMONIC_MAJOR_SETTING == 1) and (mode_name in settings.double_harmonic_major_names)) or ((NEAPOLITAN_MAJOR_SETTING == 1) and (mode_name in settings.neapolitan_major_names)) or ((NEAPOLITAN_MINOR_SETTING == 1) and (mode_name in settings.neapolitan_minor_names)) or ((HUNGARIAN_MAJOR_SETTING == 1) and (mode_name in settings.hungarian_major_names)) or ((ROMANIAN_MAJOR_SETTING == 1) and (mode_name in settings.romanian_major_names)):
                    created_mode = Scale(Note(mode_root), mode_name)
                    Output_Scales.append(created_mode)
    elif N_Notes_in == 4:
        if FLAT_SETTING == 1:
            for a in modes_4.modes_4_flat.get(scale_string_entry_in_dic):
                mode_string = a.split()
                mode_root = mode_string[0]
                mode_name = mode_string[1]
                if mode_string.__len__() > 2:
                    for m_n in range(2, mode_string.__len__()):
                        mode_name = mode_name + " " + mode_string[m_n]
                if ((MAJOR_SETTING == 1) and (mode_name in settings.major_names)) or ((MELODIC_MINOR_SETTING == 1) and (mode_name in settings.melodic_minor_names)) or ((HARMONIC_MINOR_SETTING == 1) and (mode_name in settings.harmonic_minor_names)) or ((HARMONIC_MAJOR_SETTING == 1) and (mode_name in settings.harmonic_major_names)) or ((DOUBLE_HARMONIC_MAJOR_SETTING == 1) and (mode_name in settings.double_harmonic_major_names)) or ((NEAPOLITAN_MAJOR_SETTING == 1) and (mode_name in settings.neapolitan_major_names)) or ((NEAPOLITAN_MINOR_SETTING == 1) and (mode_name in settings.neapolitan_minor_names)) or ((HUNGARIAN_MAJOR_SETTING == 1) and (mode_name in settings.hungarian_major_names)) or ((ROMANIAN_MAJOR_SETTING == 1) and (mode_name in settings.romanian_major_names)):
                    created_mode = Scale(Note(mode_root), mode_name)
                    Output_Scales.append(created_mode)
        else:
            for a in modes_4.modes_4_sharp[scale_string_entry_in_dic]:
                mode_string = a.split()
                mode_root = mode_string[0]
                mode_name = mode_string[1]
                if mode_string.__len__() > 2:
                    for m_n in range(2, mode_string.__len__()):
                        mode_name = mode_name + " " + mode_string[m_n]
                if ((MAJOR_SETTING == 1) and (mode_name in settings.major_names)) or ((MELODIC_MINOR_SETTING == 1) and (mode_name in settings.melodic_minor_names)) or ((HARMONIC_MINOR_SETTING == 1) and (mode_name in settings.harmonic_minor_names)) or ((HARMONIC_MAJOR_SETTING == 1) and (mode_name in settings.harmonic_major_names)) or ((DOUBLE_HARMONIC_MAJOR_SETTING == 1) and (mode_name in settings.double_harmonic_major_names)) or ((NEAPOLITAN_MAJOR_SETTING == 1) and (mode_name in settings.neapolitan_major_names)) or ((NEAPOLITAN_MINOR_SETTING == 1) and (mode_name in settings.neapolitan_minor_names)) or ((HUNGARIAN_MAJOR_SETTING == 1) and (mode_name in settings.hungarian_major_names)) or ((ROMANIAN_MAJOR_SETTING == 1) and (mode_name in settings.romanian_major_names)):
                    created_mode = Scale(Note(mode_root), mode_name)
                    Output_Scales.append(created_mode)
    elif N_Notes_in == 3:
        if FLAT_SETTING == 1:
            for a in modes_3.modes_3_flat.get(scale_string_entry_in_dic):
                mode_string = a.split()
                mode_root = mode_string[0]
                mode_name = mode_string[1]
                if mode_string.__len__() > 2:
                    for m_n in range(2, mode_string.__len__()):
                        mode_name = mode_name + " " + mode_string[m_n]
                if ((MAJOR_SETTING == 1) and (mode_name in settings.major_names)) or ((MELODIC_MINOR_SETTING == 1) and (mode_name in settings.melodic_minor_names)) or ((HARMONIC_MINOR_SETTING == 1) and (mode_name in settings.harmonic_minor_names)) or ((HARMONIC_MAJOR_SETTING == 1) and (mode_name in settings.harmonic_major_names)) or ((DOUBLE_HARMONIC_MAJOR_SETTING == 1) and (mode_name in settings.double_harmonic_major_names)) or ((NEAPOLITAN_MAJOR_SETTING == 1) and (mode_name in settings.neapolitan_major_names)) or ((NEAPOLITAN_MINOR_SETTING == 1) and (mode_name in settings.neapolitan_minor_names)) or ((HUNGARIAN_MAJOR_SETTING == 1) and (mode_name in settings.hungarian_major_names)) or ((ROMANIAN_MAJOR_SETTING == 1) and (mode_name in settings.romanian_major_names)):
                    created_mode = Scale(Note(mode_root), mode_name)
                    Output_Scales.append(created_mode)
        else:
            for a in modes_3.modes_3_sharp[scale_string_entry_in_dic]:
                mode_string = a.split()
                mode_root = mode_string[0]
                mode_name = mode_string[1]
                if mode_string.__len__() > 2:
                    for m_n in range(2, mode_string.__len__()):
                        mode_name = mode_name + " " + mode_string[m_n]
                if ((MAJOR_SETTING == 1) and (mode_name in settings.major_names)) or ((MELODIC_MINOR_SETTING == 1) and (mode_name in settings.melodic_minor_names)) or ((HARMONIC_MINOR_SETTING == 1) and (mode_name in settings.harmonic_minor_names)) or ((HARMONIC_MAJOR_SETTING == 1) and (mode_name in settings.harmonic_major_names)) or ((DOUBLE_HARMONIC_MAJOR_SETTING == 1) and (mode_name in settings.double_harmonic_major_names)) or ((NEAPOLITAN_MAJOR_SETTING == 1) and (mode_name in settings.neapolitan_major_names)) or ((NEAPOLITAN_MINOR_SETTING == 1) and (mode_name in settings.neapolitan_minor_names)) or ((HUNGARIAN_MAJOR_SETTING == 1) and (mode_name in settings.hungarian_major_names)) or ((ROMANIAN_MAJOR_SETTING == 1) and (mode_name in settings.romanian_major_names)):
                    created_mode = Scale(Note(mode_root), mode_name)
                    Output_Scales.append(created_mode)
    elif N_Notes_in == 2:
        if FLAT_SETTING == 1:
            for a in modes_2.modes_2_flat.get(scale_string_entry_in_dic):
                mode_string = a.split()
                mode_root = mode_string[0]
                mode_name = mode_string[1]
                if mode_string.__len__() > 2:
                    for m_n in range(2, mode_string.__len__()):
                        mode_name = mode_name + " " + mode_string[m_n]
                if ((MAJOR_SETTING == 1) and (mode_name in settings.major_names)) or ((MELODIC_MINOR_SETTING == 1) and (mode_name in settings.melodic_minor_names)) or ((HARMONIC_MINOR_SETTING == 1) and (mode_name in settings.harmonic_minor_names)) or ((HARMONIC_MAJOR_SETTING == 1) and (mode_name in settings.harmonic_major_names)) or ((DOUBLE_HARMONIC_MAJOR_SETTING == 1) and (mode_name in settings.double_harmonic_major_names)) or ((NEAPOLITAN_MAJOR_SETTING == 1) and (mode_name in settings.neapolitan_major_names)) or ((NEAPOLITAN_MINOR_SETTING == 1) and (mode_name in settings.neapolitan_minor_names)) or ((HUNGARIAN_MAJOR_SETTING == 1) and (mode_name in settings.hungarian_major_names)) or ((ROMANIAN_MAJOR_SETTING == 1) and (mode_name in settings.romanian_major_names)):
                    created_mode = Scale(Note(mode_root), mode_name)
                    Output_Scales.append(created_mode)
        else:
            for a in modes_2.modes_2_sharp[scale_string_entry_in_dic]:
                mode_string = a.split()
                mode_root = mode_string[0]
                mode_name = mode_string[1]
                if mode_string.__len__() > 2:
                    for m_n in range(2, mode_string.__len__()):
                        mode_name = mode_name + " " + mode_string[m_n]
                if ((MAJOR_SETTING == 1) and (mode_name in settings.major_names)) or ((MELODIC_MINOR_SETTING == 1) and (mode_name in settings.melodic_minor_names)) or ((HARMONIC_MINOR_SETTING == 1) and (mode_name in settings.harmonic_minor_names)) or ((HARMONIC_MAJOR_SETTING == 1) and (mode_name in settings.harmonic_major_names)) or ((DOUBLE_HARMONIC_MAJOR_SETTING == 1) and (mode_name in settings.double_harmonic_major_names)) or ((NEAPOLITAN_MAJOR_SETTING == 1) and (mode_name in settings.neapolitan_major_names)) or ((NEAPOLITAN_MINOR_SETTING == 1) and (mode_name in settings.neapolitan_minor_names)) or ((HUNGARIAN_MAJOR_SETTING == 1) and (mode_name in settings.hungarian_major_names)) or ((ROMANIAN_MAJOR_SETTING == 1) and (mode_name in settings.romanian_major_names)):
                    created_mode = Scale(Note(mode_root), mode_name)
                    Output_Scales.append(created_mode)

    Matched_Scales.delete(0, END)  # delete previous list so that we can add new ones

    counter = 0
    for i in Output_Scales:  # for every scale with the same number of notes in common
        if len(user_common_notes) == 0:  # User has input no common notes...
            s = str("" + str(i.root) + " " + str(i.name))  # Create the name of the scale to the list box, to be displayed.
            Matched_Scales.insert(counter, s)  # insert the string to the listbox
            counter = counter + 1
        else:  ## If user has input common notes.....
            counter02 = 0
            for w in range(0, len(user_common_notes)):
                for p in range(0, 7):  # for every note of matched scale
                    if Note(user_common_notes[w]).midi_note() == i.notes[p].midi_note():
                        counter02 = counter02 + 1
                        break
                if counter02 == len(user_common_notes):
                    s = str(str(i.root) + " " + str(i.name))
                    Matched_Scales.insert(counter, s)
                    counter = counter + 1
                    break

def create_scale_chords_left_down_right_down(scale, listbox):
    # global chord_label2, chord_label4
    counter = 0 # don't delete
    listbox.delete(0,END) # delete content of chords listbox

    search_for_this_mode = str(scale.root) + " " + str(scale.name)

    for a in chords.chords_dict.get(search_for_this_mode):
        chord_text = a.split()
        chord_root = chord_text[0]
        chord_name = chord_text[1]

        if (chord_name == 'maj' and MAJ_SETTING == 1) or (chord_name == 'majadd2' and MAJADD2_SETTING == 1) or (chord_name == 'majadd4' and MAJADD4_SETTING == 1) or (chord_name == 'majadd6' and MAJADD6_SETTING == 1) or (chord_name == 'maj7' and MAJ7_SETTING == 1) or (chord_name == 'm' and M_SETTING == 1) or (chord_name == 'madd2' and MADD2_SETTING == 1) or (chord_name == 'madd4' and MADD4_SETTING == 1) or (chord_name == 'madd6' and MADD6_SETTING == 1) or (chord_name == 'm7' and M7_SETTING == 1) or (chord_name == '7' and DOM7_SETTING == 1) or (chord_name == '7sus2' and DOM7SUS2_SETTING == 1) or (chord_name == '7sus4' and DOM7SUS4_SETTING == 1) or (chord_name == '+' and AUG_SETTING == 1) or (chord_name == 'dim' and DIM_SETTING == 1) or (chord_name == 'dim7' and DIM7_SETTING == 1) or (chord_name == 'maj7b5' and MAJ7B5_SETTING == 1) or (chord_name == 'maj7#5' and MAJ7SHARP5_SETTING == 1) or (chord_name == 'm7b5' and M7B5_SETTING == 1) or (chord_name == 'm7#5' and M7SHARP5_SETTING == 1) or (chord_name == '7b5' and DOM7B5_SETTING == 1) or (chord_name == '7#5' and DOM7SHARP5_SETTING == 1) or (chord_name == 'mM7' and mM7_SETTING == 1) or (chord_name == 'sus2' and SUS2_SETTING == 1) or (chord_name == 'sus4' and SUS4_SETTING == 1):
            listbox.insert(counter, Chord(Note(chord_root), chord_name))
            counter = counter + 1

    listbox.update_idletasks()

def create_mode_chords_left_up():
    global Root_in, Scale_in, UserScale, Chords_01_Listbox, Chords_02_Listbox

    UserScale = Scale(Note(Root_in), Scale_in)
    Chords_02_Listbox.delete(0, END)
    Chords_01_Listbox.delete(0, END)
    counter = 0

    # Let's check if any of the 25 chord formulas (Cmaj, Cmin, etc, belong to the UserScale. If so, add it to the chords lists)

    search_for_this_mode = Root_in + " " + Scale_in

    for a in chords.chords_dict.get(search_for_this_mode):
        chord_text = a.split()
        chord_root = chord_text[0]
        chord_name = chord_text[1]

        if (chord_name == 'maj' and MAJ_SETTING == 1 and chord_root == Root_in) or (chord_name == 'majadd2' and MAJADD2_SETTING == 1 and chord_root == Root_in) or (chord_name == 'majadd4' and MAJADD4_SETTING == 1 and chord_root == Root_in) or (chord_name == 'majadd6' and MAJADD6_SETTING == 1 and chord_root == Root_in) or (chord_name == 'maj7' and MAJ7_SETTING == 1 and chord_root == Root_in) or (chord_name == 'm' and M_SETTING == 1 and chord_root == Root_in) or (chord_name == 'madd2' and MADD2_SETTING == 1 and chord_root == Root_in) or (chord_name == 'madd4' and MADD4_SETTING == 1 and chord_root == Root_in) or (chord_name == 'madd6' and MADD6_SETTING == 1 and chord_root == Root_in) or (chord_name == 'm7' and M7_SETTING == 1 and chord_root == Root_in) or (chord_name == '7' and DOM7_SETTING == 1 and chord_root == Root_in) or (chord_name == '7sus2' and DOM7SUS2_SETTING == 1 and chord_root == Root_in) or (chord_name == '7sus4' and DOM7SUS4_SETTING == 1 and chord_root == Root_in) or (chord_name == '+' and AUG_SETTING == 1 and chord_root == Root_in) or (chord_name == 'dim' and DIM_SETTING == 1 and chord_root == Root_in) or (chord_name == 'dim7' and DIM7_SETTING == 1 and chord_root == Root_in) or (chord_name == 'maj7b5' and MAJ7B5_SETTING == 1 and chord_root == Root_in) or (chord_name == 'maj7#5' and MAJ7SHARP5_SETTING == 1 and chord_root == Root_in) or (chord_name == 'm7b5' and M7B5_SETTING == 1 and chord_root == Root_in) or (chord_name == 'm7#5' and M7SHARP5_SETTING == 1 and chord_root == Root_in) or (chord_name == '7b5' and DOM7B5_SETTING == 1 and chord_root == Root_in) or (chord_name == '7#5' and DOM7SHARP5_SETTING == 1 and chord_root == Root_in) or (chord_name == 'mM7' and mM7_SETTING == 1 and chord_root == Root_in) or (chord_name == 'sus2' and SUS2_SETTING == 1 and chord_root == Root_in) or (chord_name == 'sus4' and SUS4_SETTING == 1 and chord_root == Root_in):
                Chords_01_Listbox.insert(counter, Chord(Note(chord_root), chord_name))
                counter = counter + 1

    create_scale_chords_left_down_right_down(UserScale, Chords_02_Listbox)
    Chords_01_Listbox.update_idletasks()

def create_mode_chords_right_up():

    global CurrentMatchedScaleIndex, UserScaleBox02, Chords_03_Listbox, enable_second_fretboard_drawing, current_selected_chord_right

    Negative_Harmony_utils.current_selected_negative_chord_2 = None
    Negative_Harmony_utils.current_selected_negative_mode_2 = None

    current_selected_chord_right = "Nothing Here"
    enable_second_fretboard_drawing = True

    Chords_03_Listbox.delete(0, END)
    counter = 0

    a = str(Matched_Scales.get(ANCHOR))
    CurrentMatchedScaleIndex = Matched_Scales.index(ANCHOR)

    if a != (""):

        scale_root = a.split(' ', 1)[0]
        scale_name = a.split(' ', 1)[1]

        global Root_in_2, Scale_in_2
        Root_in_2 = scale_root
        Scale_in_2 = scale_name

        Negative_Harmony_utils.Root_b_temp = Root_in_2
        Negative_Harmony_utils.Scale_b_temp = Scale_in_2

        UserScaleBox02 = Scale(scale_root, scale_name)

        Negative_Harmony_utils.User_b_scale_temp = UserScaleBox02

        MN_Draw.drawModeShape(scale_name, fretboard02_canvas, notefile, fretboardfile)
        MN_Draw.drawPianoMode(Scale(scale_root, scale_name), piano02_canvas, notefile, pianofile)

        search_for_this_mode = str(scale_root) + " " + str(scale_name)

        for a in chords.chords_dict.get(search_for_this_mode):

            chord_text = a.split()
            chord_root = chord_text[0]
            chord_name = chord_text[1]

            if (chord_name == 'maj' and MAJ_SETTING == 1 and chord_root == scale_root) or (chord_name == 'majadd2' and MAJADD2_SETTING == 1 and chord_root == scale_root) or (chord_name == 'majadd4' and MAJADD4_SETTING == 1 and chord_root == scale_root) or (chord_name == 'majadd6' and MAJADD6_SETTING == 1 and chord_root == scale_root) or (chord_name == 'maj7' and MAJ7_SETTING == 1 and chord_root == scale_root) or (chord_name == 'm' and M_SETTING == 1 and chord_root == scale_root) or (chord_name == 'madd2' and MADD2_SETTING == 1 and chord_root == scale_root) or (chord_name == 'madd4' and MADD4_SETTING == 1 and chord_root == scale_root) or (chord_name == 'madd6' and MADD6_SETTING == 1 and chord_root == scale_root) or (chord_name == 'm7' and M7_SETTING == 1 and chord_root == scale_root) or (chord_name == '7' and DOM7_SETTING == 1 and chord_root == scale_root) or (chord_name == '7sus2' and DOM7SUS2_SETTING == 1 and chord_root == scale_root) or (chord_name == '7sus4' and DOM7SUS4_SETTING == 1 and chord_root == scale_root) or (chord_name == '+' and AUG_SETTING == 1 and chord_root == scale_root) or (chord_name == 'dim' and DIM_SETTING == 1 and chord_root == scale_root) or (chord_name == 'dim7' and DIM7_SETTING == 1 and chord_root == scale_root) or (chord_name == 'maj7b5' and MAJ7B5_SETTING == 1 and chord_root == scale_root) or (chord_name == 'maj7#5' and MAJ7SHARP5_SETTING == 1 and chord_root == scale_root) or (chord_name == 'm7b5' and M7B5_SETTING == 1 and chord_root == scale_root) or (chord_name == 'm7#5' and M7SHARP5_SETTING == 1 and chord_root == scale_root) or (chord_name == '7b5' and DOM7B5_SETTING == 1 and chord_root == scale_root) or (chord_name == '7#5' and DOM7SHARP5_SETTING == 1 and chord_root == scale_root) or (chord_name == 'mM7' and mM7_SETTING == 1 and chord_root == scale_root) or (chord_name == 'sus2' and SUS2_SETTING == 1 and chord_root == scale_root) or (chord_name == 'sus4' and SUS4_SETTING == 1 and chord_root == scale_root):
                Chords_03_Listbox.insert(counter, Chord(Note(chord_root), chord_name))
                counter = counter + 1

        Chords_03_Listbox.update_idletasks()

    show_scale_notes(False, scale02_notes_label)

    create_scale_chords_left_down_right_down(UserScaleBox02, Chords_04_Listbox)
    determine_seven_more_notes(UserScaleBox02)

    if is_extended_fretboard_open == True:
        global extended_fretboard_canvas
        extended_fretboard_canvas.delete("all")
        extended_fretboard_canvas.create_image(490,215,image=extendedfretboardfile)
        MN_Draw.drawExtendedFretboard(UserScale, UserScaleBox02, Root_in, Root_in_2,  extended_fretboard_canvas, show_chords, current_selected_chord_right, current_selected_chord_left, enable_second_fretboard_drawing, largenotefile, largerootnotefile, largechordnotefile)

    if Negative_Harmony_utils.is_negative_harmony_open == True:

        global negativeharmonybackgroundfile_pos_1, negativeharmonybackgroundfile_pos_2, negativeharmonybackgroundfile_pos_3, negativeharmonybackgroundfile_pos_4, negativeharmonybackgroundfile_pos_5, negativeharmonybackgroundfile_pos_6
        global negativeharmonybackgroundfile_pos_1_pos_1, negativeharmonybackgroundfile_pos_1_pos_2, negativeharmonybackgroundfile_pos_1_pos_3, negativeharmonybackgroundfile_pos_1_pos_4, negativeharmonybackgroundfile_pos_1_pos_5, negativeharmonybackgroundfile_pos_1_pos_6
        global negativeharmonybackgroundfile_pos_2_pos_1, negativeharmonybackgroundfile_pos_2_pos_2, negativeharmonybackgroundfile_pos_2_pos_3, negativeharmonybackgroundfile_pos_2_pos_4, negativeharmonybackgroundfile_pos_2_pos_5, negativeharmonybackgroundfile_pos_2_pos_6
        global negativeharmonybackgroundfile_pos_3_pos_1, negativeharmonybackgroundfile_pos_3_pos_2, negativeharmonybackgroundfile_pos_3_pos_3, negativeharmonybackgroundfile_pos_3_pos_4, negativeharmonybackgroundfile_pos_3_pos_5, negativeharmonybackgroundfile_pos_3_pos_6
        global negativeharmonybackgroundfile_pos_4_pos_1, negativeharmonybackgroundfile_pos_4_pos_2, negativeharmonybackgroundfile_pos_4_pos_3, negativeharmonybackgroundfile_pos_4_pos_4, negativeharmonybackgroundfile_pos_4_pos_5, negativeharmonybackgroundfile_pos_4_pos_6
        global negativeharmonybackgroundfile_pos_5_pos_1, negativeharmonybackgroundfile_pos_5_pos_2, negativeharmonybackgroundfile_pos_5_pos_3, negativeharmonybackgroundfile_pos_5_pos_4, negativeharmonybackgroundfile_pos_5_pos_5, negativeharmonybackgroundfile_pos_5_pos_6
        global negativeharmonybackgroundfile_pos_6_pos_1, negativeharmonybackgroundfile_pos_6_pos_2, negativeharmonybackgroundfile_pos_6_pos_3, negativeharmonybackgroundfile_pos_6_pos_4, negativeharmonybackgroundfile_pos_6_pos_5, negativeharmonybackgroundfile_pos_6_pos_6

        Negative_Harmony_utils.clearcolors(2)

        Negative_Harmony_utils.compare_notes_to_circle(2, False, Root_in_2, Scale_in_2, greencolor, redcolor, UserScaleBox02, negativeharmonybackgroundfile_pos_1, negativeharmonybackgroundfile_pos_2, negativeharmonybackgroundfile_pos_3, negativeharmonybackgroundfile_pos_4, negativeharmonybackgroundfile_pos_5, negativeharmonybackgroundfile_pos_6, negativeharmonybackgroundfile_pos_1_pos_1, negativeharmonybackgroundfile_pos_1_pos_2, negativeharmonybackgroundfile_pos_1_pos_3, negativeharmonybackgroundfile_pos_1_pos_4, negativeharmonybackgroundfile_pos_1_pos_5, negativeharmonybackgroundfile_pos_1_pos_6, negativeharmonybackgroundfile_pos_2_pos_1, negativeharmonybackgroundfile_pos_2_pos_2, negativeharmonybackgroundfile_pos_2_pos_3, negativeharmonybackgroundfile_pos_2_pos_4, negativeharmonybackgroundfile_pos_2_pos_5, negativeharmonybackgroundfile_pos_2_pos_6, negativeharmonybackgroundfile_pos_3_pos_1, negativeharmonybackgroundfile_pos_3_pos_2, negativeharmonybackgroundfile_pos_3_pos_3, negativeharmonybackgroundfile_pos_3_pos_4, negativeharmonybackgroundfile_pos_3_pos_5, negativeharmonybackgroundfile_pos_3_pos_6, negativeharmonybackgroundfile_pos_4_pos_1, negativeharmonybackgroundfile_pos_4_pos_2, negativeharmonybackgroundfile_pos_4_pos_3, negativeharmonybackgroundfile_pos_4_pos_4, negativeharmonybackgroundfile_pos_4_pos_5, negativeharmonybackgroundfile_pos_4_pos_6, negativeharmonybackgroundfile_pos_5_pos_1, negativeharmonybackgroundfile_pos_5_pos_2, negativeharmonybackgroundfile_pos_5_pos_3, negativeharmonybackgroundfile_pos_5_pos_4, negativeharmonybackgroundfile_pos_5_pos_5, negativeharmonybackgroundfile_pos_5_pos_6, negativeharmonybackgroundfile_pos_6_pos_1, negativeharmonybackgroundfile_pos_6_pos_2, negativeharmonybackgroundfile_pos_6_pos_3, negativeharmonybackgroundfile_pos_6_pos_4, negativeharmonybackgroundfile_pos_6_pos_5, negativeharmonybackgroundfile_pos_6_pos_6)

        list_of_inverted_scale_notes = Negative_Harmony_utils.calculate_inverted_scale_notes(2, Root_in_2, Scale_in_2)

        Negative_Harmony_utils.Mode_1_label_right.config(text=((Root_in_2 + " " + Scale_in_2)), font=font_01, bg=listbox_color)
        Negative_Harmony_utils.update_scale_labels(Scale(Note(Root_in_2), Scale_in_2), Negative_Harmony_utils.Mode1_notes_label_right, 2, listbox_color, font_01)

        Negative_Harmony_utils.Mode_1_Chords_Listbox_right.delete(0, END)

        for c in range(0, Chords_04_Listbox.size()):
            Negative_Harmony_utils.Mode_1_Chords_Listbox_right.insert(c, Chords_04_Listbox.get(c))

        Negative_Harmony_utils.Mode_1_Negative_Chords_Listbox_right.delete(0, END)
        Negative_Harmony_utils.calculate_inverted_chord_notes(2, Negative_Harmony_utils.Mode_1_Chords_Listbox_right, Negative_Harmony_utils.Mode_1_Negative_Chords_Listbox_right)

        Negative_Harmony_utils.Mode_1_Negative_label_right.config(text=(Negative_Harmony_utils.InvertedScale(list_of_inverted_scale_notes, Negative_Harmony_utils.Mode_1_Negative_Chords_Listbox_right)), foreground="white", bg=darkgrey, font=font_01)
        Negative_Harmony_utils.update_scale_labels(Negative_Harmony_utils.InvertedScale(list_of_inverted_scale_notes, Negative_Harmony_utils.Mode_1_Negative_Chords_Listbox_right), Negative_Harmony_utils.Mode2_notes_label_right, 2, darkgrey, font_01)

        Negative_Harmony_utils.current_selected_negative_mode_2 = Negative_Harmony_utils.Mode_1_Negative_label_right.cget('text')

        Negative_Harmony_utils.negative_harmony_window.lift()


def show_Chord_Notes(event, frame, match_list):
    global CurrentChord02, CurrentChord3Index, CurrentChord1Index, CurrentChord2Index, CurrentChord4Index, chord_label1, chord_label2, chord_label3, chord_label4, current_selected_chord_left, current_selected_chord_right

    chord_notes = 0

    if frame == "frame_01":
        current_selected_chord_left = "Nothing Here"
        CurrentChord1Index = match_list.index(ANCHOR)
        chord_notes = Chord(match_list.get(CurrentChord1Index)).notes
        current_selected_chord_left = chord_notes

    if frame == "frame_02":
        current_selected_chord_left = "Nothing Here"
        CurrentChord2Index = match_list.index(ANCHOR)
        chord_notes = Chord(match_list.get(CurrentChord2Index)).notes
        current_selected_chord_left = chord_notes


    if frame == "frame_03":
        current_selected_chord_right = "Nothing Here"
        CurrentChord3Index = match_list.index(ANCHOR)
        chord_notes = Chord(match_list.get(CurrentChord3Index)).notes
        current_selected_chord_right = chord_notes


    if frame == "frame_04":
        current_selected_chord_right = "Nothing Here"
        CurrentChord4Index = match_list.index(ANCHOR)
        chord_notes = Chord(match_list.get(CurrentChord4Index)).notes
        current_selected_chord_right = chord_notes


    chord_label = Label(window, borderwidth=2, width=8)
    chord_label.config(text=(chord_notes), bg=(color), font=font_01)

    if frame == "frame_04" and hidden_more_chords[1] == False:
        chord_label4.destroy()
        chord_label4 = chord_label
        chord_label4.place(x=695, y=458)

    if frame == "frame_03":
        chord_label3 = chord_label
        chord_label3.place(x=695, y=140)

    if frame == "frame_02" and hidden_more_chords[0] == False:
        chord_label2.destroy()
        chord_label2 = chord_label
        chord_label2.place(x=210, y=462)

    if frame == "frame_01":
        chord_label1 = chord_label
        chord_label1.place(x=210, y=140)


def show_scale_notes(userscale, scale_notes_label):
    if not userscale:
        global UserScaleBox02
        root = UserScaleBox02.root
        scale = UserScaleBox02.name
        scale_notes = Scale(root, scale).notes
    else:
        scale_notes = UserScale.notes

    scale_notes_label.config(text=(scale_notes), bg=(color), font=font_01_bold_02)
    scale_notes_label.update_idletasks()

def play_and_show_mode_chords_left_up_right_up(event, scale_list, chord_list, text, frame, r, s):
    global enable_second_fretboard_drawing, extendedfretboardfile
    if text == "Matched_Chords2":
        enable_second_fretboard_drawing = True
    MN_AUDIO.playMatchedChord(event, scale_list, chord_list, text, r, s)
    show_Chord_Notes(event, frame, chord_list)
    if show_chords == True and is_extended_fretboard_open == True:
        extended_fretboard_canvas.delete("all")
        extended_fretboard_canvas.create_image(490, 215, image=extendedfretboardfile)
        MN_Draw.drawExtendedFretboard(UserScale, UserScaleBox02, Root_in, Root_in_2,  extended_fretboard_canvas, show_chords, current_selected_chord_right, current_selected_chord_left, enable_second_fretboard_drawing, largenotefile, largerootnotefile, largechordnotefile)


def play_and_show_scale_chords_left_down_right_down(event, chord_list, seven_list, frame): # This plays the SCALE CHORDS both on the LEFT and RIGHT
    global enable_second_fretboard_drawing, extendedfretboardfile
    # enable_second_fretboard_drawing = True
    MN_AUDIO.playMoreChord(event, chord_list, seven_list)
    show_Chord_Notes(event, frame, chord_list)
    if show_chords == True and is_extended_fretboard_open == True:
        extended_fretboard_canvas.delete("all")
        extended_fretboard_canvas.create_image(490, 215, image=extendedfretboardfile)
        MN_Draw.drawExtendedFretboard(UserScale, UserScaleBox02, Root_in, Root_in_2,  extended_fretboard_canvas, show_chords, current_selected_chord_right, current_selected_chord_left, enable_second_fretboard_drawing, largenotefile, largerootnotefile, largechordnotefile)


def OnEntryDown(event):
    try:
        pos = Scale_in_box.index(ANCHOR) + 1
        if not pos:
            return
        Scale_in_box.selection_set(pos)
        Scale_in_box.selection_anchor(pos)
    except:
        pass

def OnEntryUp(event):
    try:
        pos = Scale_in_box.index(ANCHOR) - 1
        if not pos:
            if Scale_in_box.index(ANCHOR) - 1 <= 0:
                pos = 0
            else:
                return

        if Scale_in_box.index(ANCHOR) - 1 <= 0:
            pos = 0
        Scale_in_box.selection_set(pos)
        Scale_in_box.selection_anchor(pos)
    except:
        pass


check_checkbox()
initialize_scales()  # calls function to create a list with all the scales

Root_in_box = Listbox(window, exportselection=0, height=12, width=3, selectbackground='Gray')

counter_root = 0
for note in all_notes:
    Root_in_box.insert(counter_root, note)
    counter_root = counter_root + 1
Root_in_box.select_set(0)
Root_in_box.bind('<<ListboxSelect>>', read_root)
Root_in_box.bind("<Down>", lambda event: "break")
Root_in_box.bind("<Up>", lambda event: "break")
Root_in_box.config(font=font_01, bg=listbox_color)
Root_in_box.place(x=6, y=33)
Root_in_box.update_idletasks()

Scale_in_box = Listbox(window, exportselection=0, height=29, width=21, selectbackground='Gray')
Scale_in_box.bind('<<ListboxSelect>>', read_scale)
Scale_in_box.bind("<Down>", OnEntryDown)
Scale_in_box.bind("<Up>", OnEntryUp)
counter_scale = 0
for scale in settings.scales_names:
    Scale_in_box.insert(counter_scale, scale)
    counter_scale = counter_scale + 1
Scale_in_box.select_set(0)
Scale_in_box.place(x=37, y=33)
Scale_in_box.config(font=font_01, bg=listbox_color)
Scale_in_box.update_idletasks()

Chords_01_Listbox = Listbox(window, exportselection=0, height=6, width=9, selectbackground='Gray')
Chords_01_Listbox.bind('<<ListboxSelect>>', lambda event: play_and_show_mode_chords_left_up_right_up(event, Matched_Scales, Chords_01_Listbox, "Matched_Chords", "frame_01", Root_in, Scale_in))

Chords_01_Listbox.place(x=210, y=33)
Chords_01_Listbox.config(font=font_01, bg=listbox_color)
Chords_01_Listbox.bind("<Down>", lambda event: "break")
Chords_01_Listbox.bind("<Up>", lambda event: "break")

Chords_02_Listbox = Listbox(window, exportselection=0, height=15, width=9, selectbackground='Gray')
Chords_02_Listbox.place(x=210, y=211)
Chords_02_Listbox.lower()
Chords_02_Listbox.config(font=font_01, bg=listbox_color)
Chords_02_Listbox.bind("<Down>", lambda event: "break")
Chords_02_Listbox.bind("<Up>", lambda event: "break")
Chords_02_Listbox.bind('<<ListboxSelect>>', lambda event: play_and_show_scale_chords_left_down_right_down(event, Chords_02_Listbox, seven_notes, "frame_02"))

Chords_04_Listbox = Listbox(window, exportselection=0, height=15, width=9, selectbackground='Gray')
Chords_04_Listbox.place(x=693, y=207)
Chords_04_Listbox.lower()
Chords_04_Listbox.config(font=font_01, bg=listbox_color)
Chords_04_Listbox.bind("<Down>", lambda event: "break")
Chords_04_Listbox.bind("<Up>", lambda event: "break")
Chords_04_Listbox.bind('<<ListboxSelect>>', lambda event: play_and_show_scale_chords_left_down_right_down(event, Chords_04_Listbox, other_seven_notes, "frame_04"))

N_Notes_in_box = ttk.Combobox(window, textvariable=y, values=common_notes_list, state='readonly', width=4)
N_Notes_in_box.bind('<<ComboboxSelected>>', read_number)
N_Notes_in_box.place(x=505, y=33)
N_Notes_in_box.config(font=font_01)
N_Notes_in_box.current(5)

notes_in_common_entry = Entry(window, width=17, borderwidth=0, relief=FLAT, textvariable=z)
notes_in_common_entry.bind("<Return>", lambda event: update_notes_in_common())
notes_in_common_entry.place(x=505, y=73)
notes_in_common_entry.config(font=font_01, bg=listbox_color)

Matched_Scales = Listbox(window, height=21, width=23, exportselection=0, selectbackground='Gray')
Matched_Scales.place(x=505, y=115)
Matched_Scales.bind("<<ListboxSelect>>", lambda event: create_mode_chords_right_up())
Matched_Scales.config(font=font_01, bg=listbox_color)

Matched_Scales.bind("<Down>", lambda event: "break")
Matched_Scales.bind("<Up>", lambda event: "break")

Chords_03_Listbox = Listbox(window, exportselection=0, height=6, width=9, selectbackground='Gray')
Chords_03_Listbox.place(x=692, y=33)
Chords_03_Listbox.config(font=font_01, bg=listbox_color)
Chords_03_Listbox.bind('<<ListboxSelect>>', lambda event: play_and_show_mode_chords_left_up_right_up(event, Matched_Scales, Chords_03_Listbox, "Matched_Chords2", "frame_03", Root_in, Scale_in))
Chords_03_Listbox.bind("<Down>", lambda event: "break")
Chords_03_Listbox.bind("<Up>", lambda event: "break")

scale01_notes_label = Label(window, borderwidth=2, width=17)
scale02_notes_label = Label(window, borderwidth=2, width=17)
scale01_notes_label.place(x=305, y=265)
scale02_notes_label.place(x=795, y=265)


def show_hide_more_chords(listbox01, index):
    global chord_label2, chord_label4, hidden_more_chords

    if not hidden_more_chords[index]:
        listbox01.lower()
        if index == 0:
            chord_label2.lower()
        else:
            chord_label4.lower()
        hidden_more_chords[index] = True
    else:
        listbox01.lift()
        if index == 0:
            chord_label2.lift()
        else:
            chord_label4.lift()
        hidden_more_chords[index] = False


more01_button = Button(window, text="+", width=1, highlightthickness=0, command=lambda: show_hide_more_chords(Chords_02_Listbox, 0))
more01_button.place(x=213, y=176)

more02_button = Button(window, text="+", width=1, highlightthickness=0, command=lambda: show_hide_more_chords(Chords_04_Listbox, 1))
more02_button.place(x=695, y=176)


#Expanded Fretboard
def Expand_Fretboard():
    global is_extended_fretboard_open, largenotefile
    if is_extended_fretboard_open == False:
        extend_fretboard_button.lower()
        is_extended_fretboard_open = True
        extended_fretboard_window = Toplevel()
        extended_fretboard_window.geometry("980x430+550+400")
        extended_fretboard_window.title("Fretboard Extended View")
        extended_fretboard_window.resizable(False, False)
        extended_fretboard_window.config(bg=color)

        extended_fretboard_window.bind('c', Show_Chords)

        global extended_fretboard_canvas
        extended_fretboard_canvas = Canvas(extended_fretboard_window, height=450, width=980, bg="black", highlightthickness=0, highlightbackground=color)
        extended_fretboard_canvas.place(height=450, width=980)
        extended_fretboard_canvas.create_image(490,215,image=extendedfretboardfile)

        fretboard_menu = Menu(extended_fretboard_window)
        extended_fretboard_window.config(menu=fretboard_menu)
        fileMenu = Menu(fretboard_menu, tearoff=0)
        fretboard_menu.add_cascade(label="Options", menu=fileMenu)
        fileMenu.add_command(label="Show / Hide Chord Notes (C)", command=lambda: Show_Chords_Menu())

        update_guitar_notes_array()

    global UserScale, UserScaleBox02
    global enable_second_fretboard_drawing

    if (Root_in != None and Scale_in != None):
        MN_Draw.drawExtendedFretboard(UserScale, UserScaleBox02, Root_in, Root_in_2,  extended_fretboard_canvas, show_chords, current_selected_chord_right, current_selected_chord_left, enable_second_fretboard_drawing, largenotefile, largerootnotefile, largechordnotefile)

    def on_closing_fretboard():
        global is_extended_fretboard_open
        is_extended_fretboard_open = False
        extend_fretboard_button.lift()
        extended_fretboard_window.destroy()

    extended_fretboard_window.protocol("WM_DELETE_WINDOW", on_closing_fretboard)

def update_guitar_notes_array():
    half_step = Interval('A1')
    first_note = Note(FIRST_STRING_SETTING)
    second_note = Note(SECOND_STRING_SETTING)
    third_note = Note(THIRD_STRING_SETTING)
    fourth_note = Note(FOURTH_STRING_SETTING)
    fifth_note = Note(FIFTH_STRING_SETTING)
    sixth_note = Note(SIXTH_STRING_SETTING)

    first_string_notes.insert(0, first_note)
    second_string_notes.insert(0, second_note)
    third_string_notes.insert(0, third_note)
    fourth_string_notes.insert(0, fourth_note)
    fifth_string_notes.insert(0, fifth_note)
    sixth_string_notes.insert(0, sixth_note)

    for n in range(1, 25):
        first_string_notes.insert(n, first_note + half_step)
        second_string_notes.insert(n, second_note + half_step)
        third_string_notes.insert(n, third_note + half_step)
        fourth_string_notes.insert(n, fourth_note + half_step)
        fifth_string_notes.insert(n, fifth_note + half_step)
        sixth_string_notes.insert(n, sixth_note + half_step)

        first_note = first_note + half_step
        second_note = second_note + half_step
        third_note = third_note + half_step
        fourth_note = fourth_note + half_step
        fifth_note = fifth_note + half_step
        sixth_note = sixth_note + half_step

extend_fretboard_button = Button(window, text="Extended Fretboard", width=20, command=lambda: Expand_Fretboard())
extend_fretboard_button.place(x=300, y=368)

composer_mode_button = Button(window, text="Composer Mode ", width=20,  command=lambda: Open_Composer_Mode())
composer_mode_button.place(x=300, y=400)

negative_harmony_button = Button(window, text="Negative Harmony ", width=20, command=lambda: Negative_Harmony_utils.Open_Negative_Harmony_Mode(Root_in, Scale_in, Root_in_2, Scale_in_2, UserScale, UserScaleBox02, FLAT_SETTING, font_01, color, darkgrey, listbox_color, redcolor, greencolor, negativeharmonybackgroundfile_pos_1, negativeharmonybackgroundfile_pos_2, negativeharmonybackgroundfile_pos_3, negativeharmonybackgroundfile_pos_4, negativeharmonybackgroundfile_pos_5, negativeharmonybackgroundfile_pos_6, negative_harmony_button, negativeharmonybackgroundfile, circle_of_notes_left, circle_of_notes_right, parser, circle_of_notes_options, Chords_02_Listbox, Chords_04_Listbox, negativeharmonybackgroundfile_pos_1_pos_1, negativeharmonybackgroundfile_pos_1_pos_2, negativeharmonybackgroundfile_pos_1_pos_3, negativeharmonybackgroundfile_pos_1_pos_4, negativeharmonybackgroundfile_pos_1_pos_5, negativeharmonybackgroundfile_pos_1_pos_6, negativeharmonybackgroundfile_pos_2_pos_1, negativeharmonybackgroundfile_pos_2_pos_2, negativeharmonybackgroundfile_pos_2_pos_3, negativeharmonybackgroundfile_pos_2_pos_4, negativeharmonybackgroundfile_pos_2_pos_5, negativeharmonybackgroundfile_pos_2_pos_6, negativeharmonybackgroundfile_pos_3_pos_1, negativeharmonybackgroundfile_pos_3_pos_2, negativeharmonybackgroundfile_pos_3_pos_3, negativeharmonybackgroundfile_pos_3_pos_4, negativeharmonybackgroundfile_pos_3_pos_5, negativeharmonybackgroundfile_pos_3_pos_6, negativeharmonybackgroundfile_pos_4_pos_1, negativeharmonybackgroundfile_pos_4_pos_2, negativeharmonybackgroundfile_pos_4_pos_3, negativeharmonybackgroundfile_pos_4_pos_4, negativeharmonybackgroundfile_pos_4_pos_5, negativeharmonybackgroundfile_pos_4_pos_6, negativeharmonybackgroundfile_pos_5_pos_1, negativeharmonybackgroundfile_pos_5_pos_2, negativeharmonybackgroundfile_pos_5_pos_3, negativeharmonybackgroundfile_pos_5_pos_4, negativeharmonybackgroundfile_pos_5_pos_5, negativeharmonybackgroundfile_pos_5_pos_6, negativeharmonybackgroundfile_pos_6_pos_1, negativeharmonybackgroundfile_pos_6_pos_2, negativeharmonybackgroundfile_pos_6_pos_3, negativeharmonybackgroundfile_pos_6_pos_4, negativeharmonybackgroundfile_pos_6_pos_5, negativeharmonybackgroundfile_pos_6_pos_6, usersettingspath))
negative_harmony_button.place(x=300, y=432)

#Composer Mode
def Open_Composer_Mode():

    global is_composer_mode_open

    if is_composer_mode_open == False:
        composer_mode_button.lower()
        is_composer_mode_open = True
        composer_mode_window = Toplevel()
        composer_mode_window.geometry("700x370+550+400")
        composer_mode_window.title("Composer Mode")
        composer_mode_window.resizable(False, False)
        # composer_mode_window.attributes("-topmost", True)
        composer_mode_window.config(bg=color)
        composer_background = Label(composer_mode_window, height=370, width=700, image=composerbackgroundfile)
        composer_background.place(x=-3, y=-3)

        Chord_Progression_Listbox = Listbox(composer_mode_window, selectmode=BROWSE, exportselection=False, height=21, width=9, selectbackground='Gray')
        Chord_Progression_Listbox.bind("<<ListboxSelect>>", lambda event: Composer_Mode_utils.Chord_Progression_Listbox_Select(Chord_Progression_Listbox, Chord_Progression_Modes_Listbox))
        Chord_Progression_Listbox.select_set(0)
        Chord_Progression_Listbox.config(font=font_01, bg=listbox_color)
        Chord_Progression_Listbox.place(x=2, y=18)

        Chord_Progression_Modes_Listbox = Listbox(composer_mode_window, selectmode=BROWSE, exportselection=False, height=21, width=23, selectbackground='Gray')
        Chord_Progression_Modes_Listbox.bind("<<ListboxSelect>>", lambda event: Composer_Mode_utils.Chord_Progression_Modes_Listbox_Select(Chord_Progression_Modes_Listbox, Chord_Progression_Listbox))
        Chord_Progression_Modes_Listbox.select_set(0)
        Chord_Progression_Modes_Listbox.config(font=font_01, bg=listbox_color)
        Chord_Progression_Modes_Listbox.place(x=78, y=18)

        Composer_Mode_utils.load_temp_chord_progressions(Chord_Progression_Listbox, Chord_Progression_Modes_Listbox, tmpcomposerpath)

        Add_Chord_01 = Button(composer_mode_window, text="Add Mode Chord 1", width=14, highlightthickness=0, command=lambda: Composer_Mode_utils.add_chord(1, CurrentChord1Index, CurrentChord2Index, CurrentChord3Index, CurrentChord4Index, Chord_Progression_Listbox, Chord_Progression_Modes_Listbox, Chords_01_Listbox, Chords_02_Listbox, Chords_03_Listbox, Chords_04_Listbox, Root_in, Scale_in, Root_in_2, Scale_in_2))
        composer_mode_window.bind("1",  lambda event: Composer_Mode_utils.add_chord(1, CurrentChord1Index, CurrentChord2Index, CurrentChord3Index, CurrentChord4Index, Chord_Progression_Listbox, Chord_Progression_Modes_Listbox, Chords_01_Listbox, Chords_02_Listbox, Chords_03_Listbox, Chords_04_Listbox, Root_in, Scale_in, Root_in_2, Scale_in_2))
        Add_Chord_02 = Button(composer_mode_window, text="Add Scale Chord 1", width=14, highlightthickness=0, command=lambda: Composer_Mode_utils.add_chord(2, CurrentChord1Index, CurrentChord2Index, CurrentChord3Index, CurrentChord4Index, Chord_Progression_Listbox, Chord_Progression_Modes_Listbox, Chords_01_Listbox, Chords_02_Listbox, Chords_03_Listbox, Chords_04_Listbox, Root_in, Scale_in, Root_in_2, Scale_in_2))
        composer_mode_window.bind("2",  lambda event: Composer_Mode_utils.add_chord(2, CurrentChord1Index, CurrentChord2Index, CurrentChord3Index, CurrentChord4Index, Chord_Progression_Listbox, Chord_Progression_Modes_Listbox, Chords_01_Listbox, Chords_02_Listbox, Chords_03_Listbox, Chords_04_Listbox, Root_in, Scale_in, Root_in_2, Scale_in_2))
        Add_Chord_03 = Button(composer_mode_window, text="Add Mode Chord 2", width=14, highlightthickness=0, command=lambda: Composer_Mode_utils.add_chord(3, CurrentChord1Index, CurrentChord2Index, CurrentChord3Index, CurrentChord4Index, Chord_Progression_Listbox, Chord_Progression_Modes_Listbox, Chords_01_Listbox, Chords_02_Listbox, Chords_03_Listbox, Chords_04_Listbox, Root_in, Scale_in, Root_in_2, Scale_in_2))
        composer_mode_window.bind("3",  lambda event: Composer_Mode_utils.add_chord(3, CurrentChord1Index, CurrentChord2Index, CurrentChord3Index, CurrentChord4Index, Chord_Progression_Listbox, Chord_Progression_Modes_Listbox, Chords_01_Listbox, Chords_02_Listbox, Chords_03_Listbox, Chords_04_Listbox, Root_in, Scale_in, Root_in_2, Scale_in_2))
        Add_Chord_04 = Button(composer_mode_window, text="Add Scale Chord 2", width=14, highlightthickness=0, command=lambda: Composer_Mode_utils.add_chord(4, CurrentChord1Index, CurrentChord2Index, CurrentChord3Index, CurrentChord4Index, Chord_Progression_Listbox, Chord_Progression_Modes_Listbox, Chords_01_Listbox, Chords_02_Listbox, Chords_03_Listbox, Chords_04_Listbox, Root_in, Scale_in, Root_in_2, Scale_in_2))
        composer_mode_window.bind("4",  lambda event: Composer_Mode_utils.add_chord(4, CurrentChord1Index, CurrentChord2Index, CurrentChord3Index, CurrentChord4Index, Chord_Progression_Listbox, Chord_Progression_Modes_Listbox, Chords_01_Listbox, Chords_02_Listbox, Chords_03_Listbox, Chords_04_Listbox, Root_in, Scale_in, Root_in_2, Scale_in_2))
        Add_Negative_Chord_01 = Button(composer_mode_window, text="Add Negative Chord 1", width=17, highlightthickness=0, bg=darkgrey, command=lambda: Composer_Mode_utils.add_chord(5, CurrentChord1Index, CurrentChord2Index, CurrentChord3Index, CurrentChord4Index, Chord_Progression_Listbox, Chord_Progression_Modes_Listbox, Chords_01_Listbox, Chords_02_Listbox, Chords_03_Listbox, Chords_04_Listbox, Root_in, Scale_in, Root_in_2, Scale_in_2))
        composer_mode_window.bind("5",  lambda event: Composer_Mode_utils.add_chord(5, CurrentChord1Index, CurrentChord2Index, CurrentChord3Index, CurrentChord4Index, Chord_Progression_Listbox, Chord_Progression_Modes_Listbox, Chords_01_Listbox, Chords_02_Listbox, Chords_03_Listbox, Chords_04_Listbox, Root_in, Scale_in, Root_in_2, Scale_in_2))
        Add_Negative_Chord_02 = Button(composer_mode_window, text="Add Negative Chord 2", width=17, highlightthickness=0, command=lambda: Composer_Mode_utils.add_chord(6, CurrentChord1Index, CurrentChord2Index, CurrentChord3Index, CurrentChord4Index, Chord_Progression_Listbox, Chord_Progression_Modes_Listbox, Chords_01_Listbox, Chords_02_Listbox, Chords_03_Listbox, Chords_04_Listbox, Root_in, Scale_in, Root_in_2, Scale_in_2))
        composer_mode_window.bind("6",  lambda event: Composer_Mode_utils.add_chord(6, CurrentChord1Index, CurrentChord2Index, CurrentChord3Index, CurrentChord4Index, Chord_Progression_Listbox, Chord_Progression_Modes_Listbox, Chords_01_Listbox, Chords_02_Listbox, Chords_03_Listbox, Chords_04_Listbox, Root_in, Scale_in, Root_in_2, Scale_in_2))
        Move_Up = Button(composer_mode_window, text="Move Up", width=10, highlightthickness=0, command=lambda: Composer_Mode_utils.move_up(Chord_Progression_Listbox, Chord_Progression_Modes_Listbox))
        Move_Down = Button(composer_mode_window, text="Move Down", width=10, highlightthickness=0, command=lambda: Composer_Mode_utils.move_down(Chord_Progression_Listbox, Chord_Progression_Modes_Listbox))
        Remove = Button(composer_mode_window, text="Remove", width=10, highlightthickness=0, command=lambda: Composer_Mode_utils.remove_chord(Chord_Progression_Listbox, Chord_Progression_Modes_Listbox))
        composer_mode_window.bind("<BackSpace>",  lambda event: Composer_Mode_utils.remove_chord(Chord_Progression_Listbox, Chord_Progression_Modes_Listbox))
        Clear_All = Button(composer_mode_window, text="Clear All", width=10, highlightthickness=0, command=lambda: Composer_Mode_utils.delete_all_chords(Chord_Progression_Modes_Listbox, Chord_Progression_Listbox))
        Composer_Mode_utils.Play = Button(composer_mode_window, text="Play", width=11, fg='#54FA9B',  highlightthickness=0, command=lambda: Composer_Mode_utils.play_chord_progression(composer_mode_window, PLAY_STYLE_SETTING, Chord_Progression_Listbox, Chord_Progression_Modes_Listbox))
        Stop = Button(composer_mode_window, text="Stop", width=11, fg='#F05151', highlightthickness=0, command=lambda: Composer_Mode_utils.stopComposer())
        Save = Button(composer_mode_window, text="Save", width=11, highlightthickness=0, command=lambda: Composer_Mode_utils.save_chord_progression(composer_mode_window, fd, Chord_Progression_Modes_Listbox, Chord_Progression_Listbox))
        Load = Button(composer_mode_window, text="Load", width=11, highlightthickness=0, command=lambda: Composer_Mode_utils.open_chord_progression(composer_mode_window, fd, Chord_Progression_Modes_Listbox, Chord_Progression_Listbox))
        Export_MIDI = Button(composer_mode_window, text="Export MIDI", width=11, highlightthickness=0, command=lambda: Composer_Mode_utils.EXPORT_MIDI(Chord_Progression_Listbox, fd))
        Tempo = Entry (composer_mode_window, exportselection=False, width = 8, insertontime=0, textvariable=tempo)

        play_style_options = ["Scale", "Chord", "Chord + Click"]

        def update_PlayStyle(event):
            global PLAY_STYLE_SETTING

            Composer_Mode_utils.stopComposer()

            option =  play_style.get()

            parser.set('usersettings', 'play_style', option)
            with open(usersettingspath, 'w') as configfile:
                parser.write(configfile)
                PLAY_STYLE_SETTING = option

        PlayStyle = OptionMenu(composer_mode_window, play_style, *play_style_options, command=update_PlayStyle)
        PlayStyle["highlightthickness"] = 0
        PlayStyle.bind()
        PlayStyle.config(font=font_01)

        def enterTempo(event):
            try:
                settings.composer_tempo = int(tempo.get())
            except ValueError:
                a = ''.join(c for c in tempo.get() if c.isdigit())
                tempo.set(a)
                settings.composer_tempo = a

            parser.set('usersettings', 'tempo', str(settings.composer_tempo))
            with open(usersettingspath, 'w') as configfile:
                parser.write(configfile)

        Add_Chord_01.place(x=268, y=18)
        Add_Chord_02.place(x=268, y=42)
        Add_Chord_03.place(x=398, y=18)
        Add_Chord_04.place(x=398, y=42)
        Add_Negative_Chord_01.place(x=527, y=18)
        Add_Negative_Chord_02.place(x=527, y=42)

        Move_Up.place(x=268, y=260)
        Move_Down.place(x=268, y=285)
        Remove.place(x=268, y=310)
        Clear_All.place(x=268, y=335)
        Composer_Mode_utils.Play.place(x=380, y=310)
        Stop.place(x=485, y=310)
        Save.place(x=380, y=335)
        Load.place(x=485, y=335)
        PlayStyle.place(x=590, y=310)
        Export_MIDI.place(x=590, y=335)
        Tempo.place(x=600, y=255)
        Tempo.bind('<Return>', enterTempo)

        composer_mode_window.focus()



        def on_closing_composer():
            global is_composer_mode_open
            is_composer_mode_open = False
            Composer_Mode_utils.stopComposer()
            Composer_Mode_utils.save_temp_chord_progressions(Chord_Progression_Modes_Listbox, Chord_Progression_Listbox, tmpcomposerpath)
            composer_mode_button.lift()
            composer_mode_window.destroy()

        composer_mode_window.protocol("WM_DELETE_WINDOW", on_closing_composer)

def Show_Chords(event):
    global show_chords
    if show_chords == False:
        show_chords = True
    else:
        show_chords = False

    if is_extended_fretboard_open == True:
        global extended_fretboard_canvas
        extended_fretboard_canvas.delete("all")
        extended_fretboard_canvas.create_image(490,215,image=extendedfretboardfile)
        MN_Draw.drawExtendedFretboard(UserScale, UserScaleBox02, Root_in, Root_in_2,  extended_fretboard_canvas, show_chords, current_selected_chord_right, current_selected_chord_left, enable_second_fretboard_drawing, largenotefile, largerootnotefile, largechordnotefile)

def Show_Chords_Menu():
    global show_chords
    if show_chords == False:
        show_chords = True
    else:
        show_chords = False

    if is_extended_fretboard_open == True:
        global extended_fretboard_canvas
        extended_fretboard_canvas.delete("all")
        extended_fretboard_canvas.create_image(490,215,image=extendedfretboardfile)
        MN_Draw.drawExtendedFretboard(UserScale, UserScaleBox02, Root_in, Root_in_2,  extended_fretboard_canvas, show_chords, current_selected_chord_right, current_selected_chord_left, enable_second_fretboard_drawing, largenotefile, largerootnotefile, largechordnotefile)

window.bind('c', Show_Chords)
window.protocol("WM_DELETE_WINDOW", Exit)

window.mainloop()
