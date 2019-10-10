import numpy as np
import cv2
import zbar

cap = cv2.VideoCapture(0)
qrDecoder = cv2.QRCodeDetector()
scanner = zbar.Scanner()

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow('Frame', gray)

    # cv2 detecting qr code 
    data, box, rectifiedImage = qrDecoder.detectAndDecode(frame)
    # zbar detecting qr code
    results = scanner.scan(gray)
    
    if len(results) > 0:
        print(results[0].data)
        print(results[0].position)
        print('Zbar')
    if len(data) > 0: 
        print('CV2')

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
