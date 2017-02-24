import ctypes
import requests
import os
import threading

def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def set_background():
    drive = "C:\\"
    folder = "images"
    image = "background.bmp"
    image_path = os.path.join(drive, folder, image)
    r = requests.get('https://unsplash.it/1920/1080?random')
    if r.status_code == 200:
        with open(image_path,'wb') as f:
            for chunk in r:
                f.write(chunk)
        SDI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoA(
                            SDI_SETDESKWALLPAPER,
                            0,
                            image_path,
                            3)
    return r.status_code

set_interval(set_background,30)
