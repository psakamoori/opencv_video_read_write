import cv2 as cv

video_path = "<your sample video file path .mp4>"

vclip = cv.VideoCapture(str(video_path))
frame_width = int(vclip.get(3))
frame_height = int(vclip.get(4))
	 
out = cv.VideoWriter('output.avi', cv.VideoWriter_fourcc('M','J','P','G'), 60, (frame_width, frame_height))

frame_cnt = 0
while(True):
  ret, frame = vclip.read()
  if ret == True:
     yuv_frame = cv.cvtColor(frame, cv.COLOR_RGB2YUV)
     blur_yuv = cv.medianBlur(yuv_frame, 5)
     out.write(blur_yuv)
     if cv.waitKey(5) & 0xFF == ord('q'):
        break
     frame_cnt += 1
     print("Frame Counter: ", frame_cnt, end='\r')
  else:
    print("End of Stream..\n")
    break
vclip.release()
out.release()
  



