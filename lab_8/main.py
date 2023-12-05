from csv_loader import CSVLoader
from data_exploration import DataExploration
from visualization import DataVisualizer  # Update import statement
from data_processing import DataPreprocessing
from exporter import DataExporter
import os

current_directory = os.path.dirname(os.path.abspath(__file__))


class DataAnalyzer:
    def __init__(self, csv_file_path):
        self.loader = CSVLoader()
        self.exploration = DataExploration()
        self.visualization = DataVisualizer()  # Update class instantiation
        self.preprocessing = DataPreprocessing()
        self.exporter = DataExporter()

        self.data = self.loader.load_csv(csv_file_path)

    def run_analysis(self):
        # Task 3: Data Exploration
        self.exploration.find_extremes(self.data)

        # Task 4: Choose Visualization Types
        # Task 5: Data Preparation
        preprocessed_data = self.preprocessing.preprocess_data(self.data)

        # Task 6: Basic Visualization
        self.visualization.basic_visualization(preprocessed_data, "Price")

        # Task 7: Advanced Visualizations
        self.visualization.advanced_visualizations(preprocessed_data)

        # Task 8: Multiple Subplots
        # Task 9: Export and Share
        self.exporter.export_visualization(
            preprocessed_data, filename="exported_visualization.png"
        )


if __name__ == "__main__":
    # Task 1: Choose CSV Dataset
    csv_file_path = os.path.join(current_directory, "books_sales_data.csv")
    analyzer = DataAnalyzer(csv_file_path)
    analyzer.run_analysis()
