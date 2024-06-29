import sys
import os
import random
import ctypes
import re
from pathlib import Path

# Configuration variables.
path3dm = os.getcwd() + "/"

# Put folder(character) name which you DO NOT want to apply
# Example ["char1", "char2"]
characterlist = [
    "_기타", "느비", "타탈", "카즈하", "리니", "_남캐", "종려",
]

def randomizeOutfit(character):
    directory_path = path3dm + "Mods/" + character
    folders = [
        f
        for f in os.listdir(directory_path)
        if os.path.isdir(os.path.join(directory_path, f)) and f.lower().startswith("disabled") and not f.split()[1].startswith("_")
    ]

    for folder_name in os.listdir(directory_path):
        if folder_name.startswith('_'):
            continue
        folder_path = os.path.join(directory_path, folder_name)
        if os.path.isdir(folder_path) and not folder_name.lower().startswith("disabled"):
            new_folder_name = "DISABLED " + folder_name.strip()
            new_folder_path = os.path.join(directory_path, new_folder_name)
            os.rename(folder_path, new_folder_path)
            folders.append(new_folder_name)

    if folders:
        folder_to_rename = random.choice(folders)
        redata = re.compile(re.escape('disabled'), re.IGNORECASE)
        new_folder_name = redata.sub('', folder_to_rename).strip()
        folder_to_rename_path = os.path.join(directory_path, folder_to_rename)
        new_folder_path = os.path.join(directory_path, new_folder_name)
        os.rename(folder_to_rename_path, new_folder_path)
        print(character, f" Outfit Chosen: ", new_folder_name)

if __name__ == "__main__":
    try:
        for character in os.scandir(path3dm + "Mods/"):
            if character.is_file() or character.name in characterlist or character.name.startswith('_'):
                pass
            else:
                randomizeOutfit(character.name)
    except Exception as e:
        print(f"An error occurred, randomization skipped. Error: {e}")
    finally:
        print("Execution complete")
