import urllib.request

c = urllib.request.urlopen('https://news.google.com/?hl=es-419&gl=CO&ceid=CO:es-419')
for linea in c:
    print(linea.decode().strip())