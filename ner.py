data = []
sentence_and_tags = []
sentence = ""
tags = []
with open("train") as f:
    for line in f:
        line = line.strip().split()
        if len(line) != 0:
            sentence += " "
            sentence += line[0]
            tags.append(line[1])
        else:
            sentence_and_tags.append(sentence.strip())
            sentence_and_tags.append(tags)
            data.append(sentence_and_tags)
            sentence_and_tags = []
            sentence = ""
            tags = []


