
######### the custom play #####
from scamp import *

s = Session()
s.tempo = int(input("Set tempo (200 default) : "))
piano = s.new_part("piano")	

def arpej2(nota, length, instruman):
    s = Session()
    s.tempo = 2000
    piano = s.new_part(instruman)
    addon = [4, 3, 5]
    while( nota <= 108):
        piano.play_note(nota, 100, length)
        nota = nota + addon[0]
        piano.play_note(nota, 100, length)
        nota = nota + addon[1]
        piano.play_note(nota, 100, length)
        nota = nota + addon[2]

def chords(nota):
# s = Session()
# s.tempo = 120
	note = 0
	nota = nota.upper()
	chord_sequence = [4,3]
	arr = list(nota)
	if len(arr) == 1:
		arr.append("none")
		arr.append("none")
	if len(arr) == 2:
		arr.append("none")
	if len(arr) == 0:
		return
	print(arr)
	nota = arr[0]
	if nota == "C" :
		note = 60
	elif nota == "D":
		note = 62
	elif nota == "E":
		note = 64
	elif nota == "F":
		note = 65
	elif nota == "G":
		note = 67
	elif nota == "A":
		note = 69
	elif nota == "B":
		note = 71
	else:
		note = 0
	print(arr[1] == "M")
	if arr[1].upper() == "B":
		note = note - 1
	elif arr[1].upper() == "#":
		note = note + 1
	elif arr[1].upper() == "M":
		print("true")
		chord_sequence = [3,4]
	if arr[2].upper() == "M":
		print("true")
		chord_sequence = [3,4]
	print(chord_sequence)
# 	piano = s.new_part("piano")
	piano.play_note(note, 0.8, 1, blocking=False)
	piano.play_note(note + chord_sequence[0] , 0.8, 1, blocking=False)
	piano.play_note(note + chord_sequence[0] + chord_sequence[1], 0.8, 1, blocking=False)
	

	
def play(nota,length):
# 	s = Session()
# 	s.tempo = 120
	note = 0
	nota = nota.upper()
	arr = list(nota)
	if len(arr) == 1:
		arr.append("none")
		arr.append("none")
	else:
		arr.append("none")
	print(arr)
	nota = arr[0]
	if nota == "C" :
		note = 60
	elif nota == "D":
		note = 62
	elif nota == "E":
		note = 64
	elif nota == "F":
		note = 65
	elif nota == "G":
		note = 67
	elif nota == "A":
		note = 69
	elif nota == "B":
		note = 71
	else:
		note = 1000
		
	for i in arr:
		print(i)
		if i == "b":
			note = note - 1
		elif i.upper() == "#":
			note = note + 1
		elif i.upper() == "\\":
			note = note - 12
		elif i.upper() == "/":
			note = note + 12
		
		
# 	if arr[1].upper() == "B":
# 		note = note - 1
# 	elif arr[1].upper() == "#":
# 		note = note + 1
# 	elif arr[1].upper() == "D":
# 		note = note - 12
# 	elif arr[1].upper() == "U":
# 		note = note + 12
# 		
# 	if arr[2].upper() == "D":
# 		note = note - 12
# 	elif arr[2].upper() == "U":
# 		note = note + 12
		

# 	piano = s.new_part("piano")
	piano.play_note(note, 0.8, length, blocking=True)





########The pack itself
text_music = ""
text_music2 = ""
with open ("/Users/dehaay/Desktop/music project/turkish march.txt") as f:
    lines = f.readline()
    while(lines):
        text_music = f'{text_music}{lines}'
        lines = f.readline()


print(text_music)
notes_each = text_music.split("\n")

notes_each = ' '.join(notes_each)

notes_each = notes_each.split(" ")

notes_cleaned = []

for x in notes_each:
    print(x)
    if (x != ""):
        notes_cleaned.append(x)
        
print(notes_cleaned)


tempo = 1
for i in notes_cleaned:
    if (i[0] == "("):
        tempo = eval(i.strip("()"))
        print(tempo)
    else:
        print(i)
        play(i,tempo)
        
        

