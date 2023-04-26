import cv2

# List of video files to play
video_files = [
    'videos/cherrypie.mp4',
    'videos/Damn Yankess - High Enough.mp4',
    'videos/Def Leppard - Pour Some Sugar On Me.mp4',
    'videos/Posion - Nothin But A Good Time.mp4',
    'videos/Under the Influence(r).mp4'
]

# Create a window to display the video
cv2.namedWindow('Video Player')

# Play each video file in the list
for file in video_files:
    try:
        # Load the video file
        video = cv2.VideoCapture(file)
    except:
        print(f"Error: Could not load video file {file}")
        continue

    # Play the video frame by frame
    while True:
        ret, frame = video.read()

        if ret:
            # Display the frame in the window
            cv2.imshow('Video Player', frame)

            # Wait for 25 milliseconds
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            # Break the loop if there are no more frames
            break

    # Release the video object
    video.release()

# Destroy the window
cv2.destroyAllWindows()
