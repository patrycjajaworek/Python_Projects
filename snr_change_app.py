import numpy
import librosa
import soundfile
from pydub import AudioSegment


def add_noise_snr(audio, noise, snr):
    clean_db = 10 * numpy.log10(numpy.mean(audio ** 2) + 1e-4)
    audio_length = audio.shape[0]

    if noise.shape[0] < audio_length:
        shortage = audio_length - noise.shape[0]
        noise = numpy.pad(noise, (0, shortage), 'wrap')
    elif noise.shape[0] > audio_length:
        noise = noise[:audio_length]  # Truncate the noise to match the length of audio because of error

    noise_db = 10 * numpy.log10(numpy.mean(noise ** 2) + 1e-4)
    add_noise = numpy.sqrt(10 ** ((clean_db - noise_db - snr) / 10)) * noise
    mix_audio = audio + add_noise
    return mix_audio


def read_audio(file_audio):
    audio, sr = librosa.load(file_audio, sr=8000, mono=True)
    return audio


def save_wav(audio, fx, sr=8000):
    soundfile.write(fx, audio, sr, "PCM_16")

#converter because files from sound_app are in mp3 format
def convert_mp3_to_wav(mp3_filename):
    sound = AudioSegment.from_mp3(mp3_filename)
    wav_filename = mp3_filename.replace(".mp3", ".wav")
    sound.export(wav_filename, format="wav")
    return wav_filename



wav_file = r"obiadek.wav"
audio = read_audio(wav_file)
noise_file = "audiocheck.net_whitenoisegaussian.wav"
noise = read_audio(noise_file)
audio_noise = add_noise_snr(audio, noise, snr = 0)
save_wav(audio_noise, "audio_noise_0.wav")
audio_noise = add_noise_snr(audio, noise, snr = 5)
save_wav(audio_noise, "audio_noise_5.wav")
audio_noise = add_noise_snr(audio, noise, snr = 10)
save_wav(audio_noise, "audio_noise_10.wav")
audio_noise = add_noise_snr(audio, noise, snr = 15)
save_wav(audio_noise, "audio_noise_15.wav")
audio_noise = add_noise_snr(audio, noise, snr = 20)
save_wav(audio_noise, "audio_noise_20.wav")
audio_noise = add_noise_snr(audio, noise, snr = 25)
save_wav(audio_noise, "audio_noise_25.wav")
audio_noise = add_noise_snr(audio, noise, snr = 30)
save_wav(audio_noise, "audio_noise_30.wav")


audio_noise = add_noise_snr(audio, noise, snr = -5)
save_wav(audio_noise, "audio_noise_-5.wav")
audio_noise = add_noise_snr(audio, noise, snr = -8)
save_wav(audio_noise, "audio_noise_-8.wav")

audio_noise = add_noise_snr(audio, noise, snr = -10)
save_wav(audio_noise, "audio_noise_-10.wav")
audio_noise = add_noise_snr(audio, noise, snr = -20)
save_wav(audio_noise, "audio_noise_-20.wav")
audio_noise = add_noise_snr(audio, noise, snr = -30)
save_wav(audio_noise, "audio_noise_-30.wav")


#add function to add snr to list of files not only one
# integrate this code with sound_app