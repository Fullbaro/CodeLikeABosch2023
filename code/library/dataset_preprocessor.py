import pandas as pd


def read(path="../data/DevelopmentData.csv"):
    data = pd.read_csv(path, sep=";")
    data.set_index("Unnamed: 0", inplace=True)
    data.index.rename("ind", inplace=True)
    return data

def normalize(data):
    data_norm = data.copy()

    data_norm[["FirstObjectDistance_X", "FirstObjectDistance_Y", "SecondObjectDistance_X", "SecondObjectDistance_Y", "ThirdObjectDistance_X", "ThirdObjectDistance_Y", "FourthObjectDistance_X", "FourthObjectDistance_Y"]] = \
    data[["FirstObjectDistance_X", "FirstObjectDistance_Y", "SecondObjectDistance_X", "SecondObjectDistance_Y", "ThirdObjectDistance_X", "ThirdObjectDistance_Y", "FourthObjectDistance_X", "FourthObjectDistance_Y"]] / 128

    data_norm[["VehicleSpeed", "FirstObjectSpeed_X", "FirstObjectSpeed_Y", "SecondObjectSpeed_X", "SecondObjectSpeed_Y", "ThirdObjectSpeed_X", "ThirdObjectSpeed_Y", "FourthObjectSpeed_X", "FourthObjectSpeed_Y"]] = \
    data[["VehicleSpeed", "FirstObjectSpeed_X", "FirstObjectSpeed_Y", "SecondObjectSpeed_X", "SecondObjectSpeed_Y", "ThirdObjectSpeed_X", "ThirdObjectSpeed_Y", "FourthObjectSpeed_X", "FourthObjectSpeed_Y"]] / 256

    return data_norm
