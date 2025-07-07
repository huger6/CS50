months_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    try:
        month, day, year = date.split("/")
        if ( 0 < int(month) < 13 and 0 < int(day) < 32):
            break
    except:
        try:
            old_month, old_day, year = date.split(" ")
            if old_month.title() in months_list:
                month = months_list.index(old_month) + 1
            day = old_day.replace(",", "")
            if not old_day.endswith(","):
                continue
            if ( 0 < int(month) < 13 and 0 < int(day) < 32):
                break
            else:
                continue
        except:
            print()
            pass

print(f"{year.rstrip()}-{int(month):02}-{int(day):02}")
