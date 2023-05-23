# GermanTime [<img style="float: right;" src="https://i.postimg.cc/k4LQt1CH/German-Time.png" width="160">](https://postimg.cc/bDHD7Rs0)

GermanTime is a Python-based graphical user interface (GUI) program that enables users to input time in a 12-hour format and convert it to German words.

## Using the program

### Downloading and Running

To use the program, all you need to do is download the `GermanTime` file directory from the latest release at [Releases](https://github.com/Ali246801232/GermanTime/releases). All required files and dependencies are included inside of this, so no additional installation is necessary. After downloading, simply execute the `GermanTime.exe` file inside of the mentioned directory.

### How to Use

Upon running the program, you will be greeted with a window with 3 input boxes and 1 drop-down box. To convert a given time into German words:
1. enter the hour (01-12), the minute (00-59), and the period (AM/PM).
2. select the format (Numeric/Analog). 
3. press the "Convert" button.
The program will then show you a popup with the converted time and will copy this text to your clipboard.

## How German Time Works

German uses 24-hour time which starts from "Null" and ends at "Dreiundzwanzig".

There's two main ways to tell the time in German. The first format, what the program calls "**Numeric**", you simply write the hour, then write *"Uhr"*, and then write the minutes. So 04:25 PM, for example, would be *"sechzehn Uhr fünfundzwanzig"*. If it's exactly that hour, like 02:00 PM, then you don't write the minutes, and it's just *"vierzehn Uhr"*. In this case, *"Uhr"* is basically the German equivalent of o'clock in English.

The second format, what the program calls "**Relative**", is a bit tricker. Instead of just writing the hour and minute, you have to use *"nach"* (after) or *"vor"* (before) in reference to the hour. Let's take an example of when *"nach"* is used, 07:13 AM. It's thirteen minutes after seven, which would make it *"dreizehn nach sieben"*. However, if it's closer to the next hour, then you have to reference the next hour with *"vor"*. So, as an example, 08:57 PM would be *"drei vor zwanzig"*.

There are two exceptions in the second format:
1. First, when it's exactly 15 minutes before or after an hour. In that case, instead of *"fünfzehn"*, we use *"viertel"*, like in *"viertel nach zwanzig"* (08:15 PM) or *"viertel vor drei"*. In this case, *"viertel"* is the German equivalent to quarter in English.
2. Second, when it's between 5 minutes before or after half-past an hour. In that case, the word *"halb"* is used. If it's exactly half-past an hour, then we write *"halb"* and then the next hour. For example, 04:30 PM would be *"halb siebzehn"*. If it's 5 or less minutes before half-past, then we write the minutes, then *"vor halb"*, and then the next hour. For example, 04:25 PM would be *"fünf vor halb siebzehn"*, as it's 5 minutes before 04:30 PM. If it's 5 or less minutes after half-past, then we write the minutes, then *"nach halb"*, and then then next hour. For example, 04:35 PM would be *"fünf nach halb siebzehn"*, as it's 5 minutes after 04:30 PM.

## License

This project is licensed under the terms of The Unlicense. A copy of the license can be found in the [LICENSE](LICENSE) file.

## Changelog

### Version 1.0.0 (2023-05-DD)

- Initial release of the program
