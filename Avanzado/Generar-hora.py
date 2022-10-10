def number2string(number, string):
    return str(number) + ' ' + string + "s"*(number > 1)

def format_duration(seconds):
    if seconds == 0:
        return "now"
    all_seconds = [31536000,86400,3600,60]
    time_string = ["year", "day", "hour", "minute", "second"]
    time = {}
    format = ""
    for s in range(len(all_seconds)):
        unit = seconds // all_seconds[s]
        if unit > 0:
            time[time_string[s]] = unit
            seconds -= time[time_string[s]] * all_seconds[s]
    if seconds > 0:
        time[time_string[-1]] = seconds
    
    i = len(time.keys())
    
    for j in time_string:
        if j in time.keys():
            if i >= 3:
                format += number2string(time[j], j) + ", "
            elif i == 2:
                format += number2string(time[j], j) + " and "
            else:
                format += number2string(time[j], j)
            i -= 1
    
    return format