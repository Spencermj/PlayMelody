import echonest.remix.audio as audio
import echonest.remix.modify as modify
import os

AUDIO_EXTENSIONS = set(['mp3', 'm4a', 'wav', 'ogg', 'au', 'mp4'])

def main(directory, inputfile_name, output_filename):
    semitones = []
    noteList = []
    collect = []
    createSemitones(directory, semitones)
    for note in semitones:
        noteList.append(note)
    for i in range(1,4):
        addOctave(semitones, i, noteList)
    for i in range(1,3):
        addOctave(semitones, i*-1, noteList)
    audiofile = audio.LocalAudioFile(input_filename)
    songPitches = audiofile.segments.pitches
    bmd = 10000.0
    bmi = 0
    for i in range(len(songPitches)):
        for j in range(len(noteList)):
            notePitches = noteList[j].pitches
            dist = distFinder.cosine(songPitches[i], notePitches[0]) 
            if dist < bmd:
                bmd = dist
                bmi = j
        collect.append(noteList[bmi])
    out = audio.assemble(collect)
    out.encode(output_filename)

def addOctave(semitones, octaves, noteList):
    for note in semitones:
        changeOneNoteOctave(note, noteList, octaves)

def changeOneNoteOctave(note, noteList, octaves):
    soundtouch = modify.Modify()
    new_note = soundtouch.shiftPitchOctaves(note, octaves)
    noteList.append(new_note)

def createSemitones(directory, notes):
    for f in os.listdir(directory):
        if _isAudio(f):
            path = os.path.join(directory, f)
            _addOneNote(path, notes)

def _addOneNote(path, notes):
    audiofile = audio.LocalAudioFile(path)
    notes.append(audiofile)

def _isAudio(f):
    _, ext = os.path.splitext(f)
    ext = ext[1:]
    return ext in AUDIO_EXTENSIONS

if __name__ == '__main__':
    import sys
    try:
        directory = sys.argv[1]
        input_filename = sys.argv[2]
        output_filename = sys.argv[3]
    except:
        print usage
    main(directory, input_filename, output_filename)


