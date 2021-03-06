import cv2 as cv
import sys

cap = cv.VideoCapture(sys.argv[1])

r, frame1 = cap.read()
r, frame2 = cap.read()

while cap.isOpened():
    if not r:
        print("Frame error")
        break

    r, frame = cap.read()
    diff = cv.absdiff(frame1, frame2)

    # get the grayscale frame
    grayscl = cv.cvtColor(diff, cv.COLOR_BGR2GRAY)
    _, binary = cv.threshold(grayscl, 7, 255, cv.THRESH_BINARY_INV)

    # get the contour
    contours, hierarch = cv.findContours(binary, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # draw the rectangles
    for c in contours:
        x,y,w,h = cv.boundingRect(c)
        if cv.contourArea(c) > 2000:
            frame = cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

    # show the frame
    cv.imshow("frame", frame)

    # update frame1 and frame2 for next calculation
    frame1 = frame2
    r, frame2 = cap.read()

    if cv.waitKey(15) == 7:
        break

cap.release()
cv.destroyAllWindows()
