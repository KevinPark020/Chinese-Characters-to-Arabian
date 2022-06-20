"""
한문 이미지를 숫자로 변환
authority of ktaepark72@gmail.com
"""

import csv
from pycnnum import cn2num
import cv2
import pytesseract
from PIL import Image

# image에 있는 text 한자로 설정
LANG = 'chi_tra'

# 숫자 하나만 인식
CONFIG_ONE_LETTER = '--psm 8'

# 이미지 파일 안에 모든걸 다 변환
CONFIG_ALL_LETTER = '--psm 6'

# 이미지가 수직으로 나열되어 있을 경우
CONFIG_VERTICAL = '--psm 5'

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"


class ImageToChineseConverter:

    __slots__ = ["__filename", "__kanji_list", "__num_list", "__imagename"]

    # 한자 리스트, 숫자 리스트 생성
    def __init__(self):
        self.__kanji_list = []
        self.__num_list = []
        self.__filename = ""
        self.__imagename = ""

    # 한자 -> 숫자 변환기
    def chinese_converter(self, text):
        string = ""
        for letters in text:
            if(letters != '\n'):
                string = string + letters
        return cn2num(string)

    # 이미지가 있는 파일 불러주기(cv로 읽음)
    def image_to_textNum(self, imagename):
        try:
            self.__imagename = imagename
            # image 읽어오기
            img = cv2.imread(imagename)
            chi_letter = pytesseract.image_to_string(img, lang=LANG)
            print(chi_letter)
            result_num = self.chinese_converter(chi_letter)
            return result_num
        except FileNotFoundError as te:
            print("올바른 이미지를 불러와주세요.")

    # opencv가 아닌 이미지 파일을 읽어와 변환
    def imagefile_to_textNum(self, image_filename):
        try:
            img = Image.open(image_filename)
            chi_letter = pytesseract.image_to_string(img, lang=LANG, config=CONFIG_ALL_LETTER)
            print(chi_letter)
            result_num = self.chinese_converter(chi_letter)
            return result_num
        except FileNotFoundError as fe:
            print("올바른 이미지 파일이 아닙니다. 다시 입력해주세요.")











