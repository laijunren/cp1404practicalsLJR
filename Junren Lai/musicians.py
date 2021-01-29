"""
musicians question (using original.txt)
"""


def main():
    """
    Program entrance
    """
    lines = read_datas("original.txt")
    if len(lines) <= 0:
        return
    header = lines[0]
    datas = []
    if len(lines) > 1:
        datas = dispose(lines[1:])
    write_datas("musicians.txt", header, datas)


def read_datas(file_name):
    """
    Read file data
    """
    try:
        lines = []
        file = open(file_name)
        for line in file:
            line = line.strip()
            if line:
                lines.append(line)
        file.close()
        return lines
    except:
        return []


def dispose(lines):
    """
    Process each row of data by format
    """
    datas = []
    if lines:
        for line in lines:
            parts = line.split(",")
            name = parts[0]
            birthday = parts[1]
            datas.append([name, tuple(birthday.split("/"))])
    datas.sort(key=lambda x: x[0])
    return datas


def write_datas(file_name, header, datas):
    """
    Write data to a file
    """
    try:
        file = open(file_name, "w")
        file.write(header + "\n")
        for data in datas:
            birthday = data[1]
            birthday_str = "-".join(birthday[::-1])
            file.write(birthday_str + " = " + data[0] + "\n")
        file.close()
    except:
        pass


main()
