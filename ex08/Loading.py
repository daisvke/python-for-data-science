from time import time
from shutil import get_terminal_size


"""
Implementation of tqdm from the tdqm package

 - Handled option: unit, leave, delay, colour
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
    delay: float=0.0,
    colour: str="white"
    ) -> any:

    """
	Implementation of tqdm
    """

    # Get terminal size
    terminal_size = get_terminal_size()
    # Get terminal width
    terminal_width = terminal_size.columns

    total_len = len(iterable)
	# Quit if iterable is empty
    if total_len == 0:
        print(f"\r0{unit} [00:00, ?{unit}/s]", end="")

    start_time = time()

    # Set colours
    colour_dict = get_ansi_colours()
    ansi_colour = colour_dict[colour.lower()]
    reset_colour = "\033[0m"

    for i, item in enumerate(iterable, start=1):
        progress = i / total_len
        percentage = int(progress * 100)

        elapsed_time = time() - start_time
        minutes, seconds = divmod(int(elapsed_time), 60)
        formatted_elapsed_time = f"{minutes:02}:{seconds:02}"

        # Create time info
        total_time = elapsed_time / progress if progress > 0 else 0
        remaining_time = total_time - elapsed_time 
        minutes, seconds = divmod(int(remaining_time), 60)
        formatted_remaining_time = f"{minutes:02}:{seconds:02}"

        # Create speed info
        speed = i / elapsed_time if elapsed_time > 0 else 0
        speed_info = f"{speed:.2f}{unit}/s"

        # Contacenate all time info
        info_time = f" [{formatted_elapsed_time}<{formatted_remaining_time}, {speed_info}]"

        # Concatenate all iteration info
        info_iteration = f"{i}/{total_len}"

        """
		Some caracteristics from the original tqdm that we have copied:
		 - The whole visual module has to occupy 100% of the terminal's width.
		 - The width of the bar itself varies according to the info printed
		  just afterwards:
           when the iteration value 'i' goes from 9 to 10 or from 99 to 100
		   and gets an additional digit, the bar's width loses 1 char of width.
		"""
        # Progression bar width: terminal width - infos around bar
        bar_len = terminal_width - 7 - len(info_time) - len(info_iteration)

        # Create the progress bar
        filled_len = int(bar_len * progress)
        empty_len = bar_len - filled_len
        bar = f"{ansi_colour}█{reset_colour}" * filled_len + " " * empty_len

        if delay == 0 or (delay and elapsed_time > delay):
        # The percentage number is right-aligned within a field of 3 spaces
            print(f"\r{percentage:>3}%|{bar}| {info_iteration}{info_time}", end="")

        yield item

    # If leave is set to False, then we remove the bar before quitting
    if not leave:
    	print("\r" + " " * terminal_width, end="\r")
