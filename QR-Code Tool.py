import pyqrcode

print("URL -> QR-Code konvertierer by Erum")
while True:
    aw1 = input(str("URL oder Text zum konvertieren > "))
    aw2 = input(str("Größe des QR-Codes [1-40]      > "))
    aw3 = input(str("Speicherort                    > "))

    url = pyqrcode.create(aw1, error='H')
    url.png(aw3, module_color=(120, 0, 0, 255), background=(0, 0, 0, 255), scale = aw2)
    print("QR-Code wurde erstellt!")
    print("Vorschau:")
    print(url.terminal())
    print("")
