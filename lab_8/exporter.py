import matplotlib.pyplot as plt

class DataExporter:
    def export_visualization(self, data, filename="visualization.png"):
        plt.figure(figsize=(10, 6))
        plt.plot(data["Price"])
        plt.title("Exported Visualization: Price")
        plt.xlabel("Index")
        plt.ylabel("Price")
        plt.savefig(filename)
        print(f"Visualization exported as {filename}")
