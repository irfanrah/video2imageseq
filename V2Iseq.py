import cv2
import os

def vid2seqimg(video_name, input_path, output_path, TOTAL_SEQ_IMAGE, concat_direction='horizontal'):
    image_list = []
    vidcap = cv2.VideoCapture(os.path.join(input_path, video_name))
    frame_count = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    print(video_name)
    print(f"Total frames: {frame_count}")
    print(f"Video FPS: {fps}")
    division = frame_count // TOTAL_SEQ_IMAGE
    current_frame = 0
    
    while True:
        ret, frame = vidcap.read()
        if ret:
            if current_frame % division == 0 and current_frame != 0:
                image_list.append(frame)
                print(f"Frame {current_frame} added to image_list")
            current_frame += 1
        else:
            break
    
    if concat_direction == 'horizontal':
        concatenated_img = cv2.hconcat([cv2.resize(i, (300, 300), interpolation=cv2.INTER_LINEAR) for i in image_list])
        cv2.imshow('Horizontal', concatenated_img)
    else:
        concatenated_img = cv2.vconcat([cv2.resize(i, (3*300, 300), interpolation=cv2.INTER_LINEAR) for i in image_list])
        cv2.imshow('Vertical', concatenated_img)
    
    cv2.imwrite(os.path.join(output_path, video_name[:-4] + ".jpg"), concatenated_img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    TOTAL_SEQ_IMAGE = 6
    input_folder_path = "video_input"
    output_folder_path = "image_output"
    video_list_from_input = os.listdir(input_folder_path)
    concat_direction = 'vertical'  # Change to 'vertical' if needed
    
    for video_name in video_list_from_input:
        vid2seqimg(video_name, input_folder_path, output_folder_path, TOTAL_SEQ_IMAGE, concat_direction)

