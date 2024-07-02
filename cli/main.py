import argparse
import argcomplete
from pathlib import Path
from .fileio import read, write
from .ui import __show, display_labels


VALUES = [0,1,None]
NAMES = ["cat", "elephant", "bird"]

def increment(state, id):
    value = state[id][1]
    if value == 0: new = 1
    elif value == 1: new = None
    elif value is None: new = 0
    else: raise ValueError("Illegal value", value)
    state[id][1] = new 
    return state

def parse_args():
    parser = argparse.ArgumentParser(description="Process a folder path.")

    # ARGS
    parser.add_argument(
        "folder",
        type=str,
        help="Path to the folder (use tab to autocomplete)",
    ).completer = argcomplete.completers.DirectoriesCompleter()

    # KWARGS
    parser.add_argument(
        "-r", 
        "--recursive",
        action="store_true",
        default=False,
        help="Use all images in this folder recursively"
    )

    argcomplete.autocomplete(parser)
    args = parser.parse_args()

    return Path(args.folder), args.recursive

def main():
    print("")
    try:
        image_folder, recursive = parse_args()
    except:
        image_folder = ""


    for p in image_folder.rglob("*"):




    done = False
    state = [[name,None] for name in NAMES]
    print(state)
    while not done:
        _input = input().lower().strip()
            
        for key in _input:
            if key.isnumeric():
                increment(state, id=int(key)-1)
                
            elif key == "q":
                done=True

        display_labels(state)

if __name__ == '__main__':
    main()
