# Python에 openCV 설치하는 방법
#     1. python -m pip install opencv-python 을 터미널에 입력
#     2. 아래의 example로 확인해보기 -> import 가 된다면 문제가 없는 것이다!
import cv2

image = cv2.imread('image.jpg',cv2.IMREAD_COLOR)

cv2.imshow("TEST", image)
cv2.waitKey(0)
cv2.destroyAllWindows()