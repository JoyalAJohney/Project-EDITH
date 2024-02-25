import cv2
import os
import datetime
import threading
from openai_request import upload_image_and_ask



# Save screenshot and call OpenAI

def process_image(frame):
    curr_dir = os.getcwd()
    screenshot_dir = "screenshots"

    full_dir = os.path.join(curr_dir, screenshot_dir)
    if not os.path.exists(full_dir):
        os.makedirs(full_dir)

        
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    filename = f'screenshot_{timestamp}.png'
    directory = os.path.join(full_dir, filename)

    cv2.imwrite(directory, frame)
    print(f'Screenshot saved as {directory}')

    # Call OpenAI API
    response = upload_image_and_ask(directory)
    print("\n" + response)



def capture_screenshot():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        cv2.imshow('Video Stream', frame)

        # Wait for the 's' key to take a screenshot
        if cv2.waitKey(1) & 0xFF == ord('s'):
            threading.Thread(target=process_image, args=(frame.copy(),)).start()

        elif cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    capture_screenshot()