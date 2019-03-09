"""Script to add video to database."""
if __name__ == "__main__":
    from modules import args, stdout
    from modules.database import database
    import cv2
    import time
    from os import path
    import base64
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "video_file", help="File to be inserted")
    parser.add_argument(
        "video_title", help="Title of the file")

    args = parser.parse_args()
    stdout = stdout.Stdout(False)
    start_time = time.time() * 1000
    stdout.write("Inserting video...")
    video_file = args.video_file

    if not path.isfile(video_file):
        stdout.write("%s is not a file" % video_file)
        exit(-1)

    # read video file to extract meta data
    video_cap = cv2.VideoCapture(video_file)
    fps = video_cap.get(cv2.CAP_PROP_FPS)
    total_frame = video_cap.get(cv2.CAP_PROP_FRAME_COUNT)
    width = int(video_cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video_cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    video_cap.release()

    title = args.video_title
    length = (total_frame/fps)*1000
    name = path.basename(video_file)
    extension = path.splitext(name)[1]
    size = path.getsize(video_file)

    with open(video_file) as file:
        content = file.read()
        encoded_content = base64.b64encode(content)

    data = (
        title,
        length,
        extension,
        name,
        size,
        encoded_content,
        fps,
        total_frame,
        width,
        height
    )

    database.insert_video(data)

    stdout.passed_time(start_time, "Finished in")

    exit(0)
