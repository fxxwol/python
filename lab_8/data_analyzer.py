from csv_loader import CSVLoader
from data_exploration import DataExploration
from visualization import DataVisualizer  # Update import statement
from data_processing import DataPreprocessing
from exporter import DataExporter
import os

# Get the current script directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# Navigate up one level to the root directory
root_directory = os.path.dirname(script_directory)

# Create a path to the "results" directory in the root
results_directory = os.path.join(root_directory, "results")

file_path = os.path.join(root_directory, "results", "exported_visualization.png")

class DataAnalyzer:
    def __init__(self, csv_file_path):
        self.loader = CSVLoader()
        self.exploration = DataExploration()
        self.visualization = DataVisualizer()  # Update class instantiation
        self.preprocessing = DataPreprocessing()
        self.exporter = DataExporter()

        self.data = self.loader.load_csv(csv_file_path)

    def run_analysis(self):
        # Data Exploration
        self.exploration.find_extremes(self.data)

        # Choose Visualization Types
        # Data Preparation
        preprocessed_data = self.preprocessing.preprocess_data(self.data)

        # Basic Visualization
        self.visualization.basic_visualization(preprocessed_data, "Price")

        # Advanced Visualizations
        self.visualization.advanced_visualizations(preprocessed_data)

        # Multiple Subplots
        # Export and Share
        self.exporter.export_visualization(
            preprocessed_data,
            column_name="Price",
            filename=file_path,
        )
