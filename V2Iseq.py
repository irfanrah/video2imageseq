import cv2
import os
from PIL import Image






def vid2seqimg(video_name , input_path, output_path, TOTAL_SEQ_IMAGE):
    image_list = []
    vidcap = cv2.VideoCapture(os.path.join(input_path, video_name))
    frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    print(f"total frame: {frame_count}")
    division = frame_count// (TOTAL_SEQ_IMAGE )
    current_frame = 0
    while True:
        ret,frame = vidcap.read()
        if ret:
            if current_frame % (division) == 0 and current_frame != 0:
                image_list.append(frame)    
            current_frame += 1
        else: break
    h_img_stack = cv2.hconcat([cv2.resize(i, (300,300), interpolation= cv2.INTER_LINEAR) for i in image_list])
    cv2.imshow('Horizontal', h_img_stack)
    cv2.imwrite(os.path.join(output_path, video_name[:-4] + ".jpg"), h_img_stack)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

if __name__=="__main__":
    TOTAL_SEQ_IMAGE = 5
    input_folder_path = "video_input"
    output_folder_path = "image_output"
    video_list_from_input = os.listdir(input_folder_path)
    for i in video_list_from_input:
        vid2seqimg(i, input_folder_path, output_folder_path, TOTAL_SEQ_IMAGE )

