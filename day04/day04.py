import sys
from datetime import datetime, timedelta
from collections import defaultdict

def parse_event(line):
    timestr, action = line.strip().split("] ")
    time = datetime.strptime(timestr, "[%Y-%m-%d %H:%M")
    return (time, action)

def count_minutes(shifts):
    minutes = 0
    for shift in shifts:
        awake = True
        sleep = None
        for e in shift:
            if awake:
                sleep = e
                awake = False
            else:
                elapsed = e - sleep
                minutes += int(elapsed.total_seconds() / 60)
                awake = True

    return minutes

def get_sleep_times(events):
    guards = defaultdict(list)
    guard = ""
    shift = []
    for time, action in events:
        a = action.split()
        if len(a) == 4:
            guards[guard].append(shift)
            shift = []
            guard = a[1][1:]
        else:
            shift.append(time)

    guards[guard].append(shift)

    return guards

def sleep_metrics(shifts):
    minutes = [0 for _ in range(60)]
    for shift in shifts:
        awake = True
        sleep = None
        for e in shift:
            if awake:
                sleep = e
                awake = False
            else:
                for i in range(sleep.minute, e.minute):
                    minutes[i] += 1

                awake = True

    minute_amount = max(minutes)
    minute = minutes.index(minute_amount)
    total = count_minutes(shifts)
    return (total, minute, minute_amount)

def main():
    # Part 1
    events = sorted(list(map(parse_event, sys.stdin.readlines())))
    sleep_times = get_sleep_times(events)
    minutes = [(guard, sleep_metrics(shifts)) for guard, shifts in sleep_times.items()]
    guard1, (_, minute1, _) = max(minutes, key=lambda x: x[1][0])
    print(int(guard1) * minute1)

    # Part 2
    guard2, (_, minute2, _) = max(minutes, key=lambda x: x[1][2])
    print(int(guard2) * minute2)

if __name__ == "__main__":
    main()
