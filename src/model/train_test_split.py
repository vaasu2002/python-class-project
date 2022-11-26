import sys
import numpy as np
import random
from src.exception import GeoException
class TrainTestSplit:
    def __init__(self,):
        pass

    def train_test_split(self,dataframe,test_size:float=0.2):
        """Performing train-test split on the dataframe

        Args:
            X (array): numpy array of features
            y (array): numpy array of target vlasses
            test_size (float, optional): Percentage of data to be taken as the testing data . Defaults to 0.2.

        Raises:
            GeoException: exception 

        Returns:
            arrays: X_train, y_train, X_test, y_test
        """
        try:
            self.dataframe = dataframe
            total_rows = len(dataframe)





            total_rows = X.shape[0]
            total_testing_rows = int(total_rows*test_size)
            random_row = np.random.randint(0,total_rows,total_testing_rows)
            X_train = np.array(X[random_row])
            X_test = np.delete(X, random_row, axis=0)
            y_train = np.array(y[random_row])
            y_test = np.delete(y, random_row, axis=0)
            return X_train, y_train, X_test, y_test



        except Exception as e:
            raise GeoException(e,sys)