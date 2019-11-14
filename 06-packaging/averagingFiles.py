"""Computation of column-wise average of a array-like file.

INPUTS: .csv file named data_NUMBER 
RETURNS: .csv or .txt named results_NUMBER"""
from argparse import ArgumentParser
import numpy
import pandas as pd


if __name__ == "__main__":
    # python squares.py <numbers file> <weights file>
    parser = ArgumentParser(description="Averaging data columnwise")
    parser.add_argument('--data', '-d')
    parser.add_argument('--txt', '-t')
    parser.add_argument('--csv', '-csv')

    arguments = parser.parse_args()

    # importing the file as a pandas array
    data = pd.read_csv(arguments.data, skipinitialspace = True, delimiter=",", header=None)

    string = (arguments.data.split('_')) # finding the first character after .csv or .txt
    stringNumber = (string[1]).split('.') # finding the number vs the text type
    
    # Exceptions TODO

    # We average the data columnwise using the inbuilt function
    average = data.mean(axis = 0).to_numpy()
    
    # Now we turn the numpy array into a txt or csv
    if (arguments.csv):
        numpy.savetxt(("results_"+stringNumber[0]+".csv"), (average.round(1)).T, delimiter =",")
    if (arguments.txt):
        numpy.savetxt(("results_" + stringNumber[0] + ".txt"), (average.round(1)).T)
        
    print('Saved', average.T)