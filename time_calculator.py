def add_time(start, duration, day=""):
    exchange_rate_information = ""
    start_clock = start.split()
    start_time = start_clock[0].split(":")
    end_time = duration.split(":")
    meridiems = ["AM", "PM"]
    all_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    minutes = int(start_time[1]) + int(end_time[1])
    hours = int(start_time[0]) + int(end_time[0]) + int(minutes / 60)
    minutes = str(minutes % 60)
    if len(minutes) == 1:
        minutes = "0"+minutes

    meridiem_change = int(hours / 12)
    hours = str(hours % 12)
    if hours == "0":
        hours = "12"

    if start_clock[1] == "PM":
        days_changed = int((meridiem_change + 1) / 2)
        meridiem = meridiems[(meridiem_change + 1) % 2]
    else:
        days_changed = int(meridiem_change / 2)
        meridiem = meridiems[meridiem_change % 2]
    meridiem = " " + meridiem
    if len(day) > 0:
        day = day.capitalize()
        code_day = all_days.index(day)
        code_day = (code_day + days_changed) % 7
        day = all_days[code_day]
        day = ", " + day

    if days_changed == 1:
        exchange_rate_information = " (next day)"
    elif days_changed > 1:
        exchange_rate_information = f" ({days_changed} days later)"

    new_time = hours + ":" + minutes + meridiem + day + exchange_rate_information

    return new_time
