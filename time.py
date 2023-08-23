def convert_to_24_hour(hour, minute, period):
    hour_in_24_hour_format = hour
    if period == "pm":
        hour_in_24_hour_format += 12
    hour_in_24_hour_format = f"{hour_in_24_hour_format:02d}"
    minute = f"{minute:02d}"
    return hour_in_24_hour_format + minute

print(convert_to_24_hour(8, 30, "am"))
