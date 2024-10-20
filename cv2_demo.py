import cv2
print(cv2.__file__)

# 加载人脸和眼睛检测的级联分类器
face_cascade = cv2.CascadeClassifier('D:\python\Lib\site-packages\cv2\data\haarcascade_eye.xml')
eye_cascade = cv2.CascadeClassifier('D:\python\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')

# 打开摄像头
cap = cv2.VideoCapture(0)

while True:
    # 读取摄像头画面
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 检测人脸
    #faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        # 在原图上绘制人脸矩形框
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # 截取人脸区域用于眼睛检测
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        # 在人脸区域内检测眼睛
        eyes = eye_cascade.detectMultiScale(roi_gray)
        
        for (ex, ey, ew, eh) in eyes:
            # 在人脸区域图上绘制眼睛矩形框
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (255, 10, 185), 2)
    
    # 显示结果图像
    cv2.imshow('Frame', frame)
    
    # 按下'q'键退出循环
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头并关闭所有窗口
cap.release()
cv2.destroyAllWindows()