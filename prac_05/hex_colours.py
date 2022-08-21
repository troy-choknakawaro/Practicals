COLOR_CODES = {'Absolute Zero': '#0048ba', 'Acid Green': '#b0bf1a', 'Alizarin crimson': '#e32636',
               'Amber': '#ffbf00', 'Amethyst': '#9966cc', 'Aqua': '#00ffff', 'Baby Pink': '#f4c2c2',
               'Bitter Lime': '#bfff00', 'Bittersweet': '#fe6f5e', 'Blue Green': '#0d98ba'}
color_name = input('Enter color name: ')
while color_name != '':
    if color_name in COLOR_CODES:
        print('The code for {} is {}'.format(color_name, COLOR_CODES[color_name]))
    color_name = input('Enter color name: ')