# csv-data-analyzer
This is a Django-based web application that allows users to upload CSV files and analyze the data.

## Features
- Upload CSV files
- Display first few rows of data
- Show summary statistics
- Handle missing values
- Display histogram of the data

# Setup Instructions

1. Clone the repository:
git clone https://github.com/varsha-wagh-45/csv-data-analyzer.git

2. Navigate to the project directory:
cd csv_analysis_project

3. Create a virtual environment:
python -m venv env

4. Activate the virtual environment:
- On Windows:
  .\env\Scripts\activate

5. Install the dependencies:
pip install -r requirements.txt

6. Run the Django development server:
python manage.py runserver

7. Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Sample CSV File
A sample CSV file for testing is included in the `uploads` directory.
