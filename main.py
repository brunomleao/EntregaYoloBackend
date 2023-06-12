import cv2 as cv
import requests
import base64
import numpy as np
from ultralytics import YOLO

endpoint_url = "http://localhost:3000/salvar-imagem"

cam = cv.VideoCapture(0)
model = YOLO("./best.pt")

while True:
    ret, frame = cam.read()
    result = model.predict(frame, conf=0.6)
    
    if len(result) > 0 and result[0].boxes is not None and len(result[0].boxes) > 0:
        _, img_encoded = cv.imencode('.jpg', frame)
        img_base64 = base64.b64encode(img_encoded).decode('utf-8')

        payload = {'imagem': img_base64}
        response = requests.post(endpoint_url, json=payload)
        print(response.text)

    cv.imshow("Resultados", result[0].plot())
    if cv.waitKey(1) == ord('q'):
        break

cam.release()
cv.destroyAllWindows()
