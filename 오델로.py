from tkinter import *
import time


# TK 생성
w = Tk()
w.geometry("560x640")
w.title("오델로 게임")
Label(w, text = "White :").place( x = 65, y = 590)
Label(w, text = "Black :").place( x = 395, y = 590)
#돌 이미지
black = PhotoImage(file = "black.png")
white = PhotoImage(file = "white.png")

#현재 턴 표시 및 현재 돌의 개수
class Now:
    def __init__(self):
        self.id = Label(w, image = black)
        self.id.place( x = 245, y = 570)
        self.id2 = Label(w, text = "2")
        self.id2.place( x = 115, y = 590)
        self.id3 = Label(w, text = "2")
        self.id3.place( x = 445, y = 590)
        
        
    def update(self, turn):
        w = 0
        b = 0
        for i in range(8):
            w += yorn[i].count(1)
        for i in range(8):
            b += yorn[i].count(2)
        if turn == 1:
            self.id["image"] = white
        if turn == 2:
            self.id["image"] = black
        self.id2["text"] = w
        self.id3["text"] = b
        
        
#오델로 판 만들기
class Othello:
    global yorn
    turn = 2
    yorn = [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]
    #정의
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
        self.id = Button(w, height = 4, width = 9, command = self.pick)
        self.id.place( x = 70 * self.x, y = 70 * self.y)

        self.sta = 0
        yorn[self.x][self.y] = self.sta
    #선택했을때          
    def pick(self):
        
        if self.sta == 0:
            if turn == 1:
                self.id.config(image = white, height = 67, width = 67)
                self.sta = 1
                yorn[self.x][self.y] = self.sta
                
                
            if turn == 2:
                self.id.config(image = black, height = 67, width = 67)
                self.sta = 2
                yorn[self.x][self.y] = self.sta
                
            if Othello.turn == 1:
                Othello.turn = 2
            elif Othello.turn == 2:
                Othello.turn = 1
            self.possible()
        elif self.sta == 1:
            self.id.config(image = black, height = 67, width = 67)
            self.sta = 2
            yorn[self.x][self.y] = self.sta
        elif self.sta == 2:
            self.id.config(image = white, height = 67, width = 67)
            self.sta = 1
            yorn[self.x][self.y] = self.sta
       
    #상태 변경       
    def update(self):
        self.sta = yorn[self.x][self.y]
        if self.sta == 1:
            self.id.config(image = white, height = 67, width = 67)           
        if self.sta == 2:
            self.id.config(image = black, height = 67, width = 67)
    #바꿀 수 있을 때
    def possible(self):
        #밑으로
        reverse = -1
        i = 0
        while (self.y +i < 7):
            i += 1
            reverse += 1
            if(yorn[self.x][self.y +i] == turn):
                i = 7
            elif(yorn[self.x][self.y +i] == 0):
                i = 7
                reverse = -1
        i = 0
        while(i < reverse):
            yorn[self.x][self.y + i+1] = turn
            i += 1
        #위로    
        reverse = -1
        i = 0
        while (self.y  - i > 0):
            i += 1
            reverse += 1
            if(yorn[self.x][self.y  -i] == turn):
                i = 7
            elif(yorn[self.x][self.y  -i] == 0):
                i = 7
                reverse = -1
        i = 0
        print(reverse)
        while(i < reverse):
            yorn[self.x][self.y - i - 1] = turn
            i += 1
        #오른쪽으로
        reverse = -1
        i = 0
        while (self.x +i < 7):
            i += 1
            reverse += 1
            if(yorn[self.x + i][self.y] == turn):
                i = 7
            elif(yorn[self.x + i][self.y] == 0):
                i = 7
                reverse = -1
        i = 0
        while(i < reverse):
            yorn[self.x+i+1][self.y] = turn
            i +=1
        #왼쪽으로    
        reverse = -1
        i = 0
        while (self.x -i > 0):
            i += 1
            reverse += 1
            if(yorn[self.x - i][self.y] == turn):
                i = 7
            elif(yorn[self.x - i][self.y] == 0):
                i = 7
                reverse = -1
        i = 0
        while(i < reverse):
            yorn[self.x - i-1][self.y] = turn
            i +=1
            
        #밑 오 
        reverse = -1
        i = 0
        while (self.x + i < 7 and self.y +i < 7):
            i += 1
            reverse += 1
            if(yorn[self.x + i][self.y + i] == turn):
                i = 7
            elif(yorn[self.x + i][self.y + i] == 0):
                i = 7
                reverse = -1
        i = 0
        while(i < reverse):
            yorn[self.x + i + 1][self.y + i + 1] = turn
            i += 1
        #위 오    
        reverse = -1
        i = 0
        while (self.x + i < 7 and self.y  - i > 0):
            i += 1
            reverse += 1
            if(yorn[self.x + i][self.y  -i] == turn):
                i = 7
            elif(yorn[self.x + i][self.y  -i] == 0):
                i = 7
                reverse = -1
        i = 0
        while(i < reverse):
            yorn[self.x + i + 1][self.y - i - 1] = turn
            i += 1
        #밑 왼
        reverse = -1
        i = 0
        while (self.x -i > 0 and self.y + i < 7):
            i += 1
            reverse += 1
            if(yorn[self.x - i][self.y + i] == turn):
                i = 7
            elif(yorn[self.x - i][self.y + i] == 0):
                i = 7
                reverse = -1
        i = 0
        while(i < reverse):
            yorn[self.x -i-1][self.y + i + 1] = turn
            i +=1
        #위 왼    
        reverse = -1
        i = 0
        while (self.x -i > 0 and self.x - i > 0):
            i += 1
            reverse += 1
            if(yorn[self.x - i][self.y - i] == turn):
                i = 7
            elif(yorn[self.x - i][self.y - i] == 0):
                i = 7
                reverse = -1
        i = 0
        while(i < reverse):
            yorn[self.x - i-1][self.y - i -1] = turn
            i +=1
#버튼 이름 저장할 곳
o = [[0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]]       
        
            
                            

#버튼 생성
for i in range(8):
    for j in range(8):
        o[i][j] = Othello(i, j)
        if (i == 3 and j == 3) or (i == 4 and j == 4):
            o[i][j].sta = 1
            yorn[i][j] = 1
            o[i][j].update()
        elif (i == 4 and j == 3) or (i == 3 and j == 4):
            o[i][j].sta = 2
            yorn[i][j] = 2
            o[i][j].update()            
    



#현재 턴 및 돌의 개수 생성
n = Now()


#게임 시작
while True:
    turn = Othello.turn
    n.update(turn)
    for i in range(8):
        for j in range(8):
            o[i][j].update()
    w.update()
    time.sleep(0.01)
