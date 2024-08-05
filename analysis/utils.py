import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

def process_file(file_path):
    # Read the CSV file using pandas
    df = pd.read_csv(file_path)

    # Display first few rows
    first_rows = df.head()

    # Calculate summary statistics
    summary_stats = df.describe()

    # Handle missing values
    missing_values = df.isnull().sum()

    # Convert missing_values to DataFrame for HTML rendering
    missing_values_df = missing_values.to_frame(name='Missing Values')

    # Generate visualizations
    plt.figure(figsize=(10, 6))
    df.hist(bins=30)
    plt.tight_layout()

    # Save plot to a string buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    # Encode image to base64 string
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    context = {
        'first_rows': first_rows.to_html(),
        'summary_stats': summary_stats.to_html(),
        'missing_values': missing_values_df.to_html(),  # Updated to DataFrame
        'graphic': graphic,
    }
    return context
