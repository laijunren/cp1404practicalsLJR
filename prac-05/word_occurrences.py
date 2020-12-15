words = {}
max = 0
texts = input('Text: ')
if texts == '':
    exit()
for i in texts.split(' '):
    if i == '':
        continue
    if i in words:
        words[i] += 1
    else:
        words[i] = 1
        if len(i) > max:
            max = len(i)
max += 3
for i in sorted(words):
    fmt = '{:<' + str(max) + 's}'
    temp = i + ' : '
    print(fmt.format(temp) + str(words[i]))
