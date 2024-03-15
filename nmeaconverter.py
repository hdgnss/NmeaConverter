import argparse
import os
import sys

import pynmea2 as nmeaparse

def converter(input_file, output_file):
    file_in = open(input_file, encoding='utf-8')
    file_out = open(output_file, "w")
    line_break = os.linesep

    for line in file_in.readlines():
        try:
            msg = nmeaparse.parse(line)
            if type(msg)==nmeaparse.types.talker.GGA:
                msg.talker = 'GP'
                file_out.write(str(msg)+line_break)
            elif type(msg)==nmeaparse.types.talker.RMC:
                msg.talker = 'GP'
                file_out.write(str(msg)+line_break)
            elif type(msg)==nmeaparse.types.talker.GLL:
                msg.talker = 'GP'
                file_out.write(str(msg)+line_break)
            elif type(msg)==nmeaparse.types.talker.GSV:
                file_out.write(line.strip()+line_break)
        except nmeaparse.ParseError as e:
            continue
    file_out.close()


def main():
    print('Version: 0.0.1')
    arg_parser = argparse.ArgumentParser(description='NMEA Converter Tool', epilog='Example>> nmeaconverter gps.nmea')
    arg_parser.add_argument('input',     type=str, help= "input file: nmea file")
    args = arg_parser.parse_args()

    input_file=args.input

    directory, filename = os.path.split(args.input)
    name, ext = os.path.splitext(filename)
    new_filename = f"{name}_new{ext}"

    output_file = os.path.join(directory, new_filename)

    if not os.path.isfile(output_file):
        converter(input_file, output_file)
    else:
    	print("Error: File exists " + output_file)

if __name__ == '__main__':
    main()