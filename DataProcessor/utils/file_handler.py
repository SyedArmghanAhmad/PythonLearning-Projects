# handles loading and saving files
import pandas as pd

class FileHandler:
    @staticmethod
    def load_csv(file_path):
        """Load a CSV file into a DataFrame."""
        try:
            data =pd.read_csv(file_path)
            print("File loaded successfully!")
            return data
        except FileNotFoundError:
            print("Error: File not found!!")
        except Exception as e:
            print(f"An error occurred: {e}")
        return None

    @staticmethod

    def save_to_csv(df):
        """Save the DataFrame to a CSV file."""
        try:
            path = input("Enter the path to save the CSV file (include filename, e.g., 'E:\\DataProcessor\\data.csv'): ")
            # Check if the path ends with '.csv'
            if not path.lower().endswith('.csv'):
                print("Error: Please include a valid file name with the '.csv' extension.")
                return
            df.to_csv(path, index=False)
            print(f"File saved successfully at {path}")
        except Exception as e:
            print(f"An error occurred: {e}")
    @staticmethod
    def save_processed_data(df):
        """Save the processed DataFrame to a CSV file."""
        try:
            # Ask the user for the file path where the processed data should be saved
            path = input("Enter the path to save the processed data (include filename, e.g., 'E:\\DataProcessor\\processed_data.csv'): ")
            # Check if the file name ends with '.csv'
            if not path.lower().endswith('.csv'):
                print("Error: Please include a valid file name with the '.csv' extension.")
                return
            # Save the processed data to the provided path
            df.to_csv(path, index=False)
            print(f"Processed data saved successfully to {path}.")
        except Exception as e:
            print(f"An error occurred: {e}")

