time_string = '1h 45m,360s,25m,30m 120s,2h 60s'

time_values = time_string.split(',')

total_minutes = 0

for time in time_values:
    minutes = 0
    parts = time.split()
    for part in parts:
        if 'h' in part:
            minutes += int(part.replace('h', '')) * 60
        elif 'm' in part:
            minutes += int(part.replace('m', ''))
        elif 's' in part:
            minutes += int(part.replace('s', '')) // 60
    total_minutes += minutes

print(f'Общее количество минут:{total_minutes}')