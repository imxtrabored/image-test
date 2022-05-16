import os
import shutil
from pathlib import Path

for file in Path().glob("*.jpg"):
    dirname = file.name[0:-4]
    try:
        os.mkdir(dirname)
    except FileExistsError:
        pass
    shutil.copy(file, dirname + "\\image.jpg")
