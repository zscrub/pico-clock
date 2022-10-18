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
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
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
    
    # output = f"{weekdays[day]}, {months[month]} {time_values['mday']} {year} {time_values['hour']}:{time_values['minute']}:{time_values['second']} {time_of_day}"
    top_output = f"{weekdays[day]}, {months[month]} {time_values['mday']}"
    bot_output = f"{year} {time_values['hour']}:{time_values['minute']}:{time_values['second']} {time_of_day}"
    lcd.clear()
    # lcd.putstr(output)
    lcd.putstr(top_output)
    lcd.move_to(0, lcd.cursor_y+1)
    lcd.putstr(bot_output)
    # time.sleep_ms(650)

