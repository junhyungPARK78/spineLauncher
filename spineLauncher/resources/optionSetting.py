import os
import platform
import pickle
import tkinter as tk

# 現在のオペレーティングシステム調べる
thisPlatform = platform.system() # 「Darwin」：Mac、「Windows」：windows。

def Main(): # 【関数】設定ファイル用のGUI
    resourcesFolder = os.path.abspath("resources") # resources フォルダーの経路
    settingSaveFile = "settingSave.bin" # 設定のセーブのファイル

    def OptionOkClick(): # 【関数】設定のファイルを作る

        # セーブファイルを作る（Windows）
        if thisPlatform == "Windows":
            with open(os.path.join(resourcesFolder, settingSaveFile), 'rb') as f:
                spinePathDictionary = pickle.load(f)

                # path オプションのセーブの文言を作る
                spinePathInput = entryOptionInput.get()
                # print(spinePathInput)
                if spinePathInput[0] == "\"":
                    spinePathInput = spinePathInput[1:]
                if spinePathInput[-1] == "\"":
                    spinePathInput = spinePathInput[:-1]
                # print(spinePathInput)
                spinePathInput = os.path.dirname(spinePathInput)
                spinePathInput = "\"" + spinePathInput + "\\Spine.exe\" -u"
                spinePathDictionary["spinePathWindows"] = spinePathInput

                # セーブファイルを作る
                with open(os.path.join(resourcesFolder, settingSaveFile), 'wb') as f:
                    pickle.dump(spinePathDictionary, f)
                    print(spinePathDictionary)

        # セーブファイルを作る（Mac）
        if thisPlatform == "Darwin":
            with open(os.path.join(resourcesFolder, settingSaveFile), 'rb') as f:
                spinePathDictionary = pickle.load(f)

                # path オプションのセーブの文言を作る
                spinePathInput = entryOptionInput.get()
                if spinePathInput[-1] == "\\":
                    spinePathInput = spinePathInput[:-1]
                spinePathInput = spinePathInput + " -u"
                spinePathDictionary["spinePathDarwin"] = spinePathInput

                # セーブファイルを作る
                with open(os.path.join(resourcesFolder, settingSaveFile), 'wb') as f:
                    pickle.dump(spinePathDictionary, f)
                    print(spinePathDictionary)

        window.destroy()

        return
    
    # 設定をデフォルトに戻す
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
    オプションを修正します。
    ----------------------------------------------------------------------

    ------------------------------------------------------------
    spineの設置のフォルダーをお入力してください。："""
    
    textLine = "------------------------------------------------------------"
    
    textDefault = """
    ------------------------------------------------------------
    オプションをデフォルトに戻します。"""

    labelOptionComment1 = tk.Label(window, \
        text = textHead)
    labelOptionComment1.pack()
        
    entryOptionInput = tk.Entry(window, \
        justify = "right", \
        width = 40)
    entryOptionInput.pack()

    buttonOk = tk.Button(window, \
        text = "入力完了", \
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
        text = "デフォルト", \
        command = SetDefault, \
        width = 20, height = 2)
    buttonDefaultOption.pack()

    labelOptionComment4 = tk.Label(window, \
        text = textLine)
    labelOptionComment4.pack()

    window.mainloop()

if __name__ == '__main__':
    Main()
