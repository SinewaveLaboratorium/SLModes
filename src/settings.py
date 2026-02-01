import os
import sys
from MN_Scales import Chord

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

slmodes_version = "2.5.3"

pianopath = resource_path("piano.png")
backgroundpath = resource_path("Background01.png")
negativeharmonybackgroundpath = resource_path("negative_harmony_background.png")
negativeharmonybackgroundpath_pos_1 = resource_path("negative_harmony_pos_1.png")
negativeharmonybackgroundpath_pos_1_pos_1 = resource_path("negative_harmony_pos_1_pos_1.png")
negativeharmonybackgroundpath_pos_1_pos_2 = resource_path("negative_harmony_pos_1_pos_2.png")
negativeharmonybackgroundpath_pos_1_pos_3 = resource_path("negative_harmony_pos_1_pos_3.png")
negativeharmonybackgroundpath_pos_1_pos_4 = resource_path("negative_harmony_pos_1_pos_4.png")
negativeharmonybackgroundpath_pos_1_pos_5 = resource_path("negative_harmony_pos_1_pos_5.png")
negativeharmonybackgroundpath_pos_1_pos_6 = resource_path("negative_harmony_pos_1_pos_6.png")
negativeharmonybackgroundpath_pos_2 = resource_path("negative_harmony_pos_2.png")
negativeharmonybackgroundpath_pos_2_pos_1 = resource_path("negative_harmony_pos_2_pos_1.png")
negativeharmonybackgroundpath_pos_2_pos_2 = resource_path("negative_harmony_pos_2_pos_2.png")
negativeharmonybackgroundpath_pos_2_pos_3 = resource_path("negative_harmony_pos_2_pos_3.png")
negativeharmonybackgroundpath_pos_2_pos_4 = resource_path("negative_harmony_pos_2_pos_4.png")
negativeharmonybackgroundpath_pos_2_pos_5 = resource_path("negative_harmony_pos_2_pos_5.png")
negativeharmonybackgroundpath_pos_2_pos_6 = resource_path("negative_harmony_pos_2_pos_6.png")
negativeharmonybackgroundpath_pos_3 = resource_path("negative_harmony_pos_3.png")
negativeharmonybackgroundpath_pos_3_pos_1 = resource_path("negative_harmony_pos_3_pos_1.png")
negativeharmonybackgroundpath_pos_3_pos_2 = resource_path("negative_harmony_pos_3_pos_2.png")
negativeharmonybackgroundpath_pos_3_pos_3 = resource_path("negative_harmony_pos_3_pos_3.png")
negativeharmonybackgroundpath_pos_3_pos_4 = resource_path("negative_harmony_pos_3_pos_4.png")
negativeharmonybackgroundpath_pos_3_pos_5 = resource_path("negative_harmony_pos_3_pos_5.png")
negativeharmonybackgroundpath_pos_3_pos_6 = resource_path("negative_harmony_pos_3_pos_6.png")
negativeharmonybackgroundpath_pos_4 = resource_path("negative_harmony_pos_4.png")
negativeharmonybackgroundpath_pos_4_pos_1 = resource_path("negative_harmony_pos_4_pos_1.png")
negativeharmonybackgroundpath_pos_4_pos_2 = resource_path("negative_harmony_pos_4_pos_2.png")
negativeharmonybackgroundpath_pos_4_pos_3 = resource_path("negative_harmony_pos_4_pos_3.png")
negativeharmonybackgroundpath_pos_4_pos_4 = resource_path("negative_harmony_pos_4_pos_4.png")
negativeharmonybackgroundpath_pos_4_pos_5 = resource_path("negative_harmony_pos_4_pos_5.png")
negativeharmonybackgroundpath_pos_4_pos_6 = resource_path("negative_harmony_pos_4_pos_6.png")
negativeharmonybackgroundpath_pos_5 = resource_path("negative_harmony_pos_5.png")
negativeharmonybackgroundpath_pos_5_pos_1 = resource_path("negative_harmony_pos_5_pos_1.png")
negativeharmonybackgroundpath_pos_5_pos_2 = resource_path("negative_harmony_pos_5_pos_2.png")
negativeharmonybackgroundpath_pos_5_pos_3 = resource_path("negative_harmony_pos_5_pos_3.png")
negativeharmonybackgroundpath_pos_5_pos_4 = resource_path("negative_harmony_pos_5_pos_4.png")
negativeharmonybackgroundpath_pos_5_pos_5 = resource_path("negative_harmony_pos_5_pos_5.png")
negativeharmonybackgroundpath_pos_5_pos_6 = resource_path("negative_harmony_pos_5_pos_6.png")
negativeharmonybackgroundpath_pos_6 = resource_path("negative_harmony_pos_6.png")
negativeharmonybackgroundpath_pos_6_pos_1 = resource_path("negative_harmony_pos_6_pos_1.png")
negativeharmonybackgroundpath_pos_6_pos_2 = resource_path("negative_harmony_pos_6_pos_2.png")
negativeharmonybackgroundpath_pos_6_pos_3 = resource_path("negative_harmony_pos_6_pos_3.png")
negativeharmonybackgroundpath_pos_6_pos_4 = resource_path("negative_harmony_pos_6_pos_4.png")
negativeharmonybackgroundpath_pos_6_pos_5 = resource_path("negative_harmony_pos_6_pos_5.png")
negativeharmonybackgroundpath_pos_6_pos_6 = resource_path("negative_harmony_pos_6_pos_6.png")
composerbackgroundpath = resource_path("composer_background.png")
settingsbackgroundpath = resource_path("Settings.png")
fretboarddpath = resource_path("fretboard.png")
fretboardnotepath = resource_path("fretnote.png")
fretboarddpathlarge = resource_path("LargeNote.png")
fretboarddpathrootnote = resource_path("Root_Note.png")
fretboarddchordnote = resource_path("Chord_Note.png")
fretboarddpathopenlarge = resource_path("OpenFret.png")
extendedfretboardpath = resource_path("extended_fretboard.png")
submit_suggestions_background = resource_path("Submit_Suggestions.png")
support_further_development_background =  resource_path("Support_Further_Development.png")
share_your_music_background = resource_path("Share_Your_Music.png")

composer_tempo = 120

is_play_stopped = True
is_playing = False

midi_port = 0
midi_ports_list = []
midi_ports_list_index = []
midi_no_ports = ["No MIDI Port available"]

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

font_01 = ("ansi", 9)
font_01_bold = ("ansi", 10, "bold")
font_01_bold_02 = ("ansi", 11, "bold")

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

inverted_chord = None

# Circle_of_Chromatic_notes = (Note('C'), Note('G'), Note('D'), Note('A'), Note('E'), Note('B'), Note('F#'), Note('C#'), Note('G#'), Note('D#'), Note('A#'), Note('F'))
# Circle_of_Fourths_notes = (Note('C'), Note('F'), Note('A#'), Note('D#'), Note('G#'), Note('C#'), Note('F#'), Note('B'), Note('E'), Note('A'), Note('D'), Note('G'))
# Circle_of_Fifths_notes = (Note('C'), Note('G'), Note('D'), Note('A'), Note('E'), Note('B'), Note('F#'), Note('C#'), Note('G#'), Note('D#'), Note('A#'), Note('F'))

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

                  # 'Cbb4': [black_key_width * 1 - 1, black_key_height], # Bb3
                  #
                  # 'Dbb4': [black_key_width * 1 - 1, black_key_height], # B3
                  # 'Ebb4': [black_key_width * 2 + 1, black_key_height], # C4
                  # 'Gbb4': [black_key_width * 4 - 1, black_key_height], # Db4
                  # 'Abb4': [black_key_width * 5 + 1, black_key_height], # D4
                  # 'Bbb4': [black_key_width * 6 + 2, black_key_height], # Eb4
                  # 'Dbb5': [black_key_width * 8 - 1, black_key_height], # E4
                  # 'Ebb5': [black_key_width * 9 + 1, black_key_height], # Fb4
                  # 'Gbb5': [black_key_width * 11 - 2, black_key_height], # F4
                  # 'Abb5': [black_key_width * 12, black_key_height],
                  # 'Bbb5': [black_key_width * 13 + 1, black_key_height],

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