import os
import shutil


def main():
    """Move files into where user wants to store them based on extension."""
    ext_cat_dict = {}
    os.chdir("FilesToSort")
    for filename in os.listdir():
        if os.path.isfile(filename):
            ext = filename[filename.rindex(".") + 1:]
            if ext not in ext_cat_dict:
                cat = input("What category would you like to sort %s files into? " % ext)
                ext_cat_dict[ext] = cat
                os.makedirs(cat, exist_ok=True)
            shutil.move(filename, os.path.join(ext_cat_dict.get(ext), filename))


main()
