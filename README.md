# Python Data Quality Checker
Python script to read a SQL database and check the data quality. It also includes a simple GUI for interaction.

![image](https://github.com/blacksheepaway/Data-Parser/assets/50200471/1c6f19c3-3b91-40c2-b390-118d6ec84e87)


## Project Structure

This project consists of three main Python scripts:

1. `setup_db.py`: sets up a SQLite database and populates it with randomly generated car data for example purposes.
2. `data_quality_checker.py`: extracts data from the SQLite database and checks its quality, outputting any issues found.
3. `data_quality_checker_gui.py`: provides a simple graphical user interface to run the database setup and data quality check functions.

## Installation

1. Clone this repository or download the scripts.
2. Install the required packages using pip:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Run `data_quality_checker_gui.py` from the command line:

    ```
    python data_quality_checker_gui.py
    ```

2. In the GUI, enter the name of the database file (e.g., `my_database.db`) in the text box and click the "Setup DB" button to create and populate the database.

3. Click the "Check Data Quality" button to perform the data quality check. The results will appear in the text box below the buttons.

## Features

- Set up a SQLite database and populate it with randomly generated car data.
- Check the quality of the data, looking for issues such as missing values and duplicate rows.
- User-friendly GUI that allows easy use of the database setup and data quality check functions.

## Dependencies

- Python 3.8 or later
- pandas
- sqlite3
- tkinter

## License

This project is licensed under the terms of the MIT license.
