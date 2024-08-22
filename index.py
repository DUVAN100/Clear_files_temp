from typing import AnyStr, Dict, Union
from pathlib import Path
import os

# route : str = 'C:\Users\usuario\AppData\Local\Temp'
route: Path = Path(r'C:\Users\usuario\AppData\Local\Temp')
try:
    if route.exists():
            files = list(route.iterdir())
            for file in files:
                try:
                    if file.is_file():
                        file.unlink()
                        print(f"Deleted file: {file}")
                except Exception as ex:
                      print(f"Error occurred while deleting {file}: {ex}")
    else:
        print(f"The path '{route}' does not exist.")
except Exception as ex:
    print("Error ocurred", {ex})