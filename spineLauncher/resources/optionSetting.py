import os
import os.path
import sys
import platform
import tkinter as tk

# [함수] 세팅 파일용 GUI
def OptionSetting():
    # [함수] 세팅 파일 만들기
    def optionOkClick():
        spinePathInput = optionInput.get()
        if spinePathInput[-1] == "\\":
            spinePathInput = spinePathInput[:-1]

        spinePathInput = f"\"{spinePathInput}\\Spine.exe\" -u"

        with open("./resources/settingForWindows.txt", 'w') as f:
            f.write(spinePathInput)

        window.destroy()

        return

    window = tk.Tk()
    window.title("Option")
    optionComment1 = tk.Label(window, text = "spine의 설치 폴더를 입력해주세요. : ")
    optionComment1.grid(row = 0, column = 0)
        
    optionInput = tk.Entry(window, justify = "right", width = 20)
    optionInput.grid(row = 1, column = 0)

    okButton = tk.Button(window, text = "    OK    ", command = optionOkClick)
    okButton.grid(row = 2, column = 0)

    window.mainloop()
