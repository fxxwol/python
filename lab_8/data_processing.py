class DataPreprocessing:
    def preprocess_data(self, data):
        # Simple example: drop rows with missing values
        preprocessed_data = data.dropna()
        return preprocessed_data
