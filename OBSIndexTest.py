import cv2

# Test which camera index OBS virtual camera is using
for i in range(10):
    cap = cv2.VideoCapture(i)
    if cap.read()[0]:
        print(f'OBS Virtual Camera is found at index {i}')
        cap.release()
        break
    cap.release()
else:
    print("OBS Virtual Camera not found.")
