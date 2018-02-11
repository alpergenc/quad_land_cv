import cv2
import numpy as np

# Renk filtresiyle konum bulma



# TO DO LIST:
# nothing here!

roll_kp=0.01
roll_kd=0.01

pitch_kp=roll_kp
pitch_kd=roll_kd
last_roll_error=0
last_pitch_error=0
counter=0
thr=80
coor_x=0
coor_y=0
lowh = 0
high = 49
lows = 0
higs = 136
lowv = 0
higv = 51


print "Start"
cap = cv2.VideoCapture(1)


fr = 1  # bool first run
while 1:

    ret, frame = cap.read()
    imgOriginal = frame
    img = frame

    if(fr):
        rows, cols,at = frame.shape
        center_y = rows / 2
        center_x = cols / 2
        font = cv2.FONT_HERSHEY_SIMPLEX
        d = np.array([lowh, lows, lowv])
        t = np.array([high, higs, higv])


    fr = 0   # baslangic degiskeni 0 oldu


    filt=cv2.inRange(img, d, t)

    y=0
    x=0
    y_c=0
    x_c=0
    tt=0





    while(y<rows):
        while(x<cols):
            if(filt[y,x]>5):
                y_c=y+y_c
                x_c=x+x_c
                tt=tt+1
            x+=3

        x=0
        y+=3

    if(tt<thr):
        tt=1
        counter+=1
        if(counter>20):
            print "LOST"
            while 1:
                print "land"



    else:
        coor_y = y_c / tt
        coor_x = x_c / tt
        counter=0


    print coor_y   #y
    print coor_x  #x





    roll_error=(coor_x-center_x)
    pitch_error=(coor_y-center_y)

    roll=roll_error*roll_kp+(last_roll_error-roll_error)*roll_kd
    pitch=pitch_error*pitch_kp+(last_pitch_error-pitch_error)*pitch_kd

    last_roll_error=roll_error

    last_pitch_error=pitch_error






    """
    if(coor_x>center_x):
        print "sagda"

    if(coor_x<center_x):
        print "solda"

    if(coor_y>center_y):
        print "asagida"

    if(coor_y<center_y):
        print "yukarida"
    """

    print int(roll)



    cv2.putText(imgOriginal,
                ".",
                (coor_x, coor_y), font, 2,
                (255, 255, 5), 2, cv2.LINE_AA) #coordinates

    cv2.imshow('detected circles', imgOriginal)
    cv2.waitKey(1)

cv2.destroyAllWindows()