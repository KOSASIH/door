# services/data_analysis.py

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import logging

logger = logging.getLogger(__name__)

class DataAnalyzer:
    def __init__(self, data):
        """
        Initialize the DataAnalyzer with a DataFrame.
        
        :param data: A pandas DataFrame containing the data to analyze.
        """
        self.data = data

    def preprocess_data(self):
        """
        Preprocess the data for analysis.
        This can include handling missing values, encoding categorical variables, etc.
        """
        logger.info("Preprocessing data...")
        self.data.fillna(method='ffill', inplace=True)  # Forward fill for missing values
        logger.info("Data preprocessing complete.")

    def analyze_trends(self, feature, target):
        """
        Analyze trends using linear regression.
        
        :param feature: The feature column name as a string.
        :param target: The target column name as a string.
        :return: The regression model and predictions.
        """
        logger.info(f"Analyzing trends for {feature} predicting {target}...")
        X = self.data[[feature]]
        y = self.data[target]

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create and fit the model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Make predictions
        predictions = model.predict(X_test)

        # Plotting the results
        plt.scatter(X_test, y_test, color='blue', label='Actual')
        plt.plot(X_test, predictions, color='red', label='Predicted')
        plt.title(f'Trend Analysis: {feature} vs {target}')
        plt.xlabel(feature)
        plt.ylabel(target)
        plt.legend()
        plt.show()

        logger.info("Trend analysis complete.")
        return model, predictions

    def advanced_analysis(self, features, target):
        """
        Perform advanced analysis using Random Forest regression.
        
        :param features: A list of feature column names.
        :param target: The target column name as a string.
        :return: The trained model and predictions.
        """
        logger.info(f"Performing advanced analysis with features: {features} predicting {target}...")
        X = self.data[features]
        y = self.data[target]

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Create and fit the model
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Make predictions
        predictions = model.predict(X_test)

        logger.info("Advanced analysis complete.")
        return model, predictions

    def real_time_analysis(self, new_data):
        """
        Analyze new incoming data in real-time.
        
        :param new_data: A pandas DataFrame containing new data to analyze.
        :return: Predictions based on the trained model.
        """
        logger.info("Performing real-time analysis...")
        # Assuming the model is already trained and available
        # This is a placeholder for real-time analysis logic
        # In practice, you would load a pre-trained model and use it here
        predictions = self.model.predict(new_data)
        logger.info("Real-time analysis complete.")
        return predictions
