# from setuptools import setup # Py2App

from cx_Freeze import setup, Executable

# APP = ['SLModes.py']
APP = 'SLModes.py'


DATA_FILES = [
    'Background01.png',
    'Chord_Note.png',
    'Root_Note.png',
    'LargeNote.png',
    'extended_fretboard.png',
    'composer_background.png',
    'fretboard.png',
    'piano.png',
    'icon.icns',
    'Settings.png',
    'fretnote.png',
    'instruments.tsv',
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
    'click.ogg',
    '55.ogg',
    '56.ogg',
    '57.ogg',
    '58.ogg',
    '59.ogg',
    '60.ogg',
    '61.ogg',
    '62.ogg',
    '63.ogg',
    '64.ogg',
    '65.ogg',
    '66.ogg',
    '67.ogg',
    '68.ogg',
    '69.ogg',
    '70.ogg',
    '71.ogg',
    '72.ogg',
    '73.ogg',
    '74.ogg',
    '75.ogg',
    '76.ogg',
    '77.ogg',
    '78.ogg',
    '79.ogg',
    '80.ogg',
    '81.ogg',
    '82.ogg',
    '83.ogg']

# OPTIONS = { 'iconfile': 'icon.icns', 'argv_emulation': True, 'packages': []}
OPTIONS = {'packages': []}


BASE = None

setup(
    name='slmodes',
    version='2.5.0',
    author='Sinewave Lab',
    options={"build_exe": OPTIONS},
    executables=[Executable(APP, base=BASE)],
)
# setup(name='slmodes', version='2.5.0', author='Sinewave Lab', description='SLModes 2.5.0', app=APP, data_files=DATA_FILES, options={'py2app': OPTIONS}, setup_requires=['py2app'], install_requires=[''],)
# setup(name='SLModes 2.5.0', version='2.5.0', author='Sinewave Lab', description='SLModes 2.5.0', app=APP, data_files=DATA_FILES, options={'py2app': OPTIONS}, setup_requires=['py2app'], install_requires=[''],)

