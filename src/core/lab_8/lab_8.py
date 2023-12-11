from src.core.lab_8.data_analyzer import DataAnalyzer
import os

current_directory = os.path.dirname(os.path.abspath(__file__))


def main():
    csv_file_path = os.path.join(current_directory, "books_sales_data.csv")
    analyzer = DataAnalyzer(csv_file_path)
    analyzer.run_analysis()

if __name__ == "__main__":
    main()