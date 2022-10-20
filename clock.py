import time
import micropython

from lcd_init import lcd

months = {
        1: "Jan",
        2: "Feb",
        3: "Mar",
        4: "Apr",
        5: "May",
        6: "June",
        7: "July",
        8: "Aug",
        9: "Sep",
        10: "Oct",
        11: "Nov",
        12: "Dec"
}

weekdays = {
        0: "Mon",
        1: "Tue",
        2: "Wed",
        3: "Thu",
        4: "Fri",
        5: "Sat",
        6: "Sun"
}

def convert_hour(hour: int) -> tuple:
    """Takes integer as parameter to convert to 12 hour clock with time of day."""
    if hour > 12:
        return hour-12, "PM"
    if hour == 0:
        hour = 12
    return hour, "AM"

def convert_time(time_values: dict) -> None:
    # need an algorithm to check if any elems are less than 10 and return their index
    # month, mday, hour, minute, second, day
    for k,v in time_values.items():
        if isinstance(v, int) and v < 10:
            time_values[k] = f"0{v}"

now_time = ()

time_values = {}

while True:
    now = time.localtime()
    if now == now_time:
        continue

    now_time = now
    year, month, time_values["mday"], time_values["hour"], time_values["minute"], time_values["second"], day, yearday = now
    time_values["hour"], time_of_day = convert_hour(time_values["hour"])
    convert_time(time_values)
    
    top_output = f"{weekdays[day]}, {months[month]}-{time_values['mday']}-{year}"
    bot_output = f"{time_values['hour']}:{time_values['minute']}:{time_values['second']} {time_of_day}"
    print(top_output)
    print(bot_output)
    lcd.clear()
    lcd.putstr(top_output)
    lcd.move_to(2, 1)
    lcd.putstr(bot_output)

