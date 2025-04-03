import numpy as np

def get_noise_size(sample_rate=44100, num_channels=1, seconds=5):
    return sample_rate * num_channels * seconds

def modify_white_noise(sample_rate=44100, num_channels=1, seconds=5, amp_modifier=[]):
    white_noise = generate_white_noise(sample_rate=sample_rate, num_channels=num_channels, seconds=seconds)
    white_noise_rfft = np.fft.rfft(white_noise)

    return np.fft.irfft(white_noise_rfft * amp_modifier).astype(np.short)

def generate_white_noise(sample_rate=44100, num_channels=1, seconds=5):
    int16_info = np.iinfo(np.int16)
    min_value = int16_info.min
    max_value = int16_info.max

    rng = np.random.default_rng()
    size = get_noise_size(
        sample_rate=sample_rate,
        num_channels=num_channels,
        seconds=seconds
    )

    return rng.integers(
        low=min_value,
        high=max_value,
        size=size,
        dtype=np.short
    )

def generate_pink_noise(sample_rate=44100, num_channels=1, seconds=5):
    size = get_noise_size(sample_rate=sample_rate, num_channels=num_channels, seconds=seconds)

    freq = np.fft.rfftfreq(size, d=(1./sample_rate))
    amp_modifier = 1./np.where(freq == 0, float('inf'), np.sqrt(freq))
    return modify_white_noise(
        sample_rate=sample_rate,
        num_channels=num_channels,
        seconds=seconds,
        amp_modifier=amp_modifier
    )

def generate_red_noise(sample_rate=44100, num_channels=1, seconds=5):
    size = get_noise_size(sample_rate=sample_rate, num_channels=num_channels, seconds=seconds)

    freq = np.fft.rfftfreq(size, d=(1./sample_rate))
    amp_modifier = 1./np.where(freq == 0, float('inf'), freq)
    return modify_white_noise(
        sample_rate=sample_rate,
        num_channels=num_channels,
        seconds=seconds,
        amp_modifier=amp_modifier
    )