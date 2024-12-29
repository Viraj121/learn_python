import pandas as pd

def read_excel_links(file_path="sheet2.xlsx", column_name="rtpLink"):
    """
    Reads a list of links from an Excel file.

    :param file_path: Path to the Excel file.
    :param column_name: Name of the column containing the URLs.
    :return: A list of URLs or an empty list if the column is not found.
    """
    try:
        # Load the Excel file
        data = pd.read_excel(file_path, engine="openpyxl")

        # Check if the column exists (case-insensitive)
        columns_lower = [col.lower() for col in data.columns]
        if column_name.lower() not in columns_lower:
            print(f"ERROR: Column '{column_name}' not found in the Excel file.")
            return []

        # Get the exact column name with matching case
        column_name_actual = data.columns[columns_lower.index(column_name.lower())]

        # Drop any rows with missing links and return the column as a list
        links = data[column_name_actual].dropna().tolist()
        return list(set(links))  # Remove duplicates

    except FileNotFoundError:
        print(f"ERROR: File '{file_path}' not found.")
        return []

    except Exception as e:
        print(f"ERROR: An error occurred while reading the Excel file: {e}")
        return []
