from moviepy.editor import VideoFileClip

# Load your video
video = VideoFileClip("/storage/emulated/0/DCIM/Camera/232e82666493a9b96bbad258a5fcbdb0.mp4")

# Extract audio
audio = video.audio
audio.write_audiofile("audio.mp3")

# Save the video without audio
video.without_audio().write_videofile("video_no_audio.mp4")
