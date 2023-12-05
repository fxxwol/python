import matplotlib.pyplot as plt


class DataExporter:
    def export_visualization(
        self, data, column_name=None, filename="exported_visualization.png"
    ):
        fig, ax = plt.subplots(figsize=(10, 6))
        
        if column_name and column_name in data.columns:
            ax.plot(data[column_name])
            ax.set_title(f"Exported Visualization - {column_name}")
            ax.set_xlabel("Index")
            ax.set_ylabel(column_name)
            fig.savefig(filename)
            plt.close(fig) 
            print(f"Visualization exported as {filename}")
        else:
            print(f"Error: Column {column_name} not found in the dataset.")
