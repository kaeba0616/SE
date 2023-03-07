import os
from bs4 import BeautifulSoup


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Creating directory. " + directory)


def save_file_at_dir(dir_path, filename, file_content, mode="w"):
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, filename), mode) as f:
        f.write(file_content)


color = {
    "red": ["stop-color: rgb(255, 147, 147)", "stop-color: rgb(211, 6, 6)"],
    "blue": ["stop-color: rgb(156, 147, 255)", "stop-color: rgb(45, 45, 255)"],
    "yellow": ["stop-color: rgb(255, 248, 147)", "stop-color: rgb(253, 218, 39)"],
    "green": ["stop-color: rgb(159, 255, 147)", "stop-color: rgb(39,253,43)"],
}


# for x in range(0, 10):
#     for y in color:
#         save_file_at_dir("./UNO/card/" + str(x), y + ".svg", "new text")


for x in range(0, 10):
    createFolder(f"./UNO/asset/card/{x}")

# replace element value in svg file

for x in range(0, 10):
    for y in color:
        with open(f"./UNO/asset/card/cardOriginal/blue.svg", "r") as f:
            soup = BeautifulSoup(f, "xml")
            soup.find_all("stop")[0]["style"] = color[y][0]
            soup.find_all("stop")[1]["style"] = color[y][1]
            with open(f"./UNO/asset/card/{x}/{y}_{x}.svg", "w") as f:
                f.write(str(soup))

if __name__ == "__main__":
    print("start")
