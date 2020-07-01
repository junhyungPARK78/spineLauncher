"""
버전을 선택해서 실행하게 만드는 방법
    먼저 맥 기준으로 만든다.
"""

import os, sys
import platform

# start = "/Applications/Spine/Spine.app/Contents/MacOS/Spine -u 3.6.53"
# # “C:\Program Files (x86)\Spine\Spine.exe” -u 3.6.53
# # /Applications/Spine/Spine.app/Contents/MacOS/Spine -u 3.6.53
# os.system(start)

print(platform.system()) # 「Darwin」은 맥이다.「Windows」는 윈도우즈.
