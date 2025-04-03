import argparse
import wave

from utils.generators import generate_white_noise, generate_pink_noise, generate_red_noise
from utils.validators import validate_output_path, validate_sample_rate, validate_num_channels, validate_num_seconds

WHITE_NOISE = 'white'
PINK_NOISE = 'pink'
RED_NOISE = 'red'

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        help="output file destination",
        required=True,
        type=validate_output_path,
    )
    parser.add_argument(
        "--sample_rate",
        help="sample rate",
        default=44100,
        type=validate_sample_rate,
    )
    parser.add_argument(
        "--channels",
        help="number of channels",
        default=1,
        type=validate_num_channels,
    )
    parser.add_argument(
        "--seconds",
        help="number of seconds",
        default=1,
        type=validate_num_seconds,
    )

    subparser = parser.add_subparsers(dest="generate", required=True)
    white_noise_parser = subparser.add_parser(WHITE_NOISE, help="Generate white noise")
    pink_noise_parser = subparser.add_parser(PINK_NOISE, help="Generate pink noise")
    red_noise_parser = subparser.add_parser(RED_NOISE, help="Generate red noise")

    args = parser.parse_args()

    noise = []
    if args.generate == WHITE_NOISE:
        noise = generate_white_noise(
            sample_rate=args.sample_rate,
            num_channels=args.channels,
            seconds=args.seconds,
        )

    elif args.generate == PINK_NOISE:
        noise = generate_pink_noise(
            sample_rate=args.sample_rate,
            num_channels=args.channels,
            seconds=args.seconds,
        )

    elif args.generate == RED_NOISE:
        noise = generate_red_noise(
            sample_rate=args.sample_rate,
            num_channels=args.channels,
            seconds=args.seconds,
        )

    else:
        raise Exception('Unknown command')

    with wave.open(args.output, "wb") as wav_file:
        wav_file.setnchannels(args.channels)
        wav_file.setsampwidth(2)
        wav_file.setframerate(args.sample_rate)

        wav_file.writeframes(noise)

if __name__ == '__main__':
    main()