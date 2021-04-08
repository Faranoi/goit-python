message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
encoded_message = ""
for ch in message:
    if ch in ("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        encoded_symbol = ord("A") + (ord(ch) - ord("A") + offset) % (ord("Z") - ord("A") + 1)
    elif ch in ("abcdefghijklmnopqrstuvwxyz"):
        encoded_symbol = ord("a") + (ord(ch) - ord("a") + offset) % (ord("z") - ord("a") + 1)
    else:
        encoded_symbol = ord(ch)
    encoded_message = encoded_message + chr(encoded_symbol)
print (encoded_message)