from tkinter import *
from configparser import ConfigParser
import MN_MIDI
# import MN_Scales
from MN_Scales import *
import chords_notes
import scales_notes

XY_parser = ConfigParser()
XY_parser.read('windows_2_xy.txt')

Note1_Circle_of_Notes_index_left = []
Note2_Circle_of_Notes_index_left = []
Note3_Circle_of_Notes_index_left = []
Note4_Circle_of_Notes_index_left = []
Note5_Circle_of_Notes_index_left = []
Note6_Circle_of_Notes_index_left = []
Note7_Circle_of_Notes_index_left = []

Note1_Circle_of_Notes_index_right = []
Note2_Circle_of_Notes_index_right = []
Note3_Circle_of_Notes_index_right = []
Note4_Circle_of_Notes_index_right = []
Note5_Circle_of_Notes_index_right = []
Note6_Circle_of_Notes_index_right = []
Note7_Circle_of_Notes_index_right = []

left_notes_index = []
right_notes_index = []

Note1L_LEFT = None
Note1R_LEFT = None
Note2L_LEFT = None
Note2R_LEFT = None
Note3L_LEFT = None
Note3R_LEFT = None
Note4L_LEFT = None
Note4R_LEFT = None
Note5L_LEFT = None
Note5R_LEFT = None
Note6L_LEFT = None
Note6R_LEFT = None

Note1L_RIGHT = None
Note1R_RIGHT = None
Note2L_RIGHT = None
Note2R_RIGHT = None
Note3L_RIGHT = None
Note3R_RIGHT = None
Note4L_RIGHT = None
Note4R_RIGHT = None
Note5L_RIGHT = None
Note5R_RIGHT = None
Note6L_RIGHT = None
Note6R_RIGHT = None

negative_display = None

Mode_1_Negative_Chords_Listbox_left = None
Mode1_notes_label_left = None
Mode_1_label_left = None
Mode_1_Negative_label_left = None
Mode2_notes_label_left = None
Mode_1_Chords_Listbox_left = None
Mode1_chord_notes_label_left = None
Mode2_chord_notes_label_left = None

Mode_1_Negative_Chords_Listbox_right = None
Mode1_notes_label_right = None
Mode_1_label_right = None
Mode_1_Negative_label_right = None
Mode2_notes_label_right = None
Mode_1_Chords_Listbox_right = None
Mode1_chord_notes_label_right = None
Mode2_chord_notes_label_right = None

negative_harmony_window = None
negative_harmony_background = None
negative_harmony_background_right = None

is_negative_harmony_open = False

Root_1_temp = None
Scale_1_temp = None
Root_b_temp = None
Scale_b_temp = None
User_b_scale_temp = None
Root_2_temp = None
Scale_2_temp = None

no_scale_match = False

current_selected_negative_chord_1 = None
current_selected_negative_chord_2 = None
current_selected_negative_mode_1 = None
current_selected_negative_mode_2 = None

CIRCLE_OF_NOTES_LEFT_SETTING = None
CIRCLE_OF_NOTES_RIGHT_SETTING = None

chord_ready_to_play = None

Circle_of_Notes_Rotation_Degree_left = 0
Circle_of_Notes_Rotation_Degree_right = None

go_flag = "go"

def calculateNegativeIndex(current_index, rotation_degree):

    if (rotation_degree == 0) or (rotation_degree == 6):
        if current_index == 0:
            return 1
        elif current_index == 1:
            return 0
        elif current_index == 2:
            return 11
        elif current_index == 3:
            return 10
        elif current_index == 4:
            return 9
        elif current_index == 5:
            return 8
        elif current_index == 6:
            return 7
        elif current_index ==7:
            return 6
        elif current_index == 8:
            return 5
        elif current_index == 9:
            return 4
        elif current_index == 10:
            return 3
        elif current_index == 11:
            return 2
    elif (rotation_degree == 1) or (rotation_degree == 7):
        if current_index == 0:
            return 3
        elif current_index == 1:
            return 2
        elif current_index == 2:
            return 1
        elif current_index == 3:
            return 0
        elif current_index == 4:
            return 11
        elif current_index == 5:
            return 10
        elif current_index == 6:
            return 9
        elif current_index == 7:
            return 8
        elif current_index == 8:
            return 7
        elif current_index == 9:
            return 6
        elif current_index == 10:
            return 5
        elif current_index == 11:
            return 4
    elif (rotation_degree == 2) or (rotation_degree == 8):
        if current_index == 0:
            return 5
        elif current_index == 1:
            return 4
        elif current_index == 2:
            return 3
        elif current_index == 3:
            return 2
        elif current_index == 4:
            return 1
        elif current_index == 5:
            return 0
        elif current_index == 6:
            return 11
        elif current_index ==7:
            return 10
        elif current_index == 8:
            return 9
        elif current_index == 9:
            return 8
        elif current_index == 10:
            return 7
        elif current_index == 11:
            return 6
    elif (rotation_degree == 3) or (rotation_degree == 9):
        if current_index == 0:
            return 7
        elif current_index == 1:
            return 6
        elif current_index == 2:
            return 5
        elif current_index == 3:
            return 4
        elif current_index == 4:
            return 3
        elif current_index == 5:
            return 2
        elif current_index == 6:
            return 1
        elif current_index == 7:
            return 0
        elif current_index == 8:
            return 11
        elif current_index == 9:
            return 10
        elif current_index == 10:
            return 9
        elif current_index == 11:
            return 8
    elif (rotation_degree == 4) or (rotation_degree == 10):
        if current_index == 0:
            return 9
        elif current_index == 1:
            return 8
        elif current_index == 2:
            return 7
        elif current_index == 3:
            return 6
        elif current_index == 4:
            return 5
        elif current_index == 5:
            return 4
        elif current_index == 6:
            return 3
        elif current_index == 7:
            return 2
        elif current_index == 8:
            return 1
        elif current_index == 9:
            return 0
        elif current_index == 10:
            return 11
        elif current_index == 11:
            return 10
    elif (rotation_degree == 5) or (rotation_degree == 11):
        if current_index == 0:
            return 11
        elif current_index == 1:
            return 10
        elif current_index == 2:
            return 9
        elif current_index == 3:
            return 8
        elif current_index == 4:
            return 7
        elif current_index == 5:
            return 6
        elif current_index == 6:
            return 5
        elif current_index == 7:
            return 4
        elif current_index == 8:
            return 3
        elif current_index == 9:
            return 2
        elif current_index == 10:
            return 1
        elif current_index == 11:
            return 0

def getIndex(note, label_array):
    for i in range(0, label_array.__len__()):
        index_chord = label_array[i].cget("text")
        chord = Note(index_chord)
        if note.compare(chord) == True:
            return i

def InvertedScale(list_of_inverted_notes, listbox):

    global negative_display

    try:

        if negative_display == "Determined by Negative Root Note":

            if (list_of_inverted_notes[0].compare_letter(Note("C"))):
                for k in range(0, scales_notes.c_scales.__len__()):
                    if scales_notes.c_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.c_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.c_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.c_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.c_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.c_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.c_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.c_scales[k]

            elif (list_of_inverted_notes[0].compare_letter(Note("C#"))):
                for k in range(0, scales_notes.csharp_scales.__len__()):
                    if scales_notes.csharp_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.csharp_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.csharp_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.csharp_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.csharp_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.csharp_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.csharp_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.csharp_scales[k]

            elif (list_of_inverted_notes[0].compare_letter(Note("Db"))):
                for k in range(0, scales_notes.db_scales.__len__()):
                    if scales_notes.db_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.db_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.db_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.db_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.db_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.db_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.db_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.db_scales[k]

            elif (list_of_inverted_notes[0].compare_letter(Note("D"))):
                for k in range(0, scales_notes.d_scales.__len__()):
                    if scales_notes.d_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.d_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.d_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.d_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.d_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.d_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.d_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.d_scales[k]

            elif (list_of_inverted_notes[0].compare_letter(Note("D#"))):
                for k in range(0, scales_notes.dsharp_scales.__len__()):
                    if scales_notes.dsharp_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.dsharp_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.dsharp_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.dsharp_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.dsharp_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.dsharp_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.dsharp_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.dsharp_scales[k]

            elif (list_of_inverted_notes[0].compare_letter(Note("Eb"))):
                for k in range(0, scales_notes.eb_scales.__len__()):
                    if scales_notes.eb_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.eb_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.eb_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.eb_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.eb_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.eb_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.eb_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.eb_scales[k]

            elif (list_of_inverted_notes[0].compare_letter(Note("E"))):
                for k in range(0, scales_notes.e_scales.__len__()):
                    if scales_notes.e_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.e_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.e_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.e_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.e_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.e_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.e_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.e_scales[k]

            elif (list_of_inverted_notes[0].compare_letter(Note("F"))):
                for k in range(0, scales_notes.f_scales.__len__()):
                    if scales_notes.f_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.f_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.f_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.f_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.f_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.f_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.f_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.f_scales[k]

            elif (list_of_inverted_notes[0].compare_letter(Note("F#"))):
                for k in range(0, scales_notes.fsharp_scales.__len__()):
                    if scales_notes.fsharp_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.fsharp_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.fsharp_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.fsharp_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.fsharp_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.fsharp_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.fsharp_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.fsharp_scales[k]

            elif (list_of_inverted_notes[0].compare_letter(Note("Gb"))):
                for k in range(0, scales_notes.gb_scales.__len__()):
                    if scales_notes.gb_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.gb_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.gb_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.gb_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.gb_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.gb_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.gb_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.gb_scales[k]

            elif (list_of_inverted_notes[0].compare_letter(Note("G"))):
                for k in range(0, scales_notes.g_scales.__len__()):
                    if scales_notes.g_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.g_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.g_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.g_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.g_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.g_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.g_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.g_scales[k]

            elif (list_of_inverted_notes[0].compare_letter(Note("G#"))):
                for k in range(0, scales_notes.gsharp_scales.__len__()):
                    if scales_notes.gsharp_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.gsharp_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.gsharp_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.gsharp_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.gsharp_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.gsharp_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.gsharp_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.gsharp_scales[k]

            elif (list_of_inverted_notes[0].compare_letter(Note("Ab"))):
                for k in range(0, scales_notes.ab_scales.__len__()):
                    if scales_notes.ab_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.ab_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.ab_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.ab_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.ab_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.ab_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.ab_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.ab_scales[k]

            elif (list_of_inverted_notes[0].compare_letter(Note("A"))):
                for k in range(0, scales_notes.a_scales.__len__()):
                    if scales_notes.a_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.a_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.a_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.a_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.a_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.a_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.a_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.a_scales[k]

            elif (list_of_inverted_notes[0].compare_letter(Note("A#"))):
                for k in range(0, scales_notes.asharp_scales.__len__()):
                    if scales_notes.asharp_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.asharp_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.asharp_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.asharp_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.asharp_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.asharp_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.asharp_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.asharp_scales[k]

            elif (list_of_inverted_notes[0].compare_letter(Note("Bb"))):
                for k in range(0, scales_notes.bb_scales.__len__()):
                    if scales_notes.bb_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.bb_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.bb_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.bb_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.bb_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.bb_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.bb_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.bb_scales[k]

            elif (list_of_inverted_notes[0].compare_letter(Note("B"))):
                for k in range(0, scales_notes.b_scales.__len__()):
                    if scales_notes.b_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.b_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.b_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.b_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.b_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.b_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.b_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.b_scales[k]


        elif negative_display == "Determined by Negative Chord":


            if Chord(str(listbox.get(0))).notes[0].compare_letter(Note("C")):
                for k in range(0, scales_notes.c_scales.__len__()):
                    if scales_notes.c_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.c_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.c_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.c_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.c_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.c_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.c_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.c_scales[k]
            elif Chord(str(listbox.get(0))).notes[0].compare_letter(Note("C#")):
                for k in range(0, scales_notes.csharp_scales.__len__()):
                    if scales_notes.csharp_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.csharp_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.csharp_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.csharp_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.csharp_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.csharp_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.csharp_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.csharp_scales[k]
            elif Chord(str(listbox.get(0))).notes[0].compare_letter(Note("Db")):
                for k in range(0, scales_notes.db_scales.__len__()):
                    if scales_notes.db_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.db_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.db_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.db_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.db_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.db_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.db_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.db_scales[k]
            elif Chord(str(listbox.get(0))).notes[0].compare_letter(Note("D")):
                for k in range(0, scales_notes.d_scales.__len__()):
                    if scales_notes.d_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.d_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.d_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.d_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.d_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.d_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.d_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.d_scales[k]
            elif Chord(str(listbox.get(0))).notes[0].compare_letter(Note("D#")):
                for k in range(0, scales_notes.dsharp_scales.__len__()):
                    if scales_notes.dsharp_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.dsharp_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.dsharp_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.dsharp_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.dsharp_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.dsharp_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.dsharp_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.dsharp_scales[k]
            elif Chord(str(listbox.get(0))).notes[0].compare_letter(Note("Eb")):
                for k in range(0, scales_notes.eb_scales.__len__()):
                    if scales_notes.eb_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.eb_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.eb_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.eb_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.eb_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.eb_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.eb_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.eb_scales[k]
            elif Chord(str(listbox.get(0))).notes[0].compare_letter(Note("E")):
                for k in range(0, scales_notes.e_scales.__len__()):
                    if scales_notes.e_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.e_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.e_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.e_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.e_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.e_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.e_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.e_scales[k]
            elif Chord(str(listbox.get(0))).notes[0].compare_letter(Note("F")):
                for k in range(0, scales_notes.f_scales.__len__()):
                    if scales_notes.f_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.f_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.f_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.f_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.f_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.f_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.f_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.f_scales[k]
            elif Chord(str(listbox.get(0))).notes[0].compare_letter(Note("F#")):
                for k in range(0, scales_notes.fsharp_scales.__len__()):
                    if scales_notes.fsharp_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.fsharp_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.fsharp_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.fsharp_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.fsharp_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.fsharp_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.fsharp_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.fsharp_scales[k]
            elif Chord(str(listbox.get(0))).notes[0].compare_letter(Note("Gb")):
                for k in range(0, scales_notes.gb_scales.__len__()):
                    if scales_notes.gb_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.gb_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.gb_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.gb_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.gb_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.gb_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.gb_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.gb_scales[k]
            elif Chord(str(listbox.get(0))).notes[0].compare_letter(Note("G")):
                for k in range(0, scales_notes.g_scales.__len__()):
                    if scales_notes.g_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.g_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.g_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.g_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.g_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.g_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.g_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.g_scales[k]
            elif Chord(str(listbox.get(0))).notes[0].compare_letter(Note("G#")):
                for k in range(0, scales_notes.gsharp_scales.__len__()):
                    if scales_notes.gsharp_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.gsharp_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.gsharp_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.gsharp_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.gsharp_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.gsharp_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.gsharp_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.gsharp_scales[k]
            elif Chord(str(listbox.get(0))).notes[0].compare_letter(Note("Ab")):
                for k in range(0, scales_notes.ab_scales.__len__()):
                    if scales_notes.ab_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.ab_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.ab_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.ab_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.ab_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.ab_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.ab_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.ab_scales[k]
            elif Chord(str(listbox.get(0))).notes[0].compare_letter(Note("A")):
                for k in range(0, scales_notes.a_scales.__len__()):
                    if scales_notes.a_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.a_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.a_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.a_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.a_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.a_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.a_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.a_scales[k]
            elif Chord(str(listbox.get(0))).notes[0].compare_letter(Note("A#")):
                for k in range(0, scales_notes.asharp_scales.__len__()):
                    if scales_notes.asharp_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.asharp_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.asharp_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.asharp_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.asharp_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.asharp_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.asharp_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.asharp_scales[k]
            elif Chord(str(listbox.get(0))).notes[0].compare_letter(Note("Bb")):
                for k in range(0, scales_notes.bb_scales.__len__()):
                    if scales_notes.bb_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.bb_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.bb_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.bb_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.bb_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.bb_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.bb_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.bb_scales[k]
            elif Chord(str(listbox.get(0))).notes[0].compare_letter(Note("B")):
                for k in range(0, scales_notes.b_scales.__len__()):
                    if scales_notes.b_scales[k].contains(list_of_inverted_notes[0]) and scales_notes.b_scales[k].contains(list_of_inverted_notes[1]) and scales_notes.b_scales[k].contains(list_of_inverted_notes[2]) and scales_notes.b_scales[k].contains(list_of_inverted_notes[3]) and scales_notes.b_scales[k].contains(list_of_inverted_notes[4]) and scales_notes.b_scales[k].contains(list_of_inverted_notes[5]) and scales_notes.b_scales[k].contains(list_of_inverted_notes[6]):
                        return scales_notes.b_scales[k]

    except:
        pass

def InvertedChord(list_of_inverted_notes, size):

    global go_flag

    for i in range(0, size):

        if (list_of_inverted_notes[i].compare_letter(Note("C"))):
            for k in range(0,  chords_notes.c_chords.__len__()):
                if chords_notes.c_chords[k].notes_to_chord(list_of_inverted_notes) == True:
                    return chords_notes.c_chords[k]

        elif (list_of_inverted_notes[i].compare_letter(Note("C#"))):
            for k in range(0,  chords_notes.csharp_chords.__len__()):
                if chords_notes.csharp_chords[k].notes_to_chord(list_of_inverted_notes) == True:
                    return chords_notes.csharp_chords[k]

        elif (list_of_inverted_notes[i].compare_letter(Note("Db"))):
            for k in range(0,  chords_notes.db_chords.__len__()):
                if chords_notes.db_chords[k].notes_to_chord(list_of_inverted_notes) == True:
                    return chords_notes.db_chords[k]

        elif (list_of_inverted_notes[i].compare_letter(Note("D"))):
            for k in range(0,  chords_notes.d_chords.__len__()):
                if chords_notes.d_chords[k].notes_to_chord(list_of_inverted_notes) == True:
                    return chords_notes.d_chords[k]

        elif (list_of_inverted_notes[i].compare_letter(Note("D#"))):
            for k in range(0,  chords_notes.dsharp_chords.__len__()):
                if chords_notes.dsharp_chords[k].notes_to_chord(list_of_inverted_notes) == True:
                    return chords_notes.dsharp_chords[k]

        elif (list_of_inverted_notes[i].compare_letter(Note("Eb"))):
            for k in range(0,  chords_notes.eb_chords.__len__()):
                if chords_notes.eb_chords[k].notes_to_chord(list_of_inverted_notes) == True:
                    return chords_notes.eb_chords[k]

        elif (list_of_inverted_notes[i].compare_letter(Note("E"))):
            for k in range(0,  chords_notes.e_chords.__len__()):
                if chords_notes.e_chords[k].notes_to_chord(list_of_inverted_notes) == True:
                    return chords_notes.e_chords[k]

        elif (list_of_inverted_notes[i].compare_letter(Note("F"))):
            for k in range(0,  chords_notes.f_chords.__len__()):
                if chords_notes.f_chords[k].notes_to_chord(list_of_inverted_notes) == True:
                    return chords_notes.f_chords[k]

        elif (list_of_inverted_notes[i].compare_letter(Note("F#"))):
            for k in range(0,  chords_notes.fsharp_chords.__len__()):
                if chords_notes.fsharp_chords[k].notes_to_chord(list_of_inverted_notes) == True:
                    return chords_notes.fsharp_chords[k]

        elif (list_of_inverted_notes[i].compare_letter(Note("Gb"))):
            for k in range(0,  chords_notes.gb_chords.__len__()):
                if chords_notes.gb_chords[k].notes_to_chord(list_of_inverted_notes) == True:
                    return chords_notes.gb_chords[k]

        elif (list_of_inverted_notes[i].compare_letter(Note("G"))):
            for k in range(0,  chords_notes.g_chords.__len__()):
                if chords_notes.g_chords[k].notes_to_chord(list_of_inverted_notes) == True:
                    return chords_notes.g_chords[k]

        elif (list_of_inverted_notes[i].compare_letter(Note("G#"))):
            for k in range(0,  chords_notes.gsharp_chords.__len__()):
                if chords_notes.gsharp_chords[k].notes_to_chord(list_of_inverted_notes) == True:
                    return chords_notes.gsharp_chords[k]

        elif (list_of_inverted_notes[i].compare_letter(Note("Ab"))):
            for k in range(0,  chords_notes.ab_chords.__len__()):
                if chords_notes.ab_chords[k].notes_to_chord(list_of_inverted_notes) == True:
                    return chords_notes.ab_chords[k]

        elif (list_of_inverted_notes[i].compare_letter(Note("A"))):
            for k in range(0,  chords_notes.a_chords.__len__()):
                if chords_notes.a_chords[k].notes_to_chord(list_of_inverted_notes) == True:
                    return chords_notes.a_chords[k]

        elif (list_of_inverted_notes[i].compare_letter(Note("A#"))):
            for k in range(0,  chords_notes.asharp_chords.__len__()):
                if chords_notes.asharp_chords[k].notes_to_chord(list_of_inverted_notes) == True:
                    return chords_notes.asharp_chords[k]

        elif (list_of_inverted_notes[i].compare_letter(Note("Bb"))):
            for k in range(0,  chords_notes.bb_chords.__len__()):
                if chords_notes.bb_chords[k].notes_to_chord(list_of_inverted_notes) == True:
                    return chords_notes.bb_chords[k]

        elif (list_of_inverted_notes[i].compare_letter(Note("B"))):
            for k in range(0,  chords_notes.b_chords.__len__()):
                if chords_notes.b_chords[k].notes_to_chord(list_of_inverted_notes) == True:
                    return chords_notes.b_chords[k]

    go_flag = "no go"

def Listbox_Select(Number1, Number2, Mode_Negative_Chords_Listbox, Mode_Chords_Listbox, Mode_1_chord_notes_label, Mode_2_chord_notes_label, listbox_color,  darkgrey, font_01):

    global current_selected_negative_chord_1, current_selected_negative_chord_2, current_selected_negative_mode_1, current_selected_negative_mode_2, chord_ready_to_play

    if Number2 == 1:
        cursel = Mode_Chords_Listbox.curselection()
        chord_ready_to_play = Mode_Chords_Listbox.get(cursel)
        print(str(chord_ready_to_play))
    elif Number2 == 2:
        cursel = Mode_Negative_Chords_Listbox.curselection()
        if Mode_Negative_Chords_Listbox.get(cursel) != "-":
            chord_ready_to_play = Mode_Negative_Chords_Listbox.get(cursel)
            print(str(chord_ready_to_play))
        else:
            chord_ready_to_play = None


    Mode_Chords_Listbox.selection_clear(0, END)
    Mode_Negative_Chords_Listbox.selection_clear(0, END)

    Mode_Negative_Chords_Listbox.selection_set(cursel)
    Mode_Chords_Listbox.selection_set(cursel)


    if Number2 == 1:
        ANC = update_chord_labels(Number2, Mode_Chords_Listbox, Mode_1_chord_notes_label, listbox_color, font_01, darkgrey)
        update_chord_labels_without_anchor(Number2, Mode_Negative_Chords_Listbox, ANC, Mode_2_chord_notes_label, darkgrey, font_01, listbox_color)
    elif Number2 == 2:
        ANC = update_chord_labels(Number2, Mode_Negative_Chords_Listbox, Mode_2_chord_notes_label, listbox_color, font_01, darkgrey)
        update_chord_labels_without_anchor(Number2, Mode_Chords_Listbox, ANC, Mode_1_chord_notes_label, darkgrey, font_01, listbox_color)

    if Number1 == 1 :
        current_selected_negative_chord_1 = Mode_Negative_Chords_Listbox.get(cursel)
    elif Number1 == 2:
        current_selected_negative_chord_2 = Mode_1_Negative_Chords_Listbox_right.get(cursel)

def compare_notes_to_circle(number, Scale_2_None, root, scale, greencolor, redcolor, UserScale, negativeharmonybackgroundfile_pos_1, negativeharmonybackgroundfile_pos_2, negativeharmonybackgroundfile_pos_3, negativeharmonybackgroundfile_pos_4, negativeharmonybackgroundfile_pos_5, negativeharmonybackgroundfile_pos_6, negativeharmonybackgroundfile_pos_1_pos_1, negativeharmonybackgroundfile_pos_1_pos_2, negativeharmonybackgroundfile_pos_1_pos_3, negativeharmonybackgroundfile_pos_1_pos_4, negativeharmonybackgroundfile_pos_1_pos_5, negativeharmonybackgroundfile_pos_1_pos_6, negativeharmonybackgroundfile_pos_2_pos_1, negativeharmonybackgroundfile_pos_2_pos_2, negativeharmonybackgroundfile_pos_2_pos_3, negativeharmonybackgroundfile_pos_2_pos_4, negativeharmonybackgroundfile_pos_2_pos_5, negativeharmonybackgroundfile_pos_2_pos_6, negativeharmonybackgroundfile_pos_3_pos_1, negativeharmonybackgroundfile_pos_3_pos_2, negativeharmonybackgroundfile_pos_3_pos_3, negativeharmonybackgroundfile_pos_3_pos_4, negativeharmonybackgroundfile_pos_3_pos_5, negativeharmonybackgroundfile_pos_3_pos_6, negativeharmonybackgroundfile_pos_4_pos_1, negativeharmonybackgroundfile_pos_4_pos_2, negativeharmonybackgroundfile_pos_4_pos_3, negativeharmonybackgroundfile_pos_4_pos_4, negativeharmonybackgroundfile_pos_4_pos_5, negativeharmonybackgroundfile_pos_4_pos_6, negativeharmonybackgroundfile_pos_5_pos_1, negativeharmonybackgroundfile_pos_5_pos_2, negativeharmonybackgroundfile_pos_5_pos_3, negativeharmonybackgroundfile_pos_5_pos_4, negativeharmonybackgroundfile_pos_5_pos_5, negativeharmonybackgroundfile_pos_5_pos_6, negativeharmonybackgroundfile_pos_6_pos_1, negativeharmonybackgroundfile_pos_6_pos_2, negativeharmonybackgroundfile_pos_6_pos_3, negativeharmonybackgroundfile_pos_6_pos_4, negativeharmonybackgroundfile_pos_6_pos_5, negativeharmonybackgroundfile_pos_6_pos_6):

    # This function receives a Note + Scale and then goes through the Circle (number 1 or number 2) comparing notes.
    # First, it determines the location of the root. When it finds, it paints it green.
    # Then, it determines the degree

    global Note1_Circle_of_Notes_index_left, Note1_Circle_of_Notes_index_right
    global Note2_Circle_of_Notes_index_left, Note2_Circle_of_Notes_index_right
    global Note3_Circle_of_Notes_index_left, Note3_Circle_of_Notes_index_right
    global Note4_Circle_of_Notes_index_left, Note4_Circle_of_Notes_index_right
    global Note5_Circle_of_Notes_index_left, Note5_Circle_of_Notes_index_right
    global Note6_Circle_of_Notes_index_left, Note6_Circle_of_Notes_index_right
    global Note7_Circle_of_Notes_index_left, Note7_Circle_of_Notes_index_right
    global Circle_of_Notes_Rotation_Degree_left, Circle_of_Notes_Rotation_Degree_right
    global Note1L_LEFT, Note1L_RIGHT
    global left_notes_index, right_notes_index
    global negative_harmony_background

    global Root_2_temp, Scale_2_temp

    Root_2_temp = root
    Scale_2_temp = scale

    root_1_found = False

    if (root != None and scale != None):
        for n in range(0, 12):
            skip = False
            if number == 1:
                label_note = left_notes_index[n]
            elif number == 2:
                label_note = right_notes_index[n]
            text_note = label_note.cget("text")
            note = Note(text_note)
            if Note(root).compare(note) and root_1_found == False:
                if number == 1:
                    left_notes_index[n].config(bg=(greencolor))
                    Circle_of_Notes_Rotation_Degree_left = n
                    Note1_Circle_of_Notes_index_left = [Note(root), n]
                    # left_notes_index[n].update()
                elif number == 2:
                    right_notes_index[n].config(bg=(greencolor))
                    Circle_of_Notes_Rotation_Degree_right = n
                    Note1_Circle_of_Notes_index_right = [Note(root), n]
                root_1_found = True
                skip = True

                if Scale_2_None == False:

                    # if (Circle_of_Notes_Rotation_Degree_left == 0 or Circle_of_Notes_Rotation_Degree_left == 6) and (Root_2_temp == None or Scale_2_temp == None):
                    if (Circle_of_Notes_Rotation_Degree_left == 0 or Circle_of_Notes_Rotation_Degree_left == 6) and Circle_of_Notes_Rotation_Degree_right == None:
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_1)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)

                    # elif (Circle_of_Notes_Rotation_Degree_left == 1 or Circle_of_Notes_Rotation_Degree_left == 7) and (Root_2_temp == None or Scale_2_temp == None):
                    elif (Circle_of_Notes_Rotation_Degree_left == 1 or Circle_of_Notes_Rotation_Degree_left == 7) and Circle_of_Notes_Rotation_Degree_right == None:
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_2)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)

                    # elif (Circle_of_Notes_Rotation_Degree_left == 2 or Circle_of_Notes_Rotation_Degree_left == 8) and (Root_2_temp == None or Scale_2_temp == None):
                    elif (Circle_of_Notes_Rotation_Degree_left == 2 or Circle_of_Notes_Rotation_Degree_left == 8) and Circle_of_Notes_Rotation_Degree_right == None:
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_3)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)

                    # elif (Circle_of_Notes_Rotation_Degree_left == 3 or Circle_of_Notes_Rotation_Degree_left == 9) and (Root_2_temp == None or Scale_2_temp == None):
                    elif (Circle_of_Notes_Rotation_Degree_left == 3 or Circle_of_Notes_Rotation_Degree_left == 9) and Circle_of_Notes_Rotation_Degree_right == None:
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_4)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)

                    # elif (Circle_of_Notes_Rotation_Degree_left == 4 or Circle_of_Notes_Rotation_Degree_left == 10) and (Root_2_temp == None or Scale_2_temp == None):
                    elif (Circle_of_Notes_Rotation_Degree_left == 4 or Circle_of_Notes_Rotation_Degree_left == 10) and Circle_of_Notes_Rotation_Degree_right == None:
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_5)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)


                    # elif (Circle_of_Notes_Rotation_Degree_left == 5 or Circle_of_Notes_Rotation_Degree_left == 11) and (Root_2_temp == None or Scale_2_temp == None):
                    elif (Circle_of_Notes_Rotation_Degree_left == 5 or Circle_of_Notes_Rotation_Degree_left == 11) and Circle_of_Notes_Rotation_Degree_right == None:
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_6)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)

                    elif (Circle_of_Notes_Rotation_Degree_left == 0 or Circle_of_Notes_Rotation_Degree_left == 6) and (Circle_of_Notes_Rotation_Degree_right == 0 or Circle_of_Notes_Rotation_Degree_right == 6) :
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_1_pos_1)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)
                    elif (Circle_of_Notes_Rotation_Degree_left == 0 or Circle_of_Notes_Rotation_Degree_left == 6) and (Circle_of_Notes_Rotation_Degree_right == 1 or Circle_of_Notes_Rotation_Degree_right == 7):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_1_pos_2)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)
                    elif (Circle_of_Notes_Rotation_Degree_left == 0 or Circle_of_Notes_Rotation_Degree_left == 6) and (Circle_of_Notes_Rotation_Degree_right == 2 or Circle_of_Notes_Rotation_Degree_right == 8):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_1_pos_3)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)
                    elif (Circle_of_Notes_Rotation_Degree_left == 0 or Circle_of_Notes_Rotation_Degree_left == 6) and (Circle_of_Notes_Rotation_Degree_right == 3 or Circle_of_Notes_Rotation_Degree_right == 9):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_1_pos_4)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)
                    elif (Circle_of_Notes_Rotation_Degree_left == 0 or Circle_of_Notes_Rotation_Degree_left == 6) and (Circle_of_Notes_Rotation_Degree_right == 4 or Circle_of_Notes_Rotation_Degree_right == 10):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_1_pos_5)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)
                    elif (Circle_of_Notes_Rotation_Degree_left == 0 or Circle_of_Notes_Rotation_Degree_left == 6) and (Circle_of_Notes_Rotation_Degree_right == 5 or Circle_of_Notes_Rotation_Degree_right == 11):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_1_pos_6)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)

                    elif (Circle_of_Notes_Rotation_Degree_left == 1 or Circle_of_Notes_Rotation_Degree_left == 7) and (Circle_of_Notes_Rotation_Degree_right == 0 or Circle_of_Notes_Rotation_Degree_right == 6):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_2_pos_1)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)
                    elif (Circle_of_Notes_Rotation_Degree_left == 1 or Circle_of_Notes_Rotation_Degree_left == 7) and (Circle_of_Notes_Rotation_Degree_right == 1 or Circle_of_Notes_Rotation_Degree_right == 7):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_2_pos_2)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)
                    elif (Circle_of_Notes_Rotation_Degree_left == 1 or Circle_of_Notes_Rotation_Degree_left == 7) and (Circle_of_Notes_Rotation_Degree_right == 2 or Circle_of_Notes_Rotation_Degree_right == 8):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_2_pos_3)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)
                    elif (Circle_of_Notes_Rotation_Degree_left == 1 or Circle_of_Notes_Rotation_Degree_left == 7) and (Circle_of_Notes_Rotation_Degree_right == 3 or Circle_of_Notes_Rotation_Degree_right == 9):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_2_pos_4)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)
                    elif (Circle_of_Notes_Rotation_Degree_left == 1 or Circle_of_Notes_Rotation_Degree_left == 7) and (Circle_of_Notes_Rotation_Degree_right == 4 or Circle_of_Notes_Rotation_Degree_right == 10):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_2_pos_5)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)
                    elif (Circle_of_Notes_Rotation_Degree_left == 1 or Circle_of_Notes_Rotation_Degree_left == 7) and (Circle_of_Notes_Rotation_Degree_right == 5 or Circle_of_Notes_Rotation_Degree_right == 11):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_2_pos_6)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)

                    elif (Circle_of_Notes_Rotation_Degree_left == 2 or Circle_of_Notes_Rotation_Degree_left == 8) and (Circle_of_Notes_Rotation_Degree_right == 0 or Circle_of_Notes_Rotation_Degree_right == 6):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_3_pos_1)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)
                    elif (Circle_of_Notes_Rotation_Degree_left == 2 or Circle_of_Notes_Rotation_Degree_left == 8) and (Circle_of_Notes_Rotation_Degree_right == 1 or Circle_of_Notes_Rotation_Degree_right == 7):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_3_pos_2)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)
                    elif (Circle_of_Notes_Rotation_Degree_left == 2 or Circle_of_Notes_Rotation_Degree_left == 8) and (Circle_of_Notes_Rotation_Degree_right == 2 or Circle_of_Notes_Rotation_Degree_right == 8):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_3_pos_3)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)
                    elif (Circle_of_Notes_Rotation_Degree_left == 2 or Circle_of_Notes_Rotation_Degree_left == 8) and (Circle_of_Notes_Rotation_Degree_right == 3 or Circle_of_Notes_Rotation_Degree_right == 9):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_3_pos_4)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)
                    elif (Circle_of_Notes_Rotation_Degree_left == 2 or Circle_of_Notes_Rotation_Degree_left == 8) and (Circle_of_Notes_Rotation_Degree_right == 4 or Circle_of_Notes_Rotation_Degree_right == 10):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_3_pos_5)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)
                    elif (Circle_of_Notes_Rotation_Degree_left == 2 or Circle_of_Notes_Rotation_Degree_left == 8) and (Circle_of_Notes_Rotation_Degree_right == 5 or Circle_of_Notes_Rotation_Degree_right == 11):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_3_pos_6)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)

                    elif (Circle_of_Notes_Rotation_Degree_left == 3 or Circle_of_Notes_Rotation_Degree_left == 9) and (Circle_of_Notes_Rotation_Degree_right == 0 or Circle_of_Notes_Rotation_Degree_right == 6):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_4_pos_1)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)
                    elif (Circle_of_Notes_Rotation_Degree_left == 3 or Circle_of_Notes_Rotation_Degree_left == 9) and (Circle_of_Notes_Rotation_Degree_right == 1 or Circle_of_Notes_Rotation_Degree_right == 7):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_4_pos_2)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)
                    elif (Circle_of_Notes_Rotation_Degree_left == 3 or Circle_of_Notes_Rotation_Degree_left == 9) and (Circle_of_Notes_Rotation_Degree_right == 2 or Circle_of_Notes_Rotation_Degree_right == 8):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_4_pos_3)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)
                    elif (Circle_of_Notes_Rotation_Degree_left == 3 or Circle_of_Notes_Rotation_Degree_left == 9) and (Circle_of_Notes_Rotation_Degree_right == 3 or Circle_of_Notes_Rotation_Degree_right == 9):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_4_pos_4)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)
                    elif (Circle_of_Notes_Rotation_Degree_left == 3 or Circle_of_Notes_Rotation_Degree_left == 9) and (Circle_of_Notes_Rotation_Degree_right == 4 or Circle_of_Notes_Rotation_Degree_right == 10):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_4_pos_5)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)
                    elif (Circle_of_Notes_Rotation_Degree_left == 3 or Circle_of_Notes_Rotation_Degree_left == 9) and (Circle_of_Notes_Rotation_Degree_right == 5 or Circle_of_Notes_Rotation_Degree_right == 11):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_4_pos_6)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)

                    elif (Circle_of_Notes_Rotation_Degree_left == 4 or Circle_of_Notes_Rotation_Degree_left == 10) and (Circle_of_Notes_Rotation_Degree_right == 0 or Circle_of_Notes_Rotation_Degree_right == 6):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_5_pos_1)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)
                    elif (Circle_of_Notes_Rotation_Degree_left == 4 or Circle_of_Notes_Rotation_Degree_left == 10) and (Circle_of_Notes_Rotation_Degree_right == 1 or Circle_of_Notes_Rotation_Degree_right == 7):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_5_pos_2)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)
                    elif (Circle_of_Notes_Rotation_Degree_left == 4 or Circle_of_Notes_Rotation_Degree_left == 10) and (Circle_of_Notes_Rotation_Degree_right == 2 or Circle_of_Notes_Rotation_Degree_right == 8):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_5_pos_3)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)
                    elif (Circle_of_Notes_Rotation_Degree_left == 4 or Circle_of_Notes_Rotation_Degree_left == 10) and (Circle_of_Notes_Rotation_Degree_right == 3 or Circle_of_Notes_Rotation_Degree_right == 9):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_5_pos_4)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)
                    elif (Circle_of_Notes_Rotation_Degree_left == 4 or Circle_of_Notes_Rotation_Degree_left == 10) and (Circle_of_Notes_Rotation_Degree_right == 4 or Circle_of_Notes_Rotation_Degree_right == 10):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_5_pos_5)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)
                    elif (Circle_of_Notes_Rotation_Degree_left == 4 or Circle_of_Notes_Rotation_Degree_left == 10) and (Circle_of_Notes_Rotation_Degree_right == 5 or Circle_of_Notes_Rotation_Degree_right == 11):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_5_pos_6)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)

                    elif (Circle_of_Notes_Rotation_Degree_left == 5 or Circle_of_Notes_Rotation_Degree_left == 11) and (Circle_of_Notes_Rotation_Degree_right == 0 or Circle_of_Notes_Rotation_Degree_right == 6):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_6_pos_1)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)
                    elif (Circle_of_Notes_Rotation_Degree_left == 5 or Circle_of_Notes_Rotation_Degree_left == 11) and (Circle_of_Notes_Rotation_Degree_right == 1 or Circle_of_Notes_Rotation_Degree_right == 7):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_6_pos_2)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)
                    elif (Circle_of_Notes_Rotation_Degree_left == 5 or Circle_of_Notes_Rotation_Degree_left == 11) and (Circle_of_Notes_Rotation_Degree_right == 2 or Circle_of_Notes_Rotation_Degree_right == 8):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_6_pos_3)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)
                    elif (Circle_of_Notes_Rotation_Degree_left == 5 or Circle_of_Notes_Rotation_Degree_left == 11) and (Circle_of_Notes_Rotation_Degree_right == 3 or Circle_of_Notes_Rotation_Degree_right == 9):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_6_pos_4)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)
                    elif (Circle_of_Notes_Rotation_Degree_left == 5 or Circle_of_Notes_Rotation_Degree_left == 11) and (Circle_of_Notes_Rotation_Degree_right == 4 or Circle_of_Notes_Rotation_Degree_right == 10):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_6_pos_5)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)
                    elif (Circle_of_Notes_Rotation_Degree_left == 5 or Circle_of_Notes_Rotation_Degree_left == 11) and (Circle_of_Notes_Rotation_Degree_right == 5 or Circle_of_Notes_Rotation_Degree_right == 11):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_6_pos_6)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)

                elif Scale_2_None == True:
                    if (Circle_of_Notes_Rotation_Degree_left == 0 or Circle_of_Notes_Rotation_Degree_left == 6):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_1)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)

                    elif (Circle_of_Notes_Rotation_Degree_left == 1 or Circle_of_Notes_Rotation_Degree_left == 7):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_2)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)

                    elif (Circle_of_Notes_Rotation_Degree_left == 2 or Circle_of_Notes_Rotation_Degree_left == 8):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_3)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)

                    elif (Circle_of_Notes_Rotation_Degree_left == 3 or Circle_of_Notes_Rotation_Degree_left == 9):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_4)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)

                    elif (Circle_of_Notes_Rotation_Degree_left == 4 or Circle_of_Notes_Rotation_Degree_left == 10):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_5)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)

                    elif (Circle_of_Notes_Rotation_Degree_left == 5 or Circle_of_Notes_Rotation_Degree_left == 11):
                        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_6)
                        negative_harmony_background.place(x=-1, y=0)
                        negative_harmony_background.lower(Note1L_LEFT)


            if skip == False:
                for sn in range(1, 7):
                    if UserScale[sn].compare(note):
                        if number == 1:
                            left_notes_index[n].config(bg=(redcolor))
                        elif number == 2:
                            right_notes_index[n].config(bg=(redcolor))
                        if sn == 1:
                            if number == 1:
                                Note2_Circle_of_Notes_index_left = [note, 1]
                            elif number == 2:
                                Note2_Circle_of_Notes_index_right = [note, 1]
                        elif sn == 2:
                            if number == 1:
                                Note3_Circle_of_Notes_index_left = [note, 2]
                            elif number == 2:
                                Note3_Circle_of_Notes_index_right = [note, 2]
                        elif sn == 3:
                            if number == 1:
                                Note4_Circle_of_Notes_index_left = [note, 3]
                            elif number == 2:
                                Note4_Circle_of_Notes_index_right = [note, 3]
                        elif sn == 4:
                            if number == 1:
                                Note5_Circle_of_Notes_index_left = [note, 4]
                            elif number == 2:
                                Note5_Circle_of_Notes_index_right = [note, 4]
                        elif sn == 5:
                            if number == 1:
                                Note6_Circle_of_Notes_index_left = [note, 5]
                            elif number == 2:
                                Note6_Circle_of_Notes_index_right = [note, 5]
                        elif sn == 6:
                            if number == 1:
                                Note7_Circle_of_Notes_index_left = [note, 6]
                            elif number == 2:
                                Note7_Circle_of_Notes_index_right = [note, 6]

def process_circle_of_notes(number, CIRCLE_OF_NOTES_SETTING, FLAT_SETTING, Scale_2_None, Root_in, Scale_in, UserScale, redcolor, greencolor, negativeharmonybackgroundfile_pos_1, negativeharmonybackgroundfile_pos_2, negativeharmonybackgroundfile_pos_3, negativeharmonybackgroundfile_pos_4, negativeharmonybackgroundfile_pos_5, negativeharmonybackgroundfile_pos_6, negative_harmony_background_left_original, negativeharmonybackgroundfile_pos_1_pos_1, negativeharmonybackgroundfile_pos_1_pos_2, negativeharmonybackgroundfile_pos_1_pos_3, negativeharmonybackgroundfile_pos_1_pos_4, negativeharmonybackgroundfile_pos_1_pos_5, negativeharmonybackgroundfile_pos_1_pos_6, negativeharmonybackgroundfile_pos_2_pos_1, negativeharmonybackgroundfile_pos_2_pos_2, negativeharmonybackgroundfile_pos_2_pos_3, negativeharmonybackgroundfile_pos_2_pos_4, negativeharmonybackgroundfile_pos_2_pos_5, negativeharmonybackgroundfile_pos_2_pos_6, negativeharmonybackgroundfile_pos_3_pos_1, negativeharmonybackgroundfile_pos_3_pos_2, negativeharmonybackgroundfile_pos_3_pos_3, negativeharmonybackgroundfile_pos_3_pos_4, negativeharmonybackgroundfile_pos_3_pos_5, negativeharmonybackgroundfile_pos_3_pos_6, negativeharmonybackgroundfile_pos_4_pos_1, negativeharmonybackgroundfile_pos_4_pos_2, negativeharmonybackgroundfile_pos_4_pos_3, negativeharmonybackgroundfile_pos_4_pos_4, negativeharmonybackgroundfile_pos_4_pos_5, negativeharmonybackgroundfile_pos_4_pos_6, negativeharmonybackgroundfile_pos_5_pos_1, negativeharmonybackgroundfile_pos_5_pos_2, negativeharmonybackgroundfile_pos_5_pos_3, negativeharmonybackgroundfile_pos_5_pos_4, negativeharmonybackgroundfile_pos_5_pos_5, negativeharmonybackgroundfile_pos_5_pos_6, negativeharmonybackgroundfile_pos_6_pos_1, negativeharmonybackgroundfile_pos_6_pos_2, negativeharmonybackgroundfile_pos_6_pos_3, negativeharmonybackgroundfile_pos_6_pos_4, negativeharmonybackgroundfile_pos_6_pos_5, negativeharmonybackgroundfile_pos_6_pos_6):

    global Note1_Circle_of_Notes_index_left, Note1_Circle_of_Notes_index_right
    global Note2_Circle_of_Notes_index_left, Note2_Circle_of_Notes_index_right
    global Note3_Circle_of_Notes_index_left, Note3_Circle_of_Notes_index_right
    global Note4_Circle_of_Notes_index_left, Note4_Circle_of_Notes_index_right
    global Note5_Circle_of_Notes_index_left, Note5_Circle_of_Notes_index_right
    global Note6_Circle_of_Notes_index_left, Note6_Circle_of_Notes_index_right
    global Note7_Circle_of_Notes_index_left, Note7_Circle_of_Notes_index_right

    global left_notes_index, right_notes_index

    global Circle_of_Notes_Rotation_Degree_left, Circle_of_Notes_Rotation_Degree_right

    global Note1L_LEFT, Note1R_LEFT, Note2L_LEFT, Note2R_LEFT, Note3L_LEFT, Note3R_LEFT, Note4L_LEFT, Note4R_LEFT, Note5L_LEFT, Note5R_LEFT, Note6L_LEFT, Note6R_LEFT
    global Note1L_RIGHT, Note1R_RIGHT, Note2L_RIGHT, Note2R_RIGHT, Note3L_RIGHT, Note3R_RIGHT, Note4L_RIGHT, Note4R_RIGHT, Note5L_RIGHT, Note5R_RIGHT, Note6L_RIGHT, Note6R_RIGHT

    if CIRCLE_OF_NOTES_SETTING == "Circle of Fifths":
        if number == 1:
            Note1L_LEFT.config(text="C")
            Note1R_LEFT.config(text="G")
            Note2L_LEFT.config(text="F")
            Note2R_LEFT.config(text="D")
        elif number == 2:
            Note1L_RIGHT.config(text="C")
            Note1R_RIGHT.config(text="G")
            Note2L_RIGHT.config(text="F")
            Note2R_RIGHT.config(text="D")

        if FLAT_SETTING == 0:
            if number == 1:
                Note3L_LEFT.config(text="A#")
            elif number == 2:
                Note3L_RIGHT.config(text="A#")
        else:
            if number == 1:
                Note3L_LEFT.config(text="Bb")
            elif number == 2:
                Note3L_RIGHT.config(text="Bb")

        if number == 1:
            Note3R_LEFT.config(text="A")
        elif number == 2:
            Note3R_RIGHT.config(text="A")


        if FLAT_SETTING == 0:
            if number == 1:
                Note4L_LEFT.config(text="D#")
            elif number == 2:
                Note4L_RIGHT.config(text="D#")
        else:
            if number == 1:
                Note4L_LEFT.config(text="Eb")
            elif number == 2:
                Note4L_RIGHT.config(text="Eb")


        if number == 1:
            Note4R_LEFT.config(text="E")
        elif number == 2:
            Note4R_RIGHT.config(text="E")


        if FLAT_SETTING == 0:
            if number == 1:
                Note5L_LEFT.config(text="G#")
            elif number == 2:
                Note5L_RIGHT.config(text="G#")
        else:
            if number == 1:
                Note5L_LEFT.config(text="Ab")
            elif number == 2:
                Note5L_RIGHT.config(text="Ab")


        if number == 1:
            Note5R_LEFT.config(text="B")
        elif number == 2:
            Note5R_RIGHT.config(text="B")

        if FLAT_SETTING == 0:
            if number == 1:
                Note6L_LEFT.config(text="C#")
            elif number == 2:
                Note6L_RIGHT.config(text="C#")

        else:
            if number == 1:
                Note6L_LEFT.config(text="Db")
            elif number == 2:
                Note6L_RIGHT.config(text="Db")

        if FLAT_SETTING == 0:
            if number == 1:
                Note6R_LEFT.config(text="F#")
            elif number == 2:
                Note6R_RIGHT.config(text="F#")
        else:
            if number == 1:
                Note6R_LEFT.config(text="Gb")
            elif number == 2:
                Note6R_RIGHT.config(text="Gb")



        compare_notes_to_circle(number, Scale_2_None, Root_in, Scale_in, greencolor, redcolor, UserScale, negativeharmonybackgroundfile_pos_1, negativeharmonybackgroundfile_pos_2, negativeharmonybackgroundfile_pos_3, negativeharmonybackgroundfile_pos_4, negativeharmonybackgroundfile_pos_5, negativeharmonybackgroundfile_pos_6, negativeharmonybackgroundfile_pos_1_pos_1, negativeharmonybackgroundfile_pos_1_pos_2, negativeharmonybackgroundfile_pos_1_pos_3, negativeharmonybackgroundfile_pos_1_pos_4, negativeharmonybackgroundfile_pos_1_pos_5, negativeharmonybackgroundfile_pos_1_pos_6, negativeharmonybackgroundfile_pos_2_pos_1, negativeharmonybackgroundfile_pos_2_pos_2, negativeharmonybackgroundfile_pos_2_pos_3, negativeharmonybackgroundfile_pos_2_pos_4, negativeharmonybackgroundfile_pos_2_pos_5, negativeharmonybackgroundfile_pos_2_pos_6, negativeharmonybackgroundfile_pos_3_pos_1, negativeharmonybackgroundfile_pos_3_pos_2, negativeharmonybackgroundfile_pos_3_pos_3, negativeharmonybackgroundfile_pos_3_pos_4, negativeharmonybackgroundfile_pos_3_pos_5, negativeharmonybackgroundfile_pos_3_pos_6, negativeharmonybackgroundfile_pos_4_pos_1, negativeharmonybackgroundfile_pos_4_pos_2, negativeharmonybackgroundfile_pos_4_pos_3, negativeharmonybackgroundfile_pos_4_pos_4, negativeharmonybackgroundfile_pos_4_pos_5, negativeharmonybackgroundfile_pos_4_pos_6, negativeharmonybackgroundfile_pos_5_pos_1, negativeharmonybackgroundfile_pos_5_pos_2, negativeharmonybackgroundfile_pos_5_pos_3, negativeharmonybackgroundfile_pos_5_pos_4, negativeharmonybackgroundfile_pos_5_pos_5, negativeharmonybackgroundfile_pos_5_pos_6, negativeharmonybackgroundfile_pos_6_pos_1, negativeharmonybackgroundfile_pos_6_pos_2, negativeharmonybackgroundfile_pos_6_pos_3, negativeharmonybackgroundfile_pos_6_pos_4, negativeharmonybackgroundfile_pos_6_pos_5, negativeharmonybackgroundfile_pos_6_pos_6)

    elif CIRCLE_OF_NOTES_SETTING == "Circle of Fourths":

        if number == 1:
            Note1L_LEFT.config(text="C")
            Note1R_LEFT.config(text="F")
            Note2L_LEFT.config(text="G")
        elif number == 2:
            Note1L_RIGHT.config(text="C")
            Note1R_RIGHT.config(text="F")
            Note2L_RIGHT.config(text="G")

        if FLAT_SETTING == 0:
            if number == 1:
                Note2R_LEFT.config(text="A#")
            elif number == 2:
                Note2R_RIGHT.config(text="A#")
        else:
            if number == 1:
                Note2R_LEFT.config(text="Bb")
            elif number == 2:
                Note2R_RIGHT.config(text="Bb")

        if number == 1:
            Note3L_LEFT.config(text="D")
        elif number ==2:
            Note3L_RIGHT.config(text="D")

        if FLAT_SETTING == 0:
            if number == 1:
                Note3R_LEFT.config(text="D#")
            elif number == 2:
                Note3R_RIGHT.config(text="D#")
        else:
            if number == 1:
                Note3R_LEFT.config(text="Eb")
            elif number == 2:
                Note3R_RIGHT.config(text="Eb")

        if number == 1:
            Note4L_LEFT.config(text="A")
        elif number == 2:
            Note4L_RIGHT.config(text="A")

        if FLAT_SETTING == 0:
            if number == 1:
                Note4R_LEFT.config(text="G#")
            elif number == 2:
                Note4R_RIGHT.config(text="G#")
        else:
            if number == 1:
                Note4R_LEFT.config(text="Ab")
            elif number == 2:
                Note4R_RIGHT.config(text="Ab")

        if number == 1:
            Note5L_LEFT.config(text="E")
        elif number == 2:
            Note5L_RIGHT.config(text="E")

        if FLAT_SETTING == 0:
            if number == 1:
                Note5R_LEFT.config(text="C#")
            elif number == 2:
                Note5R_RIGHT.config(text="C#")
        else:
            if number == 1:
                Note5R_LEFT.config(text="Db")
            elif number == 2:
                Note5R_RIGHT.config(text="Db")

        if number == 1:
            Note6L_LEFT.config(text="B")
        elif number == 2:
            Note6L_RIGHT.config(text="B")

        if FLAT_SETTING == 0:
            if number == 1:
                Note6R_LEFT.config(text="F#")
            elif number == 2:
                Note6R_RIGHT.config(text="F#")
        else:
            if number == 1:
                Note6R_LEFT.config(text="Gb")
            elif number == 2:
                Note6R_RIGHT.config(text="Gb")

        compare_notes_to_circle(number, Scale_2_None, Root_in, Scale_in, greencolor, redcolor, UserScale, negativeharmonybackgroundfile_pos_1, negativeharmonybackgroundfile_pos_2, negativeharmonybackgroundfile_pos_3, negativeharmonybackgroundfile_pos_4, negativeharmonybackgroundfile_pos_5, negativeharmonybackgroundfile_pos_6, negativeharmonybackgroundfile_pos_1_pos_1, negativeharmonybackgroundfile_pos_1_pos_2, negativeharmonybackgroundfile_pos_1_pos_3, negativeharmonybackgroundfile_pos_1_pos_4, negativeharmonybackgroundfile_pos_1_pos_5, negativeharmonybackgroundfile_pos_1_pos_6, negativeharmonybackgroundfile_pos_2_pos_1, negativeharmonybackgroundfile_pos_2_pos_2, negativeharmonybackgroundfile_pos_2_pos_3, negativeharmonybackgroundfile_pos_2_pos_4, negativeharmonybackgroundfile_pos_2_pos_5, negativeharmonybackgroundfile_pos_2_pos_6, negativeharmonybackgroundfile_pos_3_pos_1, negativeharmonybackgroundfile_pos_3_pos_2, negativeharmonybackgroundfile_pos_3_pos_3, negativeharmonybackgroundfile_pos_3_pos_4, negativeharmonybackgroundfile_pos_3_pos_5, negativeharmonybackgroundfile_pos_3_pos_6, negativeharmonybackgroundfile_pos_4_pos_1, negativeharmonybackgroundfile_pos_4_pos_2, negativeharmonybackgroundfile_pos_4_pos_3, negativeharmonybackgroundfile_pos_4_pos_4, negativeharmonybackgroundfile_pos_4_pos_5, negativeharmonybackgroundfile_pos_4_pos_6, negativeharmonybackgroundfile_pos_5_pos_1, negativeharmonybackgroundfile_pos_5_pos_2, negativeharmonybackgroundfile_pos_5_pos_3, negativeharmonybackgroundfile_pos_5_pos_4, negativeharmonybackgroundfile_pos_5_pos_5, negativeharmonybackgroundfile_pos_5_pos_6, negativeharmonybackgroundfile_pos_6_pos_1, negativeharmonybackgroundfile_pos_6_pos_2, negativeharmonybackgroundfile_pos_6_pos_3, negativeharmonybackgroundfile_pos_6_pos_4, negativeharmonybackgroundfile_pos_6_pos_5, negativeharmonybackgroundfile_pos_6_pos_6)

    elif CIRCLE_OF_NOTES_SETTING == "Chromatic":

        if number == 1:
            Note1L_LEFT.config(text="C")
        elif number == 2:
            Note1L_RIGHT.config(text="C")

        if FLAT_SETTING == 0:
            if number == 1:
                Note1R_LEFT.config(text="C#")
            elif number == 2:
                Note1R_RIGHT.config(text="C#")
        else:
            if number == 1:
                Note1R_LEFT.config(text="Db")
            elif number == 2:
                Note1R_RIGHT.config(text="Db")

        if number == 1:
            Note2L_LEFT.config(text="B")
            Note2R_LEFT.config(text="D")
        elif number == 2:
            Note2L_RIGHT.config(text="B")
            Note2R_RIGHT.config(text="D")

        if FLAT_SETTING == 0:
            if number == 1:
                Note3L_LEFT.config(text="A#")
            elif number == 2:
                Note3L_RIGHT.config(text="A#")
        else:
            if number == 1:
                Note3L_LEFT.config(text="Bb")
            elif number == 2:
                Note3L_RIGHT.config(text="Bb")

        if FLAT_SETTING == 0:
            if number == 1:
                Note3R_LEFT.config(text="D#")
            elif number == 2:
                Note3R_RIGHT.config(text="D#")
        else:
            if number == 1:
                Note3R_LEFT.config(text="Eb")
            elif number == 2:
                Note3R_RIGHT.config(text="Eb")

        if number == 1:
            Note4L_LEFT.config(text="A")
            Note4R_LEFT.config(text="E")
        elif number == 2:
            Note4L_RIGHT.config(text="A")
            Note4R_RIGHT.config(text="E")

        if FLAT_SETTING == 0:
            if number == 1:
                Note5L_LEFT.config(text="G#")
            elif number == 2:
                Note5L_RIGHT.config(text="G#")
        else:
            if number == 1:
                Note5L_LEFT.config(text="Ab")
            elif number == 2:
                Note5L_RIGHT.config(text="Ab")

        if number == 1:
            Note5R_LEFT.config(text="F")
            Note6L_LEFT.config(text="G")
        elif number == 2:
            Note5R_RIGHT.config(text="F")
            Note6L_RIGHT.config(text="G")

        if FLAT_SETTING == 0:
            if number == 1:
                Note6R_LEFT.config(text="F#")
            elif number == 2:
                Note6R_RIGHT.config(text="F#")
        else:
            if number == 1:
                Note6R_LEFT.config(text="Gb")
            elif number == 2:
                Note6R_RIGHT.config(text="Gb")

        compare_notes_to_circle(number, Scale_2_None, Root_in, Scale_in, greencolor, redcolor, UserScale, negativeharmonybackgroundfile_pos_1, negativeharmonybackgroundfile_pos_2, negativeharmonybackgroundfile_pos_3, negativeharmonybackgroundfile_pos_4, negativeharmonybackgroundfile_pos_5, negativeharmonybackgroundfile_pos_6, negativeharmonybackgroundfile_pos_1_pos_1, negativeharmonybackgroundfile_pos_1_pos_2, negativeharmonybackgroundfile_pos_1_pos_3, negativeharmonybackgroundfile_pos_1_pos_4, negativeharmonybackgroundfile_pos_1_pos_5, negativeharmonybackgroundfile_pos_1_pos_6, negativeharmonybackgroundfile_pos_2_pos_1, negativeharmonybackgroundfile_pos_2_pos_2, negativeharmonybackgroundfile_pos_2_pos_3, negativeharmonybackgroundfile_pos_2_pos_4, negativeharmonybackgroundfile_pos_2_pos_5, negativeharmonybackgroundfile_pos_2_pos_6, negativeharmonybackgroundfile_pos_3_pos_1, negativeharmonybackgroundfile_pos_3_pos_2, negativeharmonybackgroundfile_pos_3_pos_3, negativeharmonybackgroundfile_pos_3_pos_4, negativeharmonybackgroundfile_pos_3_pos_5, negativeharmonybackgroundfile_pos_3_pos_6, negativeharmonybackgroundfile_pos_4_pos_1, negativeharmonybackgroundfile_pos_4_pos_2, negativeharmonybackgroundfile_pos_4_pos_3, negativeharmonybackgroundfile_pos_4_pos_4, negativeharmonybackgroundfile_pos_4_pos_5, negativeharmonybackgroundfile_pos_4_pos_6, negativeharmonybackgroundfile_pos_5_pos_1, negativeharmonybackgroundfile_pos_5_pos_2, negativeharmonybackgroundfile_pos_5_pos_3, negativeharmonybackgroundfile_pos_5_pos_4, negativeharmonybackgroundfile_pos_5_pos_5, negativeharmonybackgroundfile_pos_5_pos_6, negativeharmonybackgroundfile_pos_6_pos_1, negativeharmonybackgroundfile_pos_6_pos_2, negativeharmonybackgroundfile_pos_6_pos_3, negativeharmonybackgroundfile_pos_6_pos_4, negativeharmonybackgroundfile_pos_6_pos_5, negativeharmonybackgroundfile_pos_6_pos_6)

def update_accidental():

    global Note1L_LEFT, Note1R_LEFT, Note2L_LEFT, Note2R_LEFT, Note3L_LEFT, Note3R_LEFT, Note4L_LEFT, Note4R_LEFT, Note5L_LEFT, Note5R_LEFT, Note6L_LEFT, Note6R_LEFT
    global Note1L_RIGHT, Note1R_RIGHT, Note2L_RIGHT, Note2R_RIGHT, Note3L_RIGHT, Note3R_RIGHT, Note4L_RIGHT, Note4R_RIGHT, Note5L_RIGHT, Note5R_RIGHT, Note6L_RIGHT, Note6R_RIGHT

    if Note1R_LEFT.cget("text") == "Db":
        Note1R_LEFT.config(text="C#")
    elif Note1R_LEFT.cget("text") == "C#":
        Note1R_LEFT.config(text="Db")

    if Note1R_RIGHT.cget("text") == "Db":
        Note1R_RIGHT.config(text="C#")
    elif Note1R_RIGHT.cget("text") == "C#":
        Note1R_RIGHT.config(text="Db")

    if Note2R_LEFT.cget("text") == "Bb":
        Note2R_LEFT.config(text="A#")
    elif Note2R_LEFT.cget("text") == "A#":
        Note2R_LEFT.config(text="Bb")

    if Note2R_RIGHT.cget("text") == "Bb":
        Note2R_RIGHT.config(text="A#")
    elif Note2R_RIGHT.cget("text") == "A#":
        Note2R_RIGHT.config(text="Bb")

    if Note3L_LEFT.cget("text") == "Bb":
        Note3L_LEFT.config(text="A#")
    elif Note3L_LEFT.cget("text") == "A#":
        Note3L_LEFT.config(text="Bb")

    if Note3L_RIGHT.cget("text") == "Bb":
        Note3L_RIGHT.config(text="A#")
    elif Note3L_RIGHT.cget("text") == "A#":
        Note3L_RIGHT.config(text="Bb")

    if Note3R_LEFT.cget("text") == "Eb":
        Note3R_LEFT.config(text="D#")
    elif Note3R_LEFT.cget("text") == "D#":
        Note3R_LEFT.config(text="Eb")

    if Note3R_RIGHT.cget("text") == "Eb":
        Note3R_RIGHT.config(text="D#")
    elif Note3R_RIGHT.cget("text") == "D#":
        Note3R_RIGHT.config(text="Eb")

    if Note4L_LEFT.cget("text") == "Eb":
        Note4L_LEFT.config(text="D#")
    elif Note4L_LEFT.cget("text") == "D#":
        Note4L_LEFT.config(text="Eb")

    if Note4L_RIGHT.cget("text") == "Eb":
        Note4L_RIGHT.config(text="D#")
    elif Note4L_RIGHT.cget("text") == "D#":
        Note4L_RIGHT.config(text="Eb")

    if Note4R_LEFT.cget("text") == "Ab":
        Note4R_LEFT.config(text="G#")
    elif Note4R_LEFT.cget("text") == "G#":
        Note4R_LEFT.config(text="Ab")

    if Note4R_RIGHT.cget("text") == "Ab":
        Note4R_RIGHT.config(text="G#")
    elif Note4R_RIGHT.cget("text") == "G#":
        Note4R_RIGHT.config(text="Ab")

    if Note5L_LEFT.cget("text") == "Ab":
        Note5L_LEFT.config(text="G#")
    elif Note5L_LEFT.cget("text") == "G#":
        Note5L_LEFT.config(text="Ab")

    if Note5L_RIGHT.cget("text") == "Ab":
        Note5L_RIGHT.config(text="G#")
    elif Note5L_RIGHT.cget("text") == "G#":
        Note5L_RIGHT.config(text="Ab")

    if Note5R_LEFT.cget("text") == "Db":
        Note5R_LEFT.config(text="C#")
    elif Note5R_LEFT.cget("text") == "C#":
        Note5R_LEFT.config(text="Db")

    if Note5R_RIGHT.cget("text") == "Db":
        Note5R_RIGHT.config(text="C#")
    elif Note5R_RIGHT.cget("text") == "C#":
        Note5R_RIGHT.config(text="Db")

    if Note6L_LEFT.cget("text") == "Db":
        Note6L_LEFT.config(text="C#")
    elif Note6L_LEFT.cget("text") == "C#":
        Note6L_LEFT.config(text="Db")

    if Note6L_RIGHT.cget("text") == "Db":
        Note6L_RIGHT.config(text="C#")
    elif Note6L_RIGHT.cget("text") == "C#":
        Note6L_RIGHT.config(text="Db")

    if Note6R_LEFT.cget("text") == "Gb":
        Note6R_LEFT.config(text="F#")
    elif Note6R_LEFT.cget("text") == "F#":
        Note6R_LEFT.config(text="Gb")

    if Note6R_RIGHT.cget("text") == "Gb":
        Note6R_RIGHT.config(text="F#")
    elif Note6R_RIGHT.cget("text") == "F#":
        Note6R_RIGHT.config(text="Gb")

def clearcolors(number):

    global Note1L_LEFT, Note1R_LEFT, Note2L_LEFT, Note2R_LEFT, Note3L_LEFT, Note3R_LEFT, Note4L_LEFT, Note4R_LEFT, Note5L_LEFT, Note5R_LEFT, Note6L_LEFT, Note6R_LEFT
    global Note1L_RIGHT, Note1R_RIGHT, Note2L_RIGHT, Note2R_RIGHT, Note3L_RIGHT, Note3R_RIGHT, Note4L_RIGHT, Note4R_RIGHT, Note5L_RIGHT, Note5R_RIGHT, Note6L_RIGHT, Note6R_RIGHT

    if number == 1:
        Note1L_LEFT.config(bg=("white"))
        Note1R_LEFT.config(bg=("white"))
        Note2L_LEFT.config(bg=("white"))
        Note2R_LEFT.config(bg=("white"))
        Note3L_LEFT.config(bg=("white"))
        Note3R_LEFT.config(bg=("white"))
        Note4L_LEFT.config(bg=("white"))
        Note4R_LEFT.config(bg=("white"))
        Note5L_LEFT.config(bg=("white"))
        Note5R_LEFT.config(bg=("white"))
        Note6L_LEFT.config(bg=("white"))
        Note6R_LEFT.config(bg=("white"))
    elif number == 2:
        Note1L_RIGHT.config(bg=("white"))
        Note1R_RIGHT.config(bg=("white"))
        Note2L_RIGHT.config(bg=("white"))
        Note2R_RIGHT.config(bg=("white"))
        Note3L_RIGHT.config(bg=("white"))
        Note3R_RIGHT.config(bg=("white"))
        Note4L_RIGHT.config(bg=("white"))
        Note4R_RIGHT.config(bg=("white"))
        Note5L_RIGHT.config(bg=("white"))
        Note5R_RIGHT.config(bg=("white"))
        Note6L_RIGHT.config(bg=("white"))
        Note6R_RIGHT.config(bg=("white"))

def calculate_inverted_scale_notes(number, root, scale):

    global  Circle_of_Notes_Rotation_Degree_left, Circle_of_Notes_Rotation_Degree_right
    global left_notes_index, right_notes_index

    list_of_inverted_scale_notes = []

    if (root != None and scale != None):
        for i in range(0, Scale(root, scale).notes.__len__()):
            if number == 1:
                get_original_note_index_0 = getIndex(Scale(root, scale).notes[i],left_notes_index)
                get_inverted_note_index_0 = calculateNegativeIndex(get_original_note_index_0, Circle_of_Notes_Rotation_Degree_left)
                inverted_label_0 = left_notes_index[get_inverted_note_index_0]
            elif number == 2:
                get_original_note_index_0 = getIndex(Scale(root, scale).notes[i], right_notes_index)
                get_inverted_note_index_0 = calculateNegativeIndex(get_original_note_index_0, Circle_of_Notes_Rotation_Degree_right)
                inverted_label_0 = right_notes_index[get_inverted_note_index_0]

            inverted_note_name_0 = inverted_label_0.cget("text")
            list_of_inverted_scale_notes.append(Note(inverted_note_name_0))

    return list_of_inverted_scale_notes

def calculate_inverted_chord_notes(number, Mode_Chords_Listbox, Negative_Chords_Listbox):

    global Circle_of_Notes_Rotation_Degree_left, Circle_of_Notes_Rotation_Degree_right
    global left_notes_index, right_notes_index
    global go_flag

    for i in range(0, Mode_Chords_Listbox.size()):  # for every chord in the original listbox
        list_of_inverted_notes = []
        note_count = 0
        for j in range(0, Chord(Mode_Chords_Listbox.get(i)).notes.__len__()):  # for every note in each chord of the original scale
            # print(Chord(Mode_Chords_Listbox.get(i)))
            if number == 1:
                get_original_note_index = getIndex(Chord(Mode_Chords_Listbox.get(i)).notes[j],left_notes_index)
                get_inverted_note_index = calculateNegativeIndex(get_original_note_index, Circle_of_Notes_Rotation_Degree_left)
                inverted_label = left_notes_index[get_inverted_note_index]
            elif number == 2:
                get_original_note_index = getIndex(Chord(Mode_Chords_Listbox.get(i)).notes[j], right_notes_index)
                get_inverted_note_index = calculateNegativeIndex(get_original_note_index, Circle_of_Notes_Rotation_Degree_right)
                inverted_label = right_notes_index[get_inverted_note_index]


            inverted_note_name = inverted_label.cget("text")
            list_of_inverted_notes.append(Note(inverted_note_name)) # add Inverted Note to list
            note_count = note_count + 1 # for every note in chord, add 1. At the end we'll either get 3 or 4 notes.

            if note_count == Chord(Mode_Chords_Listbox.get(i)).notes.__len__(): # if we reach all notes in the chord, process to SEARCH for it, then ADD it.
                note_count = 0
                iv = InvertedChord(list_of_inverted_notes,list_of_inverted_notes.__len__())
                if go_flag == "go":
                    Negative_Chords_Listbox.insert(i, iv)
                else:
                    Negative_Chords_Listbox.insert(i, "-")
                    go_flag = "go"





def update_scale_labels(scale, label, number, listbox_color, font_01):

    try:
        scale_notes = scale.notes
        label.config(text=(scale_notes), bg=listbox_color, font=font_01)
    except:
        global Mode_1_Negative_label_left, Mode_1_Negative_label_right, Mode2_notes_label_left, Mode2_notes_label_right, Mode_1_Negative_Chords_Listbox_left, Mode_1_Negative_Chords_Listbox_right
        if number == 1:
            Mode_1_Negative_label_left.config(text="")
            Mode2_notes_label_left.config(text="")
            Mode_1_Negative_Chords_Listbox_left.delete(0, END)
        elif number == 2:
            Mode_1_Negative_label_right.config(text="")
            Mode2_notes_label_right.config(text="")
            Mode_1_Negative_Chords_Listbox_right.delete(0, END)

def update_chord_labels(Number, Chords_Listbox, label, listbox_color, font_01, fontcolor):
    current_selected_chord = "Nothing Here"
    CurrentChordIndex = Chords_Listbox.index(ANCHOR)
    if Chords_Listbox.get(CurrentChordIndex) != "-":
        chord_from_list = Chords_Listbox.get(CurrentChordIndex)
        chord_notes = Chord(chord_from_list).notes
        current_selected_chord = chord_notes
        if Number == 1:
            label.config(text=(current_selected_chord), bg=listbox_color, font=font_01, foreground = fontcolor)
        elif Number == 2:
            label.config(text=(current_selected_chord), bg=fontcolor, font=font_01, foreground = listbox_color)
        return CurrentChordIndex
    else:
        pass
        # print("No Negative Chord")

def update_chord_labels_without_anchor(Number, Mode_Chords_Listbox, ANCHOR, label, listbox_color, font_01, fontcolor):
    try:
        current_selected_chord = "Nothing Here"
        CurrentChordIndex = Mode_Chords_Listbox.index(ANCHOR)
        if Mode_Chords_Listbox.get(CurrentChordIndex) != "-":
            chord_from_list = Mode_Chords_Listbox.get(CurrentChordIndex)
            chord_notes = Chord(chord_from_list).notes
            current_selected_chord = chord_notes
            if Number == 1:
                label.config(text=(current_selected_chord), bg=listbox_color, font=font_01, foreground = fontcolor)
            elif Number == 2:
                label.config(text=(current_selected_chord), bg=fontcolor, font=font_01, foreground=listbox_color)
    except:
        pass

def update_listboxes():
    pass

def Open_Negative_Harmony_Mode(Root_in, Scale_in, Root_in_2, Scale_in_2, UserScale, UserScaleBox02, FLAT_SETTING, font_01, icon, color, darkgrey, listbox_color, redcolor, greencolor, negativeharmonybackgroundfile_pos_1, negativeharmonybackgroundfile_pos_2, negativeharmonybackgroundfile_pos_3, negativeharmonybackgroundfile_pos_4, negativeharmonybackgroundfile_pos_5, negativeharmonybackgroundfile_pos_6, negative_harmony_button, negativeharmonybackgroundfile, circle_of_notes_left, circle_of_notes_right, parser, circle_of_notes_options, Chords_02_Listbox_left, Chords_02_Listbox_right, negativeharmonybackgroundfile_pos_1_pos_1, negativeharmonybackgroundfile_pos_1_pos_2, negativeharmonybackgroundfile_pos_1_pos_3, negativeharmonybackgroundfile_pos_1_pos_4, negativeharmonybackgroundfile_pos_1_pos_5, negativeharmonybackgroundfile_pos_1_pos_6, negativeharmonybackgroundfile_pos_2_pos_1, negativeharmonybackgroundfile_pos_2_pos_2, negativeharmonybackgroundfile_pos_2_pos_3, negativeharmonybackgroundfile_pos_2_pos_4, negativeharmonybackgroundfile_pos_2_pos_5, negativeharmonybackgroundfile_pos_2_pos_6, negativeharmonybackgroundfile_pos_3_pos_1, negativeharmonybackgroundfile_pos_3_pos_2, negativeharmonybackgroundfile_pos_3_pos_3, negativeharmonybackgroundfile_pos_3_pos_4, negativeharmonybackgroundfile_pos_3_pos_5, negativeharmonybackgroundfile_pos_3_pos_6, negativeharmonybackgroundfile_pos_4_pos_1, negativeharmonybackgroundfile_pos_4_pos_2, negativeharmonybackgroundfile_pos_4_pos_3, negativeharmonybackgroundfile_pos_4_pos_4, negativeharmonybackgroundfile_pos_4_pos_5, negativeharmonybackgroundfile_pos_4_pos_6, negativeharmonybackgroundfile_pos_5_pos_1, negativeharmonybackgroundfile_pos_5_pos_2, negativeharmonybackgroundfile_pos_5_pos_3, negativeharmonybackgroundfile_pos_5_pos_4, negativeharmonybackgroundfile_pos_5_pos_5, negativeharmonybackgroundfile_pos_5_pos_6, negativeharmonybackgroundfile_pos_6_pos_1, negativeharmonybackgroundfile_pos_6_pos_2, negativeharmonybackgroundfile_pos_6_pos_3, negativeharmonybackgroundfile_pos_6_pos_4, negativeharmonybackgroundfile_pos_6_pos_5, negativeharmonybackgroundfile_pos_6_pos_6, md):

    global is_negative_harmony_open

    global Circle_of_Notes_Rotation_Degree_left # This will become a global variable in this class only
    global negative_harmony_window
    global negative_harmony_background
    global Mode_1_Negative_Chords_Listbox_left, Mode_1_Negative_Chords_Listbox_right
    global Mode_1_Negative_label_left, Mode_1_Negative_label_right
    global Mode_1_Chords_Listbox_left, Mode_1_Chords_Listbox_right
    global Mode1_notes_label_left, Mode1_notes_label_right
    global Mode2_notes_label_left, Mode2_notes_label_right
    global Mode_1_label_left, Mode_1_label_right
    global Mode1_chord_notes_label_left, Mode1_chord_notes_label_right
    global Mode2_chord_notes_label_left, Mode2_chord_notes_label_right
    global Note1L_LEFT, Note1R_LEFT, Note2L_LEFT, Note2R_LEFT, Note3L_LEFT, Note3R_LEFT, Note4L_LEFT, Note4R_LEFT, Note5L_LEFT, Note5R_LEFT, Note6L_LEFT, Note6R_LEFT
    global Note1L_RIGHT, Note1R_RIGHT, Note2L_RIGHT, Note2R_RIGHT, Note3L_RIGHT, Note3R_RIGHT, Note4L_RIGHT, Note4R_RIGHT, Note5L_RIGHT, Note5R_RIGHT, Note6L_RIGHT, Note6R_RIGHT
    global left_notes_index, right_notes_index
    global current_selected_negative_mode_1, current_selected_negative_mode_2
    global negative_harmony_window

    if is_negative_harmony_open == False:
        negative_harmony_button.lower()
        is_negative_harmony_open = True

        negative_harmony_window = Toplevel()
        screen_width = negative_harmony_window.winfo_screenwidth()
        screen_height = negative_harmony_window.winfo_screenheight()
        Negative_Harmony_x_percentage = 0.25  # 20% from the left
        Negative_Harmony_y_percentage = 0.15  # 30% from the top
        Negative_Harmony_X_Checker = int(XY_parser.get('negative-harmony', 'x5'))
        Negative_Harmony_Y_Checker = int(XY_parser.get('negative-harmony', 'y6'))
        if Negative_Harmony_X_Checker == 0 and Negative_Harmony_Y_Checker == 0:
            Negative_Harmony_x_position = int(screen_width * Negative_Harmony_x_percentage)
            Negative_Harmony_y_position = int(screen_height * Negative_Harmony_y_percentage)
        else:
            Negative_Harmony_x_position = Negative_Harmony_X_Checker
            Negative_Harmony_y_position = Negative_Harmony_Y_Checker
        window_width = 730
        window_height = 600
        negative_harmony_window.geometry(f"{window_width}x{window_height}+{Negative_Harmony_x_position}+{Negative_Harmony_y_position}")
        negative_harmony_window.title("Negative Harmony")
        negative_harmony_window.resizable(False, False)
        negative_harmony_window.config(bg=color)
        negative_harmony_window.iconbitmap(icon)
        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile)
        negative_harmony_background.place(x=-1, y=0)

        y_offset = 300
        
        Note1L_LEFT = Label(negative_harmony_window, borderwidth=2, width=3)
        Note1L_LEFT.config(bg=(color), font=font_01)
        Note1L_LEFT.place(x=104,y=30)

        Note1R_LEFT = Label(negative_harmony_window, borderwidth=2, width=3)
        Note1R_LEFT.config(bg=(color), font=font_01)
        Note1R_LEFT.place(x=160,y=30)

        Note2L_LEFT = Label(negative_harmony_window, borderwidth=2, width=3)
        Note2L_LEFT.config(bg=(color), font=font_01)
        Note2L_LEFT.place(x=59,y=60)

        Note2R_LEFT = Label(negative_harmony_window, borderwidth=2, width=3)
        Note2R_LEFT.config(bg=(color), font=font_01)
        Note2R_LEFT.place(x=201,y=60)

        Note3L_LEFT = Label(negative_harmony_window, borderwidth=2, width=3)
        Note3L_LEFT.config(bg=(color), font=font_01)
        Note3L_LEFT.place(x=35,y=103)

        Note3R_LEFT = Label(negative_harmony_window, borderwidth=2, width=3)
        Note3R_LEFT.config(bg=(color), font=font_01)
        Note3R_LEFT.place(x=223,y=104)

        Note4L_LEFT = Label(negative_harmony_window, borderwidth=2, width=3)
        Note4L_LEFT.config(bg=(color), font=font_01)
        Note4L_LEFT.place(x=35,y=150)

        Note4R_LEFT = Label(negative_harmony_window, borderwidth=2, width=3)
        Note4R_LEFT.config(bg=(color), font=font_01)
        Note4R_LEFT.place(x=223,y=150)

        Note5L_LEFT = Label(negative_harmony_window, borderwidth=2, width=3)
        Note5L_LEFT.config(bg=(color), font=font_01)
        Note5L_LEFT.place(x=59,y=190)

        Note5R_LEFT = Label(negative_harmony_window, borderwidth=2, width=3)
        Note5R_LEFT.config(bg=(color), font=font_01)
        Note5R_LEFT.place(x=201,y=190)

        Note6L_LEFT = Label(negative_harmony_window, borderwidth=2, width=3)
        Note6L_LEFT.config(bg=(color), font=font_01)
        Note6L_LEFT.place(x=104,y=217)

        Note6R_LEFT = Label(negative_harmony_window, borderwidth=2, width=3)
        Note6R_LEFT.config(bg=(color), font=font_01)
        Note6R_LEFT.place(x=160,y=217)
        
        Note1L_RIGHT = Label(negative_harmony_window, borderwidth=2, width=3)
        Note1L_RIGHT.config(bg=(color), font=font_01)
        Note1L_RIGHT.place(x=104,y=30+y_offset)

        Note1R_RIGHT = Label(negative_harmony_window, borderwidth=2, width=3)
        Note1R_RIGHT.config(bg=(color), font=font_01)
        Note1R_RIGHT.place(x=160,y=30+y_offset)

        Note2L_RIGHT = Label(negative_harmony_window, borderwidth=2, width=3)
        Note2L_RIGHT.config(bg=(color), font=font_01)
        Note2L_RIGHT.place(x=59,y=60+y_offset)

        Note2R_RIGHT = Label(negative_harmony_window, borderwidth=2, width=3)
        Note2R_RIGHT.config(bg=(color), font=font_01)
        Note2R_RIGHT.place(x=201,y=60+y_offset)

        Note3L_RIGHT = Label(negative_harmony_window, borderwidth=2, width=3)
        Note3L_RIGHT.config(bg=(color), font=font_01)
        Note3L_RIGHT.place(x=35,y=103+y_offset)

        Note3R_RIGHT = Label(negative_harmony_window, borderwidth=2, width=3)
        Note3R_RIGHT.config(bg=(color), font=font_01)
        Note3R_RIGHT.place(x=223,y=104+y_offset)

        Note4L_RIGHT = Label(negative_harmony_window, borderwidth=2, width=3)
        Note4L_RIGHT.config(bg=(color), font=font_01)
        Note4L_RIGHT.place(x=35,y=150+y_offset)

        Note4R_RIGHT = Label(negative_harmony_window, borderwidth=2, width=3)
        Note4R_RIGHT.config(bg=(color), font=font_01)
        Note4R_RIGHT.place(x=223,y=150+y_offset)

        Note5L_RIGHT = Label(negative_harmony_window, borderwidth=2, width=3)
        Note5L_RIGHT.config(bg=(color), font=font_01)
        Note5L_RIGHT.place(x=59,y=190+y_offset)

        Note5R_RIGHT = Label(negative_harmony_window, borderwidth=2, width=3)
        Note5R_RIGHT.config(bg=(color), font=font_01)
        Note5R_RIGHT.place(x=201,y=190+y_offset)

        Note6L_RIGHT = Label(negative_harmony_window, borderwidth=2, width=3)
        Note6L_RIGHT.config(bg=(color), font=font_01)
        Note6L_RIGHT.place(x=104,y=217+y_offset)

        Note6R_RIGHT = Label(negative_harmony_window, borderwidth=2, width=3)
        Note6R_RIGHT.config(bg=(color), font=font_01)
        Note6R_RIGHT.place(x=160,y=217+y_offset)

        left_notes_index = [Note1L_LEFT, Note1R_LEFT, Note2R_LEFT, Note3R_LEFT, Note4R_LEFT, Note5R_LEFT, Note6R_LEFT, Note6L_LEFT, Note5L_LEFT, Note4L_LEFT, Note3L_LEFT, Note2L_LEFT]
        right_notes_index = [Note1L_RIGHT, Note1R_RIGHT, Note2R_RIGHT, Note3R_RIGHT, Note4R_RIGHT, Note5R_RIGHT, Note6R_RIGHT, Note6L_RIGHT, Note5L_RIGHT, Note4L_RIGHT, Note3L_RIGHT, Note2L_RIGHT]

        def update_Circle_of_Notes(number):

            global CIRCLE_OF_NOTES_LEFT_SETTING, CIRCLE_OF_NOTES_RIGHT_SETTING
            global Mode_1_Negative_Chords_Listbox_left, Mode_1_Negative_Chords_Listbox_right
            global Mode_1_Negative_label_left, Mode_1_Negative_label_right
            global Mode2_notes_label_left, Mode2_notes_label_right
            global Mode_1_Chords_Listbox_left, Mode_1_Chords_Listbox_right
            global Note1L_LEFT, Note1R_LEFT, Note2L_LEFT, Note2R_LEFT, Note3L_LEFT,  Note3R_LEFT, Note4L_LEFT,  Note4R_LEFT,  Note5L_LEFT, Note5R_LEFT, Note6L_LEFT, Note6R_LEFT
            global Note1L_RIGHT, Note1R_RIGHT, Note2L_RIGHT, Note2R_RIGHT, Note3L_RIGHT,  Note3R_RIGHT, Note4L_RIGHT,  Note4R_RIGHT,  Note5L_RIGHT, Note5R_RIGHT, Note6L_RIGHT, Note6R_RIGHT
            global current_selected_negative_mode_1, current_selected_negative_mode_2
            global Root_1_temp, Scale_1_temp, Root_b_temp, Scale_b_temp

            if Root_in == None:
                pass
            else:
                Root_1_temp = Root_in

            if Scale_in == None:
                pass
            else:
                Scale_1_temp = Scale_in

            if Root_in_2 == None:
                pass
            else:
                Root_b_temp = Root_in_2

            if Scale_in_2 == None:
                pass
            else:
                Scale_b_temp = Scale_in_2

            if number == 1:

                option1 =  circle_of_notes_left.get()
                parser.set('user-settings', 'circle_of_notes_left', option1)
                with open('user-settings.txt', 'w') as configfile:
                    parser.write(configfile)

                CIRCLE_OF_NOTES_LEFT_SETTING = option1


                if (Root_1_temp != None and Scale_1_temp != None):

                    clearcolors(number)
                    process_circle_of_notes(1, CIRCLE_OF_NOTES_LEFT_SETTING, FLAT_SETTING, False, Root_1_temp, Scale_1_temp, UserScale, redcolor, greencolor, negativeharmonybackgroundfile_pos_1, negativeharmonybackgroundfile_pos_2, negativeharmonybackgroundfile_pos_3, negativeharmonybackgroundfile_pos_4, negativeharmonybackgroundfile_pos_5, negativeharmonybackgroundfile_pos_6, negative_harmony_background, negativeharmonybackgroundfile_pos_1_pos_1, negativeharmonybackgroundfile_pos_1_pos_2, negativeharmonybackgroundfile_pos_1_pos_3, negativeharmonybackgroundfile_pos_1_pos_4, negativeharmonybackgroundfile_pos_1_pos_5, negativeharmonybackgroundfile_pos_1_pos_6, negativeharmonybackgroundfile_pos_2_pos_1, negativeharmonybackgroundfile_pos_2_pos_2, negativeharmonybackgroundfile_pos_2_pos_3, negativeharmonybackgroundfile_pos_2_pos_4, negativeharmonybackgroundfile_pos_2_pos_5, negativeharmonybackgroundfile_pos_2_pos_6, negativeharmonybackgroundfile_pos_3_pos_1, negativeharmonybackgroundfile_pos_3_pos_2, negativeharmonybackgroundfile_pos_3_pos_3, negativeharmonybackgroundfile_pos_3_pos_4, negativeharmonybackgroundfile_pos_3_pos_5, negativeharmonybackgroundfile_pos_3_pos_6, negativeharmonybackgroundfile_pos_4_pos_1, negativeharmonybackgroundfile_pos_4_pos_2, negativeharmonybackgroundfile_pos_4_pos_3, negativeharmonybackgroundfile_pos_4_pos_4, negativeharmonybackgroundfile_pos_4_pos_5, negativeharmonybackgroundfile_pos_4_pos_6, negativeharmonybackgroundfile_pos_5_pos_1, negativeharmonybackgroundfile_pos_5_pos_2, negativeharmonybackgroundfile_pos_5_pos_3, negativeharmonybackgroundfile_pos_5_pos_4, negativeharmonybackgroundfile_pos_5_pos_5, negativeharmonybackgroundfile_pos_5_pos_6, negativeharmonybackgroundfile_pos_6_pos_1, negativeharmonybackgroundfile_pos_6_pos_2, negativeharmonybackgroundfile_pos_6_pos_3, negativeharmonybackgroundfile_pos_6_pos_4, negativeharmonybackgroundfile_pos_6_pos_5, negativeharmonybackgroundfile_pos_6_pos_6)
                    list_of_inverted_scale_notes = calculate_inverted_scale_notes(1, Root_1_temp, Scale_1_temp)
                    Mode_1_Negative_Chords_Listbox_left.delete(0, END)
                    calculate_inverted_chord_notes(1, Mode_1_Chords_Listbox_left, Mode_1_Negative_Chords_Listbox_left)
                    Mode_1_Negative_label_left.config(text=(InvertedScale(list_of_inverted_scale_notes, Mode_1_Negative_Chords_Listbox_left)), foreground="white", bg=darkgrey, font=font_01)
                    current_selected_negative_mode_1  = str(InvertedScale(list_of_inverted_scale_notes, Mode_1_Negative_Chords_Listbox_left))
                    update_scale_labels(InvertedScale(list_of_inverted_scale_notes, Mode_1_Negative_Chords_Listbox_left), Mode2_notes_label_left, 1, darkgrey, font_01)

            elif number == 2:

                option2 = circle_of_notes_right.get()
                parser.set('user-settings', 'circle_of_notes_right', option2)
                with open('user-settings.txt', 'w') as configfile:
                    parser.write(configfile)

                CIRCLE_OF_NOTES_RIGHT_SETTING = option2


                if (Root_b_temp != None and Scale_b_temp != None):

                    clearcolors(number)

                    process_circle_of_notes(2, CIRCLE_OF_NOTES_RIGHT_SETTING, FLAT_SETTING, False, Root_b_temp, Scale_b_temp, User_b_scale_temp, redcolor, greencolor, negativeharmonybackgroundfile_pos_1, negativeharmonybackgroundfile_pos_2, negativeharmonybackgroundfile_pos_3, negativeharmonybackgroundfile_pos_4, negativeharmonybackgroundfile_pos_5, negativeharmonybackgroundfile_pos_6, negative_harmony_background, negativeharmonybackgroundfile_pos_1_pos_1, negativeharmonybackgroundfile_pos_1_pos_2, negativeharmonybackgroundfile_pos_1_pos_3, negativeharmonybackgroundfile_pos_1_pos_4, negativeharmonybackgroundfile_pos_1_pos_5, negativeharmonybackgroundfile_pos_1_pos_6, negativeharmonybackgroundfile_pos_2_pos_1, negativeharmonybackgroundfile_pos_2_pos_2, negativeharmonybackgroundfile_pos_2_pos_3, negativeharmonybackgroundfile_pos_2_pos_4, negativeharmonybackgroundfile_pos_2_pos_5, negativeharmonybackgroundfile_pos_2_pos_6, negativeharmonybackgroundfile_pos_3_pos_1, negativeharmonybackgroundfile_pos_3_pos_2, negativeharmonybackgroundfile_pos_3_pos_3, negativeharmonybackgroundfile_pos_3_pos_4, negativeharmonybackgroundfile_pos_3_pos_5, negativeharmonybackgroundfile_pos_3_pos_6, negativeharmonybackgroundfile_pos_4_pos_1, negativeharmonybackgroundfile_pos_4_pos_2, negativeharmonybackgroundfile_pos_4_pos_3, negativeharmonybackgroundfile_pos_4_pos_4, negativeharmonybackgroundfile_pos_4_pos_5, negativeharmonybackgroundfile_pos_4_pos_6, negativeharmonybackgroundfile_pos_5_pos_1, negativeharmonybackgroundfile_pos_5_pos_2, negativeharmonybackgroundfile_pos_5_pos_3, negativeharmonybackgroundfile_pos_5_pos_4, negativeharmonybackgroundfile_pos_5_pos_5, negativeharmonybackgroundfile_pos_5_pos_6, negativeharmonybackgroundfile_pos_6_pos_1, negativeharmonybackgroundfile_pos_6_pos_2, negativeharmonybackgroundfile_pos_6_pos_3, negativeharmonybackgroundfile_pos_6_pos_4, negativeharmonybackgroundfile_pos_6_pos_5, negativeharmonybackgroundfile_pos_6_pos_6)

                    list_of_inverted_scale_notes = calculate_inverted_scale_notes(2, Root_b_temp, Scale_b_temp)

                    Mode_1_Negative_Chords_Listbox_right.delete(0, END)
                    calculate_inverted_chord_notes(2, Mode_1_Chords_Listbox_right, Mode_1_Negative_Chords_Listbox_right)

                    Mode_1_Negative_label_right.config(text=(InvertedScale(list_of_inverted_scale_notes, Mode_1_Negative_Chords_Listbox_right)), foreground="white", bg=darkgrey, font=font_01)
                    current_selected_negative_mode_2 = str(InvertedScale(list_of_inverted_scale_notes, Mode_1_Negative_Chords_Listbox_right))
                    update_scale_labels(InvertedScale(list_of_inverted_scale_notes, Mode_1_Negative_Chords_Listbox_right), Mode2_notes_label_right, 2, darkgrey, font_01)

        Circle_of_Notes_left = OptionMenu(negative_harmony_window, circle_of_notes_left, *circle_of_notes_options, command=lambda x: update_Circle_of_Notes(1))
        Circle_of_Notes_left["highlightthickness"] = 0
        Circle_of_Notes_left.bind()
        Circle_of_Notes_left.place(x=85, y=265)
        Circle_of_Notes_left.config(font=font_01)

        Circle_of_Notes_right = OptionMenu(negative_harmony_window, circle_of_notes_right, *circle_of_notes_options, command= lambda x: update_Circle_of_Notes(2))
        Circle_of_Notes_right["highlightthickness"] = 0
        Circle_of_Notes_right.bind()
        Circle_of_Notes_right.place(x=85, y=265+y_offset)
        Circle_of_Notes_right.config(font=font_01)

        process_circle_of_notes(1, CIRCLE_OF_NOTES_LEFT_SETTING, FLAT_SETTING, False, Root_in, Scale_in, UserScale, redcolor, greencolor, negativeharmonybackgroundfile_pos_1, negativeharmonybackgroundfile_pos_2, negativeharmonybackgroundfile_pos_3, negativeharmonybackgroundfile_pos_4, negativeharmonybackgroundfile_pos_5, negativeharmonybackgroundfile_pos_6, negative_harmony_background, negativeharmonybackgroundfile_pos_1_pos_1, negativeharmonybackgroundfile_pos_1_pos_2, negativeharmonybackgroundfile_pos_1_pos_3, negativeharmonybackgroundfile_pos_1_pos_4, negativeharmonybackgroundfile_pos_1_pos_5, negativeharmonybackgroundfile_pos_1_pos_6, negativeharmonybackgroundfile_pos_2_pos_1, negativeharmonybackgroundfile_pos_2_pos_2, negativeharmonybackgroundfile_pos_2_pos_3, negativeharmonybackgroundfile_pos_2_pos_4, negativeharmonybackgroundfile_pos_2_pos_5, negativeharmonybackgroundfile_pos_2_pos_6, negativeharmonybackgroundfile_pos_3_pos_1, negativeharmonybackgroundfile_pos_3_pos_2, negativeharmonybackgroundfile_pos_3_pos_3, negativeharmonybackgroundfile_pos_3_pos_4, negativeharmonybackgroundfile_pos_3_pos_5, negativeharmonybackgroundfile_pos_3_pos_6, negativeharmonybackgroundfile_pos_4_pos_1, negativeharmonybackgroundfile_pos_4_pos_2, negativeharmonybackgroundfile_pos_4_pos_3, negativeharmonybackgroundfile_pos_4_pos_4, negativeharmonybackgroundfile_pos_4_pos_5, negativeharmonybackgroundfile_pos_4_pos_6, negativeharmonybackgroundfile_pos_5_pos_1, negativeharmonybackgroundfile_pos_5_pos_2, negativeharmonybackgroundfile_pos_5_pos_3, negativeharmonybackgroundfile_pos_5_pos_4, negativeharmonybackgroundfile_pos_5_pos_5, negativeharmonybackgroundfile_pos_5_pos_6, negativeharmonybackgroundfile_pos_6_pos_1, negativeharmonybackgroundfile_pos_6_pos_2, negativeharmonybackgroundfile_pos_6_pos_3, negativeharmonybackgroundfile_pos_6_pos_4, negativeharmonybackgroundfile_pos_6_pos_5, negativeharmonybackgroundfile_pos_6_pos_6)
        process_circle_of_notes(2, CIRCLE_OF_NOTES_RIGHT_SETTING, FLAT_SETTING, False, Root_in_2, Scale_in_2, UserScaleBox02, redcolor, greencolor, negativeharmonybackgroundfile_pos_1, negativeharmonybackgroundfile_pos_2, negativeharmonybackgroundfile_pos_3, negativeharmonybackgroundfile_pos_4, negativeharmonybackgroundfile_pos_5, negativeharmonybackgroundfile_pos_6, negative_harmony_background, negativeharmonybackgroundfile_pos_1_pos_1, negativeharmonybackgroundfile_pos_1_pos_2, negativeharmonybackgroundfile_pos_1_pos_3, negativeharmonybackgroundfile_pos_1_pos_4, negativeharmonybackgroundfile_pos_1_pos_5, negativeharmonybackgroundfile_pos_1_pos_6, negativeharmonybackgroundfile_pos_2_pos_1, negativeharmonybackgroundfile_pos_2_pos_2, negativeharmonybackgroundfile_pos_2_pos_3, negativeharmonybackgroundfile_pos_2_pos_4, negativeharmonybackgroundfile_pos_2_pos_5, negativeharmonybackgroundfile_pos_2_pos_6, negativeharmonybackgroundfile_pos_3_pos_1, negativeharmonybackgroundfile_pos_3_pos_2, negativeharmonybackgroundfile_pos_3_pos_3, negativeharmonybackgroundfile_pos_3_pos_4, negativeharmonybackgroundfile_pos_3_pos_5, negativeharmonybackgroundfile_pos_3_pos_6, negativeharmonybackgroundfile_pos_4_pos_1, negativeharmonybackgroundfile_pos_4_pos_2, negativeharmonybackgroundfile_pos_4_pos_3, negativeharmonybackgroundfile_pos_4_pos_4, negativeharmonybackgroundfile_pos_4_pos_5, negativeharmonybackgroundfile_pos_4_pos_6, negativeharmonybackgroundfile_pos_5_pos_1, negativeharmonybackgroundfile_pos_5_pos_2, negativeharmonybackgroundfile_pos_5_pos_3, negativeharmonybackgroundfile_pos_5_pos_4, negativeharmonybackgroundfile_pos_5_pos_5, negativeharmonybackgroundfile_pos_5_pos_6, negativeharmonybackgroundfile_pos_6_pos_1, negativeharmonybackgroundfile_pos_6_pos_2, negativeharmonybackgroundfile_pos_6_pos_3, negativeharmonybackgroundfile_pos_6_pos_4, negativeharmonybackgroundfile_pos_6_pos_5, negativeharmonybackgroundfile_pos_6_pos_6)

        Mode_1_label_left = Label(negative_harmony_window, height=1,width=28)
        if Root_in != None and Scale_in != None:
            Mode_1_label_left.config(text=((Root_in + " " + Scale_in)), font=font_01, bg=listbox_color)
        Mode_1_label_left.place(x=280, y=18)
        
        Mode_1_label_right = Label(negative_harmony_window, height=1,width=28)
        if Root_in_2 != None and Scale_in_2 != None:
            Mode_1_label_right.config(text=((Root_in_2 + " " + Scale_in_2)), font=font_01, bg=listbox_color)
        Mode_1_label_right.place(x=280, y=18+y_offset)

        Mode1_notes_label_left = Label(negative_harmony_window, width=28)
        if (Root_in != None and Scale_in != None):
            update_scale_labels(Scale(Note(Root_in), Scale_in), Mode1_notes_label_left, 1, listbox_color, font_01)
        Mode1_notes_label_left.place(x=280, y=48)
        
        Mode1_notes_label_right = Label(negative_harmony_window, width=28)
        if (Root_in_2 != None and Scale_in_2 != None):
            update_scale_labels(Scale(Note(Root_in_2), Scale_in_2), Mode1_notes_label_right, 2, listbox_color, font_01)
        Mode1_notes_label_right.place(x=280, y=48+y_offset)

        Mode_1_Chords_Listbox_left = Listbox(negative_harmony_window, exportselection=False, height=11,width=28, selectbackground='Gray')
        Mode_1_Chords_Listbox_left.select_set(0)
        Mode_1_Chords_Listbox_left.config(font=font_01, bg=listbox_color)
        Mode_1_Chords_Listbox_left.place(x=280, y=78)
        Mode_1_Chords_Listbox_left.delete(0, END)
        Mode_1_Chords_Listbox_left.bind("<<ListboxSelect>>", lambda event: Listbox_Select(1, 1, Mode_1_Negative_Chords_Listbox_left, Mode_1_Chords_Listbox_left, Mode1_chord_notes_label_left, Mode2_chord_notes_label_left, listbox_color, darkgrey, font_01))
        for c in range(0, Chords_02_Listbox_left.size()):
            Mode_1_Chords_Listbox_left.insert(c, Chords_02_Listbox_left.get(c))
        Mode_1_Chords_Listbox_left.bind('<Double-Button>', lambda event: MN_MIDI.playchord(str(chord_ready_to_play), md))
            
        Mode_1_Chords_Listbox_right = Listbox(negative_harmony_window, exportselection=False, height=11,width=28, selectbackground='Gray')
        Mode_1_Chords_Listbox_right.select_set(0)
        Mode_1_Chords_Listbox_right.config(font=font_01, bg=listbox_color)
        Mode_1_Chords_Listbox_right.place(x=280, y=78+y_offset)
        Mode_1_Chords_Listbox_right.delete(0, END)
        Mode_1_Chords_Listbox_right.bind("<<ListboxSelect>>", lambda event: Listbox_Select(2, 1, Mode_1_Negative_Chords_Listbox_right, Mode_1_Chords_Listbox_right, Mode1_chord_notes_label_right, Mode2_chord_notes_label_right, listbox_color, darkgrey, font_01))
        for c in range(0, Chords_02_Listbox_right.size()):
            Mode_1_Chords_Listbox_right.insert(c, Chords_02_Listbox_right.get(c))
        Mode_1_Chords_Listbox_right.bind('<Double-Button>', lambda event: MN_MIDI.playchord(str(chord_ready_to_play), md))

        Mode1_chord_notes_label_left = Label(negative_harmony_window, width=28)
        Mode1_chord_notes_label_left.place(x=280, y=265)

        Mode1_chord_notes_label_right = Label(negative_harmony_window, width=28)
        Mode1_chord_notes_label_right.place(x=280, y=265+y_offset)

        negative_offset_x = 230

        Mode2_chord_notes_label_left = Label(negative_harmony_window, width=28)
        Mode2_chord_notes_label_left.config(foreground="white", bg=darkgrey, font=font_01)
        Mode2_chord_notes_label_left.place(x=280+negative_offset_x, y=265)

        Mode2_chord_notes_label_right = Label(negative_harmony_window, width=28)
        Mode2_chord_notes_label_right.config(foreground="white", bg=darkgrey, font=font_01)
        Mode2_chord_notes_label_right.place(x=280+negative_offset_x, y=265+y_offset)

        Mode_1_Negative_label_left = Label(negative_harmony_window, height=1,width=28)
        Mode_1_Negative_label_left.config(font=font_01, foreground="white", bg=darkgrey)
        Mode_1_Negative_label_left.place(x=280+negative_offset_x, y=18)
        
        Mode_1_Negative_label_right = Label(negative_harmony_window, height=1,width=28)
        Mode_1_Negative_label_right.config(font=font_01, foreground="white", bg=darkgrey)
        Mode_1_Negative_label_right.place(x=280+negative_offset_x, y=18+y_offset)

        Mode2_notes_label_left = Label(negative_harmony_window, width=28)
        Mode2_notes_label_left.config(foreground="white", bg=darkgrey, font=font_01)
        Mode2_notes_label_left.place(x=280+negative_offset_x, y=48)
        
        Mode2_notes_label_right = Label(negative_harmony_window, width=28)
        Mode2_notes_label_right.config(foreground="white", bg=darkgrey, font=font_01)
        Mode2_notes_label_right.place(x=280+negative_offset_x, y=48+y_offset)

        Mode_1_Negative_Chords_Listbox_left = Listbox(negative_harmony_window, exportselection=False, height=11,width=28, selectbackground='Gray')
        Mode_1_Negative_Chords_Listbox_left.select_set(0)
        Mode_1_Negative_Chords_Listbox_left.config(font=font_01, foreground="white", bg=darkgrey)
        Mode_1_Negative_Chords_Listbox_left.place(x=280+negative_offset_x, y=78)
        Mode_1_Negative_Chords_Listbox_left.bind("<<ListboxSelect>>", lambda event: Listbox_Select(1, 2, Mode_1_Negative_Chords_Listbox_left, Mode_1_Chords_Listbox_left, Mode1_chord_notes_label_left, Mode2_chord_notes_label_left, listbox_color, darkgrey, font_01))
        Mode_1_Negative_Chords_Listbox_left.bind('<Double-Button>', lambda event: MN_MIDI.playchord(chord_ready_to_play, md))

        Mode_1_Negative_Chords_Listbox_right = Listbox(negative_harmony_window, exportselection=False, height=11,width=28, selectbackground='Gray')
        Mode_1_Negative_Chords_Listbox_right.select_set(0)
        Mode_1_Negative_Chords_Listbox_right.config(font=font_01, foreground="white", bg=darkgrey)
        Mode_1_Negative_Chords_Listbox_right.place(x=280+negative_offset_x, y=78+y_offset)
        Mode_1_Negative_Chords_Listbox_right.bind("<<ListboxSelect>>", lambda event: Listbox_Select(2, 2, Mode_1_Negative_Chords_Listbox_right, Mode_1_Chords_Listbox_right, Mode1_chord_notes_label_right, Mode2_chord_notes_label_right, listbox_color, darkgrey, font_01))
        Mode_1_Negative_Chords_Listbox_right.bind('<Double-Button>', lambda event: MN_MIDI.playchord(chord_ready_to_play, md))


        list_of_inverted_scale_notes = calculate_inverted_scale_notes(1, Root_in, Scale_in)
        calculate_inverted_chord_notes(1, Mode_1_Chords_Listbox_left, Mode_1_Negative_Chords_Listbox_left)

        if (Root_in != None and Scale_in != None):
            Mode_1_Negative_label_left.config(text=(InvertedScale(list_of_inverted_scale_notes, Mode_1_Negative_Chords_Listbox_left)), foreground="white", bg=darkgrey, font=font_01)
            current_selected_negative_mode_1  = str(InvertedScale(list_of_inverted_scale_notes, Mode_1_Negative_Chords_Listbox_left))
            update_scale_labels(InvertedScale(list_of_inverted_scale_notes, Mode_1_Negative_Chords_Listbox_left), Mode2_notes_label_left, 1, darkgrey, font_01)

        list_of_inverted_scale_notes_2 = calculate_inverted_scale_notes(2, Root_in_2, Scale_in_2)
        calculate_inverted_chord_notes(2, Mode_1_Chords_Listbox_right, Mode_1_Negative_Chords_Listbox_right)

        if (Root_in_2 != None and Scale_in_2 != None):
            Mode_1_Negative_label_right.config(text=(InvertedScale(list_of_inverted_scale_notes_2, Mode_1_Negative_Chords_Listbox_right)), foreground="white", bg=darkgrey, font=font_01)
            current_selected_negative_mode_2 = str(InvertedScale(list_of_inverted_scale_notes_2, Mode_1_Negative_Chords_Listbox_right))
            update_scale_labels(InvertedScale(list_of_inverted_scale_notes_2, Mode_1_Negative_Chords_Listbox_right), Mode2_notes_label_right, 2, darkgrey, font_01)

        def exit_negative_harmony():

            global is_negative_harmony_open
            XY_parser.set('negative-harmony', 'x5', str(negative_harmony_window.winfo_x()))
            XY_parser.set('negative-harmony', 'y6', str(negative_harmony_window.winfo_y()))
            with open('windows_2_xy.txt', 'w') as configfile:
                XY_parser.write(configfile)
            negative_harmony_window.destroy()
            is_negative_harmony_open = False
            negative_harmony_button.lift()

        negative_harmony_window.protocol("WM_DELETE_WINDOW", exit_negative_harmony)
        
def cleareverything(number, negativeharmonybackgroundfile_pos_1, negativeharmonybackgroundfile_pos_2, negativeharmonybackgroundfile_pos_3, negativeharmonybackgroundfile_pos_4, negativeharmonybackgroundfile_pos_5, negativeharmonybackgroundfile_pos_6):
    
    global Circle_of_Notes_Rotation_Degree_left

    global Mode_1_Negative_Chords_Listbox_right 
    global Mode1_notes_label_right 
    global Mode_1_label_right 
    global Mode_1_Negative_label_right 
    global Mode2_notes_label_right 
    global Mode_1_Chords_Listbox_right 
    global Mode1_chord_notes_label_right 
    global Mode2_chord_notes_label_right
    global negative_harmony_window, negative_harmony_background

    clearcolors(number)

    Mode_1_Chords_Listbox_right.delete(0, END)
    Mode_1_Negative_Chords_Listbox_right.delete(0, END)
    Mode1_notes_label_right.config(text = "")
    Mode_1_label_right.config(text = "")
    Mode_1_Negative_label_right.config(text = "")
    Mode2_notes_label_right.config(text = "")
    Mode1_chord_notes_label_right.config(text = "")
    Mode2_chord_notes_label_right.config(text = "")

    if (Circle_of_Notes_Rotation_Degree_left == 0 or Circle_of_Notes_Rotation_Degree_left == 6):

        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_1)
        negative_harmony_background.place(x=-1, y=0)
        negative_harmony_background.lower(Note1L_LEFT)

    elif (Circle_of_Notes_Rotation_Degree_left == 1 or Circle_of_Notes_Rotation_Degree_left == 7):
        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_2)
        negative_harmony_background.place(x=-1, y=0)
        negative_harmony_background.lower(Note1L_LEFT)

    elif (Circle_of_Notes_Rotation_Degree_left == 2 or Circle_of_Notes_Rotation_Degree_left == 8):
        negative_harmony_background = Label(negative_harmony_window, height=600, width=730, image=negativeharmonybackgroundfile_pos_3)
        negative_harmony_background.place(x=-1, y=0)
        negative_harmony_background.lower(Note1L_LEFT)

    elif (Circle_of_Notes_Rotation_Degree_left == 3 or Circle_of_Notes_Rotation_Degree_left == 9):
        negative_harmony_background = Label(negative_harmony_window, height=600, width=730,image=negativeharmonybackgroundfile_pos_4)
        negative_harmony_background.place(x=-1, y=0)
        negative_harmony_background.lower(Note1L_LEFT)

    elif (Circle_of_Notes_Rotation_Degree_left == 4 or Circle_of_Notes_Rotation_Degree_left == 10):
        negative_harmony_background = Label(negative_harmony_window, height=600, width=730,image=negativeharmonybackgroundfile_pos_5)
        negative_harmony_background.place(x=-1, y=0)
        negative_harmony_background.lower(Note1L_LEFT)

    elif (Circle_of_Notes_Rotation_Degree_left == 5 or Circle_of_Notes_Rotation_Degree_left == 11):
        negative_harmony_background = Label(negative_harmony_window, height=600, width=730,image=negativeharmonybackgroundfile_pos_6)
        negative_harmony_background.place(x=-1, y=0)
        negative_harmony_background.lower(Note1L_LEFT)

def update_negative_display(neg_dis):
    global negative_display
    negative_display = neg_dis