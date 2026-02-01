import modes_7

print(modes_7.modes_7_flat['C Ionian 7'][4])

modes_7_dict = {}
# modes_6_dict = {}
# modes_5_dict = {}
# modes_4_dict = {}
# modes_3_dict = {}
# modes_2_dict = {}
# chords_dict = {}

all_notes = ['C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#', 'Ab', 'A', 'A#', 'Bb', 'B']
# all_notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
all_modes = ['Ionian', 'Dorian', 'Phrygian', 'Lydian', 'Mixolydian', 'Aeolian', 'Locrian',
             'Melodic Minor', 'Dorian b2', 'Lydian Augmented', 'Lydian Dominant', 'Mixolydian b6', 'Locrian #2', 'Altered',
             'Harmonic Minor', 'Locrian 6', 'Ionian #5', 'Dorian #4', 'Phrygian Major', 'Lydian #2', 'Ultralocrian',
             'Harmonic Major', 'Dorian b5', 'Phrygian b4', 'Lydian Minor', 'Mixolydian b2', 'Lydian Augmented #2', 'Locrian bb7',
             'Double Harmonic Major', 'Lydian #2 #6', 'Ultraphrygian', 'Hungarian Minor', 'Oriental', 'Ionian #2 #5', 'Locrian bb3 bb7',
             'Neapolitan Major', 'Leading Whole Tone', 'Lydian Augmented Dominant', 'Lydian Dominant b6', 'Major Locrian', 'Half-Diminished b4', 'Altered Dominant bb3',
             'Neapolitan Minor', 'Lydian #6', 'Mixolydian Augmented', 'Romani Minor', 'Locrian Dominant', 'Ionian #2', 'Ultralocrian bb3',
             'Hungarian Major', 'Ultralocrian bb6', 'Harmonic Minor b5', 'Superlocrian 6', 'Jazz Minor #5', 'Dorian b2 #4', 'Lydian Augmented #3',
             'Romanian Major', 'Superlydian Augmented 6', 'Locrian 2 bb7', 'Blues Phrygian b4', 'Jazz Minor b5', 'Superphrygian 6', 'Lydian Augmented b3']


# for ncommon in range(2,8):
#     for nm in all_notes:  # Master Scale Notes
#         for mm in all_modes:  # Master Scale Modes

#             a = str(nm)
#             b = " "
#             c = str(mm)
#             d = " "
#             e = str(ncommon)
#             category_modes = str(a + b + c + d + e)
#             modes_dict[category_modes] = []

# 7 NOTES DICTIONARY
for nm in all_notes:  # Master Scale Notes
    for mm in all_modes:  # Master Scale Modes
        a = str(nm)
        b = " "
        c = str(mm)
        d = " "
        e = "7"
        category_modes = str(a + b + c + d + e)
        modes_7_dict[category_modes] = []

# 6 NOTES DICTIONARY
# for nm in all_notes:  # Master Scale Notes
#     for mm in all_modes:  # Master Scale Modes
#         a = str(nm)
#         b = " "
#         c = str(mm)
#         d = " "
#         e = "6"
#         category_modes = str(a + b + c + d + e)
#         modes_6_dict[category_modes] = []
#
# # 5 NOTES DICTIONARY
# for nm in all_notes:  # Master Scale Notes
#     for mm in all_modes:  # Master Scale Modes
#         a = str(nm)
#         b = " "
#         c = str(mm)
#         d = " "
#         e = "5"
#         category_modes = str(a + b + c + d + e)
#         modes_5_dict[category_modes] = []
#
# # 4 NOTES DICTIONARY
# for nm in all_notes:  # Master Scale Notes
#     for mm in all_modes:  # Master Scale Modes
#         a = str(nm)
#         b = " "
#         c = str(mm)
#         d = " "
#         e = "4"
#         category_modes = str(a + b + c + d + e)
#         modes_4_dict[category_modes] = []
#
# # 3 NOTES DICTIONARY
# for nm in all_notes:  # Master Scale Notes
#     for mm in all_modes:  # Master Scale Modes
#         a = str(nm)
#         b = " "
#         c = str(mm)
#         d = " "
#         e = "3"
#         category_modes = str(a + b + c + d + e)
#         modes_3_dict[category_modes] = []
#
# # 2 NOTES DICTIONARY
# for nm in all_notes:  # Master Scale Notes
#     for mm in all_modes:  # Master Scale Modes
#         a = str(nm)
#         b = " "
#         c = str(mm)
#         d = " "
#         e = "2"
#         category_modes = str(a + b + c + d + e)
#         modes_2_dict[category_modes] = []


# for nm in all_notes:  # Master Scale Notes
#     for mm in all_modes:  # Master Scale Modes
#         f = str(nm)
#         g = " "
#         h = str(mm)
#         i = " "
#         j = "Chords"
#         category_chords = str(f + g + h + i + j)
#         chords_dict[category_chords] = []

# for nm in all_notes: # Master Scale Notes
#     for mm in all_modes: # Master Scale Modes
#         scale = Scale(Note(nm),mm)
#         k = str(nm)
#         l = " "
#         m = str(mm)
#         n = " "
#         o = "Chords"
#         chord_name_to_search_in_dict = k + l + m + n + o
#         for note_of_scale in range(0, 7): # for each note of the scale
#             for chord_formula in range(0, 25): # for each chord formula
#                 chord_symbol = str(list(Chord.recipes.keys())[chord_formula]) #symbol currently is one chord symbol
#                 note_of_scale_converted_into_Note = Note(str(list(scale.notes)[note_of_scale])) # transform note_of_scale into a proper Note
#                 if Chord(note_of_scale_converted_into_Note, chord_symbol).in_scale(scale) == 1: #if Chord belong to Scale
#                     y = str(list(scale.notes)[note_of_scale])
#                     space = " "
#                     x = chord_symbol
#                     chord = y + space + x
#                     chords_dict[chord_name_to_search_in_dict] += [chord]


# ncommon = 7
# ncommon = 6
# ncommon = 5
# ncommon = 4
# ncommon = 3
# ncommon = 2
#
#
# total_modes = 756
# Common_Notes = 0

# for nm in all_notes: # Master Scale Notes
#     for mm in all_modes: # Master Scale Modes
#         master_scale = Scale(Note(nm), mm)
#         # transform name into list's name
#         p = str(nm)
#         q = " "
#         r = (str)(mm)
#         s = " "
#         t = (str)(ncommon)
#         mode_name_to_search_in_dict = p + q + r + s + t
#         print("Now examining: ", mode_name_to_search_in_dict, "; Modes remaining: ", total_modes)
#         for ns in all_notes: # Slave Scale Notes
#             for ms in all_modes: # Slave Scale Modes
#                 slave_scale = Scale(Note(ns), ms)
#                 # index = 0
#                 for i in range(0, 7):  # for each of the note of the master  scale
#                     for j in range(0, 7):  # compare it with every note of current scale of all_modes
#                         if ((master_scale[i].midi_note() == slave_scale[j].midi_note()) or (
#                                 master_scale[i].midi_note() == slave_scale[j].midi_note() - 12) or (
#                                 master_scale[i].midi_note() == slave_scale[j].midi_note() + 12)):
#                             Common_Notes = Common_Notes + 1
#                             break # no need to check master_note with other slave_notes, we've found it already!
#
#                 if Common_Notes == ncommon:
#                     x = str(slave_scale.root)
#                     space = " "
#                     y = str(slave_scale.name)
#                     scale = x + space + y
                    # modes_7_dict[mode_name_to_search_in_dict] += [scale]
                    # modes_6_dict[mode_name_to_search_in_dict] += [scale]
                    # modes_5_dict[mode_name_to_search_in_dict] += [scale]
                    # modes_4_dict[mode_name_to_search_in_dict] += [scale]
                    # modes_3_dict[mode_name_to_search_in_dict] += [scale]
        #             modes_2_dict[mode_name_to_search_in_dict] += [scale]
        #
        #             # print(modes_7_dict)
        #
        #         Common_Notes = 0
        # total_modes = total_modes - 1

# with open('chords.txt', 'w') as f:
#     f.write(str(chords_dict))

# with open('modes_7.txt', 'w') as f:
#     f.write(str(modes_7_dict))
# with open('modes_6.txt', 'w') as f:
#     f.write(str(modes_6_dict))
# with open('modes_5.txt', 'w') as f:
#     f.write(str(modes_5_dict))
# with open('modes_4.txt', 'w') as f:
#     f.write(str(modes_4_dict))
# with open('modes_3.txt', 'w') as f:
#     f.write(str(modes_3_dict))
# with open('modes_2.txt', 'w') as f:
#     f.write(str(modes_2_dict))

print("Done!")





