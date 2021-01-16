import os


def main():
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):

        for filename in filenames:
            new_file_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_file_name))

            old_path = os.path.join(directory_name, filename)
            new_path = os.path.join(directory_name, new_file_name)
            os.rename(old_path, new_path)


def get_fixed_filename(filename):
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    name = ""
    for i, letter in enumerate(new_name):
        name += letter
        if i < len(new_name) - 1 and letter.islower() and new_name[i + 1].isupper():
            name += "_"
    return name


main()
