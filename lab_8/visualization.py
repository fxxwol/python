import matplotlib.pyplot as plt


class DataVisualizer:
    def basic_visualization(self, data, column_name):
        plt.figure(figsize=(10, 6))
        plt.plot(data[column_name])
        plt.title(f"Basic Visualization - {column_name}")
        plt.xlabel("Index")
        plt.ylabel(column_name)
        plt.show()

    def advanced_visualizations(self, data):
        plt.figure(figsize=(12, 8))

        # Example 1: Scatter plot between Price and QuantitySold
        plt.subplot(2, 2, 1)
        plt.scatter(data["Price"], data["QuantitySold"])
        plt.title("Scatter Plot: Price vs QuantitySold")

        # Example 2: Bar chart for Genre-wise QuantitySold
        plt.subplot(2, 2, 2)
        genre_counts = data["Genre"].value_counts()
        genre_counts.plot(kind="bar", color="skyblue")
        plt.title("Genre-wise QuantitySold")
        plt.xlabel("Genre")
        plt.ylabel("QuantitySold")

        plt.tight_layout()
        plt.show()
