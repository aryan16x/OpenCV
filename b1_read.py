import cv2 

# to read and show images
img = cv2.imread('Photos/birdImg.jpg')
cv2.imshow('Bird', img)

cv2.waitKey(0)      # img will remain open untill you press any key bcz of 0

# to read and show video
# to read video from any specific file we use path of that file
# to read video from camera we use index generally for device inbuilt camera the index is 0
# capture = cv2.VideoCapture(0)
capture = cv2.VideoCapture('Videos/horse.mp4')
while True:
    # here we display video frame by frame
    isTrue, frame = capture.read()
    cv2.imshow('Video', frame)
    
    # 0xFF means when we press 'd' then condition will be executed
    if cv2.waitKey(5) & 0xFF==ord('d'):
        break
    
capture.release()
cv2.destroyAllWindows()

