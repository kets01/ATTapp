from pydub import AudioSegment

def convert_wav(chemin):
    audio = AudioSegment.from_file(chemin)
    chemin_wav = "temp.wav"
    audio.export(chemin_wav, format="wav")
    return chemin_wav