import cv2
import time

print ("\nStarting\n")
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_FPS, 30)   

# dispW = 1280
# dispH = 720

# cam.set(cv2.CAP_PROP_FRAME_WIDTH, dispW)
# cam.set(cv2.CAP_PROP_FRAME_HEIGHT, dispH)

fps = 0
tStart = time.time()
time.sleep(1)
while True:
    ret, frame = cam.read()
    cv2.putText(frame, str(int(fps)) + " FPS", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 3)
    cv2.imshow('Camera', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("\nStopping\n")
        break
    tEnd = time.time()
    loopTime = tEnd-tStart
    fps = 0.9*fps + 0.1*1/loopTime
    tStart = time.time()

cam.release()
cv2.destroyAllWindows()