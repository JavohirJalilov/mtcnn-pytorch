from mtcnn.detector import MtcnnDetector
import cv2 

detector = MtcnnDetector()

image = cv2.imread('images/3d870e79_42823.jpg')

result = detector.detect_faces(image)

print(result)