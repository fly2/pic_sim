#opencv使用记录#
##api##
cv2.imread()读取图片  
1为rgb模式读取，输出顺序为bgr。
0为灰度模式。
-1为带透明度的格式。
**当路径错误时不会报错，但会输出为空**

cv.imshow(framname,img)展示图片  
framname窗体名称，
img展示的图片

cv.waitKey()
实验后添加说明。对于64位需写为cv2.waitKey(0) & 0xFF

cv2.destroyAllWindows()关闭全部窗口。  
对于关闭指定窗口，可以使用cv2.destroyWindow()。**里面直接输入framename。例如'image'？**

cv.imwrite(path,img)保存图像。  
path为路径，img为图片变量名。




