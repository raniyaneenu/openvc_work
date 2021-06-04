from django.shortcuts import render,redirect
from django.http import HttpResponse

# Create your views here.

#to detect blue color...

def blue_det(request):
    import cv2 as cv
    import numpy as np
    cp=cv.VideoCapture(0)
    while True:
        _, frame=cp.read()
        clr=cv.cvtColor(frame,cv.COLOR_BGR2HSV)

        #blue
        lb=np.array([94,80,2])
        hb=np.array([126,255,255])

        msk=cv.inRange(clr,lb,hb)

        blue=cv.bitwise_and(frame,frame,mask=msk)
    
        cv.imshow('Blue mask',blue)
        if cv.waitKey(15) & 0xFF==ord('d'):
            break

    return HttpResponse('<h1>Blue color detection : </h1>')
        
#to detect red color...

def red_det(request):
    import cv2 as cv
    import numpy as np
    cp=cv.VideoCapture(0)
    while True:
        _, frame=cp.read()
        clr=cv.cvtColor(frame,cv.COLOR_BGR2HSV)

        #red
        lr=np.array([161,155,84])
        hr=np.array([179,255,255])

        msk=cv.inRange(clr,lr,hr)
        red=cv.bitwise_and(frame,frame,mask=msk)
    
        cv.imshow('Red mask',red)
        if cv.waitKey(15) & 0xFF==ord('d'):
            break

    return HttpResponse('<h1>Red color detection : </h1>')


def green_det(request):
    import cv2 as cv
    import numpy as np
    cp=cv.VideoCapture(0)
    while True:
        _, frame=cp.read()
        clr=cv.cvtColor(frame,cv.COLOR_BGR2HSV)

        #red
        lg=np.array([25,52,72])
        hg=np.array([102,255,255])

        msk=cv.inRange(clr,lg,hg)
        green=cv.bitwise_and(frame,frame,mask=msk)
    
        cv.imshow('Green mask',green)
        if cv.waitKey(15) & 0xFF==ord('d'):
            break


    return HttpResponse('<h1>Red color detection : </h1>')

def index(request):
    return render(request,'index.html')

