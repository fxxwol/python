class DataExploration:
    def find_extremes(self, data):
        for column in data.columns:
            min_val = data[column].min()
            max_val = data[column].max()
            print(f"{column}: Min = {min_val}, Max = {max_val}")
