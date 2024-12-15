from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm


for elem in ft_tqdm(range(333), colour="cyan"):
    sleep(0.005)
print()
for elem in tqdm(range(333), colour="green"):
    sleep(0.005)
print()
