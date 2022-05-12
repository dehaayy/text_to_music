# text_to_music
Converts .txt file of notes to music

Replace the path with your "music txt file", run, set the tempo and listen to your masterpiece! 

This application uses the "letter notation" for identifying pitches. By default ranges from C4 to B4

-- I D E N T I F Y I N G    E A C H   N O T E ---
As each individual note the following syntax should be used

1st Argument must be one of the specified letters:
🎹(C, D, E, F, G, A, B)

Additional argument that can be added (order does not matter)
🎹 "#" Corresponds to the "sharp" notation in music, increases the note value by half a tone
🎹 "b" Corresponds to the "flat" notation in music, decreases the note by a semitone.
🎹 "/" Default uses all notes in the "4" range, "/" notation uses the 1st argument note in an octave higher (can be stacked)
🎹 "\" uses the 1st argument note in an octave lower (can be stacked)

