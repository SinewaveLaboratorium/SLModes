import threading
import time
from tkinter import *

import MN_MIDI
import Negative_Harmony_utils
import settings
from MN_Scales import Chord

from midiutil.MidiFile import MIDIFile

Play = None


def Chord_Progression_Listbox_Select(Chord_Progression_Listbox, Chord_Progression_Modes_Listbox):
    cursel = Chord_Progression_Listbox.curselection()
    Chord_Progression_Listbox.selection_clear(0, END)
    Chord_Progression_Modes_Listbox.selection_clear(0, END)
    Chord_Progression_Modes_Listbox.selection_set(cursel)
    Chord_Progression_Listbox.selection_set(cursel)

def Chord_Progression_Modes_Listbox_Select(Chord_Progression_Modes_Listbox, Chord_Progression_Listbox):
    cursel = Chord_Progression_Modes_Listbox.curselection()
    Chord_Progression_Listbox.selection_clear(0, END)
    Chord_Progression_Modes_Listbox.selection_clear(0, END)
    Chord_Progression_Modes_Listbox.selection_set(cursel)
    Chord_Progression_Listbox.selection_set(cursel)

def load_temp_chord_progressions(Chord_Progression_Listbox, Chord_Progression_Modes_Listbox):

    try:
        temp_chord_progression = open('tmp_composer.txt', 'r', encoding='utf-8')
        temp_chord_progression_lines = temp_chord_progression.readlines()
        temp_chord_progression.close()

        for line in temp_chord_progression_lines:
            first, *middle, last = line.split()
            str = ""
            for i in middle:
                count = 0
                if count == 0:
                    str = str + i + " "
                else:
                    str = str + " " + i
                count += 1
            l2 = str + last
            Chord_Progression_Listbox.insert("end", first)
            Chord_Progression_Modes_Listbox.insert("end", l2)
    except:
        pass

def add_chord(chord_number, CurrentChord1Index, CurrentChord2Index, CurrentChord3Index, CurrentChord4Index, Chord_Progression_Listbox, Chord_Progression_Modes_Listbox, Chords_01_Listbox, Chords_02_Listbox, Chords_03_Listbox, Chords_04_Listbox, Root_in, Scale_in, Root_in_2, Scale_in_2):
    box_index = 0

    if chord_number == 1:
        box_index = CurrentChord1Index
        if box_index != -1:
            Chord_Progression_Listbox.insert("end", Chords_01_Listbox.get(box_index))
            Chord_Progression_Modes_Listbox.insert("end", (Root_in + " " + Scale_in))
    elif chord_number == 2:
        box_index = CurrentChord2Index
        if box_index != -1:
            Chord_Progression_Listbox.insert("end", Chords_02_Listbox.get(box_index))
            Chord_Progression_Modes_Listbox.insert("end", (Root_in + " " + Scale_in))
    elif chord_number == 3:
        box_index = CurrentChord3Index
        if box_index != -1:
            Chord_Progression_Listbox.insert("end", Chords_03_Listbox.get(box_index))
            Chord_Progression_Modes_Listbox.insert("end", (Root_in_2 + " " + Scale_in_2))
    elif chord_number == 4:
        box_index = CurrentChord4Index
        if box_index != -1:
            Chord_Progression_Listbox.insert("end", Chords_04_Listbox.get(box_index))
            Chord_Progression_Modes_Listbox.insert("end", (Root_in_2 + " " + Scale_in_2))
    elif chord_number == 5:
        if Negative_Harmony_utils.current_selected_negative_chord_1 != None and Negative_Harmony_utils.current_selected_negative_mode_1 != None and Negative_Harmony_utils.current_selected_negative_chord_1 != "-" and Negative_Harmony_utils.current_selected_negative_chord_1 != "":
            Chord_Progression_Listbox.insert("end", Negative_Harmony_utils.current_selected_negative_chord_1)
            Chord_Progression_Modes_Listbox.insert("end", Negative_Harmony_utils.current_selected_negative_mode_1)
    elif chord_number == 6:
        if Negative_Harmony_utils.current_selected_negative_chord_2 != None and Negative_Harmony_utils.current_selected_negative_mode_2 != None and Negative_Harmony_utils.current_selected_negative_chord_2 != "-" and Negative_Harmony_utils.current_selected_negative_chord_2 != "":
            Chord_Progression_Listbox.insert("end", Negative_Harmony_utils.current_selected_negative_chord_2)
            Chord_Progression_Modes_Listbox.insert("end", Negative_Harmony_utils.current_selected_negative_mode_2)



def remove_chord(Chord_Progression_Listbox, Chord_Progression_Modes_Listbox):
    index = Chord_Progression_Listbox.curselection()
    Chord_Progression_Listbox.delete(index)
    Chord_Progression_Modes_Listbox.delete(index)

def delete_all_chords(Chord_Progression_Modes_Listbox, Chord_Progression_Listbox):
    Chord_Progression_Modes_Listbox.delete(0, END)
    Chord_Progression_Listbox.delete(0, END)

def select(listbox, index):
    listbox.select_clear(0, "end")
    listbox.selection_set(index)
    listbox.see(index)
    listbox.activate(index)
    listbox.selection_anchor(index)

def move_up(Chord_Progression_Listbox, Chord_Progression_Modes_Listbox):
    try:
        idxs = Chord_Progression_Listbox.curselection()
        if not idxs:
            return
        for pos in idxs:
            if pos == 0:
                continue
            text = Chord_Progression_Listbox.get(pos)
            text2 = Chord_Progression_Modes_Listbox.get(pos)
            Chord_Progression_Listbox.delete(pos)
            Chord_Progression_Modes_Listbox.delete(pos)
            Chord_Progression_Listbox.insert(pos - 1, text)
            Chord_Progression_Modes_Listbox.insert(pos - 1, text2)
            select(Chord_Progression_Listbox, pos - 1)
            select(Chord_Progression_Modes_Listbox, pos - 1)
    except:
        pass

def move_down(Chord_Progression_Listbox, Chord_Progression_Modes_Listbox):
    try:
        idxs = Chord_Progression_Listbox.curselection()
        idxs_2 = Chord_Progression_Modes_Listbox.curselection()
        if not idxs:
            return
        for pos in idxs:
            text = Chord_Progression_Listbox.get(pos)
            text2 = Chord_Progression_Modes_Listbox.get(pos)
            Chord_Progression_Listbox.delete(pos)
            Chord_Progression_Modes_Listbox.delete(pos)
            Chord_Progression_Listbox.insert(pos + 1, text)
            Chord_Progression_Modes_Listbox.insert(pos + 1, text2)
            select(Chord_Progression_Listbox, pos+1)
            select(Chord_Progression_Modes_Listbox, pos +1)
    except:
        pass

def save_chord_progression(composer_mode_window, fd, Chord_Progression_Modes_Listbox, Chord_Progression_Listbox):

    try:
        save_text = ""

        for i in range(0, Chord_Progression_Modes_Listbox.size()):
            a = Chord_Progression_Listbox.get(i)
            b = Chord_Progression_Modes_Listbox.get(i)
            save_text = save_text + a + " " +  b + "\n"

        filetype = [('Text Document', '*.txt')]
        # file = fd.asksaveasfile(title="Save Chord Progression - Sinewave Lab", filetypes=filetype, defaultextension=filetype)
        # file.write(save_text)
        # file.close()

        file = fd.asksaveasfilename(defaultextension='.txt', filetypes=filetype, title="Save Chord Progression - Sinewave Lab")
        with open(file, 'w', encoding='utf-8') as f:
            f.write(save_text)

        composer_mode_window.lift()

    except:
        pass


def save_temp_chord_progressions(Chord_Progression_Modes_Listbox, Chord_Progression_Listbox):
    save_text = ""

    for i in range(0, Chord_Progression_Modes_Listbox.size()):
        a = Chord_Progression_Listbox.get(i)
        b = Chord_Progression_Modes_Listbox.get(i)
        save_text = save_text + a + " " + b + "\n"

    temp_chord_progression = open('tmp_composer.txt', 'w', encoding='utf-8')
    temp_chord_progression.write(save_text)
    temp_chord_progression.close()

def open_chord_progression(composer_mode_window, fd, Chord_Progression_Modes_Listbox, Chord_Progression_Listbox):
    try:
        filetype = [('Text Document', '*.txt')]
        filename = fd.askopenfilename(title="Open Chord Progression - Sinewave Lab", filetypes=filetype, defaultextension=filetype)
        chord_progression = open(filename, 'r', encoding='utf-8')
        chord_progression_lines = chord_progression.readlines()
        chord_progression.close()

        delete_all_chords(Chord_Progression_Modes_Listbox, Chord_Progression_Listbox)

        for line in chord_progression_lines:
            first, *middle, last = line.split()
            str = ""
            for i in middle:
                count = 0
                if count == 0:
                    str = str + i + " "
                else:
                    str = str + " " + i
                count += 1
            l2 = str + last
            Chord_Progression_Listbox.insert("end", first)
            Chord_Progression_Modes_Listbox.insert("end", l2)

    except:
        pass

    composer_mode_window.lift()

def play_chord_progression(composer_mode_window, PLAY_STYLE_SETTING, Chord_Progression_Listbox, Chord_Progression_Modes_Listbox, midiout):

    global Play

    Play.config(state=DISABLED)

    style = PLAY_STYLE_SETTING
    if settings.is_playing == False and settings.is_play_stopped == True:
        MN_MIDI.playComposerChords(Chord_Progression_Listbox, Chord_Progression_Modes_Listbox, style, composer_mode_window, midiout)

def EXPORT_MIDI (Chord_Progression_Listbox, fd):

    mf = MIDIFile(1)

    track = 0
    time = 0
    mf.addTrackName(track, time, "Chord Track")
    mf.addTempo(track, time, settings.composer_tempo)

    duration = 4
    channel = 0
    volume = 100

    if Chord_Progression_Listbox.size() > 0:
        time = 0
        for c in range(0, Chord_Progression_Listbox.size()):
            for d in Chord(Chord_Progression_Listbox.get(c)).notes:
                pitch = d.midi_note()
                mf.addNote(track, channel, pitch, time, duration, volume)
            time = time + 4

    filetype = [('MIDI File', '*.mid')]
    file = fd.asksaveasfilename(title="Export MIDI - Sinewave Lab", filetypes=filetype, defaultextension=filetype)
    with open(file, 'wb') as outf:
        mf.writeFile(outf)



def stopComposer(midiout):

    # settings.is_play_stopped = True
    # time.sleep(0.1)

    global Play

    def change_play_stopped():
        settings.is_play_stopped = True
        time.sleep(1)
        try:
            Play.config(state=NORMAL)
        except:
            pass


    threading.Thread(target=change_play_stopped).start()