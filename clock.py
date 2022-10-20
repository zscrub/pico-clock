import time
import micropython

from lcd_init import lcd

from schema import (
    units,
    months,
    weekdays,
    Units
)


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
        if isinstance(v, int):
            if v < 10:
                time_values[k] = f"0{v}"
            else:
                time_values[k] = str(v)

now_time = ()
time_values = {}

while True:
    now = time.localtime()
    if now == now_time:
        continue
    
    now_time = now
    year, time_values["month"], time_values["mday"], time_values["hour"], time_values["minute"], time_values["second"], day, yearday = now
    time_values["hour"], time_of_day = convert_hour(time_values["hour"])
    convert_time(time_values)

    Units.year =   year
    Units.month =  time_values["month"]
    Units.mday =   time_values["mday"] 
    Units.day =    weekdays[day]
    Units.hour =   time_values["hour"]
    Units.minute = time_values["min"]
    Units.second = time_values["sec"]
    Units.tod =    time_of_day

    # output = f"{weekdays[day]}, {*months[month]} {time_values['mday']} {year} {time_values['hour']}:{time_values['minute']}:{time_values['second']} {time_of_day}"
    top_output = f"{weekdays[day]} {time_values['month']}-{time_values['mday']}-{year}"
    bot_output = f"{time_values['hour']}:{time_values['minute']}:{time_values['second']}{time_of_day}"
    lcd.clear()

    lcd.replace_str(1, 0, top_output)
    lcd.replace_str(3, 1, bot_output)
