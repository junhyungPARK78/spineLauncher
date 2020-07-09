import os
import platform
import pickle
import tkinter as tk

# 현재 운영체제 알아내기
thisPlatform = platform.system() # 「Darwin」은 맥이다.「Windows」는 윈도우즈.

def Main(): # [함수] 세팅 파일용 GUI
    resourcesFolder = os.path.join(".", "resources") # resources 폴더 경로
    settingSaveFile = "settingSave.bin" # 세팅 세이브 파일

    def OptionOkClick(): # [함수] 세팅 파일 만들기

        # 윈도우 용 세이브 파일 만들기
        if thisPlatform == "Windows":
            with open(os.path.join(resourcesFolder, settingSaveFile), 'rb') as f:
                spinePathDictionary = pickle.load(f)

                # path 옵션 세이브 문구 만들기
                spinePathInput = entryOptionInput.get()
                if spinePathInput[-1] == "\\":
                    spinePathInput = spinePathInput[:-1]
                spinePathInput = f"\"{spinePathInput}\\Spine.exe\" -u"
                spinePathDictionary["spinePathWindows"] = spinePathInput

                # 세이브 파일 작성하기
                with open(os.path.join(resourcesFolder, settingSaveFile), 'wb') as f:
                    pickle.dump(spinePathDictionary, f)
                    print(spinePathDictionary)

        # 맥 용 세이브 파일 만들기
        if thisPlatform == "Darwin":
            with open(os.path.join(resourcesFolder, settingSaveFile), 'rb') as f:
                spinePathDictionary = pickle.load(f)

                # path 옵션 세이브 문구 만들기
                spinePathInput = entryOptionInput.get()
                if spinePathInput[-1] == "\\":
                    spinePathInput = spinePathInput[:-1]
                spinePathInput = f"{spinePathInput} -u"
                spinePathDictionary["spinePathDarwin"] = spinePathInput

                # 세이브 파일 작성하기
                with open(os.path.join(resourcesFolder, settingSaveFile), 'wb') as f:
                    pickle.dump(spinePathDictionary, f)
                    print(spinePathDictionary)

        window.destroy()

        return
    
    # 설정을 디폴트로 돌리기
    def SetDefault():
        defaultSettingDictionary = \
            {'spinePathWindows':'“C:\\Program Files (x86)\\Spine\\Spine.exe” -u', 'spinePathDarwin':'/Applications/Spine/Spine.app/Contents/MacOS/Spine -u'}
        with open(os.path.join(resourcesFolder, settingSaveFile), 'wb') as f:
            pickle.dump(defaultSettingDictionary, f)
            print(defaultSettingDictionary)
        
        window.destroy()

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

    labelOptionComment1 = tk.Label(window, \
        text = textHead)
    labelOptionComment1.pack()
        
    entryOptionInput = tk.Entry(window, \
        justify = "right", \
        width = 40)
    entryOptionInput.pack()

    buttonOk = tk.Button(window, \
        text = "입력 완료", \
        command = OptionOkClick, \
        width = 30, height = 3)
    buttonOk.pack()

    labelOptionComment2 = tk.Label(window, \
        text = textLine)
    labelOptionComment2.pack()

    labelOptionComment3 = tk.Label(window, \
        text = textDefault)
    labelOptionComment3.pack()

    buttonDefaultOption = tk.Button(window, \
        text = "Default", \
        command = SetDefault, \
        width = 20, height = 2)
    buttonDefaultOption.pack()

    labelOptionComment4 = tk.Label(window, \
        text = textLine)
    labelOptionComment4.pack()

    window.mainloop()

if __name__ == '__main__':
    Main()
