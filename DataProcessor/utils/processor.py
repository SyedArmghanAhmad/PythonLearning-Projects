# data processing and analysis
class Processor:
    @staticmethod
    def get_basic_stats(df):
        """Display basic Statistics of the DataFrame."""
        print("\nBasic Statistics: ")
        print(df.describe())

    @staticmethod
    def add_column(df, new_col_name, default_value):
        """Add a new column with a default value"""
        df[new_col_name] = default_value
        print(f"Column '{new_col_name}' added with default value '{default_value}'.")

    @staticmethod
    def drop_column(df, col_name):
        """Drop a specified column."""
        if col_name in df.columns:
            df.drop(columns = [col_name], inplace=True)
            print(f"Column '{col_name} dropped.'")
        else:
            print(f"Column'{col_name}' does not exist.")
    @staticmethod
    def display_raw_data(df):
        """Display the entire dataset."""
        print("\nRaw Dataset:")
        print(df.to_string(index=False))