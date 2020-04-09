import xlrd
from PIL import Image, ImageDraw, ImageFont

alphabet = {
    "あ": "a",
    "い": "i",
    "う": "u",
    "え": "e",
    "お": "o",
    "か": "ka",
    "き": "ki",
    "く": "ku",
    "け": "ke",
    "こ": "ko",
    "さ": "sa",
    "し": "shi",
    "す": "su",
    "せ": "se",
    "そ": "so",
    "た": "ta",
    "ち": "chi",
    "つ": "tsu",
    "て": "te",
    "と": "to",
    "な": "na",
    "に": "ni",
    "ぬ": "nu",
    "ね": "ne",
    "の": "no",
    "は": "ha",
    "ひ": "hi",
    "ふ": "fu",
    "へ": "he",
    "ほ": "ho",
    "ま": "ma",
    "み": "mi",
    "む": "mu",
    "め": "me",
    "も": "mo",
    "や": "ya",
    "ゆ": "yu",
    "よ": "yo",
    "ら": "ra",
    "り": "ri",
    "る": "ru",
    "れ": "re",
    "ろ": "ro",
    "わ": "wa",
    "を": "wo",
    "ん": "n",
}

#List to hold names of students we pull from the excel spreadsheet
hiragana_student_names = []

#List to hold the English version names of students after they are converted
english_student_names = []


#Open spreadsheet containing names. Example of list of names
# Column A
# はると
# そうた
# ゆうと
# はるき
# りく
# さくら
student_names_spreadsheet = xlrd.open_workbook("hiraganaNames.xlsx")
#Open Sheet 0. Since My spreadsheet only had one sheet, I opened the first one
sheet = student_names_spreadsheet.sheet_by_index(0)

#Iterate through the rows in the column and add each student name to the list
for name in sheet.col(0):
    hiragana_student_names.append(name.value)

#Iterate through the Hiragana names and convert them to the English Names
for name in hiragana_student_names:
    english_name = ""
    for letter in name:
        english_name = english_name + alphabet[letter]
    english_student_names.append(english_name)


#Create a blank white canvas that is 2480 pixels wide and 3508 pixels long
image = Image.new(mode="RGB", size=(2480, 3508), color="white")
draw = ImageDraw.Draw(image)

#Set the font to comic sans and font size to 72
text_font = ImageFont.truetype("comic.ttf", 72)

#A 4x4 grid based on the above canvas size to populate the names
name_positions = [(240, 400),  (860, 400),  (1470, 400),  (2080, 400),
                  (240, 1200), (860, 1200), (1470, 1200), (2080, 1200),
                  (240, 2000), (860, 2000), (1470, 2000), (2080, 2000),
                  (240, 2800), (860, 2800), (1470, 2800), (2080, 2800)]


#For each of the 16 students in my spreadsheet, put each one in the corresponding grid location
counter = 0
for name in english_student_names:
    draw.text(name_positions[counter], name, font=text_font, fill="black")
    counter = counter + 1
    
#Generate the text    
draw.text

#Save the image file to a file named img0.png
image.save("img0.png")


