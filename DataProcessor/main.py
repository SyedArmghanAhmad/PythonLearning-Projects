# Entry point of the project
from utils.file_handler import FileHandler
from utils.processor import Processor
from utils.visualizer import Visualizer

class DataProcessingTool:
    def __init__(self):
        self.data=None

    def menu(self):
        while True:
            print("\n--- Data Processing Tool ---")
            print("1. Load CSV File")
            print("2. Display Data Raw")
            print("3. Display Basic Statistics")
            print("4. Add Column")
            print("5. Drop Column")
            print("6. Visualize Column Distribution")
            print("7. Save Processed Data")
            print("8. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                file_path = input("Enter the  path to the CSV file: ")
                self.data = FileHandler.load_csv(file_path)
            elif choice == "2" and self.data is not None:
                Processor.display_raw_data(self.data)
            elif choice =="3" and self.data is not None :
                Processor.get_basic_stats(self.data)
            elif choice == "4" and self.data is not None:
                col_name = input("Enter new column name: ")
                default_value = input("Enter the default value for the column: ")
                Processor.add_column(self.data,col_name,default_value)
            elif choice =="5" and self.data is not None:
                col_name = input("Enter column nae to drop: ")
                Processor.drop_column(self.data, col_name)
            elif choice == "6" and self.data is not None:
                col_name = input("Enter the column name to visualize: ")
                Visualizer.plot_column_distribution(self.data, col_name)
            elif choice == "7" and self.data is not None:
                file_path = input("Enter the path to save the CSV file: ")
                FileHandler.save_csv(self.data, file_path)
            elif choice == "8":
                print("Exiting the tool. Bye!!😉")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    tool = DataProcessingTool()
    tool.menu()
    