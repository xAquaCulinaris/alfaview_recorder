import cv2

output = "raw.avi"
converted = "video.avi"


def convert_video(multiplier, width, height):
    print("Starting conversion..")
    cap = cv2.VideoCapture(output)
    codec = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(converted, codec, multiplier, (width,height))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("video ended")
            break
        out.write(frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print("Finished conversion..")
