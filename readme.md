# NmeaConverter

NmeaConverter is a simple Python tool designed to convert NMEA messages from GNXXX format to GPXXX format. It's particularly useful for supporting outdated tools or systems that rely on GPXXX format.

## Installation

You can clone this repo:

```bash
git clone https://github.com/hdgnss/NmeaConverter.git
```

## Dependencies

NmeaConverter depends on pynmea2, a Python library for parsing NMEA sentences.

```bash
pip install pynmea2
```

## Usage

To use NmeaConverter:

```bash
python ./nmeaconverter.py /Users/xxx/test.nmea 
```
You will find a new file `/Users/xxx/test_new.nmea`


## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.

## License

NmeaConverter is licensed under the MIT License. See LICENSE for more information.
Feel free to customize it further to include more details about usage, examples, or additional features.
