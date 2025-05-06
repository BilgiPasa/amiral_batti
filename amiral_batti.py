from random import randint
from time import *
board = []
sayac = 0
puan = 250
for i in range(5):
    board.append(["0"]*5)
def print_board(board):
    for satir in board:
        print(" ".join(satir))
def rand(board):
    return randint(1, len(board) - 1)
print("-" * 65)
print('Amiral battı oyununa hoş geldiniz! (Çıkmak için "exit" yazınız)')
print("-" * 65)
print("Oyundaki amacınız, en fazla puan ile oyunu bitirmek.")
print("Her yanlış yaptığınızda 10 puanınız gider.")
print("-" * 65)
print("Başlangıç Puanınız : ", puan)
print("-" * 65)
gemi_satir = rand(board)
gemi_satir = int(gemi_satir)
gemi_sutun = rand(board)
gemi_sutun = int(gemi_sutun)
gemi1_satir = rand(board)
gemi1_satir = int(gemi1_satir)
gemi1_sutun = rand(board)
gemi1_sutun = int(gemi1_sutun)
gemi2_satir = rand(board)
gemi2_satir = int(gemi2_satir)
gemi2_sutun = rand(board)
gemi2_sutun = int(gemi2_sutun)
while True:
    if gemi_satir == gemi1_satir and gemi_sutun == gemi1_sutun:
        gemi1_satir = rand(board)
        gemi1_sutun = rand(board)
        continue
    elif gemi_satir == gemi2_satir and gemi_sutun == gemi2_sutun:
        gemi2_satir = rand(board)
        gemi2_sutun = rand(board)
        continue
    elif gemi1_satir == gemi2_satir and gemi1_sutun == gemi2_sutun:
        gemi2_satir = rand(board)
        gemi2_sutun = rand(board)
        continue
    else:
        print_board(board)
        print("-" * 65)
        tahmin_satir = input("Satır giriniz : ")
        if tahmin_satir.isdigit():
            tahmin_sutun = input("Sütun giriniz : ")
            if tahmin_sutun.isdigit():
                if (int(tahmin_satir) == gemi_satir and int(tahmin_sutun) == gemi_sutun) or (int(tahmin_satir) == gemi1_satir and
                    int(tahmin_sutun) == gemi1_sutun) or (int(tahmin_satir) == gemi2_satir and int(tahmin_sutun) == gemi2_sutun):
                    if board[int(tahmin_satir) - 1][int(tahmin_sutun) - 1] == "/":
                        print("-" * 65)
                        print("Zaten tahmin ettiniz")
                        print(puan)
                    else:
                        print("-" * 65)
                        print("Tebrikler, gemiyi batırdınız!")
                        board[int(tahmin_satir) - 1][int(tahmin_sutun) - 1] = "/"
                        print("Puanınız : ", puan)
                        print("-" * 65)
                        sayac += 1
                        if sayac == 3:
                            print("-" * 65)
                            print("Tebrikler, bütün gemileri batırdınız ve oyunu kazadınız!")
                            print("-" * 65)
                            tekrar_ya_da_çıkış = input("\nOyunu yeniden oynamak için 'again', oyundan çıkmak için 'exit' yazınız : ")
                            if (tekrar_ya_da_çıkış == "again"):
                                continue
                            elif (tekrar_ya_da_çıkış == "exit"):
                                quit()
                            else:
                                print("\nDüzgün girdi yazmadığınız için oyun otomatik olarak kapanacak.")
                                sleep(3)
                                quit()
                else:
                    if (int(tahmin_satir) < 0 or int(tahmin_sutun) < 0) or (int(tahmin_satir) > 5 or int(tahmin_sutun) > 5):
                        print("-" * 65)
                        print("Alan sınırları dışında değer girdiniz")
                        print("-" * 65)
                    elif board[int(tahmin_satir) - 1][int(tahmin_sutun) - 1] == "X":
                        print("-" * 65)
                        print("Zaten tahmin ettiniz")
                        print("-" * 65)
                    else:
                        print("-" * 65)
                        print("Vuramadınız")
                        board[int(tahmin_satir) - 1][int(tahmin_sutun) - 1] = "X"
                        puan -= 10
                        print("Puanınız : ", puan)
                        print("-" * 65)
            elif tahmin_sutun == "exit":
                print("-" * 65)
                print("Oyundan çıkıldı")
                print("-" * 65)
                quit()
            else:
                print("-" * 65)
                print("Lütfen sütunu 1'den 5'e kadar bir tam sayı olarak seçiniz.")
                print("-" * 65)
        elif tahmin_satir == "exit":
            print("-" * 65)
            print("Oyundan çıkıldı")
            print("-" * 65)
            quit()
        else:
            print("-" * 65)
            print("Lütfen satırı 1'den 5'e kadar bir tam sayı olarak seçiniz.")
            print("-" * 65)
