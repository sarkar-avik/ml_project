import os
import sys

from dataclasses import dataclass

import numpy as np
import pandas as pd

import dill

from src.logger import logging
from src.exception import CustomException
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV


def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj,file_obj)

        pass
    except Exception as e:
        raise CustomException(e,sys)


def evaluate_models(X_train, y_train, X_test, y_test, models, params):
    try:
        # report_train = {}
        report_test = {}

        for i in range(len(models)):
            model=list(models.values())[i]
            para=params[list(models.keys())[i]]

            # GridSearchCV can be used here to find the best hyperparameters for the model
            gs = GridSearchCV(model, para, cv=3)
            gs.fit(X_train, y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            # Make predictions
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            # Evaluate Train and Test 
            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            # report_train[list(models.keys())[i]] = train_model_score
            report_test[list(models.keys())[i]] = test_model_score

        # return (f"Train Report: {report_train}", f"Test Report: {report_test}")
        return report_test

    except Exception as e:
        raise CustomException(e, sys)


def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise CustomException(e, sys)
