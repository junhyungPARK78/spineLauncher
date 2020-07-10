import os
import platform
import pickle
import tkinter as tk

import resources.optionSetting as optionSetting

# # 현재 운영체제 알아내기
# thisPlatform = platform.system() # 「Darwin」은 맥이다.「Windows」는 윈도우즈.

def Main(): # [함수] 지정된 폴더에 spine 파일이 없을 때 처리하는 방법
    window = tk.Tk()
    window.title("ERROR")
    window.geometry("500x200+300+300")

    textError = """
    spine이 설치되어 있지 않거나,
    경로 설정이 잘못되어 있습니다.

    이 창을 닫고
    「spine path seting」에서 설정해주세요."""

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
