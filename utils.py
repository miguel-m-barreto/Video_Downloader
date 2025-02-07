import datetime

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

# Generate a unique output folder with a timestamp
def get_timestamp_output_folder(base_folder):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    safe_base_folder = base_folder.replace(":", "-").replace(" ", "_")  # Ensure safe folder names
    return f"{safe_base_folder}_{timestamp}"