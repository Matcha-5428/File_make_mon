# Coding : utf-8

# version
ver = "version : 1,1"

# Module
import os
from time import sleep
import tkinter
from tkinter import messagebox
import sys

a = 1

def run(ok_button):
    ret = messagebox.askyesno('確認', 'この操作は取り消せません。本当に実行してよろしいですか？')
    if ret == True:
        print("プログラムを実行中")
        sleep(0.5)
        print("値を取得中")
        sleep(0.1)

        file_path = file_pass.get()
        name = file_name.get()
        file_ex = file_extension.get()
        volume = file_vol.get()
        write = file_text.get()

        print(file_path)
        print(name)
        print(file_ex)
        print(volume)
        print(write)

        if write == "中に記載する文字列（任意）":
            write = "　"

        for i in range(int(volume)):
            def make():
                global a
                sleep(0.05)
                print("パッチを作成しました。")

                f = open(main_path, 'w')
                f.write(write)
                f.close()

                print("ファイル作成が完了しました。")
                a = a + 1

            main_path = file_path + "/" + name + str(a) + "." + file_ex
            print(main_path)
            print("メインパッチです")

            print("パッチを作成中")

            make()

        messagebox.showinfo('完了', '正常にファイルが作成されました。')
        ret = messagebox.askyesno('確認', '終了しますか？')
        if ret == True:
            sys.exit()
    else:
        sys.exit()

# Window
root = tkinter.Tk()
root.geometry("600x400")
root.resizable(0, 0)
root.title("ファイル作成マン")

head_1 = tkinter.Label(text="基本情報", font=("MSゴシック","30","bold"))
head_1.pack()

file_pass = tkinter.Entry(width=100)
file_pass.insert(tkinter.END,"ファイルを作成する場所のパス（フルパスで）")
file_pass.pack()

file_name = tkinter.Entry(width=100)
file_name.insert(tkinter.END,"ファイルの名前")
file_name.pack()

file_extension = tkinter.Entry(width=100)
file_extension.insert(tkinter.END,"ファイルの拡張子(ピリオドは省略)")
file_extension.pack()

file_vol = tkinter.Entry(width=100)
file_vol.insert(tkinter.END,"作成するファイルの数（半角英数で入力）")
file_vol.pack()

file_text = tkinter.Entry(width=100)
file_text.insert(tkinter.END,"中に記載する文字列（任意）")
file_text.pack()

ok_button = tkinter.Button(text="作成", width=100, height=3)
ok_button.bind("<Button-1>", run)
ok_button.pack()

head_2 = tkinter.Label(text="間違いがないか確認してください。")
head_2.pack()

head_3 = tkinter.Label(text="　　　")
head_3.pack()

head_4 = tkinter.Label(text="　　　")
head_4.pack()

head_5 = tkinter.Label(text=ver)
head_5.pack()



root.mainloop()





