import cv2
vidcap = cv2.VideoCapture('WhatsApp Video 2018-09-12 at 20.17.51.mp4')
success,image = vidcap.read()
count = 3643
success = True
while success:
  success,image = vidcap.read()
  cv2.imwrite("dataset/frame%d.jpg" % count, image)     # save frame as JPEG file
  if cv2.waitKey(10) == 27:                     # exit if Escape is hit
      break
  count += 1
