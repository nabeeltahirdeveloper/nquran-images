import requests
# https://app.quranflash.com/book/Medina3/epub/EPUB/imgs/0607.png


for i in range(1, 621):
    if i < 10:
        i = '000' + str(i)
    elif i < 100:
        i = '00' + str(i)
    elif i < 1000:
        i = '0' + str(i)
    else:
        i = i
    try:
        url = 'https://app.quranflash.com/book/Medina3/epub/EPUB/imgs/' + \
            str(i) + '.png'
        r = requests.get(url)
        file = open(f'jawamee/{i}.png', 'wb')
        file.write(r.content)
        file.close()
    except:
        file = open("jawamee/error.txt", "a")
        file.write(str(i) + "\n")
        file.close()
