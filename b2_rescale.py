import cv2

# for images,videos and live videos
def reScaleFrame(frame, scale=0.75):
    # here frame means image
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    
    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)

# only for live videos
def changeResolution(width, height):
    capture.set(3,width)
    capture.set(4,height)

# to resize image
img = cv2.imread('Photos/birdImg.jpg')
cv2.imshow('Bird', img)

imgResized = reScaleFrame(img)
cv2.imshow('Bird_Resized', imgResized)
cv2.waitKey(0)

# to resize videos
# capture = cv2.VideoCapture('Videos/horse.mp4')
capture = cv2.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    frameResized = reScaleFrame(frame)
    cv2.imshow('Video', frameResized)
    
    if cv2.waitKey(5) & 0xFF==ord('d'):
        break
    
capture.release()
cv2.destroyAllWindows()


