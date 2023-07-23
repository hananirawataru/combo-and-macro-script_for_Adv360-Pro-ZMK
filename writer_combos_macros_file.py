
timeout_ms = 50

fingers = [ 1,  2,  3,  4,  5,      8,  9, 10, 11, 12, 13,\
           15, 16, 17, 18, 19,     22, 23, 24, 25, 26, 27,\
           29, 30, 31, 32, 33,     40, 41, 42, 43, 44, 45,\
           47, 48, 49, 50, 51,     54, 55, 56, 57, 58, 59\
           ]
left_thumb  = 65
right_thumb = 70

base_macros = [\
 'JPN1',     'JPN2', 'JPN3', 'JPN4', 'JPN5',       'JPN6', 'JPN7', 'JPN8', 'JPN9', 'JPN0',      'JPMINUS1',\
 'JPPERIOD', 'KA',   'TA',   'KO',   'SA',         'RA',   'TI',   'KU',   'TU',   'JPCOMMA2',  'JPCOMMA1',\
 'U',        'SI',   'TE',   'KE',   'SE',         'HA',   'TO',   'KI',   'I',    'NN',        'JPBACKSPACE',\
 'JPTEN',    'HI',   'SU',   'HU',   'HE',         'ME',   'SO',   'NE',   'HO',   'JPNAKATEN', 'JPEN'\
 ]
print(len(base_macros))

left_macros = [\
 'JPQMARKL', 'JPSLASHL', 'JPTILDEL', 'JPLKAGIL', 'JPRKAGIL',      'JPLKADOL', 'JPRKADOL', 'JPLMARUL', 'JPRMARUL', 'JPLDKAGIL', 'JPRDKAGIL',\
 'XA',       'E',        'RI',       'XYA',      'RE',            'PA',       'DI',       'GU',       'DU',       'PI',        'NONE',\
 'WO',       'A',        'NA',       'XYU',      'MO',            'BA',       'DO',       'GI',       'PO',       'NONE',      'NONE',\
 'XU',       'JPMINUS2', 'RO',       'YA',       'XI',            'PU',       'ZO',       'PE',       'BO',       'NONE',      'NONE'\
 ]
print(len(left_macros))

right_macros = [\
 'JPQMARKR', 'JPSLASHR', 'JPTILDER', 'JPLKAGIR', 'JPRKAGIR',      'JPLKADOR', 'JPRKADOR', 'JPLMARUR', 'JPRMARUR', 'JPLDKAGIR', 'JPRDKAGIR',\
 'NONE',     'GA',       'DA',       'GO',       'ZA',            'YO',       'NI',       'RU',       'MA',       'XE',        'NONE',\
 'VU',       'JI',       'DE',       'GE',       'ZE',            'MI',       'O',        'NO',       'XYO',      'XTU',       'NONE',\
 'NONE',     'BI',       'ZU',       'BU',       'BE',            'NU',       'YU',       'MU',       'WA',       'XO',        'NONE'\
 ]
print(len(right_macros))

base_bindings =[\
('N1',),         ('N2',),    ('N3',),   ('N4',),   ('N5',),       ('N6',),   ('N7',),   ('N8',),   ('N9',),   ('N0',),        ('MINUS',),\
('PERIOD',),     ('K','A'),  ('T','A'), ('K','O'), ('S','A'),     ('R','A'), ('T','I'), ('K','U'), ('T','U'), ('LA(COMMA)',), ('COMMA',),\
('U',),          ('S', 'I'), ('T','E'), ('K','E'), ('S','E'),     ('H','A'), ('T','O'), ('K','I'), ('I',),     ('N','N'),     ('BACKSPACE',),\
('LA(PERIOD)',), ('H','I'),  ('S','U'), ('H','U'), ('H','E'),     ('M','E'), ('S','O'), ('N','E'), ('H','O'), ('SLASH',),     ('LA(BACKSLASH)',)\
]
print(len(base_bindings))

left_bindings = [\
('QMARK',), ('LA(SLASH)',), ('TILDE',), ('LBKT',),      ('RBKT',),        ('LA(LBKT)',), ('LA(RBKT)',), ('LS(N9)',), ('LS(N0)',), ('LS(LBKT)',), ('LS(RBKT)',),\
('X','A'),  ('E',),         ('R','I'),  ('X','Y','A'),  ('R','E'),        ('P','A'),     ('D','I'),     ('G','U'),   ('D','U'),   ('P','I'),     ('NONE'),\
('W','O'),  ('A',),         ('N','A'),  ('X','Y','U'),  ('M','O'),        ('B','A'),     ('D','O'),     ('G','I'),   ('P','O'),   ('NONE'),      ('NONE'),\
('X','U'),  ('MINUS',),     ('R','O'),  ('Y','A'),      ('X','I'),        ('P','U'),     ('Z','O'),     ('P','E'),   ('B','O'),   ('NONE'),      ('NONE')\
]
print(len(left_bindings))

right_bindings = [\
('QMARK',), ('LA(SLASH)',), ('TILDE',), ('LBKT',), ('RBKT',),        ('LA(LBKT)',), ('LA(RBKT)',), ('LS(N9)',), ('LS(N0)',),   ('LS(LBKT)',), ('LS(RBKT)',),\
('NONE'),   ('G','A'),      ('D','A'),  ('G','O'), ('Z','A'),        ('Y','O'),     ('N','I'),     ('R','U'),   ('M','A'),     ('X','E'),     ('NONE'),\
('V','U'),  ('J','I'),      ('D','E'),  ('G','E'), ('Z','E'),        ('M','I'),     ('O',),        ('N','O'),   ('X','Y','O'), ('X','T','U'), ('NONE'),\
('NONE'),   ('B','I'),      ('Z','U'),  ('B','U'), ('B','E'),        ('N','U'),     ('Y','U'),     ('M','U'),   ('W','A'),     ('X','O'),     ('NONE')\
]
print(len(right_bindings))


def write_combo(fingers, thumb, macros):
    if len(fingers) == len(macros):
        for finger, macro in zip(fingers, macros):
            if macro != 'NONE':
                f.write('\tcombo_' + macro + ' {\n')
                f.write('\t\ttimeout-ms = <' + str(timeout_ms) + '>;\n')
                f.write('\t\tkey-positions = <' + str(finger) + ' ' + str(thumb) + '>;\n')
                f.write('\t\tlayers = <4>;\n')
                f.write('\t\tbindings = <&macro_' + macro + '>;\n')
                f.write('\t};\n\n')
            else:
                pass
    else:
        print('length is not equal at combo.')

path_w = 'combos.keymap'
with open(path_w, mode='w') as f:
    f.write('combos {\n')
    f.write('\tcompatible = "zmk,combos";\n\n')
    write_combo(fingers, left_thumb,  left_macros)
    write_combo(fingers, right_thumb, right_macros)
    f.write('};')



def write_change_lang_macro():
    f.write('macro_LCSP4: macro_LCSP4{\n')
    f.write('compatible = "zmk,behavior-macro";\n')
    f.write('label = "macro_LCSP4";\n')
    f.write('#binding-cells = <0>;\n')
    f.write('bindings = <&kp LC(SPACE)>, <&tog 4>;\n')
    f.write('};\n\n')


def write_macro(macros, bindings):
    if len(macros) == len(bindings):
        for macro, binding in zip(macros, bindings):
            if macro != 'NONE' and binding != 'NONE' and binding != 'YET':
                # print(bindcing)
                # print(macro)
                # print(binding)
                f.write('macro_' + macro + ': macro_' + macro + '{\n')
                f.write('compatible = "zmk,behavior-macro";\n')
                f.write('label = "macro_' + macro + '";\n')
                f.write('#binding-cells = <0>;\n')
                f.write('bindings = ')
                for i,s in enumerate(binding):
                    if i == 0:
                        f.write('<&kp ' + s + '>')
                    else:
                        f.write(', <&kp ' + s + '>')  
                f.write(';\n')
                f.write('};\n\n')
            elif (macro != 'NONE' and binding == 'NONE') or (macro == 'NONE' and binding != 'NONE'):
                print('macro-binding pair error.')
            else:
                pass
    else:
        print('length is not equal at macro.')


path_w = 'macros.dtsi'
with open(path_w, mode='w') as f:
    write_change_lang_macro()
    write_macro(base_macros, base_bindings)
    write_macro(left_macros, left_bindings)
    write_macro(right_macros, right_bindings)
