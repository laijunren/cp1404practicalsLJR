import os
import shutil


def main():
    """Move files into folders with the same name as their extension."""
    os.chdir("FilesToSort")
    for filename in os.listdir():
        if os.path.isfile(filename):
            ext = filename[filename.rindex(".") + 1:]
            os.makedirs(ext, exist_ok=True)
            print("{}/{}".format(ext, filename))
            shutil.move(filename, os.path.join(ext, filename))


main()
