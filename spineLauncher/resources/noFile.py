import os
import platform
import pickle
import tkinter as tk

import resources.optionSetting as optionSetting

def Main(): # 【関数】指定されたフォルダーにspineの実行ファイルがない場合の処理
    window = tk.Tk()
    window.title("ERROR")
    window.geometry("500x200+300+300")

    textError = """
    spineが設置されたいないか、
    経路の設定が間違っています。

    このウィンドウを閉じて、
    「spine path seting」から設定してください。"""

    messageError = tk.Message(window, \
        anchor = "center", \
        text = textError, \
        width = 400, \
        padx = 20, \
        pady = 20)
    messageError.pack()

    buttonOK = tk.Button(window, \
        text = "OK", \
        command = lambda : ClickOK(), \
        width = 20, height = 2)
    buttonOK.pack(pady = 10)

    def ClickOK():
        window.destroy()

    window.mainloop()



if __name__ == '__main__':
    Main()
