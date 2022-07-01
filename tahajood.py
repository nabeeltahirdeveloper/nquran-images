import requests
# https://app.quranflash.com/book/Tahajod/epub/EPUB/imgs/003.png


for i in range(1, 621):
    if i < 10:
        i = '00' + str(i)
    elif i < 100:
        i = '0' + str(i)
    else:
        i = i
    try:
        url = 'https://app.quranflash.com/book/Tahajod/epub/EPUB/imgs/' + \
            str(i) + '.png'
        r = requests.get(url)
        file = open(f'tahajood/{i}.png', 'wb')
        file.write(r.content)
        file.close()
    except:
        file = open("tahajood/error.txt", "a")
        file.write(str(i) + "\n")
        file.close()
