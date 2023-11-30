import cv2
import numpy as np
import time

print("Starting\n")
cam_port = 0
cam = cv2.VideoCapture(cam_port)
print("Got camera\n")
cam.set(cv2.CAP_PROP_FPS, 30)
fps = 0
tStart = time.time()
time.sleep(1)

while True:
    ret, frame = cam.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Use Canny edge detector
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours in the edged frame
    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop over the contours
    for contour in contours:
        # Approximate the contour
        epsilon = 0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # Check the number of vertices to determine the shape
        num_vertices = len(approx)
        shape = "circle" if num_vertices > 15 else "triangle" if num_vertices == 3 else "rectangle" if num_vertices == 4 else ""

        # Draw the shape on the frame
        cv2.drawContours(frame, [approx], -1, (0, 255, 0), 2)
        cv2.putText(frame, shape, (approx.ravel()[0], approx.ravel()[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # Display the result
    cv2.putText(frame, str(int(fps)) + " FPS", (20, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 3)
    cv2.imshow("Result", frame)
    tEnd = time.time()
    loopTime = tEnd-tStart
    fps = 0.9*fps + 0.1*1/loopTime
    tStart = time.time()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
