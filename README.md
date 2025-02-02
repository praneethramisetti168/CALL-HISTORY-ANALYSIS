# CALL-HISTORY-ANALYSIS

**Overview**

This project analyzes call history data from a CSV file, extracts key details, and visualizes call statistics. It includes functionality for filtering call records based on specific names and generating insightful charts to display call trends.

**Features**

- Reads call history from a CSV file
- Filters calls based on specified names
- Extracts details such as call duration, call type, and timestamps
- Identifies the most recent contact
- Generates visualizations for:
  - Total calls and call duration per contact
  - Outgoing vs. Incoming calls per contact
- Provides interactive plots with hover functionality for better insights

**Requirements**

Ensure you have the following Python packages installed:

- `csv` (built-in)
- `collections` (built-in)
- `datetime` (built-in)
- `matplotlib`
- `mplcursors`

You can install the required external libraries using:

```sh
pip install matplotlib mplcursors
```

***File Descriptions***

- `filter_call_history.py`: Filters call history based on specified names.
- `analyze_call_history.py`: Reads, processes, and visualizes call data.
- `filtered_call_history.csv`: Output file containing filtered call records.

## Usage

### Step 1: Filter Call History

Run the following command to filter call records by specific names:

```sh
python filter_call_history.py
```

This will create a `filtered_call_history.csv` file containing only relevant records.

### Step 2: Analyze Call History

After filtering, run the analysis script:

```sh
python analyze_call_history.py
```

This will generate interactive visualizations showing:

- Total calls and call duration per contact
- Outgoing vs. Incoming calls

**Customization**

To filter by different names, modify the `filter_names` list in `filter_call_history.py`:

```python
filter_names = ['Name1', 'Name2', 'Name3']  # Replace with desired names
```

**Notes**

- Ensure the input CSV file (`h1.csv`) follows the format with headers: `Name`, `Number`, `Duration`, `Date`, `Type`.
- The script assumes the date format is `%Y-%m-%d %H:%M`.
- The duration column should contain values in seconds.

**License**

This project is open-source and free to use.


**Author**

Ramisetti Praneeth
CONTACT ME:praneethramisetti9\@gmail.com

