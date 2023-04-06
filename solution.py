import pandas as pd
import numpy as np

from scipy.stats import gamma


chat_id = 475225606  # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = x.shape[0]
    m = x.mean()
    return m/8 - 0.25 + gamma.ppf((1 - p)/2, n) / (2 * n), m/8 - 0.25 + gamma.ppf((1 + p)/2, n) / (2 * n)
