#opencv使用记录#
##api##
cv2.imread()读取图片  
1为rgb模式读取，输出顺序为bgr。
0为灰度模式。
-1为带透明度的格式。
**当路径错误时不会报错，但会输出为空**

cv2.imshow(framename,img)展示图片  
framename窗体名称,img展示的图片

cv2.namedWindow(framename,flags)  
创造一个窗口。  
framename为窗口名称，flags为窗口设置选项。
常设置窗口是否可以更改大小。
flags为`cv2.WINDOW_AUTOSIZE`则自动根据图片改变窗口大小，不可手动更改。为`cv2.WINDOW_NORMAL`，可以手动改变窗口大小。可以利用cv2.resizeWindow(framename,width,height)实现。

cv2.waitKey()
实验后添加说明。等待时间以毫秒计。对于64位需写为cv2.waitKey(0) & 0xFF

cv2.destroyAllWindows()关闭全部窗口。  
对于关闭指定窗口，可以使用cv2.destroyWindow()。**里面直接输入framename。例如'image'？**

cv2.imwrite(path,img)保存图像。  
path为路径，img为图片变量名。

cv2.VideoCapture()  
捕获视频流。**使用cv2.VideoCapture前需要安装ffmpeg 或者gstreamer**  
```python
import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
```
上面为捕获摄像头的情形，index可以更改，具体需要实验下。有时cap可能没有初始化导致展示错误，可以通过`cap.isOpened()`检查是否正确开启，如果没有，用`cap.open()`打开。对于接受的视频可以使用`cap.get(propId)`获取特征，propId有0-18可以获取。设置的话可以使用对应的`cap.set(propId,value)`去设置。具体细节[Property Identifier](http://docs.opencv.org/2.4/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture-get)。当使用视频文件时，将设备数字改为视频名称。`cap=cv2.VideoCapture('vtest.avi')`

cv2.VideoWriter(filename,fourcc,fps,frameSize,isColor=True)  
导出视频文件。filename视频文件名。[fourcc](http://www.fourcc.org/codecs.php)是一个4个字符编码的帧间压缩编解码器的应用。fps帧数，frameSize视频尺寸。isColor如果为0，则输出灰度视频，否则为彩色。**只支持Windows。**  
```python
import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#fourcc =cv2.VideoWriter_fourcc('X','V','I','D')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
```


