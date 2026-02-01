from musthe import *

class MN_Scales(object):
    pass

class Note:
    pattern = re.compile(r'([A-G])(b{0,3}|#{0,3})(\d{0,1})$')

    @staticmethod
    def all(min_octave=4, max_octave=4):
        for octave in range(min_octave, max_octave + 1):
            for letter in Letter.all():
                letter_accidentals = ['']
                if letter.has_flat():
                    letter_accidentals.insert(0, 'b')
                if letter.has_sharp():
                    letter_accidentals.append('#')
                for acc in letter_accidentals:
                    yield Note('{}{}{:d}'.format(letter.name, acc, octave))

    @staticmethod
    def accidental_value(acc):
        if acc == '':
            return 0
        # return {'#': 1, 'b': -1, 'bb': -2}[acc[0]] + Note.accidental_value(acc[1:])
        return {'#': 1, 'b': -1}[acc[0]] + Note.accidental_value(acc[1:])

    @staticmethod
    def accidental_str(val):
        return 'b' * max(0, -val) + '#' * max(0, val)

    def __init__(self, note):
        m = self.pattern.match(note)
        if m is None:
            raise ValueError('Could not parse the note {!r}'.format(note))

        self.letter = Letter(m.group(1))
        self.accidental = m.group(2)
        self.octave = int(m.group(3) or '4')

        self.number = self.letter.number() + self.octave * 12 + \
                      Note.accidental_value(self.accidental)

        if self.letter == ('E') and self.accidental == ('#'):  # REGULAR NOTE MAINTENANCE
            self.letter = Letter('F')
            self.accidental = ('')
        if self.letter == ('B') and self.accidental == ('#'):  # REGULAR NOTE MAINTENANCE
            self.letter = Letter('C')
            self.accidental = ('')
        if self.letter == ('C') and self.accidental == ('b'):  # REGULAR NOTE MAINTENANCE
            self.letter = Letter('B')
            self.accidental = ('')
        if self.letter == ('F') and self.accidental == ('b'):  # REGULAR NOTE MAINTENANCE
            self.letter = Letter('E')
            self.accidental = ('')

        if self.letter == ('B') and self.accidental == ('##'):  # REGULAR NOTE MAINTENANCE
            self.letter = Letter('C')
            self.accidental = ('#')
        if self.letter == ('E') and self.accidental == ('##'):  # REGULAR NOTE MAINTENANCE
            self.letter = Letter('F')
            self.accidental = ('#')
        if self.accidental == ('##'):
            self.accidental = ('')
            self.letter = self.letter + 2
        if self.letter == ('C') and self.accidental == ('###'):
            self.accidental = ('#')
            self.letter = Letter('D')
        if self.letter == ('D') and self.accidental == ('###'):
            self.accidental = ('')
            self.letter = Letter('F')
        if self.letter == ('F') and self.accidental == ('###'):
            self.accidental = ('#')
            self.letter = Letter('G')
        if self.letter == ('G') and self.accidental == ('###'):
            self.accidental = ('#')
            self.letter = Letter('A')
        if self.letter == ('A') and self.accidental == ('###'):
            self.accidental = ('')
            self.letter = Letter('C')

        if self.letter == ('C') and self.accidental == ('bb'):  # REGULAR NOTE MAINTENANCE
            self.letter = Letter('B')
            self.accidental = ('b')
        if self.letter == ('F') and self.accidental == ('bb'):  # REGULAR NOTE MAINTENANCE
            self.letter = Letter('E')
            self.accidental = ('bb')
        if self.accidental == ('bb'):  # REGULAR NOTE MAINTENANCE
            self.accidental = ('')
            self.letter = self.letter - 2

        if self.letter == ('D') and self.accidental == ('bbb'):
            self.accidental = ('')
            self.letter = Letter('B')
        if self.letter == ('E') and self.accidental == ('bbb'):
            self.accidental = ('b')
            self.letter = Letter('D')
        if self.letter == ('G') and self.accidental == ('bbb'):
            self.accidental = ('')
            self.letter = Letter('E')
        if self.letter == ('A') and self.accidental == ('bbb'):
            self.accidental = ('b')
            self.letter = Letter('G')
        if self.letter == ('B') and self.accidental == ('bbb'):
            self.accidental = ('b')
            self.letter = Letter('A')

    def __add__(self, other):
        if isinstance(other, Interval):
            if other.is_compound():
                from functools import reduce
                return reduce(lambda a, b: a + b, other.split(), self)

            new_letter = self.letter + other.number
            new_number = self.number + other.semitones
            new_note_octave = self.octave + \
                              int(self.letter.name in Letter.letters[8 - other.number:])
            difference = new_number % 12 - new_letter.number()
            if difference < -3:
                difference += 12
            if difference > 3:
                difference -= 12
            return Note(new_letter.name + Note.accidental_str(difference) +
                        str(new_note_octave))
        else:
            raise UnsupportedOperands('+', self, other)

    def __sub__(self, other):
        if isinstance(other, Interval):
            if other.is_compound():
                from functools import reduce
                return reduce(lambda a, b: a - b, other.split(), self)

            return self.to_octave(self.octave - 1) + other.complement()
        elif isinstance(other, Note):
            notes = list((n.midi_note(), n) for n in (self, other))
            semitones = notes[0][0] - notes[1][0]
            if semitones < -1:
                raise ArithmeticError('Interval smaller than d1')
            number = notes[0][1].letter - notes[1][1].letter
            octaves = 0
            while semitones >= 12:
                semitones -= 12
                octaves += 1
            number = (number + (1 if number < 0 else -1)) % 7 + 1
            for i in Interval.all():
                if i.number == number and i.semitones == semitones:
                    return Interval(i.quality + str(octaves * 7 + number))
            raise ValueError('Interval N={} S={}'.format(number, semitones))
        else:
            raise UnsupportedOperands('-', self, other)

    def midi_note(self):
        return self.number + 12

    def frequency(self):
        from math import pow
        return 440.0 * pow(2, (self.number - Note('A4').number) / 12.)

    def to_octave(self, octave):
        return Note(self.letter.name + self.accidental + str(octave))

    def lilypond_notation(self):
        return str(self).replace('b', 'es').replace('#', 'is').lower()

    def scientific_notation(self):
        return str(self) + str(self.octave)

    def compare(self, other):
        if (self.number == other.number) or (self.number == other.number + 12) or (self.number == other.number - 12):
            return True
        else:
            return False

    def compare_letter(self, other):
        if (self.letter == other.letter) and (self.accidental == other.accidental):
            return True
        else:
            return False

    def __repr__(self):
        return 'Note({!r})'.format(self.scientific_notation())

    def __str__(self):
        return self.letter.name + self.accidental

    def __eq__(self, other):
        return self.scientific_notation() == other.scientific_notation()


class Scale:
    scales = {
        # Major modes:
        'Ionian': ['P1', 'M2', 'M3', 'P4', 'P5', 'M6', 'M7'],
        'Dorian': ['P1', 'M2', 'm3', 'P4', 'P5', 'M6', 'm7'],
        'Phrygian': ['P1', 'm2', 'm3', 'P4', 'P5', 'm6', 'm7'],
        'Lydian': ['P1', 'M2', 'M3', 'A4', 'P5', 'M6', 'M7'],
        'Mixolydian': ['P1', 'M2', 'M3', 'P4', 'P5', 'M6', 'm7'],
        'Aeolian': ['P1', 'M2', 'm3', 'P4', 'P5', 'm6', 'm7'],
        'Locrian': ['P1', 'm2', 'm3', 'P4', 'd5', 'm6', 'm7'],

        # Melodic Minor modes:
        'Melodic Minor': ['P1', 'M2', 'm3', 'P4', 'P5', 'M6', 'M7'],
        'Dorian b2': ['P1', 'm2', 'm3', 'P4', 'P5', 'M6', 'm7'],
        'Lydian Augmented': ['P1', 'M2', 'M3', 'A4', 'A5', 'M6', 'M7'],
        'Lydian Dominant': ['P1', 'M2', 'M3', 'A4', 'P5', 'M6', 'm7'],
        'Mixolydian b6': ['P1', 'M2', 'M3', 'P4', 'P5', 'm6', 'm7'],
        'Locrian #2': ['P1', 'M2', 'm3', 'P4', 'd5', 'm6', 'm7'],
        'Altered': ['P1', 'm2', 'm3', 'M3', 'd5', 'm6', 'm7'],

        # Harmonic Minor modes:
        'Harmonic Minor': ['P1', 'M2', 'm3', 'P4', 'P5', 'm6', 'M7'],
        'Locrian 6': ['P1', 'm2', 'm3', 'P4', 'd5', 'M6', 'm7'],
        'Ionian #5': ['P1', 'M2', 'M3', 'P4', 'A5', 'M6', 'M7'],
        'Dorian #4': ['P1', 'M2', 'm3', 'A4', 'P5', 'M6', 'm7'],
        'Phrygian Major': ['P1', 'm2', 'M3', 'P4', 'P5', 'm6', 'm7'],
        'Lydian #2': ['P1', 'A2', 'M3', 'A4', 'P5', 'M6', 'M7'],
        'Ultralocrian': ['P1', 'm2', 'm3', 'M3', 'd5', 'm6', 'M6'],

        # Harmonic Major Modes:
        'Harmonic Major': ['P1', 'M2', 'M3', 'P4', 'P5', 'm6', 'M7'],
        'Dorian b5': ['P1', 'M2', 'm3', 'P4', 'd5', 'M6', 'm7'],
        'Phrygian b4': ['P1', 'm2', 'm3', 'd4', 'P5', 'm6', 'm7'],
        'Lydian Minor': ['P1', 'M2', 'm3', 'A4', 'P5', 'M6', 'M7'],
        'Mixolydian b2': ['P1', 'm2', 'M3', 'P4', 'P5', 'M6', 'm7'],
        'Lydian Augmented #2': ['P1', 'A2', 'M3', 'A4', 'A5', 'M6', 'M7'],
        'Locrian bb7': ['P1', 'm2', 'm3', 'P4', 'd5', 'm6', 'd7'],

        # Double Harmonic Major Modes:
        'Double Harmonic Major': ['P1', 'm2', 'M3', 'P4', 'P5', 'm6', 'M7'],
        'Lydian #2 #6': ['P1', 'A2', 'M3', 'A4', 'P5', 'A6', 'M7'],
        'Ultraphrygian': ['P1', 'm2', 'm3', 'd4', 'P5', 'm6', 'd7'],
        'Hungarian Minor': ['P1', 'M2', 'm3', 'A4', 'P5', 'm6', 'M7'],
        'Oriental': ['P1', 'm2', 'M3', 'P4', 'd5', 'M6', 'm7'],
        'Ionian #2 #5': ['P1', 'A2', 'M3', 'P4', 'A5', 'M6', 'M7'],
        'Locrian bb3 bb7': ['P1', 'm2', 'd3', 'P4', 'd5', 'm6', 'd7'],

        # Neapolitan Major Modes:
        'Neapolitan Major': ['P1', 'm2', 'm3', 'P4', 'P5', 'M6', 'M7'],
        'Leading Whole Tone': ['P1', 'M2', 'M3', 'A4', 'A5', 'A6', 'M7'],
        'Lydian Augmented Dominant': ['P1', 'M2', 'M3', 'A4', 'A5', 'M6', 'm7'],
        'Lydian Dominant b6': ['P1', 'M2', 'M3', 'A4', 'P5', 'm6', 'm7'],
        'Major Locrian': ['P1', 'M2', 'M3', 'P4', 'd5', 'm6', 'm7'],
        'Half-Diminished b4': ['P1', 'M2', 'm3', 'd4', 'd5', 'm6', 'm7'],
        'Altered Dominant bb3': ['P1', 'm2', 'd3', 'd4', 'd5', 'm6', 'm7'],

        # Neapolitan Minor Modes:
        'Neapolitan Minor': ['P1', 'm2', 'm3', 'P4', 'P5', 'm6', 'M7'],
        'Lydian #6': ['P1', 'M2', 'M3', 'A4', 'P5', 'A6', 'M7'],
        'Mixolydian Augmented': ['P1', 'M2', 'M3', 'P4', 'A5', 'M6', 'm7'],
        'Romani Minor': ['P1', 'M2', 'm3', 'A4', 'P5', 'm6', 'm7'],
        'Locrian Dominant': ['P1', 'm2', 'M3', 'P4', 'd5', 'm6', 'm7'],
        'Ionian #2': ['P1', 'A2', 'M3', 'P4', 'P5', 'M6', 'M7'],
        'Ultralocrian bb3': ['P1', 'm2', 'd3', 'd4', 'd5', 'm6', 'd7'],

        # Hungarian Major Modes:
        'Hungarian Major': ['P1', 'A2', 'M3', 'A4', 'P5', 'M6', 'm7'],
        'Ultralocrian bb6': ['P1', 'm2', 'm3', 'd4', 'd5', 'd6', 'd7'],
        'Harmonic Minor b5': ['P1', 'M2', 'm3', 'P4', 'd5', 'm6', 'M7'],
        'Superlocrian ♮6': ['P1', 'm2', 'm3', 'd4', 'd5', 'M6', 'm7'],
        'Jazz Minor #5': ['P1', 'M2', 'm3', 'P4', 'A5', 'M6', 'M7'],
        'Dorian b2 #4': ['P1', 'm2', 'm3', 'A4', 'P5', 'M6', 'm7'],
        'Lydian Augmented #3': ['P1', 'M2', 'A3', 'A4', 'A5', 'M6', 'M7'],

        # Romanian Major
        'Romanian Major': ['P1', 'm2', 'M3', 'A4', 'P5', 'M6', 'm7'],
        'Superlydian Augmented ♮6': ['P1', 'A2', 'A3', 'A4', 'A5', 'M6', 'M7'],
        'Locrian ♮2 bb7': ['P1', 'M2', 'm3', 'P4', 'd5', 'm6', 'd7'],
        'Blues Phrygian b4': ['P1', 'm2', 'm3', 'd4', 'd5', 'd6', 'm7'],
        'Jazz Minor b5': ['P1', 'M2', 'm3', 'P4', 'd5', 'M6', 'M7'],
        'Superphrygian ♮6': ['P1', 'm2', 'm3', 'd4', 'P5', 'M6', 'm7'],
        'Lydian Augmented b3': ['P1', 'M2', 'm3', 'A4', 'A5', 'M6', 'M7'],
    }

    @staticmethod
    def all():
        for root in Note.all():
            for name in Scale.scales:
                yield Scale(root, name)

    def __init__(self, root, name):
        if isinstance(root, str):
            root = Note(root)

        if not isinstance(root, Note):
            raise TypeError('Invalid root note type: {}'.format(type(root)))
        if name not in self.scales:
            raise NameError('No such scale: {}'.format(name))

        self.root = root
        self.name = name
        self.intervals = [Interval(i) for i in self.scales[name]]
        self.notes = [(root + i).to_octave(4) for i in self.intervals]

    def __getitem__(self, k):
        if isinstance(k, int):
            try:
                octaves = k // len(self)
                offset = k - octaves * len(self)
                return self.root.to_octave(self.root.octave + octaves) + \
                       self.intervals[offset]
            except ValueError:
                raise IndexError('Index out of range')
        elif isinstance(k, slice):
            start = k.start or 0
            stop = k.stop or self.max_index
            step = k.step or 1
            return [self[i] for i in range(start, stop, step)]
        else:
            raise TypeError('Scale cannot be indexed by {}.'.format(type(k)))

    def __len__(self):
        return len(self.intervals)

    def __contains__(self, k):
        if isinstance(k, Note):
            return k.to_octave(0) in self.notes
        elif isinstance(k, Chord):
            return all(n in self for n in k.notes)
        elif isinstance(k, (list, set, tuple)):
            return all(x in self for x in k)
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.root, self.name)

    def __repr__(self):
        return 'Scale({!r}, {!r})'.format(self.root, self.name)

    def compare(self, scale02):

        count = 0

        for i in range(0, 7):  # for each of the note of the user scale
            for j in range(0, 7):  # compare it with every note of current scale of the scales_list
                if ((self[i].midi_note() == scale02[j].midi_note()) or (
                        self[i].midi_note() == scale02[j].midi_note() - 12) or (
                        self[i].midi_note() == scale02[j].midi_note() + 12)):
                    count = count + 1
                    break

        if count == 7:
            return True
        else:
            return False

        if (self.notes[1] in scale02.notes) and (self.notes[1] in scale02.notes) and (
                self.notes[2] in scale02.notes) and (self.notes[3] in scale02.notes) and (
                self.notes[4] in scale02.notes) and (self.notes[5] in scale02.notes) and (
                self.notes[6] in scale02.notes):
            return True
        else:
            return False

    def contains(self, note):
        comparison = False
        for j in range(0, 7):
            if self[j].compare(note) == True:
                comparison = True

        return comparison


class Chord:
    recipes = {
        'maj': ['P1', 'M3', 'P5'],
        'majadd2': ['P1', 'M2', 'M3', 'P5'],
        'majadd4': ['P1', 'M3', 'P4', 'P5'],
        'majadd6': ['P1', 'M3', 'P5', 'M6'],
        'maj7': ['P1', 'M3', 'P5', 'M7'],
        'm': ['P1', 'm3', 'P5'],
        'madd2': ['P1', 'M2', 'm3', 'P5'],
        'madd4': ['P1', 'm3', 'P4', 'P5'],
        'madd6': ['P1', 'm3', 'P5', 'M6'],
        'm7': ['P1', 'm3', 'P5', 'm7'],
        '7': ['P1', 'M3', 'P5', 'm7'],
        '7sus2': ['P1', 'M2', 'P5', 'm7'],
        '7sus4': ['P1', 'P4', 'P5', 'm7'],
        '+': ['P1', 'M3', 'A5'],
        'dim': ['P1', 'm3', 'd5'],
        'dim7': ['P1', 'm3', 'd5', 'd7'],
        'maj7b5': ['P1', 'M3', 'd5', 'M7'],
        'maj7#5': ['P1', 'M3', 'A5', 'M7'],
        'm7b5': ['P1', 'm3', 'd5', 'm7'],
        'm7#5': ['P1', 'm3', 'A5', 'm7'],
        '7b5': ['P1', 'M3', 'd5', 'm7'],
        '7#5': ['P1', 'M3', 'A5', 'm7'],
        'mM7': ['P1', 'm3', 'P5', 'M7'],
        'sus2': ['P1', 'M2', 'P5'],
        'sus4': ['P1', 'P4', 'P5']

    }
    aliases = {
        'M': 'maj',
        'majadd2': 'majadd2',
        'majadd4': 'majadd4',
        'majadd6': 'majadd6',
        'm': 'm',
        'madd2': 'madd2',
        'madd4': 'madd4',
        'madd6': 'madd6',
        '7sus2': '7sus2',
        '7sus4': '7sus4',
        '+': '+',
        'dim': 'dim',
        'dim7': 'dim7',
        '7': '7',
        'm7': 'm7',
        'M7': 'maj7',
        '7#5': '7#5',
        '°7': 'm7dim5',
        'ø7': 'm7dim5',
        'maj7b5': 'maj7b5',
        'maj7#5': 'maj7#5',
        '7b5': '7b5',
        'm7b5': 'm7b5',
        'm7#5': 'm7#5',
        'mM7': 'mM7',
        'sus2': 'sus2',
        'sus4': 'sus4',
        'sus2sus4': 'sus2sus4'
    }
    valid_types = list(recipes.keys()) + list(aliases.keys())

    @staticmethod
    def all(min_octave=4, max_octave=4, root=None):
        if root is None:
            roots = Note.all()
        elif isinstance(root, (list, set, tuple)):
            roots = root
        elif isinstance(root, Note):
            roots = [root]
        else:
            raise TypeError('Invalid root type: {}'.format(type(root)))
        for root in roots:
            for name in Chord.recipes:
                yield Chord(root, name)

    def __init__(self, root, chord_type='M', inversion=0):
        if isinstance(root, str):
            for s in sorted(self.valid_types, key=lambda x: -len(x)):
                if root.endswith(s):
                    chord_type = s
                    root = Note(root[:-len(s)])
                    break
            if not isinstance(root, Note):
                print("No Chord to Play")
                raise ValueError('Invalid chord: {!r}'.format(root))

        if chord_type in self.aliases:
            chord_type = self.aliases[chord_type]
        if chord_type not in self.recipes.keys():
            raise ValueError('Invalid chord type: {}.'.format(chord_type))

        self.chord_type = chord_type
        self.notes = [root + Interval(i) for i in self.recipes[chord_type]]
        self.inversion = inversion

    def __repr__(self):
        # None
        return "Chord({!r}, {!r})".format(self.notes[0], self.chord_type)

    def __str__(self):
        if self.inversion == 0:
            return "{}{}".format(str(self.notes[0]), self.chord_type)
        else:
            return "{}{}{}{}".format(str(self.notes[0]), self.chord_type,"/",str(self.notes[1]))

    def __eq__(self, other):
        if len(self.notes) != len(other.notes):
            # if chords dont have the same number of notes, def not equal
            return False
        else:
            return all(self.notes[i] == other.notes[i]
                       for i in range(len(self.notes)))

    def in_scale(self, sc):

        counter = 0
        for i in self.notes:  # for every note of the scale
            for j in range(0, 7):  # check every note of the scale
                if i.midi_note() == sc[j].midi_note() or i.midi_note() == sc[j].midi_note() + 12 or i.midi_note() == sc[
                    j].midi_note() - 12:
                    counter = counter + 1  # if the note of the chord matches with the note of the scale, add 1.
                    break
        if counter == list(self.notes).__len__():
            return 1
        else:
            return 0

    def notes_to_chord(self, note_array):

        number_of_notes = note_array.__len__()

        if number_of_notes != self.notes.__len__():
            return False
        else:
            if number_of_notes == 3:
                if ((self.notes[0].compare(note_array[0])) or (self.notes[0].compare(note_array[1])) or (self.notes[0].compare(note_array[2]))):
                    if ((self.notes[1].compare(note_array[0])) or (self.notes[1].compare(note_array[1])) or (self.notes[1].compare(note_array[2]))):
                        if ((self.notes[2].compare(note_array[0])) or (self.notes[2].compare(note_array[1])) or (self.notes[2].compare(note_array[2]))):

                            return True

            elif number_of_notes == 4:
                if (self.notes[0].compare(note_array[0]) or (self.notes[0].compare(note_array[1])) or (self.notes[0].compare(note_array[2])) or (self.notes[0].compare(note_array[3]))):
                    if ((self.notes[1].compare(note_array[0])) or (self.notes[1].compare(note_array[1])) or (self.notes[1].compare(note_array[2])) or (self.notes[1].compare(note_array[3]))):
                        if ((self.notes[2].compare(note_array[0])) or (self.notes[2].compare(note_array[1])) or (self.notes[2].compare(note_array[2])) or (self.notes[2].compare(note_array[3]))):
                            if ((self.notes[3].compare(note_array[0])) or (self.notes[3].compare(note_array[1])) or (self.notes[3].compare(note_array[2])) or (self.notes[3].compare(note_array[3]))):
                                return True

            else:
                return False


class Interval:
    """
    The interval class.

    The intervals are to be parsed in th following way:
    * the quality, (m, M, p, A, d)
    * the number.

    For example, 'd8', 'P1', 'A5' are valid intervals. 'P3', '5' are not.
    """

    intervals = {
        'd1': -1, 'P1': 0, 'A1': 1,
        'd2': 0, 'm2': 1, 'M2': 2, 'A2': 3,
        'd3': 2, 'm3': 3, 'M3': 4, 'A3': 5,
        'd4': 4, 'P4': 5, 'A4': 6,
        'd5': 6, 'P5': 7, 'A5': 8,
        'd6': 7, 'm6': 8, 'M6': 9, 'A6': 10,
        'd7': 9, 'm7': 10, 'M7': 11, 'A7': 12,
        'd8': 11, 'P8': 12, 'A8': 13,
    }
    quality_inverse = {
        'P': 'P',
        'd': 'A',
        'A': 'd',
        'm': 'M',
        'M': 'm'
    }

    @staticmethod
    def all():
        for name in Interval.intervals:
            yield Interval(name)

    def __init__(self, interval):
        self.quality = interval[0]
        self.number = int(interval[1:])
        self.semitones = 0

        # compound intervals:
        number = self.number
        while number > 8:
            number -= 7
            self.semitones += 12
        interval1 = self.quality + str(number)

        try:
            self.semitones += self.intervals[interval1]
        except KeyError:
            raise ValueError('Invalid interval {!r}.'.format(interval))

    def __str__(self):
        return self.quality + str(self.number)

    def __repr__(self):
        return 'Interval({!r})'.format(str(self))

    def __eq__(self, other):
        return str(self) == str(other)

    def is_compound(self):
        return self.number > 8

    def split(self):
        """
        Split a compound interval into simple intervals.
        The sum of splitted intervals is equal to the compound interval.
        """
        ret = []
        i = Interval(str(self))
        while i.is_compound():
            i.number -= 7
            i.semitones -= 12
            ret.append(Interval('P8'))
        ret.append(i)
        return ret

    def complement(self):
        """
        Return the complement of this interval also known as inverted interval.
        The sum of this interval plus its complement is equal to 1 octave (P8),
        except for the case of A8, for which there is no d1 interval.
        """
        if self.is_compound():
            raise ValueError('Cannot invert a compound interval')
        else:
            n = 9 - self.number
            q = self.quality_inverse[self.quality]
            return Interval(q + str(n))
