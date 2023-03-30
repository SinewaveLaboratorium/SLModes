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

from musthe import * # musthe by Gonzalo Ciruelos uses a MIT License that can be found at the folder Third-Party Library Licenses
from settings import *

def drawExtendedFretboard(scale1, scale2, root1, root2, canvas, show_chords, current_selected_chord_right, current_selected_chord_left, enable_second_fretboard_drawing, imagefile, imagefileroot, largerootnotefile):


   def draw_notes(root_str, i, scale, string_notes, string_coordinates,  imageroot, image):

      y_offset = 0

      if i == 1:
         y_offset = 0
      else:
         y_offset = 222

      root_midi = Note(root_str).midi_note()

      if scale.notes[n].midi_note() == string_notes[b].midi_note() or scale.notes[n].midi_note() == string_notes[b].midi_note() - 12:
         if root_midi == string_notes[b].midi_note() or root_midi == string_notes[b].midi_note() - 12:
            if show_chords == True:
               canvas.create_image(string_coordinates[b][0], string_coordinates[b][1]+y_offset, image=image) ## change this to a blue / green dot
            else:
               canvas.create_image(string_coordinates[b][0], string_coordinates[b][1]+y_offset, image=imageroot)
         else:
            canvas.create_image(string_coordinates[b][0], string_coordinates[b][1]+y_offset, image=image)

   def draw_chord_notes(i, string_notes, string_coordinates):

      y_offset = 0

      if i == 1:
         y_offset = 0
      else:
         y_offset = 222

      if current_selected_chord_left == "Nothing Here":
         None
      else:
         if i == 1:
            for chord_note in current_selected_chord_left:
               if chord_note.midi_note() == string_notes[b].midi_note() or chord_note.midi_note() == string_notes[b].midi_note() - 12 or chord_note.midi_note() == string_notes[b].midi_note() + 12:
                  canvas.create_image(string_coordinates[b][0], string_coordinates[b][1]+y_offset, image=largerootnotefile)

      if current_selected_chord_right == "Nothing Here":
         None;
      else:
         if i == 2:
            for chord_note_2 in current_selected_chord_right:
               if enable_second_fretboard_drawing == True:
                  if chord_note_2.midi_note() == string_notes[b].midi_note() or chord_note_2.midi_note() == string_notes[b].midi_note() - 12 or chord_note_2.midi_note() == string_notes[b].midi_note() + 12:
                     canvas.create_image(string_coordinates[b][0] , string_coordinates[b][1] + y_offset, image=largerootnotefile)

   for b in range(0, 25):

      for n in range (0, 7):

         draw_notes(root1, 1, scale1, first_string_notes, first_string_coordinates, imagefileroot, imagefile)
         if show_chords == True:
            draw_chord_notes(1, first_string_notes, first_string_coordinates)
         if enable_second_fretboard_drawing == True:
            draw_notes(root2, 2,  scale2, first_string_notes, first_string_coordinates, imagefileroot, imagefile)
            if show_chords == True:
               draw_chord_notes(2, first_string_notes, first_string_coordinates)

         draw_notes(root1, 1, scale1, second_string_notes, second_string_coordinates, imagefileroot, imagefile)
         if show_chords == True:
            draw_chord_notes(1, second_string_notes, second_string_coordinates)
         if enable_second_fretboard_drawing == True:
            draw_notes(root2, 2,  scale2, second_string_notes, second_string_coordinates, imagefileroot, imagefile)
            if show_chords == True:
               draw_chord_notes(2, second_string_notes, second_string_coordinates)

         draw_notes(root1, 1, scale1, third_string_notes, third_string_coordinates, imagefileroot, imagefile)
         if show_chords == True:
            draw_chord_notes(1, third_string_notes, third_string_coordinates)
         if enable_second_fretboard_drawing == True:
            draw_notes(root2, 2, scale2, third_string_notes, third_string_coordinates, imagefileroot, imagefile)
            if show_chords == True:
               draw_chord_notes(2, third_string_notes, third_string_coordinates)

         draw_notes(root1, 1, scale1, fourth_string_notes, fourth_string_coordinates, imagefileroot, imagefile)
         if show_chords == True:
            draw_chord_notes(1, fourth_string_notes, fourth_string_coordinates)
         if enable_second_fretboard_drawing == True:
            draw_notes(root2, 2, scale2, fourth_string_notes, fourth_string_coordinates, imagefileroot, imagefile)
            if show_chords == True:
               draw_chord_notes(2, fourth_string_notes, fourth_string_coordinates)

         draw_notes(root1, 1, scale1, fifth_string_notes, fifth_string_coordinates, imagefileroot, imagefile)
         if show_chords == True:
            draw_chord_notes(1, fifth_string_notes, fifth_string_coordinates)
         if enable_second_fretboard_drawing == True:
            draw_notes(root2, 2, scale2, fifth_string_notes, fifth_string_coordinates, imagefileroot, imagefile)
            if show_chords == True:
               draw_chord_notes(2, fifth_string_notes, fifth_string_coordinates)

         draw_notes(root1, 1, scale1, sixth_string_notes, sixth_string_coordinates, imagefileroot, imagefile)
         if show_chords == True:
            draw_chord_notes(1, sixth_string_notes, sixth_string_coordinates)
         if enable_second_fretboard_drawing == True:
            draw_notes(root2, 2, scale2, sixth_string_notes, sixth_string_coordinates, imagefileroot, imagefile)
            if show_chords == True:
               draw_chord_notes(2, sixth_string_notes, sixth_string_coordinates)


def drawModeShape(shape, canvas, notefile, freboardfile):
   global fretboardcircles

   canvas.delete("all")
   canvas.create_image(97, 57, image=freboardfile)

   count = 0

   for i in range(0, 18):
      x = list(guitar_modes_shapes.get(shape))[count]
      y = list(guitar_modes_shapes.get(shape))[count + 1]
      canvas.create_image(x, y-4, image=notefile)
      count = count + 2

def drawPianoMode(scale, canvas, notefile, pianofile):
   global pianocircles

   canvas.delete("all")
   canvas.create_image(100, 50, image=pianofile)

   previous_n = 0
   for i in range(0, 7):
      k = scale.notes[i].number
      if k < previous_n: #If current note is lower than previous, add an octave to it
         scale.notes[i] = scale.notes[i] + musthe.Interval('P8')
         n = str(scale.notes[i].scientific_notation())
         k = k + 12
      else:
         n = str(scale.notes[i].scientific_notation())

      previous_n = k

      x = pianokeyXYDict.get(n)[0]
      y = pianokeyXYDict.get(n)[1]
      canvas.create_image(x, y, image=notefile)
