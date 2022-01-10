

def is_binairo_line_valid(line):
    assert len(line)%2 == 0, f'Line {line} has an odd number of characters'

    # Return False if the line is definitly invalid
    for i in range(len(line) - 2):
        if line[i] == line[i+1] == line[i+2] == '0':
            return False
        if line[i] == line[i+1] == line[i+2] == '1':
            return False

    nb_zero = sum(1 for i in line if i == '0')
    nb_ones = sum(1 for i in line if i == '1')
    nb_dash = len(line) - nb_zero - nb_ones
    half_size = len(line) // 2

    if nb_dash > 0 and nb_ones == half_size:
        new_line = ''
        for i in line:
            if i == '-':
                new_line += '0'
            else:
                new_line += i
        return is_binairo_line_valid(new_line)
            
    if nb_zero > half_size or nb_ones > half_size:
        return False

    return True # si valide

tests = ['110110', '110100', '11-0-1-1', '11100100']
for bozo in tests:
    print(bozo, is_binairo_line_valid(bozo))