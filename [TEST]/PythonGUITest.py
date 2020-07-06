import os
import os.path
import sys
import platform
import tkinter as tk

def okClick():
    input2 = input1.get()
    print(f"adad {input2}")
    # # 이때까지 모인 정보로 spine 실행시키기
    # start = "/Applications/Spine/Spine.app/Contents/MacOS/Spine -u 3.6.53"
    # # “C:\Program Files (x86)\Spine\Spine.exe” -u 3.6.53
    # # /Applications/Spine/Spine.app/Contents/MacOS/Spine -u 3.6.53
    # os.system(start)
    window.destroy()

window = tk.Tk()
window.title("Sample")

hello_world = tk.Label(window, text = "Hello World!")
hello_world.grid(row = 0, column = 0)

input1 = tk.Entry(window, justify = "right", width = 20)
input1.grid(row = 0, column = 1)

button1 = tk.Button(window, text = "  OK  ", command=okClick)
button1.grid(row = 1, column = 1)

window.mainloop()







# window = tk.Tk()
# window.title("Option")
# optionComment1 = tk.Label(window, text = "spine의 설치 폴더를 입력해주세요. : ")
# optionComment1.grid(row = 0, column = 0)

# optionInput = tk.Entry(window, justify = "right", width = 20)
# optionInput.grid(row = 1, column = 0)

# okButton = tk.Button(window, text = "  OK  ", command=okClick)
# okButton.grid(row = 2, column = 0)

