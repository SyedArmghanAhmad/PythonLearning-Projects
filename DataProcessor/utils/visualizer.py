#Graphing and visualization
import matplotlib.pyplot as plt
class Visualizer:
    @staticmethod
    def plot_column_distribution(df,column):
        """Generate a bar chart for column value distribution."""
        if column not in df.columns:
            print(f"Column '{column} does not exist.'")
            return
        data = df[column].value_counts()
        plt.figure(figsize=(10,6))
        data.plot(kind='bar', color='skyblue')
        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

