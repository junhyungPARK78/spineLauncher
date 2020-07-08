import platform
import pickle
import tkinter as tk

# 현재 운영체제 알아내기
thisPlatform = platform.system() # 「Darwin」은 맥이다.「Windows」는 윈도우즈.

# [함수] 세팅 파일용 GUI
def OptionSetting():
    # [함수] 세팅 파일 만들기
    def optionOkClick():
        # 세이브 내용이 담겨있는 Dictionary
        spinePathDictionary = {}

        # 윈도우 용 세이브 파일 만들기
        if thisPlatform == "Windows":
            with open("./resources/settingSave.bin", 'rb') as f:
                spinePathDictionary = pickle.load(f)

                # path 옵션 세이브 문구 만들기
                spinePathInput = entryOptionInput.get()
                if spinePathInput[-1] == "\\":
                    spinePathInput = spinePathInput[:-1]
                spinePathInput = f"\"{spinePathInput}\\Spine.exe\" -u"
                spinePathDictionary["spinePathWindows"] = spinePathInput

                # 세이브 파일 작성하기
                with open("./resources/settingSave.bin", 'wb') as f:
                    pickle.dump(spinePathDictionary, f)
                    print(spinePathDictionary)

        # 맥 용 세이브 파일 만들기
        if thisPlatform == "Darwin":
            with open("./resources/settingSave.bin", 'rb') as f:
                spinePathDictionary = pickle.load(f)

                # path 옵션 세이브 문구 만들기
                spinePathInput = entryOptionInput.get()
                if spinePathInput[-1] == "\\":
                    spinePathInput = spinePathInput[:-1]
                spinePathInput = f"{spinePathInput} -u"
                spinePathDictionary["spinePathMac"] = spinePathInput

                # 세이브 파일 작성하기
                with open("./resources/settingSave.bin", 'wb') as f:
                    pickle.dump(spinePathDictionary, f)
                    print(spinePathDictionary)

        window.destroy()

        return

    window = tk.Tk()
    window.title("Option")
    window.geometry("500x420+300+200")

    textHead = """
    ----------------------------------------------------------------------
    옵션을 수정합니다.
    ----------------------------------------------------------------------

    ------------------------------------------------------------
    spine의 설치 폴더를 입력해주세요. : """
    textLine = "------------------------------------------------------------"
    textDefault = """
    ------------------------------------------------------------
    옵션을 디폴트 치로 되돌립니다."""

    labelOptionComment1 = tk.Label(window, text = textHead)
    labelOptionComment1.pack()
        
    entryOptionInput = tk.Entry(window, justify = "right", width = 40)
    entryOptionInput.pack()

    buttonOk = tk.Button(window, text = "입력 완료", command = optionOkClick, width = 30, height = 3)
    buttonOk.pack()

    labelOptionComment2 = tk.Label(window, text = textLine)
    labelOptionComment2.pack()

    labelOptionComment3 = tk.Label(window, text = textDefault)
    labelOptionComment3.pack()

    buttonDefaultOption = tk.Button(window, text = "Default", width = 20, height = 2)
    buttonDefaultOption.pack()

    labelOptionComment4 = tk.Label(window, text = textLine)
    labelOptionComment4.pack()

    window.mainloop()

if __name__ == '__main__':
    OptionSetting()
