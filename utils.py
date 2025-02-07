import datetime
import os

# Format elapsed/remaining time into a human-readable string
def format_time(seconds):
    """Formats elapsed/remaining time into a human-readable string."""
    if seconds < 60:
        return f"{seconds:.2f} Seconds"
    elif seconds < 3600:
        return f"{int(seconds // 60)} Minutes and {int(seconds % 60)} Seconds"
    elif seconds < 86400:
        return f"{int(seconds // 3600)} Hours, {int((seconds % 3600) // 60)} Minutes and {int(seconds % 60)} Seconds"
    elif seconds < 2626560:
        return f"{int(seconds // 86400)} Days, {int((seconds % 86400) // 3600)} Hours, {int((seconds % 3600) // 60)} Minutes and {int(seconds % 60)} Seconds"
    elif seconds < 31536000:
        return f"{int(seconds // 2626560)} Months, {int((seconds % 2626560) // 86400)} Days, {int((seconds % 86400) // 3600)} Hours, {int((seconds % 3600) // 60)} Minutes and {int(seconds % 60)} Seconds"
    else:
        return f"{int(seconds // 31536000)} Years, {int((seconds % 31536000) // 2626560)} Months, {int((seconds % 2626560) // 86400)} Days, {int((seconds % 86400) // 3600)} Hours, {int((seconds % 3600) // 60)} Minutes and {int(seconds % 60)} Seconds"

# Generate a unique output folder if one already exists
def get_unique_output_folder(base_folder):
    """Generate a unique folder name by appending a number if the folder already exists."""
    if not os.path.exists(base_folder):
        return None
    count = 2
    while True:
        new_folder = f"{base_folder}({count})"
        if not os.path.exists(new_folder):
            return new_folder
        count += 1

# Generate a unique output folder with a timestamp
def get_timestamp_output_folder(base_folder):
    """
    Generate a unique folder name using a timestamp to prevent overwriting.
    
    Parameters:
        base_folder (str): The base folder path where the output should be saved.
    
    Returns:
        str: A unique folder name with a timestamp.
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    unique_folder = f"{base_folder}{timestamp}"

    return unique_folder