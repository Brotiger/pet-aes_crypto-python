from aes import AESCipher

print("Выберите действие:")
print("1 - шифровать")
print("2 - дешифровать")
print("Любая другая клавиша = выход")
inp = input("")

if(inp in ["1", "2"]):
    key = input("Введите ключ: ")
    aes = AESCipher(key)

    text = input("Введите текст: ")

    if(inp == "1"):
        cr = aes.encrypt(text)
    elif(inp == "2"):
        cr = aes.decrypt(text)

    print(cr)