import cv2
from cvzone.HandTrackingModule import HandDetector
from time import sleep
from pynput.keyboard import Controller

cap = cv2.VideoCapture(0)
cap.set(3, 1366)
cap.set(4, 768)
detector = HandDetector(detectionCon = 0.6)

Keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "{", "}"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";", '"', "\\"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"],
        [" "]]



ClickedText = ""
Keyboard = Controller()


def drawAll(img, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cv2.rectangle(img, button.pos, (x + w, y + h), (0, 0, 0), cv2.FILLED)
        cv2.putText(img, button.text, (x + 15, y + 60), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 255, 255), 3)
    return img


class Botton():
    def __init__(self, pos, text, size=[70, 70]):
        self.pos = pos
        self.text = text
        self.size = size
        # x, y = self.pos
        # w, h = self.size
        # cv2.rectangle(img, self.pos, (x + w, y + h), (0, 0, 0), cv2.FILLED)
        # cv2.putText(img, self.text, (x + 20, y + 78), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 5)


# myButton = Botton([100, 70], 'Q')
# myButton1 = Botton([200, 70], 'W')
# myButton2 = Botton([300, 70], 'E')
# myButton3 = Botton([400, 70], 'R')
buttonList = []
for i in range(len(Keys)):
    for j, key in enumerate(Keys[i]):
        buttonList.append(Botton([100 * j + 50, 100 * i + 50], key))

while True:
    success, img = cap.read()
    img = cv2.flip(img, 180)
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)
    drawAll(img, buttonList)

    if lmList:
        for button in buttonList:
            x,y = button.pos
            w,h = button.size
            if x<lmList[8][0]<x+w and y<lmList[8][1]< y+h:
                cv2.rectangle(img, button.pos, (x + w, y + h), (255, 168, 0), cv2.FILLED)
                cv2.putText(img, button.text, (x + 15, y + 60), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 255, 255), 3)
                l, _,_ = detector.findDistance(4, 8, img)
                # print(l)
                if l<50:
                    Keyboard.press(button.text)
                    cv2.rectangle(img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, button.text, (x + 15, y + 60), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 255, 255), 3)
                    ClickedText += button.text
                    sleep(0.5)

    cv2.rectangle(img, (55, 345), (700, 450), (0, 0, 0), cv2.FILLED)
    cv2.putText(img, ClickedText, (60, 425), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 255, 255), 3)
    # cv2.rectangle(img,(100, 100), (200, 200), (0, 0, 0),  cv2.FILLED)
    # cv2.putText(img, "Q", (120, 180), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255), 5)

    # img = myButton.draw(img)
    # img = myButton1.draw(img)
    # img = myButton2.draw(img)
    # img = myButton3.draw(img)

    # imgResize = cv2.resize(img, (960, 540))
    cv2.imshow('Camera', img)
    cv2.waitKey(1)