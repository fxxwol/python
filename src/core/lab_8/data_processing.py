class DataPreprocessing:
    def preprocess_data(self, data):
        preprocessed_data = data.dropna()
        return preprocessed_data
