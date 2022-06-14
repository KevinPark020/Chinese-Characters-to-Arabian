# 이미지에 있는 한자를 숫자로 바꿔주기

import csv
from pycnnum import cn2num
import cv2
import pytesseract
from PIL import Image

# image안에 있는 text를 한자로 설정
LANG = 'chi_tar'
CONFIG = '--psm 11 --oem 3'


class ImageToChineseConverter:

    __slots__ = ["__filename", "__kanji_list", "__num_list", "__imagename"]

    # 한자 리스트, 숫자 리스트 생성
    def __init__(self):
        self.__kanji_list = []
        self.__num_list = []
        self.__filename = ""
        self.__imagename = ""

    def chinese_converter(self, kanji):
        return cn2num(kanji)

    # 한자 -> 숫자 변환기
    def chinese_converter(self, text):
        return cn2num(text)

    # 이미지가 있는 파일 불러주기(cv로 읽음)
    def image_to_text(self, imagename):
        self.__imagename = imagename
        # image 읽어오기
        img = cv2.imread(imagename)
        chi_letter = pytesseract.image_to_string(img, lang=LANG, config=CONFIG)
        result_num = self.chinese_converter(chi_letter)
        return result_num

    # opencv가 아닌 이미지 파일을 읽어와 변환
    def imagefile_to_text(self, image_filename):
        try:
            img = Image.open(image_filename)
            chi_letter = pytesseract.image_to_string(img, lang=LANG, config=CONFIG)
            result_num = self.chinese_converter(chi_letter)
            return result_num
        except FileNotFoundError as fe:
            print("올바른 이미지 파일이 아닙니다. 다시 입력해주세요.")



        # # 데이터가 있는 파일 불러주기(csv파일)
        # def open_file(self, filename):
        #     self.__filename = filename
        #     try:
        #         with open(filename) as csv_file:
        #             csv_reader = csv.reader(csv_file)
        #             # 첫번째 줄 생략
        #             next(csv_reader)
        #
        #             # TODO: 파일 불러와서 데이터(한자)를 kanji_list에 넣어주기
        #
        #     except FileNotFoundError as fe:
        #         print("올바른 CSV 파일이 아닙니다. 다시 입력해주세요.")













