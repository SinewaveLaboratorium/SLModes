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

import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os", "pynput"], "excludes": [],
                     "include_files": [
                         'Background01.png',
                         'Chord_Note.png',
                         'composer_background.png',
                         'extended_fretboard.png',
                         'fretboard.png',
                         'fretnote.png',
                         'icon01.ico',
                         'LargeNote.png',
                         'negative_harmony_background.png',
                         'negative_harmony_pos_1.png',
                         'negative_harmony_pos_1_pos_1.png',
                         'negative_harmony_pos_1_pos_2.png',
                         'negative_harmony_pos_1_pos_3.png',
                         'negative_harmony_pos_1_pos_4.png',
                         'negative_harmony_pos_1_pos_5.png',
                         'negative_harmony_pos_1_pos_6.png',
                         'negative_harmony_pos_2.png',
                         'negative_harmony_pos_2_pos_1.png',
                         'negative_harmony_pos_2_pos_2.png',
                         'negative_harmony_pos_2_pos_3.png',
                         'negative_harmony_pos_2_pos_4.png',
                         'negative_harmony_pos_2_pos_5.png',
                         'negative_harmony_pos_2_pos_6.png',
                         'negative_harmony_pos_3.png',
                         'negative_harmony_pos_3_pos_1.png',
                         'negative_harmony_pos_3_pos_2.png',
                         'negative_harmony_pos_3_pos_3.png',
                         'negative_harmony_pos_3_pos_4.png',
                         'negative_harmony_pos_3_pos_5.png',
                         'negative_harmony_pos_3_pos_6.png',
                         'negative_harmony_pos_4.png',
                         'negative_harmony_pos_4_pos_1.png',
                         'negative_harmony_pos_4_pos_2.png',
                         'negative_harmony_pos_4_pos_3.png',
                         'negative_harmony_pos_4_pos_4.png',
                         'negative_harmony_pos_4_pos_5.png',
                         'negative_harmony_pos_4_pos_6.png',
                         'negative_harmony_pos_5.png',
                         'negative_harmony_pos_5_pos_1.png',
                         'negative_harmony_pos_5_pos_2.png',
                         'negative_harmony_pos_5_pos_3.png',
                         'negative_harmony_pos_5_pos_4.png',
                         'negative_harmony_pos_5_pos_5.png',
                         'negative_harmony_pos_5_pos_6.png',
                         'negative_harmony_pos_6.png',
                         'negative_harmony_pos_6_pos_1.png',
                         'negative_harmony_pos_6_pos_2.png',
                         'negative_harmony_pos_6_pos_3.png',
                         'negative_harmony_pos_6_pos_4.png',
                         'negative_harmony_pos_6_pos_5.png',
                         'negative_harmony_pos_6_pos_6.png',
                         'piano.png',
                         'Root_Note.png',
                         'Settings.png',
                         'tmp_composer.txt',
                         'user-settings.txt',
                         'vcruntime140.dll'],
                     "include_msvcr": True, }

base = None

if sys.platform == "win32":
    base = "Win32GUI"

exe = Executable(script="SLMODES.py", shortcut_name="SLModes 2.5.0", shortcutDir="DesktopFolder", base=base, icon='icon01.ico')

setup(name="SLModes",
      version="2.5.0",
      author="Sinewave Lab",
      description="SLModes 2.5.0",
      options={"build_exe": build_exe_options},
      executables=[exe])
