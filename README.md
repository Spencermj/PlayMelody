# PlayMelody


**What It Does**

PlayMelody.py uses a directory containing an octave of semitones from one instrument and uses the sound clips to recreate the melody of a simple song. I was able to find .wav files of the 12 semitones from a single octave at [Free Sound], I added these to a directory and pass the directory into the paramaters upon execution of PlayMelody.py. From these semitones, my program creates a list of every note on a piano; to do this it first fills the list with each of the semitones, it then shifts the octave multiples times both up and down to capture the entire range of the piano. After this note list has been created, the program takes the song entered as a paramater and finds the euclidean distance between each pitch in the song and each sample pitch, appending the closest sample pitch to a new list and then encoding it as an audio file.

**How Did I Come Up With This Idea?**

As I was thinking of ideas for other research modules and my final project, I realized that the majority of the projects that I wanted to work on involved playing a note from a specific instrument. Most of my ideas involve something along the lines of creating a chord progression or using cellular automata to create a simple melody, and these all involve creating notes. I looked into [Echonest]'s API and couldn't find a way to properly create an AudioQuantum object that sounded natural, after that I looked into [Python Audio]'s API and learned about the methods to directly manipulate the sound card. After struggling with the previous two attempts, I realized that all I needed were 12 semitones from any octave. With these 12 pitches, I could make use of [Echonest] to pitch shift each note by an octave and create notes from any octave. I prefer this solution over the others too because it allows me to use other instruments if I choose, if I were to find .wav files for any other instruments, I could use them in the same way to generate notes as long as I have 12 semitones from any octave.

**What Problem Does It Solve?**

The completion of this program opens up a variety of possibilities for what I can do next. Now that I have a way to generate any note given a directory, I can accomplish multiple programs that I had in mind. One of the most obvious things I can do is expand on this specific project even more and mimic the melody from a much more complex song. [Extracting Melody] goes in depth on how to use fourier transformations to extract not only the melody, but also the rythm and the bass of a song. At the moment, my code can only mimic simple melodies, but I could use this resource to expand on my program and fix its shortcomings.

Another idea that could be accomplished now that I can generate notes is a simple chord progression. [Chord Probabilities] goes in depth on how to find the probability that any one chord will follow any other chord. By using this information, I can shift 4 notes and play them simulatenously to create a chord, use the probabilities to find a chord that would most likely sound good following the previous chord, and then repeat with some sort of randomized rythm.

Finally, I could make use of these notes to create a basic song based off of cellular automata. In a fashion similar to [Wolfram Tones] or [Molecular Music Box], I could experiment with simple patterns to create naturally complex songs. Cellular automata is an incredibly interesting way to create music because it makes use of analyzing simple patterns in life and using those to create an end product that is much more complex than the pattern that created it. Now that I can generate notes, I can simulate any instrument and use Stephen Wolfram's research to create generative music.

**Dependencies**

You will need Pyechonest to use playlist.py.

**Resources**

1. [Tempo Shift Example]

2. [Modify]

3. [AQ Player]

4. [Free Sound]

5. [Recurse Through Directory]

6. [Python Audio]

7. [Echonest]

8. [Extracting Melody]

9. [Chord Probabilities]

10. [Molecular Music Box]

11. [Wolfram Tones]

**How To Mimic A Melody**

To run PlayMelody.py, the user must enter the location of the song they wish to be analyzed (the simpler the melody the better), the name of the output file, and the directory containing the 12 semitones from the chosen instrument. The following command will create a .mp3 file containing the melody of Happy Birthday:

```python
python PlayMelody.py NoteList HappyBirthday.mp3 HappyMelody.mp3
```

**Code Explanation**



[Tempo Shift Example]: https://github.com/echonest/remix/blob/master/examples/stretch/beatshift.py
[Modify]: http://echonest.github.io/remix/apidocs/echonest.remix.modify.Modify-class.html
[AQ Player]: https://github.com/jlstack/PythonEchonestRemix/tree/master/aqplayer
[Free Sound]: http://www.freesound.org/people/pinkyfinger/packs/4409/
[Recurse Through Directory]: https://github.com/echonest/pyechonest/blob/master/examples/show_attrs.py
[Python Audio]: https://wiki.python.org/moin/Audio/
[Echonest]: http://the.echonest.com/
[Extracting Melody]: http://perso.telecom-paristech.fr/~grichard/Publications/2013-Salomon-SigMag.pdf
[Chord Probabilities]: http://bengio.abracadoudou.com/cv/publications/pdf/paiement_2005_ismir.pdf
[Molecular Music Box]: https://www.youtube.com/watch?v=3Z8CuAC_-bg
[Wolfram Tones]: http://tones.wolfram.com/about/
