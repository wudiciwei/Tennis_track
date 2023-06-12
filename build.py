# @Time : 18:12
# @Author : Yao Zhao
# @File:  build
# All the code was done by Yao Zhao, a PhD student of Hong Kong Polytechnic University(Polyu)
# you can connect me by E-mail
# 22117696r@connect.polyu.hk
import PyInstaller.__main__

PyInstaller.__main__.run([
    'Frame.py',
    '--onefile',
    '--windowed',
    '--icon=tennis.jpg'
])
