# SLModes - Music Software    Copyright (C) 2018-2023  Sinewave Lab
# contact: https://sinewavelab.com/contact/
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

from MN_Scales import Chord, Note

print(Note('C#').midi_note() == Note('Db').midi_note())

c_dict = {}
csharp_dict = {}
db_dict = {}
d_dict = {}
dsharp_dict = {}
eb_dict = {}
e_dict = {}
f_dict = {}
fsharp_dict = {}
gb_dict = {}
g_dict = {}
gsharp_dict = {}
ab_dict = {}
a_dict = {}
asharp_dict = {}
bb_dict = {}
b_dict = {}

c_chord_dict = []
csharp_chord_dict = []
db_chord_dict = []
d_chord_dict = []
dsharp_chord_dict = []
eb_chord_dict = []
e_chord_dict = []
f_chord_dict = []
fsharp_chord_dict = []
gb_chord_dict = []
g_chord_dict = []
gsharp_chord_dict = []
ab_chord_dict = []
a_chord_dict = []
asharp_chord_dict = []
bb_chord_dict = []
b_chord_dict = []


all_notes = ('C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#', 'Ab', 'A', 'A#', 'Bb', 'B')

all_chords = ('maj', 'majadd2', 'majadd4', 'majadd6', 'maj7', 'm', 'madd2', 'madd4', 'madd6', 'm7', '7', '7sus2', '7sus4', '+', 'dim', 'dim7', 'maj7b5', 'maj7#5', 'm7b5', 'm7#5', '7b5', '7#5', 'mM7', 'sus2', 'sus4')

for i in range(0, all_chords.__len__()):
    a = "C"
    b = str(all_chords[i])
    string = a + b
    c_dict[string] = []
    # c_dict[string] += Chord(Note(a), b).notes
    c_chord_dict.append(Chord(string))



for i in range(0, all_chords.__len__()):
    a = "C#"
    b = str(all_chords[i])
    string = a + b
    csharp_dict[string] = []
    # csharp_dict[string] += Chord(Note(a), b).notes
    csharp_chord_dict.append(Chord(string))



for i in range(0, all_chords.__len__()):
    a = "Db"
    b = str(all_chords[i])
    string = a + b
    db_dict[string] = []
    # db_dict[string] += Chord(Note(a), b).notes
    db_chord_dict.append(Chord(string))

for i in range(0, all_chords.__len__()):
    a = "D"
    b = str(all_chords[i])
    string = a + b
    d_dict[string] = []
    # d_dict[string] += Chord(Note(a), b).notes
    d_chord_dict.append(Chord(string))



for i in range(0, all_chords.__len__()):
    a = "D#"
    b = str(all_chords[i])
    string = a + b
    dsharp_dict[string] = []
    # dsharp_dict[string] += Chord(Note(a), b).notes
    dsharp_chord_dict.append(Chord(string))



for i in range(0, all_chords.__len__()):
    a = "Eb"
    b = str(all_chords[i])
    string = a + b
    eb_dict[string] = []
    # eb_dict[string] += Chord(Note(a), b).notes
    eb_chord_dict.append(Chord(string))



for i in range(0, all_chords.__len__()):
    a = "E"
    b = str(all_chords[i])
    string = a + b
    e_dict[string] = []
    # e_dict[string] += Chord(Note(a), b).notes
    e_chord_dict.append(Chord(string))



for i in range(0, all_chords.__len__()):
    a = "F"
    b = str(all_chords[i])
    string = a + b
    f_dict[string] = []
    # f_dict[string] += Chord(Note(a), b).notes
    f_chord_dict.append(Chord(string))



for i in range(0, all_chords.__len__()):
    a = "F#"
    b = str(all_chords[i])
    string = a + b
    fsharp_dict[string] = []
    # fsharp_dict[string] += Chord(Note(a), b).notes
    fsharp_chord_dict.append(Chord(string))



for i in range(0, all_chords.__len__()):
    a = "Gb"
    b = str(all_chords[i])
    string = a + b
    gb_dict[string] = []
    # gb_dict[string] += Chord(Note(a), b).notes
    gb_chord_dict.append(Chord(string))



for i in range(0, all_chords.__len__()):
    a = "G"
    b = str(all_chords[i])
    string = a + b
    g_dict[string] = []
    # g_dict[string] += Chord(Note(a), b).notes
    g_chord_dict.append(Chord(string))



for i in range(0, all_chords.__len__()):
    a = "G#"
    b = str(all_chords[i])
    string = a + b
    gsharp_dict[string] = []
    # gsharp_dict[string] += Chord(Note(a), b).notes
    gsharp_chord_dict.append(Chord(string))



for i in range(0, all_chords.__len__()):
    a = "Ab"
    b = str(all_chords[i])
    string = a + b
    ab_dict[string] = []
    # ab_dict[string] += Chord(Note(a), b).notes
    ab_chord_dict.append(Chord(string))



for i in range(0, all_chords.__len__()):
    a = "A"
    b = str(all_chords[i])
    string = a + b
    a_dict[string] = []
    # a_dict[string] += Chord(Note(a), b).notes
    a_chord_dict.append(Chord(string))



for i in range(0, all_chords.__len__()):
    a = "A#"
    b = str(all_chords[i])
    string = a + b
    asharp_dict[string] = []
    # asharp_dict[string] += Chord(Note(a), b).notes
    asharp_chord_dict.append(Chord(string))



for i in range(0, all_chords.__len__()):
    a = "Bb"
    b = str(all_chords[i])
    string = a + b
    bb_dict[string] = []
    # bb_dict[string] += Chord(Note(a), b).notes
    bb_chord_dict.append(Chord(string))



for i in range(0, all_chords.__len__()):
    a = "B"
    b = str(all_chords[i])
    string = a + b
    b_dict[string] = []
    # b_dict[string] += Chord(Note(a), b).notes
    b_chord_dict.append(Chord(string))

print(b_chord_dict)


# print(b_dict)


# for c in range(0, all_notes.__len__()):
#     chord = Chord(Note(all_notes[c]), 'maj')
#     chord_notes = chord.notes
#     print(chord_notes)
