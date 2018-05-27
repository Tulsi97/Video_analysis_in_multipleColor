import cv2

cap = cv2.VideoCapture(0)
print('Width: '+ str(cap.get(3)))
print('Height: '+ str(cap.get(4)))

#setting resolution
cap.set(3,1080)
cap.set(4,720)

print('Width: '+ str(cap.get(3)))
print('Height: '+ str(cap.get(4)))

if cap.isOpened():
    ret, frame = cap.read()
else:
    ret = False
 
while ret:
    ret, frame = cap.read()
    
    output = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    output1 = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGB)
    
    cv2.imshow('RGB color',output1)
    cv2.imshow('gray color',output)
    cv2.imshow('color video', frame)
    if cv2.waitKey(1) == 27:          
        break
    
cv2.destroyAllWindows()
cap.release()

    
    

