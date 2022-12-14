from datetime import datetime
import cv2

file = open("cameralist.csv", "r")
file2 = open(f"statusCamera{datetime.now()}.csv", "w")
i=1
for line in file:
    name , rtsp = line.rstrip().rsplit(',', 1)
    print(f"{i} - {name}:", end="")
    #print(rtsp)
    cap = cv2.VideoCapture(rtsp)

    if cap.isOpened():
        ret, frame = cap.read()
        if ret:
            #cv2.imwrite(f'screenshots/{name}.jpg',frame)
            file2.writelines(f"{name},{rtsp},Online\n")
            print("Online\n")
        else:
            file2.writelines(f"{name},{rtsp},Offline\n")
            print("Offline\n")       
    else:

        #print("Cannot open camera")
        file2.writelines(f"{name},{rtsp},Offline\n")
        print("Offline\n")
    cap.release()
    i+=1




cv2.destroyAllWindows()