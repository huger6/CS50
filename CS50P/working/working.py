import re


def main():
    hours, minutes, am_pm, hours2, minutes2, am_pm2 = convert(input("Hours: "))
    time1 = convert_format(hours, minutes, am_pm)
    time2 = convert_format(hours2, minutes2, am_pm2)
    print(f"{time1} to {time2}")


def convert(time):
    US_pattern = r"(0?[1-9]|1[0-2])(:0[0-9]|[0-5][0-9])?\s(AM|PM)"
    completed_US_pattern = rf"^{US_pattern}\sto\s{US_pattern}$"
    if matches := re.search(completed_US_pattern, time.strip()):
        hours, minutes, am_pm = matches.group(1), matches.group(2), matches.group(3)
        hours2, minutes2, am_pm2 = matches.group(4), matches.group(5), matches.group(6)
        if (int(hours) or int(hours2)) == 12 and (am_pm or am_pm2) == "PM":
            raise ValueError
        return hours, minutes, am_pm, hours2, minutes2, am_pm2
    else:
        raise ValueError

def convert_format(hours, minutes, am_pm):
    if minutes is None:
        minutes = ":00"
    if am_pm == "AM":
        if int(hours) < 10:
            new_time = f"0{int(hours)}{minutes}"
        elif 10 < int(hours) < 12:
            new_time = f"{int(hours)}{minutes}"
        elif int(hours) == 12:
            new_time = f"00{minutes}"
    elif am_pm == "PM":
        hours = int(hours) + 12
        if hours == 24:
            new_time = f"12{minutes}"
        else:
            new_time = f"{int(hours)}{minutes}"
    return new_time


if __name__ == "__main__":
    main()


