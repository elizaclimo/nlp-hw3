
def setup(filename):
    data = []
    tag_types = []
    word_types = []
    token_count = 0

    sentence_and_tags = []
    sentence = ""
    tag_sequence = []

    with open(filename) as f:
        for line in f:
            line = line.strip().split()
            if len(line) != 0:
                word = line[0]
                sentence += " "
                sentence += word
                tag = line[1]
                tag_sequence.append(tag)
                if tag not in tag_types:
                    tag_types.append(tag)
                if word not in word_types:
                    word_types.append(word)
                token_count += 1
            else:
                sentence_and_tags.append(sentence.strip())
                sentence_and_tags.append(tag_sequence)
                data.append(sentence_and_tags)
                sentence_and_tags = []
                sentence = ""
                tag_sequence = []

    return filename, data, tag_types, word_types, token_count

filename, data, tag_types, word_types, token_count = setup("train")
print("DATASET: ", filename)
print("Number of Tweets: ", len(data))
print("Number of Tokens: ", token_count)
print("Number of Word Types: ", len(word_types))
print("Number of Tag Types: ", len(tag_types))


