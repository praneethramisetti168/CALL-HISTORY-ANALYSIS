import csv
from collections import defaultdict
from datetime import datetime
import matplotlib.pyplot as plt
import mplcursors  # Import mplcursors for hover functionality

def normalize_header(header):
    return header.strip().lower().replace(' ', '_')

def analyze_call_history(call_history_file):
    # Dictionary to store call details
    call_details = defaultdict(list)
    
    # Read CSV file and extract call details
    with open(call_history_file, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        
        # Normalize headers
        normalized_fieldnames = {normalize_header(field): field for field in reader.fieldnames}
        
        for row in reader:
            name = row[normalized_fieldnames['name']]
            number = row[normalized_fieldnames['number']]
            duration = int(row[normalized_fieldnames['duration']])  # Assuming duration is in seconds
            call_datetime_str = row[normalized_fieldnames['date']]
            call_type = row[normalized_fieldnames['type']]
            
            # Parse date and time
            call_datetime = datetime.strptime(call_datetime_str, '%Y-%m-%d %H:%M')
            
            # Store call details
            call_details[number].append({
                'name': name,
                'duration': duration,
                'datetime': call_datetime,
                'type': call_type
            })
    
    # Analyze call details
    most_recent_contact = None
    most_recent_datetime = datetime.min
    caller_stats = defaultdict(lambda: {'total_calls': 0, 'total_duration': 0, 'outgoing_calls': 0, 'incoming_calls': 0, 'name': ''})
    
    for number, calls in call_details.items():
        total_calls = len(calls)
        total_duration = sum(call['duration'] for call in calls)
        outgoing_calls = sum(1 for call in calls if call['type'].lower() == 'outgoing')
        incoming_calls = sum(1 for call in calls if call['type'].lower() == 'incoming')
        name = calls[0]['name']  # Assuming the same name for all calls under a number
        
        # Find the most recent contact
        latest_call = max(calls, key=lambda x: x['datetime'])
        if latest_call['datetime'] > most_recent_datetime:
            most_recent_datetime = latest_call['datetime']
            most_recent_contact = number
        
        # Update caller statistics
        caller_stats[number]['total_calls'] = total_calls
        caller_stats[number]['total_duration'] = total_duration
        caller_stats[number]['outgoing_calls'] = outgoing_calls
        caller_stats[number]['incoming_calls'] = incoming_calls
        caller_stats[number]['name'] = name
    
    # Visualize call statistics
    visualize_call_statistics(caller_stats)

    # Print most recent contact information
    if most_recent_contact:
        print(f"\nMost recent contact:")
        print(f"Number: {most_recent_contact}")
        print(f"Date/time: {most_recent_datetime}")
    else:
        print("\nNo calls found.")

def visualize_call_statistics(caller_stats):
    # Prepare data for visualization
    numbers = []
    total_calls = []
    total_duration = []
    outgoing_calls = []
    incoming_calls = []
    names = []  # List to store names for hover display
    
    for number, stats in caller_stats.items():
        numbers.append(number)
        total_calls.append(stats['total_calls'])
        total_duration.append(stats['total_duration'] // 60)  # Convert duration to minutes
        outgoing_calls.append(stats['outgoing_calls'])
        incoming_calls.append(stats['incoming_calls'])
        names.append(stats['name'])  # Populate names list
    
    # Plotting total calls, total duration
    fig, ax1 = plt.subplots()
    
    color = 'tab:red'
    ax1.set_ylabel('Total Calls', color=color)
    bars = ax1.bar(numbers, total_calls, color=color, alpha=0.6)
    ax1.tick_params(axis='y', labelcolor=color)
    
    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('Total Duration (minutes)', color=color)
    ax2.plot(numbers, total_duration, color=color, marker='o')
    ax2.tick_params(axis='y', labelcolor=color)
    
    fig.tight_layout()
    plt.title('Call Statistics by Number')
    plt.xticks(rotation=45)
    
    # Add hover functionality using mplcursors
    mplcursors.cursor(bars, hover=True).connect("add", lambda sel: sel.annotation.set_text(
        f"Name: {names[sel.target.index]}\nTotal Calls: {total_calls[sel.target.index]}\nTotal Duration (minutes): {total_duration[sel.target.index]}"
    ))
    
    plt.show()
    
    # Plotting outgoing and incoming calls
    fig, ax = plt.subplots()
    
    width = 0.4
    IO = ax.bar(numbers, outgoing_calls, width, label='Outgoing Calls', color='tab:green', alpha=0.6)
    ax.bar([n + width for n in range(len(numbers))], incoming_calls, width, label='Incoming Calls', color='tab:orange', alpha=0.6)
    
    ax.set_ylabel('Number of Calls')
    ax.set_title('Outgoing vs Incoming Calls by Number')
    ax.set_xticks([n + width / 2 for n in range(len(numbers))])
    ax.set_xticklabels(names, rotation=45)
    ax.legend()
        
    mplcursors.cursor(IO, hover=True).connect("add", lambda sel: sel.annotation.set_text(
        f"Outgoing: {outgoing_calls[sel.target.index]}\nIncoming: {incoming_calls[sel.target.index]}\nName: {names[sel.target.index]}"
    ))
    
    plt.tight_layout()
    plt.show()

# Example usage:
call_history_file = 'filtered_call_history.csv'  # Replace with your actual CSV file path
analyze_call_history(call_history_file)
