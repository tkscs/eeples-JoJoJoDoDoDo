song = "I like to eat, eat, eat, apples and bananas"
new_song = ""
for character in song:
    if character == "a":
        new_song = new_song + character*3
    else:
        new_song = new_song + character

print(new_song)






def sing(vowel):
    print(song.replace("a", f"{vowel}"))
    

sing("ay")
sing("ee")
sing("i")
sing("o")
sing("u")







    