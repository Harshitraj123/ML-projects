import os
import sys
import dill
import numpy as np
import pandas as pd

from src.exception import CustomException

def save_object(file_path, obj):
    try:
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)