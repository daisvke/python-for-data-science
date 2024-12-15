from sys import stdout
from time import time


"""
Implementation of tqdm
"""

def get_ansi_colours() -> dict:
    """
    Returns a dictionary with all the ANSI basic colors
    """
    return {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m"
    }

def ft_tqdm(
    iterable: any, 
    unit: str="it",
    leave: bool=True,
    initial: int|float=0,
    delay: float=0.0,
    colour: str="white"
    ) -> any:

    """
	Implementation of tqdm
    """

    total_len = len(iterable)
	# Quit if iterable is empty
    if total_len == 0:
        print("0it [00:00, ?it/s]")
        return

    start_time = time()

    # Set colours
    colour_dict = get_ansi_colours()
    ansi_colour = colour_dict[colour]
    reset_colour = "\033[0m"

    for i, item in enumerate(iterable, initial + 1):
        bar_len = 40
        progress = i / total_len
        percentage = int(progress * 100)

        # Create the progress bar
        filled_len = int(bar_len * progress)
        empty_len = bar_len - filled_len
        bar = f"{ansi_colour}█{reset_colour}" * filled_len + " " * empty_len

        elapsed_time = time() - start_time
        minutes, seconds = divmod(int(elapsed_time), 60)
        formatted_elapsed_time = f"{minutes:02}:{seconds:02}"

        # Create time info
        total_time = elapsed_time / progress
        remaining_time = total_time - elapsed_time 
        minutes, seconds = divmod(int(remaining_time), 60)
        formatted_remaining_time = f"{minutes:02}:{seconds:02}"

        # Create speed info
        speed = i / elapsed_time
        speed_info = f"{speed:.2f}{unit}/s"

        # Contacenate all info
        info = f" [{formatted_elapsed_time}<{formatted_remaining_time}, {speed_info}]"

        if delay == 0 or (delay and elapsed_time > delay):
            stdout.write(f"\r{percentage}%|{bar}| {i}/{total_len}{info}")

        if leave == False:
            stdout.write("\r")

        yield item
