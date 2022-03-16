import collections

class Perceptron(object):
    """Base Perceptron model class"""

    def __init__(self, tag_types):
        self.weights = collections.Counter()
        self.tag_types = tag_types

    def get_features(self, prevTag, tag, word=None):
        '''Given a previous tag, current tag, and current word, generate a list of features.  Note that word may be omitted for <EOS>'''
        if word is not None:
            features_list = [(prevTag, tag), (tag, word)]
        else:
            features_list = [(prevTag, tag)]
        return features_list

    def score_features(self, features_list):
        '''Given a list of features, compute the score from those features'''
        score = 0
        for feat in features_list:
            score += self.weights[feat]
        return score

    def train(self, sents, epochs=10):
        '''Given a list of sentences in the form:
        ['space separated string', ['O', 'O', 'O']]
        Train the perceptron for the given number of epochs'''
        for epoch in range(epochs):
            for sent, tags in sents:
                self.train_line(sent, tags)

    def train_line(self, sent, tags):
        '''Trains from a single sentence.  
        sent is a space separated string
        tags is a list of correct tags'''
        mytags = self.viterbi(sent)
        prevCorrect = '<BOS>'
        prevPred = '<BOS>'
        for w, c, p in zip(sent.split(' '), tags, mytags):
            if c != p:
                for feat in self.get_features(prevCorrect, c, w):
                    self.weights[feat] += 1
                for feat in self.get_features(prevPred, p, w):
                    self.weights[feat] -= 1
            prevCorrect = c
            prevPred = p
        if c != p:
            # If the final tag is wrong, also update <EOS>
            for feat in self.get_features(c, '<EOS>'):
                self.weights[feat] += 1
            for feat in self.get_features(p, '<EOS>'):
                self.weights[feat] -= 1

    def tag_sents(self, sents, outFile='dev-percep.out'):
        '''Given a list of sentences in the form ['sample sentence here', ['O', 'O', 'O'] ], predicts tag sequence and writes to file for scoring. '''
        with open(outFile,'w') as g:
            for sent, tags in sents:
                mytags = self.viterbi(sent)
                for s, c, m in zip(sent.split(' '), tags, mytags):
                    g.write(s + ' ' + c + ' '+ m + '\n')
                g.write('\n')



    def viterbi(self, sent):
        '''Given a space separated string as input, produce the 
        highest weighted tag sequence for that string.'''
        # You will replace this, for now it just returns 'O' for every tag
        return ['O' for x in sent.split(' ')]
        

