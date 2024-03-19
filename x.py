import av

def video_to_frames_pyav(input_video, output_directory):
    container = av.open(input_video)
    for frame in container.decode(video=0):
        print(frame.to_image().tobytes()) #.save(f"{output_directory}/frame_{frame.index}.jpg")

# Contoh penggunaan
video_to_frames_pyav("/storage/emulated/0/DCIM/Camera/7d63d05964f3a18c775069a1e4c76989_001.mp4", "res")
