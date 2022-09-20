import cv2

file = open("cameralist.csv", "r")


for line in file:
    name , rtsp = line.rstrip().split(",")
    print(name)
    print(rtsp)
    cap = cv2.VideoCapture(rtsp)

    if cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imwrite(f'screenshots/{name}.jpg',frame)

        
    else:
        print("Cannot open camera")
    cap.release()




cv2.destroyAllWindows()