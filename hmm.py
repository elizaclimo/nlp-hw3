import math

def setup(filename):
    data = []
    tag_types_counts = {}
    word_types = []
    token_count = 0
    emission_features_counts = {}

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
                if tag in tag_types_counts:
                    tag_types_counts[tag] += 1
                else:
                    tag_types_counts[tag] = 1
                if word not in word_types:
                    word_types.append(word)
                token_count += 1
                if (word,tag) in emission_features_counts.items():
                    emission_features_counts[(word,tag)] += 1
                else:
                    emission_features_counts[(word,tag)] = 1
            else:
                sentence_and_tags.append(sentence.strip())
                sentence_and_tags.append(tag_sequence)
                data.append(sentence_and_tags)
                sentence_and_tags = []
                sentence = ""
                tag_sequence = []

    return filename, data, tag_types_counts, word_types, token_count, emission_features_counts



#setup training data from file
filename, data, tag_types_counts, word_types, token_count, emission_features_counts = setup("train")

# add all possible word-tag pairs that have not occurred
for tag,count in tag_types_counts.items():
    for word in word_types:
        if (word,tag) not in emission_features_counts.items():
            emission_features_counts[(word,tag)] = 0


# emission probabilities using estimated relative frequency
emission_probabilities = {}
for feature,count in emission_features_counts.items():
    word = feature[0]
    tag = feature[1]
    emission_probabilities[feature]= emission_features_counts[feature]/tag_types_counts[tag]



# all possible tag-tag pairs
transition_features_counts = {}
tag_types_counts['<EOS>'] = 0
tag_types_counts['<BOS>'] = 0
for tag1,c in tag_types_counts.items():
    for tag2,c in tag_types_counts.items():
        feature = (tag1,tag2)
        transition_features_counts[feature]=0

for tweet in data:
    sentence = tweet[0].split()
    tags = tweet[1]
    tags.insert(0,'<BOS>')
    tags.insert(-1,'<EOS>')
    for i in range(1,len(tags)):
        feature = (tags[i],tags[i-1])
        transition_features_counts[feature] += 1
    tag_types_counts['<BOS>'] += 1
    tag_types_counts['<EOS>'] += 1

transition_probabilities = {}
for feature,count in transition_features_counts.items():
    tag1 = feature[0]
    tag2 = feature[1]
    transition_probabilities[feature]= transition_features_counts[feature]/tag_types_counts[tag1]

print("PART 2.1")
print("p(B-person | O) = ", transition_probabilities[('O','B-person')])
print("p(B-person | B-person) = ", transition_probabilities[('B-person','B-person')])
print("p(I-person | B-person) = ", transition_probabilities[('B-person','I-person')])
print("p(B-person | I-person) = ", transition_probabilities[('I-person','B-person')])
print("p(I-person | I-person) = ", transition_probabilities[('I-person','I-person')])
print("p(O | I-person) = ", transition_probabilities[('B-person', 'O')])

