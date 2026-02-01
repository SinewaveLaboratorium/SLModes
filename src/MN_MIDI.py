import threading # MIT License
import time
from tkinter import *
import pygame
import pygame.midi
import MN_Scales
import settings
from settings import *

def initialize_port_list():


    if settings.midi_port != -1:
        for i in range(pygame.midi.get_count()):
            if pygame.midi.get_device_info(i)[3] == 1:
                device_name = pygame.midi.get_device_info(i)[1].decode("utf-8")
                settings.midi_ports_list.append(device_name)
                settings.midi_ports_list_index.append(i)

def playchord(chord, midiout):

    if chord != None:
        c = Chord(chord)

        if settings.midi_port != -1:

            if settings.is_playing == False:
                settings.is_playing = True

                for n in c.notes:
                    if c.notes[0].midi_note() >= 67:
                        midiout.note_on(n.midi_note() - 12, 127)
                        time.sleep(0.0001)
                    else:
                        midiout.note_on(n.midi_note(), 127)
                        time.sleep(0.0001)
                    time.sleep(0.0001)
                settings.is_playing = False




def playscale(scale, midiout):

    if settings.midi_port != -1:

        if settings.is_playing == False:
            settings.is_playing = True
            ordered_notes = []
            counter = 0
            for n in scale.notes:
                ordered_notes.append(n.midi_note())
                if ordered_notes.index((n.midi_note())) > 0 and ordered_notes[counter] < ordered_notes[counter - 1]:
                    ordered_notes[counter] = ordered_notes[counter] + 12
                counter = counter + 1

            ordered_notes.append(ordered_notes[0] + 12)

            if ordered_notes[0] >= 67:
                for m in ordered_notes:
                    m = m - 12

            for n in ordered_notes:
                midiout.note_on(n, 127)
                time.sleep(0.20)
            settings.is_playing = False

def playscale_tempo(scale, chord, style, midiout):

    if settings.midi_port != -1:

        if style == "Scale":

            ordered_notes = []
            counter = 0

            for n in scale.notes:
                ordered_notes.append(n.midi_note())
                if ordered_notes.index((n.midi_note())) > 0 and ordered_notes[counter] < ordered_notes[counter - 1]:
                    ordered_notes[counter] = ordered_notes[counter] + 12
                counter = counter + 1

            ordered_notes.append(ordered_notes[0] + 12)

            if ordered_notes[0] >= 67:
                for m in ordered_notes:
                    m = m - 12

            for n in ordered_notes:

                if settings.is_play_stopped == False:
                    midiout.note_on(n, 127)
                    time.sleep(60/(settings.composer_tempo*2))

        elif style == "Chord":
            playchord(str(chord), midiout)
            time.sleep((60 / settings.composer_tempo)*4)

        elif style == "Chord + Click":
            if settings.is_play_stopped == False:
                playchord(str(chord), midiout)
                midiout.set_instrument(115)
            if settings.is_play_stopped == False:
                midiout.note_on(63, 100)
                time.sleep((60 / settings.composer_tempo))
            if settings.is_play_stopped == False:
                midiout.note_on(63, 100)
                time.sleep((60 / settings.composer_tempo))
            if settings.is_play_stopped == False:
                midiout.note_on(63, 100)
                time.sleep((60 / settings.composer_tempo))
            if settings.is_play_stopped == False:
                midiout.note_on(63, 100)
                time.sleep((60 / settings.composer_tempo))
            midiout.set_instrument(1)

def playMatchedChord(event, myListbox_Scale, myListbox_Chords, myListBoxName, midiout, Root_in, Scale_in):

    if settings.midi_port != -1:
        myListbox_Chords.update_idletasks()
        if myListBoxName == "Matched_Chords2":
            a = MN_Scales.Chord(myListbox_Chords.get(ANCHOR))
            print("Chord is "+ str(a) + " and anchor is " + str(myListbox_Chords.curselection()[0]))
            b = str(myListbox_Scale.get(ANCHOR))
            root = b.split(' ', 1)[0]
            scale = b.split(' ', 1)[1]
            threading.Thread(target=playchord, args=(str(a), midiout)).start()
            time.sleep(0.5)
            threading.Thread(target=playscale, args=(MN_Scales.Scale(root, scale), midiout)).start()
        else:
            a = MN_Scales.Chord(myListbox_Chords.get(ANCHOR))
            threading.Thread(target=playchord, args=(str(a), midiout)).start()
            time.sleep(0.5)
            threading.Thread(target=playscale, args=(MN_Scales.Scale(Root_in, Scale_in), midiout)).start()

def playMoreChord(event, myListbox_Chords, seven_scale_list, midiout):

    if settings.midi_port != -1:
        myListbox_Chords.update_idletasks()
        a = MN_Scales.Chord(myListbox_Chords.get(ANCHOR))
        threading.Thread(target=playchord, args=(str(a), midiout)).start()
        time.sleep(0.5)
        for i in range(0, len(seven_scale_list)):
            if a.notes[0].midi_note() == seven_scale_list[i].notes[0].midi_note(): # CAN THIS BE IMPROVED?
                threading.Thread(target=playscale, args=(seven_scale_list[i], midiout)).start()

def playComposerChords(listbox1, listbox2, style, window, midiout):
    
    def doesModeBelong(scale, mode_note):

        if scale.name in settings.major_names:
            for m_name in settings.major_names:
                sc = MN_Scales.Scale(mode_note, m_name)
                if scale.compare(sc):
                    return m_name
        elif scale.name in settings.melodic_minor_names:
            for m_name in settings.melodic_minor_names:
                sc = MN_Scales.Scale(mode_note, m_name)
                if scale.compare(sc):
                    return m_name
        elif scale.name in settings.harmonic_minor_names:
            for m_name in settings.harmonic_minor_names:
                sc = MN_Scales.Scale(mode_note, m_name)
                if scale.compare(sc):
                    return m_name
        elif scale.name in settings.harmonic_major_names:
            for m_name in settings.harmonic_major_names:
                sc = MN_Scales.Scale(mode_note, m_name)
                if scale.compare(sc):
                    return m_name
        elif scale.name in settings.double_harmonic_major_names:
            for m_name in settings.double_harmonic_major_names:
                sc = MN_Scales.Scale(mode_note, m_name)
                if scale.compare(sc):
                    return m_name
        elif scale.name in settings.neapolitan_major_names:
            for m_name in settings.neapolitan_major_names:
                sc = MN_Scales.Scale(mode_note, m_name)
                if scale.compare(sc):
                    return m_name
        elif scale.name in settings.neapolitan_minor_names:
            for m_name in settings.neapolitan_minor_names:
                sc = MN_Scales.Scale(mode_note, m_name)
                if scale.compare(sc):
                    return m_name
        elif scale.name in settings.hungarian_major_names:
            for m_name in settings.hungarian_major_names:
                sc = MN_Scales.Scale(mode_note, m_name)
                if scale.compare(sc):
                    return m_name
        elif scale.name in settings.romanian_major_names:
            for m_name in settings.romanian_major_names:
                sc = MN_Scales.Scale(mode_note, m_name)
                if scale.compare(sc):
                    return m_name
        else:
            return None

    if settings.is_play_stopped == True:
        settings.is_play_stopped = False

        chords_array = []
        scales_array = []
        if settings.midi_port != -1:
            str = ""
            for i in range(0, listbox1.size()):
                chords_array.insert(i,MN_Scales.Chord(listbox1.get(i)))
                first, *middle, last = listbox2.get(i).split()
                str = ""
                for j in middle:
                    count = 0
                    if count == 0:
                        str = str + j + " "
                    else:
                        str = str + " " + j
                    count += 1
                l2 = first + " " + str + last
                chord = MN_Scales.Chord(listbox1.get(i))
                chord_root = chord.notes[0]
                if MN_Scales.Scale(chord_root, str+last).compare(MN_Scales.Scale(MN_Scales.Note(first), str+last)):
                    scales_array.insert(i, MN_Scales.Scale(MN_Scales.Note(first), str+last))
                else:
                    scale = MN_Scales.Scale(MN_Scales.Note(first), str+last)
                    mode = doesModeBelong(scale, chord_root)
                    if not mode is None:
                        scales_array.insert(i, MN_Scales.Scale(chord_root, mode))

            try:
                k = listbox1.curselection()[0]
            except IndexError:
                k = 0

            def infinite_play(kra):
                if settings.is_play_stopped == False:

                    listbox1.select_clear(0, "end")
                    listbox2.select_clear(0, "end")
                    listbox1.selection_set(kra)
                    listbox2.selection_set(kra)
                    listbox1.see(kra)
                    listbox2.see(kra)
                    listbox1.activate(kra)
                    listbox2.activate(kra)
                    listbox1.selection_anchor(kra)
                    listbox2.selection_anchor(kra)


                    playscale_tempo(scales_array[kra], chords_array[kra], style, midiout)

                    kra = kra + 1

                    if kra ==  scales_array.__len__():
                        kra = 0

                    threading.Thread(target=infinite_play, args=(kra,)).start()

            threading.Thread(target=infinite_play, args=(k,)).start()

