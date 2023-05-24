from pyperclip import copy  # to copy result to clipboard

# Function to convert numbers to German words
def NumToWord(number):
    # Define word mappings
    units = ["null", "ein", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn",
             "elf", "zwölf", "dreizehn", "vierzehn", "fünfzehn", "sechzehn", "siebzehn"]
    tens = [None, "zehn", "zwanzig", "dreißig", "vierzig", "fünfzig"]

    # Check if the number is 17 or less
    if number <= 17 :
        return units[number]
    
    # Construct and return string from the digits
    tens_digit = int(str(number)[0])
    units_digit = int(str(number)[1])
    if units_digit == 0:
        return tens[tens_digit]
    else:
        return units[units_digit] + "und" + tens[tens_digit]

# Function to check input values
def CheckTime(hour, minute, period):
    # Check if inputs are correct data types
    try:
        hour = int(hour)
        minute = int(minute)
        period = str(period).upper()
    except ValueError:
        return [-1, "Invalid time entered"]

    # Check if hour is within range, and adjust for period
    if 1 <= hour <= 12:
        if period == "AM":
            if hour == 12:
                hour = 0
        elif period == "PM":
            if hour != 12:
                hour += 12
        else:
            return [-1, "Invalid period entered"]
    else:
       return [-1, "Invalid hour entered"]
    
    # Check if minute is within range
    if minute < 0 or minute > 59:
        return [-1, "Invalid minute entered."]
    
    # Check for 'vor', as it will be the next hour
    if minute >= 25:
        # Check for 11 PM, as hour goes to 00, not 24
        if hour == 23:
            hour = 0
        else:
            hour += 1
    
    return [0, hour, minute, period]

# Function to convert input time to German
def ConvertTime(hour, minute, period, format):
    # Check input values
    Check = CheckTime(hour, minute, period)
    if Check[0] == -1:
        return Check
    hour, minute, period = Check[1], Check[2], Check[3]
    
    # If only hour, return as is with "Uhr"
    if minute == 0:
        return [0, f"{NumToWord(hour)} Uhr"]

    # Check and use numeric to construct and return result string
    if format == "Numerical":
        return [0, f"{NumToWord(hour)} Uhr {NumToWord(minute)}"]

    # Otherwise, use relative format to construct and return result string
    if minute >= 1 and minute <= 24 and minute != 15:
        return [0, f"{NumToWord(minute)} nach {NumToWord(hour)}"]
    elif minute == 15:
        return [0, f"viertel nach {NumToWord(hour)}"]
    elif minute >= 25 and minute <= 29:
        return [0, f"{NumToWord(30 - minute)} vor halb {NumToWord(hour)}"]
    elif minute == 30:
        return [0, f"Halb {NumToWord(hour)}"]
    elif minute >= 31 and minute <= 35:
        return [0, f"{NumToWord(minute - 30)} nach halb {NumToWord(hour)}"]
    elif minute >= 36 and minute <= 59 and minute != 45:
        return [0, f"{NumToWord(60 - minute)} vor {NumToWord(hour)}"]
    elif minute == 45:
        return [0, f"viertel vor {NumToWord(hour)}"]