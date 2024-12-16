from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm, get_ansi_colours
from shutil import get_terminal_size

# Get terminal size
terminal_size = get_terminal_size()
# Get terminal width
width = terminal_size.columns

# Create separation line
separation_line = '-' * width

# Create labels to distinguish between custom and original tqdm
ansi_colours = get_ansi_colours()
yellow = ansi_colours["yellow"]
cyan = ansi_colours["cyan"]
reset_colour = "\033[0m"
label_custom = f"[{yellow}CUSTOM{reset_colour}]"
label_original = f"[{cyan}ORIGINAL{reset_colour}]"
label_info = f"[{yellow}INFO{reset_colour}]"

# Example with leave argument set to False
print(f"{label_info} Example with 'leave' argument set to False\n")
print(label_custom)
for elem in ft_tqdm("", leave=False):
    sleep(0.005)
print()
print(label_original)
for elem in tqdm("", leave=False):
    sleep(0.005)

print(separation_line)

# Example with an empty iterator and 'elem' as unit
print(f"{label_info} Example with empty iterator + 'elem' as unit\n")
print(label_custom)
for elem in ft_tqdm("", unit="elem"):
    sleep(0.005)
print()
print(label_original)
for elem in tqdm("", unit="elem"):
    sleep(0.005)

print(separation_line)

# Example with a delay value
print(f"{label_info} Example with a delay value\n")
print(label_custom)
for elem in ft_tqdm(range(400), delay=.5):
    sleep(0.002)
print()
print(label_original)
for elem in tqdm(range(400), delay=.5):
    sleep(0.002)
print()

# Example with green colour
print(f"{label_info} Example with green colour\n")
print(label_custom)
for elem in ft_tqdm(range(333), colour="green"):
    sleep(0.005)
print()
print(label_original)
for elem in tqdm(range(333), colour="green"):
    sleep(0.005)
print()

print(separation_line)

# Example with a long sleep time
print(f"{label_info} Example with a long sleep time\n")
print(label_custom)
for elem in ft_tqdm(range(333), colour="white"):
    sleep(0.05)
print()
print(label_original)
for elem in tqdm(range(333), colour="white"):
    sleep(0.05)
print()
