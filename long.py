from tkinter import *
from time import sleep
from PIL import ImageTk, Image
from threading import Thread
from random import randrange, randint
img = [0 for i in range(9)]
game = Tk()
game.title("3 Con Long Lợn")
game.iconbitmap('ico_01_X5H_icon.ico')

canvas = Canvas(master=game, width=640, height=320, background="#fff")
canvas.pack()

img[0] = ImageTk.PhotoImage(Image.open("long3-01.png").resize((60,63)))
img[1] = ImageTk.PhotoImage(Image.open("long2-01.png").resize((60,63)))
img[2] = ImageTk.PhotoImage(Image.open("long1-01.png").resize((60,63)))
img[3] = ImageTk.PhotoImage(Image.open("may1.png").resize((120,120)))
img[4] = ImageTk.PhotoImage(Image.open("may2.png").resize((120,120)))
img[5] = ImageTk.PhotoImage(Image.open("duong-01.png").resize((642,321)))
img[6] = ImageTk.PhotoImage(Image.open("truPhanCach-01.png").resize((60, 60)))
img[7] = ImageTk.PhotoImage(Image.open("truPhanCach-02.png").resize((60, 60)))
img[8] = ImageTk.PhotoImage(Image.open("truPhanCach-03.png").resize((60, 60)))

diem = canvas.create_text(580, 20, text="Điểm: ", fill="red", font=('Times New Roman', 14))
cloud_1 = canvas.create_image(650, 5, anchor=NW, image=img[3])
cloud_2 = canvas.create_image(650, 10, anchor=NW, image=img[4])
road_1 = canvas.create_image(0, 0, anchor=NW, image=img[5])
road_2 = canvas.create_image(640, 0, anchor=NW, image=img[5])
dinosaurs_1 = canvas.create_image(50,255, anchor=NW, image=img[0])
trafficCones_1 = canvas.create_image(650,260, anchor=NW, image=img[6])
trafficCones_2 = canvas.create_image(950,260, anchor=NW, image=img[7])
trafficCones_3 = canvas.create_image(1200,261, anchor=NW, image=img[8])
canvas.update()

def may():
    global cloud_1
    global cloud_2
    global road_2
    global road_1
    while True:
        canvas.move(cloud_2, -0.3, 0)
        canvas.update()
        if canvas.coords(cloud_2)[0] < -120:
            canvas.delete(cloud_2)
            canvas.update()
            cloud_2 = canvas.create_image(650, 10, anchor=NW, image=img[4])
            canvas.update()
        canvas.move(cloud_1, -0.4, 0)
        canvas.update()
        if canvas.coords(cloud_1)[0] < -120:
            canvas.delete(cloud_1)
            canvas.update()
            cloud_1 = canvas.create_image(650, 10, anchor=NW, image=img[3])
            canvas.update()

def chuongNgaiVat():
    global road_2
    global road_1
    global trafficCones_1
    global trafficCones_2
    global trafficCones_3
    speed = -1.3 
    while True:
        a = randint(0, 1)
        b = randint(0, 1)  
        canvas.move(trafficCones_1, speed, 0)
        canvas.move(trafficCones_2, speed, 0) 
        canvas.move(trafficCones_3, speed, 0) 
        canvas.move(road_1, speed, 0)
        canvas.move(road_2, speed, 0)
        canvas.update()
        
        if canvas.coords(road_1)[0] < -640:
            canvas.delete(road_1)
            road_1 = canvas.create_image(640, 0, anchor=NW, image=img[5])
            canvas.update()
        if canvas.coords(road_2)[0] < -640:
            canvas.delete(road_2)
            road_2 = canvas.create_image(640, 0, anchor=NW, image=img[5])
            canvas.update()

            if canvas.coords(trafficCones_1)[0] < -30 and a == True:
                canvas.delete(trafficCones_1)
                trafficCones_1 = canvas.create_image(randrange(640,800,20), 260, anchor=NW, image=img[6])
                canvas.update()
            if canvas.coords(trafficCones_2)[0] < -30 and b == True:
                canvas.delete(trafficCones_2)
                trafficCones_2 = canvas.create_image(randrange(850,900,50), 260, anchor=NW, image=img[7])
                canvas.update()
            if canvas.coords(trafficCones_3)[0] < -30 and a == False and b == False:
                canvas.delete(trafficCones_3)
                trafficCones_3 = canvas.create_image(randrange(750,1000,30), 260, anchor=NW, image=img[8])
                canvas.update()
            if canvas.coords(trafficCones_3)[0] < -30 and a == False and b == True:
                canvas.delete(trafficCones_3)
                trafficCones_3 = canvas.create_image(randrange(750,1100,30), 260, anchor=NW, image=img[8])
                canvas.update()
            
        

def khungLong():
    global dinosaurs_1
    global dinosaurs_2
    global dinosaurs_3
    while True:
        dinosaurs_1 = canvas.create_image(50,255, anchor=NW, image=img[0])
        canvas.update()
        sleep(0.07)
        dinosaurs_2 = canvas.create_image(50,255, anchor=NW, image=img[1])
        canvas.delete(dinosaurs_1)
        canvas.update()
        sleep(0.07)
        dinosaurs_3 = canvas.create_image(50,255, anchor=NW, image=img[2])
        canvas.delete(dinosaurs_2)
        canvas.update()
        sleep(0.07)
        canvas.delete(dinosaurs_3)

def jump():
    for i in range(0, 30):
        canvas.move(dinosaurs_1, 0, 1)
        canvas.update()
        canvas.move(dinosaurs_2, 0, 1)
        canvas.update()
        canvas.move(dinosaurs_3, 0, 1)
        canvas.update()
    sleep(1)
    for i in range (0, 30):
        canvas.move(dinosaurs_1, 0, -1)
        canvas.update()
        canvas.move(dinosaurs_2, 0, -1)
        canvas.update()
        canvas.move(dinosaurs_3, 0, -1)
        canvas.update()
        
def keyPress(event):
    if event.keysym == 'space':
        jump()

canvas.bind_all('<KeyPress>', keyPress)
gameOver = False
moveCloud = Thread(target = may)
moveCloud.start()
moveObstacles = Thread(target = chuongNgaiVat)
moveObstacles.start()
moveDinosaurs = Thread(target = khungLong)
moveDinosaurs.start()
game.mainloop()