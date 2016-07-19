from psychopy import visual, event, core,gui ,data,  logging #import c
from numpy import sin, pi

win = visual.Window([1366,768], color='black',units='pix',fullscr=False) #buka window baru

kotak1=visual.Rect(win, width=150,height=150, pos=(10,250),)
segitiga1=visual.Polygon(win, edges=3, radius=40,pos=(10,250))
kotak2=visual.Rect(win, width= 150, height=150,pos=(400,-200))
segitiga2=visual.Polygon(win, edges=3, ori=90,radius=40, pos=(400,-200))
kotak3=visual.Rect(win,width=150, height= 150, pos=(-400,-200))
segitiga3=visual.Polygon(win,edges=3,radius=40,ori=-90,pos=(-400,-200))
kotak4=visual.Rect(win,width= 150, height=150,pos=(0,-200))
lingkaran1=visual.Circle(win,radius=40, edges=32,pos=(0,-200))

#flicker frequency
flicker_frequency= 8.57142
flicker_frequency1=10
flicker_frequency2=12
flicker_frequency3=15
#fasa awal
current_frame = 0
current_frame1=0
current_frame2=0
current_frame3=0
t=0
trialClock = core.Clock()


#run flickering stimuli
while True :
    
    if current_frame % 2*flicker_frequency < flicker_frequency :
        kotak1.draw()
        segitiga1.draw()
    win.flip()
    current_frame+=1
    
    
    if current_frame1 %2*flicker_frequency1< flicker_frequency1 :
        kotak3.draw()
        segitiga3.draw()
    win.flip()
    current_frame1+=1    
    if current_frame %2*flicker_frequency2<flicker_frequency2 :
        kotak2.draw()
        segitiga2.draw()
    win.flip()
    current_frame2+=1
    if current_frame3 %2*flicker_frequency3<flicker_frequency3 :
        kotak4.draw()
        lingkaran1.draw()    
    win.flip()
    current_frame3+=1    
    
    #current_frame1+=10*360
    #win.flip()
    #current_frame1+=10*360
    #win.flip()
    #current_frame2+=12*360
    #win.flip()
    #current_frame3+=15*360
       
for key in event.getKeys():
    if key in ['escape','q']:
        core.quit() 