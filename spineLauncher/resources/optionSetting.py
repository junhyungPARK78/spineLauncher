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
                spinePathInput = optionInput.get()
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
                spinePathInput = optionInput.get()
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
    window.geometry("420x300+200+100")
    optionComment1 = tk.Label(window, text = "spine의 설치 폴더를 입력해주세요. : ")
    optionComment1.grid(row = 0, column = 0)
        
    optionInput = tk.Entry(window, justify = "right", width = 20)
    optionInput.grid(row = 1, column = 0)

    okButton = tk.Button(window, text = "    OK    ", command = optionOkClick)
    okButton.grid(row = 2, column = 0)

    window.mainloop()
