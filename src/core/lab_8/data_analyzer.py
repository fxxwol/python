from src.core.lab_8.data_exploration import DataExploration
from src.classes.file_processor import FileProcessor
from src.core.lab_8.visualization import DataVisualizer
from src.core.lab_8.data_processing import DataPreprocessing
from src.core.lab_8.exporter import DataExporter
import os

file_path=os.path.join(os.getcwd(), "src", "results", "exported_diagram.png" )

class DataAnalyzer:
    def __init__(self, csv_file_path):
        self.exploration = DataExploration()
        self.visualization = DataVisualizer()
        self.preprocessing = DataPreprocessing()
        self.exporter = DataExporter()

        file_processor = FileProcessor(csv_file_path)
        self.data = file_processor.csv_load()

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
