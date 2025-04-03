# Noise Generator CLI 🎧
Noise Generator CLI enables the creation of different types of audio noise.

## Features
- Generate white, pink, or red noise
- Supports various audio output options (see below)

## Command Line Options
- `--output`: Output file path.
- `--sample_rate`: Sample rate for output file. (default 44100)
- `--channels`: Number of channels for output file. (default 1)
- `--seconds`: Duration of generated noise. (default 1)

## Notes
- It may be necessary to increase the output file's volume depending on the type of generated noise and the intended application. 

## Usage
To generate noise, simply run the script with preferred options:
```sh
python noise_generator.py --seconds 20 --output /path/to/output/file.wav red
```
Replace `/path/to/output/file.wav` with your preferred output file path.

## Examples
- Generate 1 second of white noise and output to `./example.wav`
```sh
python noise_generator.py --output ./example.wav white
```

- Generate 30 seconds of pink noise with 2 channels and output to `./example.wav`
```sh
python noise_generator.py --seconds 30 --channels 2 --output ./example.wav pink
```

- Generate 10 seconds of red noise with a 22050 sample rate and output to `./example.wav`
```sh
python noise_generator.py --seconds 10 --sample_rate 22050 --output ./example.wav red
```