import math
import re
import sys
import cv2
import keyboard
import pyautogui
import pytesseract
from PIL import ImageGrab
def main():
    while True:
        if keyboard.is_pressed('space'):
            print("游戏结束")
            sys.exit()
        ImageGrab.grab(bbox=(100, 300, 450, 450)).save("screenshot.png")
        pytesseract.pytesseract.tesseract_cmd = r'F:\tesseract\tesseract.exe'
        img = cv2.imread("screenshot.png")
        img = cv2.cvtColor( img, cv2.COLOR_BGR2GRAY)
        s, threshold = cv2.threshold(img, 150,100, cv2.THRESH_BINARY)
        result = pytesseract.image_to_string(threshold, config='--psm 7').split('?')
        try:
            result[0] = result[0].strip()
            result[1] = result[1].strip()
            result[1] = re.findall('\d+', result[1])[0]
            print(result)
            if result[0] == '0':
                result[0] = 0
            if result[1] == '0':
                result[1] = 0
            num1 = math.floor(float(result[0]))
            num2 = math.floor(float(result[1]))
            pyautogui.moveTo(277, 700,duration=0.1)
            if num1 > num2:
                pyautogui.mouseDown()
                pyautogui.move(100,100,duration=0.1)
                pyautogui.move(-100,100,duration=0.1)
                pyautogui.mouseUp()
                print(f"{num1} > {num2}")
            else:
                pyautogui.mouseDown()
                pyautogui.move(-100, 100, duration=0.1)
                pyautogui.move(100, 100, duration=0.1)
                pyautogui.mouseUp()
                print(f"{num1} < {num2}")
        except ValueError as e:
            print("未识别到内容")
        except Exception as e:
            print("未识别到内容")
if __name__ == '__main__':
    main()

