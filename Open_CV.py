# 이미지 출력 설정 바꾸기 : https://ddolcat.tistory.com/958
#
# IMREAD_COLOR  -> 별도로 지정하지 않은 경우 기본값, 3채널 BGR 컬러 이미지로 반환
# IMREAD_GRAYSCALE  -> 단일 채널 회색조 이미지로 반환(내부 코덱 변환)
# IMREAD_UNCHANGED  -> 이미지 원본 그대로 반환한다.
# IMREAD_ANYCOLOR  -> 가능한 모든 색상 형식으로 이미지를 읽습니다.
# IMREAD_ANYDEPTH  -> 설정된 경우 입력에 해당 깊이가있을 때 16 비트 / 32 비트 이미지를 반환하고 그렇지 않으면 8 비트로 변환
#
# cv2.imwrite('tilde_image.jpg', img)  -> img 데이터를 tilde_image 라는 이름으로 저장하라는 뜻

import cv2

img1 = cv2.imread('image.jpg')
img2 = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)
img3 = cv2.imread('image.jpg', cv2.IMREAD_ANYCOLOR)
img4 = cv2.imread('image.jpg', cv2.IMREAD_ANYDEPTH)

cv2.imshow('image1', img1)
cv2.imshow('image2', img2)
cv2.imshow('image3', img3)
cv2.imshow('image4', img4)

cv2.imwrite('tilde_image.jpg', img2) 

cv2.waitKey(0)
cv2.destroyAllWindows()