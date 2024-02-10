with open("story.txt",'r') as file:
    story = file.read()
    start = "<"
    end = ">"
    position = -1
    words = set()

    for i,char in enumerate(story):
        if char.startswith(start) & position == -1: 
            words.add(char)