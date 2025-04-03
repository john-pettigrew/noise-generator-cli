import os
import argparse

def validate_output_path(arg):
    if os.path.exists(arg):
        raise argparse.ArgumentTypeError(f'output path "{arg}" already exists.')

    if not os.path.isdir(os.path.dirname(arg)):
        raise argparse.ArgumentTypeError(f'output path "{arg}" is not a valid output destination.')

    if not os.access(os.path.dirname(arg), os.W_OK):
        raise argparse.ArgumentTypeError(f'output path "{arg}" missing write access.')

    return arg

def validate_sample_rate(arg):
    sample_rate = int(arg)
    if sample_rate < 1:
        raise argparse.ArgumentTypeError("sample_rate must be a positive integer")
    return sample_rate

def validate_num_channels(arg):
    num_channels = int(arg)
    if num_channels < 1:
        raise argparse.ArgumentTypeError("channels must be a positive integer")
    return num_channels

def validate_num_seconds(arg):
    seconds = int(arg)
    if seconds < 1:
        raise argparse.ArgumentTypeError("seconds must be a positive integer")
    return seconds
