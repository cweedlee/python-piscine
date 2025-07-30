import shutil
rom time import time, sleep


def ft_tqdm(lst: range) -> None:
    """
    like tqdm
    accepts only range
    """
    # progress (total length(length) / current position(pos))
    length = len(lst)
    pos = 0
    columns = shutil.get_terminal_size().columns
    # time passed
    start = time_passed = time()
    # time left
    # how many time for a step
    
    for curr in lst:
        pos += 1
        progress_percentage = float(pos) / float(length) * 100.0
        time_per_unit = time() - time_passed
        time_passed = time()
        time_left = time_per_unit * (length - pos)
        ncol = columns - 5 - 2 - pos - 1 - length - 2 - len(str(time_left)) - len(str(time_passed)) - 3 - len(str(time_per_unit)) - 5
        progress_ncol = int(ncol * progress_percentage) / 100
        res = f"{progress_percentage:3.0f}%|{'█':10}| {pos}/{length} [{time_passed:.2f}<{time_left:.2f}, {time_per_unit}it/s]"
        #res = f"{progress_percentage}"
        yield res


def main():
    for i in ft_tqdm(range(10)):
        sleep(0.25)
        print(i)

if __name__ == "__main__":
    main()

