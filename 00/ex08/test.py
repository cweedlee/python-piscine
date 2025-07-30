from tqdm import tqdm
import time
import shutil

text = ""
t = tqdm(["a", "b", "c", "d"])

def get_terminal_dimensions():
    """
    Retrieves the current terminal size in columns and lines.
    """
    size = shutil.get_terminal_size()
    columns = size.columns
    lines = size.lines
    return columns, lines

print(get_terminal_dimensions())
for c in tqdm(range(100)):
    time.sleep(0.5)
