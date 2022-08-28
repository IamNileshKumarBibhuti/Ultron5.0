import cv2
import winsound

cam = cv2.VideoCapture(0)
while cam.isOpened():

    '''This is our main frame'''
    ret, frame1 = cam.read()  # Here Is the eye of my computer (comment out frame2 and change diff to frame1 in line 11).
    ret, frame2 = cam.read()  # Here Is the eye of my computer.

    

    diff = cv2.absdiff(frame1 ,frame2) 
    """ diff will make u blind like invisible man(but don't move) 😉, 
    but if u move then some red ,blue , ... some more extra colour u will see 
    i.e not perfectly black and white in computer vision ."""



    black = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY) # U might think why not RGB2black since module 'cv2.cv2' has no such attribute

    blur = cv2.GaussianBlur(black ,(5,5) ,0 ) # we made it blur because to make outline little broad WIDE

    _, thresh = cv2.threshold (blur ,20 ,255 ,cv2.THRESH_BINARY)
    ''' (5,5) is the kernal size and 0 is the sigma X '''



    ''' Now our Pure image is now available ,lets make it bigger '''
    dilation = cv2.dilate(thresh, None, iterations=3)



    ''' Now lets make a rectangle around the object , easy to recognise 
    which objects are moving and what are the things are static'''
    contours, _ = cv2.findContours(dilation ,cv2.RETR_TREE ,cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame1, contours ,-1 ,(255,0,255) ,2)



    ''' Now eliminating the small contours i.e small rectangles.'''
    for i in contours :
        
        if cv2.contourArea(i) < 5000:
            continue

        x,y, w, h = cv2.boundingRect(i) # here x & y axis AND w & h is width along x & y respectively.
        cv2.rectangle(frame1 ,(x,y) ,(x+w ,y+h),(0,0,255) ,2)
        winsound.Beep(500,200) # My Advise is to use some Mp3 or wav audio like--> winsound.PlaySound('name',winsound.SND_ASYNC) but why ?
        ''' The winsound above used is synchronized 
        i.e it will make a video buffer as it first synchronize the sound then display the video so video lag will occur
        But using winsound.PlaySound('name',winsound.SND_ASYNC) will be asynchronized system i.e happens parallelly video+sound so, no lag. :) DONE '''
    
    
    
    if cv2.waitKey(10)==ord('t'):   # This is to terminate
        break

    cv2.imshow(' Moi Cam  :) ', frame1) 



