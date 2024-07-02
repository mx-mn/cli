import cv2
from colorama import init, Fore, Style
from pathlib import Path

init()
window = 'Image Viewer'
cv2.namedWindow(window, cv2.WINDOW_AUTOSIZE)



def process_image(file_path: Path, labels):
    done = False
    while not done:
        key = __show(file_path).lower()
        if key in QUIT_CHARACTERS: 
            return False
        elif
    return True


def __show(file_path: Path):
    image = cv2.imread(file_path.as_posix())
    cv2.imshow(window, image)
    key = ord(cv2.waitKey(0))
    return key

def display_labels(labels):
    end = len(labels)
    for i, (key, value) in enumerate(labels):
        if i == 0: print("<", end=" ")
        elif 0 < i < end: print("> <", end=" ")

        if value == 0: print(Fore.GREEN, end="")
        elif value == 1: print(Fore.RED, end="")
        else: print(Fore.WHITE + Style.DIM, end="")

        print(key + Style.RESET_ALL, end=" ")
        if i == end-1: print(">", end="")
