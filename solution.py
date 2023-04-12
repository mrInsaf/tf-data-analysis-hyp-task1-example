import pandas as pd
import numpy as np


chat_id = 816831722 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    flag = None
    p1 = x_success / x_cnt
    p2 = y_success / y_cnt
    p = (x_success + y_success) / (x_cnt + y_cnt)

    z = (p2 - p1) / np.sqrt(p * (1-p) * (1/x_cnt + 1/y_cnt))

    if z >= -2.33 and z <= 2.33:
      flag = False
    else:
      flag = True
    return flag
