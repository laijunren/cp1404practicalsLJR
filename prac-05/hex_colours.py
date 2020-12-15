# create a color dictionary
COLOURS = {
    'ALICEBLUE': '#f0f8ff',
    'ANTIQUEWHITE': '#faebd7',
    'ANTIQUEWHITE1': '#ffefdb',
    'ANTIQUEWHITE2': '#eedfcc',
    'ANTIQUEWHITE3': '#cdc0b0',
    'ANTIQUEWHITE4': '#8b8378',
    'AQUAMARINE1': '#7fffd4',
    'AQUAMARINE2': '#76eec6',
    'AQUAMARINE4': '#458b74',
    'AZURE1': '#f0ffff'
}

while True:
    # input color
    colours = input('Please input a colour: ')
    if colours == '':
        break
    # if it does, print does not exist print does not exist
    if colours.upper() in COLOURS:
        print(COLOURS[colours.upper()])
    else:
        print('The colour was not found.')
