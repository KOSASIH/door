# tests/test_data_analysis.py

import unittest
import pandas as pd
from services.data_analysis import DataAnalyzer

class TestDataAnalyzer(unittest.TestCase):
    def setUp(self):
        # Sample data for testing
        data = {
            'feature1': [1, 2, 3, 4, 5],
            'target': [2, 3, 5, 7, 11]
        }
        self.df = pd.DataFrame(data)
        self.analyzer = DataAnalyzer(self.df)

    def test_preprocess_data(self):
        self.analyzer.preprocess_data()
        self.assertFalse(self.df.isnull().values.any(), "Data should not contain null values after preprocessing.")

    def test_analyze_trends(self):
        model, predictions = self.analyzer.analyze_trends('feature1', 'target')
        self.assertIsNotNone(model, "Model should be created.")
        self.assertEqual(len(predictions), 1, "Predictions should be made for the test set.")

    def test_advanced_analysis(self):
        model, predictions = self.analyzer.advanced_analysis(['feature1'], 'target')
        self.assertIsNotNone(model, "Model should be created for advanced analysis.")
        self.assertEqual(len(predictions), 1, "Predictions should be made for the test set.")

if __name__ == '__main__':
    unittest.main()
