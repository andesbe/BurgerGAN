import pandas as pd
import numpy as np
from tabgan.sampler import OriginalGenerator, GANGenerator


def load_burgerdata():
    pd.read_csv("burger-king-menu.csv")

load_burgerdata()












if __name__ == "__main__":
