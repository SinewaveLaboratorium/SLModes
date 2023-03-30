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

from MN_Scales import Scale, Note
#
# c = Chord(Note('C'), 'maj')
# if Note('C') in c.notes:
#     print(True)
# else:
#     print(False)

all_notes = ('C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#', 'Ab', 'A', 'A#', 'Bb', 'B')
all_scales =  ('Ionian', 'Dorian', 'Phrygian', 'Lydian', 'Mixolydian', 'Aeolian', 'Locrian', 'Melodic Minor', 'Dorian b2', 'Lydian Augmented', 'Lydian Dominant', 'Mixolydian b6', 'Locrian #2', 'Altered', 'Harmonic Minor', 'Locrian 6', 'Ionian #5', 'Dorian #4', 'Phrygian Major', 'Lydian #2', 'Ultralocrian', 'Harmonic Major', 'Dorian b5', 'Phrygian b4', 'Lydian Minor', 'Mixolydian b2', 'Lydian Augmented #2', 'Locrian bb7', 'Double Harmonic Major', 'Lydian #2 #6', 'Ultraphrygian', 'Hungarian Minor', 'Oriental', 'Ionian #2 #5', 'Locrian bb3 bb7', 'Neapolitan Major', 'Leading Whole Tone', 'Lydian Augmented Dominant', 'Lydian Dominant b6', 'Major Locrian', 'Half-Diminished b4', 'Altered Dominant bb3', 'Neapolitan Minor', 'Lydian #6', 'Mixolydian Augmented', 'Romani Minor', 'Locrian Dominant', 'Ionian #2', 'Ultralocrian bb3', 'Hungarian Major', 'Ultralocrian bb6', 'Harmonic Minor b5', 'Superlocrian ♮6', 'Jazz Minor #5', 'Dorian b2 #4', 'Lydian Augmented #3', 'Romanian Major', 'Superlydian Augmented ♮6', 'Locrian ♮2 bb7', 'Blues Phrygian b4', 'Jazz Minor b5', 'Superphrygian ♮6', 'Lydian Augmented b3');

c_scales = []
csharp_scales = []
db_scales = []
d_scales = []
dsharp_scales = []
eb_scales = []
e_scales = []
f_scales = []
fsharp_scales = []
gb_scales = []
g_scales = []
gsharp_scales = []
ab_scales = []
a_scales = []
asharp_scales = []
bb_scales = []
b_scales = []

for i in range(0, all_scales.__len__()):
    a = "C"
    space = " "
    b = str(all_scales[i])
    string = Scale(a, b)
    c_scales.append(string)

# print(c_scales)

for i in range(0, all_scales.__len__()):
    a = "C#"
    space = " "
    b = str(all_scales[i])
    string = Scale(a, b)
    csharp_scales.append(string)


# print(csharp_scales)

for i in range(0, all_scales.__len__()):
    a = "Db"
    space = " "
    b = str(all_scales[i])
    string = Scale(a, b)
    db_scales.append(string)


# print(db_scales)

for i in range(0, all_scales.__len__()):
    a = "D"
    space = " "
    b = str(all_scales[i])
    string = Scale(a, b)
    d_scales.append(string)


# print(d_scales)

for i in range(0, all_scales.__len__()):
    a = "D#"
    space = " "
    b = str(all_scales[i])
    string = Scale(a, b)
    dsharp_scales.append(string)


# print(dsharp_scales)

for i in range(0, all_scales.__len__()):
    a = "Eb"
    space = " "
    b = str(all_scales[i])
    string = Scale(a, b)
    eb_scales.append(string)


# print(eb_scales)

for i in range(0, all_scales.__len__()):
    a = "E"
    space = " "
    b = str(all_scales[i])
    string = Scale(a, b)
    e_scales.append(string)


# print(e_scales)

for i in range(0, all_scales.__len__()):
    a = "F"
    space = " "
    b = str(all_scales[i])
    string = Scale(a, b)
    f_scales.append(string)


# print(f_scales)

for i in range(0, all_scales.__len__()):
    a = "F#"
    space = " "
    b = str(all_scales[i])
    string = Scale(a, b)
    fsharp_scales.append(string)


# print(fsharp_scales)

for i in range(0, all_scales.__len__()):
    a = "Gb"
    space = " "
    b = str(all_scales[i])
    string = Scale(a, b)
    gb_scales.append(string)


# print(gb_scales)

for i in range(0, all_scales.__len__()):
    a = "G"
    space = " "
    b = str(all_scales[i])
    string = Scale(a, b)
    g_scales.append(string)


# print(g_scales)

for i in range(0, all_scales.__len__()):
    a = "G#"
    space = " "
    b = str(all_scales[i])
    string = Scale(a, b)
    gsharp_scales.append(string)


# print(gsharp_scales)

for i in range(0, all_scales.__len__()):
    a = "Ab"
    space = " "
    b = str(all_scales[i])
    string = Scale(a, b)
    ab_scales.append(string)


# print(ab_scales)

for i in range(0, all_scales.__len__()):
    a = "A"
    space = " "
    b = str(all_scales[i])
    string = Scale(a, b)
    a_scales.append(string)


# print(a_scales)

for i in range(0, all_scales.__len__()):
    a = "A#"
    space = " "
    b = str(all_scales[i])
    string = Scale(a, b)
    asharp_scales.append(string)


# print(asharp_scales)

for i in range(0, all_scales.__len__()):
    a = "Bb"
    space = " "
    b = str(all_scales[i])
    string = Scale(a, b)
    bb_scales.append(string)


# print(bb_scales)

for i in range(0, all_scales.__len__()):
    a = "B"
    space = " "
    b = str(all_scales[i])
    string = Scale(a, b)
    b_scales.append(string)


# print(b_scales)

