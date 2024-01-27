import sys

def parse_time(minutes):
    hours, mins = divmod(minutes, 60)
    return f'{hours} Hour{"s" if hours != 1 else ""}, {mins} Minute{"s" if mins != 1 else ""}'

def analyze_log(file_path):
    cat_visits = 0
    other_cats = 0
    total_time_in_house = 0
    durations = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip() == 'END':
                    break

                cat_type, entry_time, exit_time = line.strip().split(',')
                entry_time, exit_time = int(entry_time), int(exit_time)

                if cat_type == 'OURS':
                    cat_visits += 1
                    total_time_in_house += exit_time - entry_time
                    durations.append(exit_time - entry_time)
                elif cat_type == 'THEIRS':
                    other_cats += 1

    except FileNotFoundError:
        print(f'Cannot open "{file_path}"!')
        return

    print("\nLog File Analysis\n==================")
    print(f'Cat Visits: {cat_visits}')
    print(f'Other Cats: {other_cats}')
    print(f'Total Time in House: {parse_time(total_time_in_house)}')
    
    if cat_visits > 0:
        average_duration = sum(durations) / len(durations) if len(durations) > 0 else 0
        print(f'\nAverage Visit Length: {parse_time(int(average_duration))}')
        print(f'Longest Visit:        {parse_time(max(durations))}')
        print(f'Shortest Visit:       {parse_time(min(durations))}')


if len(sys.argv) != 2:
    print('Missing command line argument!')
else:
    file_path = sys.argv[1]
    analyze_log(file_path)