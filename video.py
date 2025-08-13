#import streamlit as st
import cv2 as cv
"""
con1 = st.container(height=100)

st.sidebar.empty()"""

# Load the video
cap = cv.VideoCapture('testrun.mp4')

# Get original video properties
fps = cap.get(cv.CAP_PROP_FPS)
original_width  = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
original_height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

# Set new dimensions (e.g., half size)
new_width = int(original_width * 0.5)
new_height = int(original_height * 0.5)

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'mp4v')  # Or use 'XVID', 'MJPG', etc.
out = cv.VideoWriter('resized_video.mp4', fourcc, fps, (new_width, new_height))

# Read and resize each frame
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame
    resized_frame = cv.resize(frame, (new_width, new_height))

    # Write resized frame
    out.write(resized_frame)

# Release everything
cap.release()
out.release()
cv.destroyAllWindows()

"""with con1:
    st.video("testrun.mp4")"""