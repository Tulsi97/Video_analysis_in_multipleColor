import cv2
cap = cv2.VideoCapture(0)
filename = 'C:\\Users\\hp-u\\.spyder-py3\\.spyder-py3.hp-u'
codec = cv2.VideoWriter_fourcc('X','V','I','D')
framerate = 30
resolution = (780,520)
VideoFileOutput = cv2.VideoWriter(filename, codec, framerate, resolution)
if cap.isOpened():
    ret, frame = cap.read()
else:
    ret = False

while ret:
    ret, frame = cap.read()
    VideoFileOutput.write(frame)
    
    cv2.imshow('Live Video recording',frame)
    if cv2.waitKey(60) == 27:
        break
cv2.destroyAllWindows()
VideoFileOutput.release()
cap.release()    