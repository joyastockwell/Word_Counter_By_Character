# creating variable to store the
# number of words the non-narrator
# characters say in this scene
porfiro_words_total = 0
porfiro_words_this_scene = 0
carmen_words_total = 0
carmen_words_this_scene = 0
jonny_words_total = 0
jonny_words_this_scene = 0
martin_words_total = 0
martin_words_this_scene = 0
antigone_words_total = 0
antigone_words_this_scene = 0
viridian_words_total = 0
viridian_words_this_scene = 0
other_words_this_scene = 0
other_words_total = 0

# returns length of line if line contains
# a colon. curr_line is a string
def get_words_non_narrator_says(curr_line):
    line_narrator_words = 0
    index = curr_line.find(":")
    if index != -1:
        # print(curr_line)
        line_non_narrator_words = len(curr_line.split())
        #print(line_narrator_words)
    return line_non_narrator_words
    
 
# Opening our text file in read only
# mode using the open() function
with open(r'C:\Users\stockwja\Downloads\Porfiro.docx.txt', 'r', encoding="utf8") as file:

#with open(r'C:\Users\stockwja\Downloads\test.txt', 'r') as file:
 
    # Reading the content of the file
    # using the read() function and storing
    # them in a new variable
    data = file.read()
 
    # Splitting the data into separate lines
    # using the splitlines() function
    lines = data.splitlines()

    ep_number = 0
    scene_number = 0
    # Iterating over every line from the data
    for curr_line in lines:
        # If the line contains the word Episode, it's
        # an episode header, so print it.
        # Works for my writing because I did episode
        # headers that way and the script doesn't contain
        # the word Episode elsewhere. But I'm printing the whole
        # line instead of just incrementing a counter as a sanity
        # check in case I ever use this script on someone else's
        # writing
        # NOTE: ASSUMES NO WORDS BETWEEN EPISODE HEADERS AND SCENE HEADERS
        if "Episode" in curr_line:
            ep_number += 1
            scene_number = 0
            other_words_total += 2
        # Woah, can't believe I don't use the word Scene
        # anywhere but scene breaks in this show!
        # Had to add the word "Scene" to the end of the script to make this work lol
        # Will have to make more robust if I reuse this code...
        elif "Scene" in curr_line:
            scene_number += 1
            other_words_total += 2
            this_scene_people = porfiro_words_this_scene + carmen_words_this_scene + jonny_words_this_scene + martin_words_this_scene + antigone_words_this_scene + viridian_words_this_scene    
            # We're starting a new scene, so add all the word counts
            # from the last scene to the totals, then reset this_scene
            # word counts to zero
            # No need to do anything to a character's numbers
            # if that character had no lines during the last scene
            if porfiro_words_this_scene != 0:
                porfiro_words_total += porfiro_words_this_scene
                print("\tWords in this scene spoken by Porfiro:", porfiro_words_this_scene)
                porfiro_words_this_scene = 0
            if carmen_words_this_scene != 0:
                carmen_words_total += carmen_words_this_scene
                print("\tWords in this scene spoken by Carmen:", carmen_words_this_scene)
                carmen_words_this_scene = 0
            if jonny_words_this_scene != 0:
                jonny_words_total += jonny_words_this_scene
                print("\tWords in this scene spoken by Jonny:", jonny_words_this_scene)
                jonny_words_this_scene = 0
            if martin_words_this_scene != 0:
                martin_words_total += martin_words_this_scene
                print("\tWords in this scene spoken by Martin:", martin_words_this_scene)
                martin_words_this_scene = 0
            if antigone_words_this_scene != 0:
                antigone_words_total += antigone_words_this_scene
                print("\tWords in this scene spoken by Antigone:", antigone_words_this_scene)
                antigone_words_this_scene = 0
            if viridian_words_this_scene != 0:
                viridian_words_total += viridian_words_this_scene
                print("\tWords in this scene spoken by Viridian:", viridian_words_this_scene)
                viridian_words_this_scene = 0
            if other_words_this_scene != 0:
                other_words_total += other_words_this_scene
                print("\tOther words in this scene:", other_words_this_scene)
                other_words_this_scene = 0
            
            print("\tWords in this scene spoken by major characters:", this_scene_people)
            # We can record about 1500 words per hour
            print("\tApproximate time to record this scene:", this_scene_people * 60/1500, "minutes")


            print("Ep", ep_number, "Scene", scene_number)
        else:
            # Porfiro lines
            if curr_line.startswith("You: "):
                porfiro_words_this_scene +=  len(curr_line.split())
            elif curr_line.startswith("Carmen: "):
                carmen_words_this_scene +=  len(curr_line.split())
            elif curr_line.startswith("Jonny: "):
                jonny_words_this_scene +=  len(curr_line.split())
            elif curr_line.startswith("Martin: "):
                martin_words_this_scene +=  len(curr_line.split())
            elif curr_line.startswith("Antigone: "):
                antigone_words_this_scene +=  len(curr_line.split())
            elif curr_line.startswith("Viridian: "):
                viridian_words_this_scene +=  len(curr_line.split())
            else:
                other_words_this_scene += len(curr_line.split())
            
total_people = porfiro_words_total + carmen_words_total + jonny_words_total + martin_words_total + antigone_words_total + viridian_words_total
print("Total words spoken by Porfiro: ", porfiro_words_total)
print("Total words spoken by Carmen: ", carmen_words_total)
print("Total words spoken by Jonny: ", jonny_words_total)
print("Total words spoken by Martin: ", martin_words_total)
print("Total words spoken by Antigone: ", antigone_words_total)
print("Total words spoken by Viridian: ", viridian_words_total)
print("Total words by major characters: ", total_people)
print("Total other words: ", other_words_total)
print("Wordcount: ", other_words_total + total_people)
