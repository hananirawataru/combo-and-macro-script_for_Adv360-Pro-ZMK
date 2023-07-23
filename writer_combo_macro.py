
timeout_ms = 50
fingers = [40, 41, 42, 43]
thumbs  = [65, 70]
non_combo_letters = [      'KA', 'TA', 'KO', 'SA', 'RA', 'TI', 'KU', 'TU',\
                      'U', 'SI', 'TE', 'KE', 'SE', 'HA', 'TO', 'KI',  'I', 'NN',\
                           'HI', 'SU', 'HU', 'HE', 'ME', 'SO', 'NE', 'HO']
combo_letters = ['BA', 'DO', 'GI', 'NONE', 'MI', 'O', 'NO', 'XYO']

def write_change_lang_macro():
    f.write('macro_LCSP4: macro_LCSP4{\n')
    f.write('compatible = "zmk,behavior-macro";\n')
    f.write('label = "macro_LCSP4";\n')
    f.write('#binding-cells = <0>;\n')
    f.write('bindings = <&kp LC(SPACE)>, <&tog 4>;\n')
    f.write('};\n\n')

def write_letter_macro(letters):
    for letter in letters:
        if letter != 'NONE':
            f.write('macro_' + letter + ': macro_' + letter + '{\n')
            f.write('compatible = "zmk,behavior-macro";\n')
            f.write('label = "macro_' + letter + '";\n')
            f.write('#binding-cells = <0>;\n')
            f.write('bindings = ')
            for i,s in enumerate(letter):
                if i == 0:
                    f.write('<&kp ' + s + '>')
                else:
                    f.write(', <&kp ' + s + '>')  
            f.write(';\n')
            f.write('};\n\n')

symbol_bindings = ['QMARK', 'LA(SLASH)', 'TILDE', 'LBKT', 'RBKT',\
 'LA(LBKT)', 'LA(RBKT)', 'LS(N9)', 'LS(N0)','LS(LBKT)', 'LS(RBKT)',\
 'MINUS', 'LA(BACKSLASH)']

def write_symbol_macro(symbols_bindings):
    for symbol_binding in symbol_bindings:
        macro_name = symbol_binding.replace('(','').replace(')','')
        f.write('macro_' + macro_name + ': macro_' + macro_name + '{\n')
        f.write('compatible = "zmk,behavior-macro";\n')
        f.write('label = "macro_' + macro_name + '";\n')
        f.write('#binding-cells = <0>;\n')
        f.write('bindings = <&kp ' + symbol_binding + '>;\n')
        f.write('};\n\n')

path_w = 'macro.dtsi'
with open(path_w, mode='w') as f:
    write_change_lang_macro()
    write_symbol_macro(symbol_bindings)
    write_letter_macro(non_combo_letters)
    write_letter_macro(combo_letters)

def write_letter_combos(fingers, thumbs, combo_letters):
    key_combos = [(finger, thumb) for thumb in thumbs for finger in fingers]
    for key_combo, letter in zip(key_combos, combo_letters):
        if letter != 'NONE':
            f.write('\tcombo_' + letter + ' {\n')
            f.write('\t\ttimeout-ms = <' + str(timeout_ms) + '>;\n')
            f.write('\t\tkey-positions = <' + str(key_combo[0]) + ' ' + str(key_combo[1]) + '>;\n')
            f.write('\t\tlayers = <4>;\n')
            f.write('\t\tbindings = <&macro_' + letter + '>;\n')
            f.write('\t};\n\n')

path_w = 'combos.keymap'
with open(path_w, mode='w') as f:
    f.write('combos {\n')
    f.write('\tcompatible = "zmk,combos";\n\n')
    write_letter_combos(fingers, thumbs, combo_letters) 
    f.write('};')

