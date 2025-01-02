import pandas as pd
import os

def read_excel_links(file_path="sheet2.xlsx", column_name="rtpLink"):
    """
    Reads a specific column from an Excel file and returns the values as a list.
    
    :param file_path: Path to the Excel file.
    :param column_name: Column name to extract.
    :return: List of values from the column.
    """
    try:
        df = pd.read_excel(file_path, engine="openpyxl")
        return df[column_name].tolist()
    except Exception as e:
        print(f"ERROR: Could not read the Excel file: {e}")
        return []
# folder_path, file_name, incorrect_bleeds
def store_incorrect_bleeds(wrong_rtp, incorrect_rtp_file, incorrect_bleeds):
    """
    Stores the incorrect bleed data into an Excel file.
    If the file doesn't exist, it creates a new one. If it exists, it appends the data.

    :param folder_path: Path to the folder where the Excel file will be saved.
    :param file_name: Name of the Excel file.
    :param incorrect_bleeds: List of dictionaries containing incorrect bleed data.
    """
    try:
        # Ensure the folder exists
        if not os.path.exists(wrong_rtp):
            os.makedirs(wrong_rtp)

        file_path = os.path.join(wrong_rtp, incorrect_rtp_file)

        # Create a DataFrame from the incorrect bleeds
        df = pd.DataFrame(incorrect_bleeds)

        if os.path.exists(file_path):
            # Append to the existing file
            existing_data = pd.read_excel(file_path, engine="openpyxl")
            updated_data = pd.concat([existing_data, df], ignore_index=True)
            updated_data.to_excel(file_path, index=False, engine="openpyxl")
        else:
            # Create a new file and save the data
            df.to_excel(file_path, index=False, engine="openpyxl")

    except Exception as e:
        print(f"ERROR: Could not write to file '{incorrect_rtp_file}': {e}")
