import cv2, pafy

url   = "https://www.youtube.com/watch?v=xDDpNaQxn6E"
video = pafy.new(url)
best  = video.getbest(preftype="mp4")
capture = cv2.VideoCapture(best.url)
while True:
    check, frame = capture.read()
    print (check, frame)

    cv2.imshow('frame',frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()