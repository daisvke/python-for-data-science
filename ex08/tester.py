from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm


print("Custom tqdm:")
for elem in ft_tqdm("", colour="cyan"):
    sleep(0.005)
print()
print("Original tqdm:")
for elem in tqdm("", colour="green"):
    sleep(0.005)

print("----------------------------------------")

print("Custom tqdm:")
for elem in ft_tqdm(range(333), colour="cyan"):
    sleep(0.005)
print()
print("Original tqdm:")
for elem in tqdm(range(333), colour="green"):
    sleep(0.005)
print()
