HW 7 answers




Q:escribe your solution in detail. What neural network did you use? What dataset was it trained on? What accuracy does it achieve?


A: sed darknet YOLO. I couldn’t make DNN for face detection so just used darknet and modified darknet C source code to save image files and call mosquitto. 

  The following codes are added to the image.c in the /darknet/src/ to save detected object as JPG. 
  Then system function ran mosquitto_publish to send binary data to remote storage I setup in HW03.
  
      save_image(c1, "/tmp/test");
      int status = system("mosquitto_pub -h 158.85.194.25 -f ../../tmp/test.jpg -t test");



Q:Does it achieve reasonable accuracy in your empirical tests? Would you use this solution to develop a robust, production-grade system?  

A: bject detection performance and message sending performance was pretty good.


Q:What framerate does this method achieve on the Jetson? Where is the bottleneck?


A: ost 30. Because I used mini yolo.


Q:hich is a better quality detector: the OpenCV or yours?
YOLO


