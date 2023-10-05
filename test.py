
from tqdm import tqdm
from time import sleep


if __name__ == "__main__":

    print("TESTING")
    for i in tqdm(range(10)):
        sleep(0.2)
    print('Done')