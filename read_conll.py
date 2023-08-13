def read_conll(in_file, lowercase=False, max_example=None):
    examples = []
    with open(in_file) as f:
        word, pos, head, label = [], [], [], []
        for line in f.readlines():
            sp = line.strip().split('\t')
            if len(sp) == 10:
                if '-' not in sp[0]:
                    word.append(sp[1].lower() if lowercase else sp[1])
                    pos.append(sp[4])
                    head.append(int(sp[6]))
                    label.append(sp[7])
            elif len(word) > 0:
                examples.append({'word': word, 'pos': pos, 'head': head, 'label': label})
                word, pos, head, label = [], [], [], []
                if (max_example is not None) and (len(examples) == max_example):
                    break
        if len(word) > 0:
            examples.append({'word': word, 'pos': pos, 'head': head, 'label': label})
    return examples
k = read_conll('/Users/doge/Documents/Stanford Summer/CS224/student/data/test1.conll')

#刚读取完的数据
print(k) #[{'word': ['No', ',', 'it', 'was', "n't", 'Black', 'Monday', '.'], 'pos': ['DT', ',', 'PRP', 'VBD', 'RB', 'JJ', 'NNP', '.'], 'head': [7, 7, 7, 7, 7, 7, 0, 7], 'label': ['discourse', 'punct', 'nsubj', 'cop', 'neg', 'compound', 'root', 'punct']}, {'word': ['But', 'while', 'the', 'New', 'York', 'Stock', 'Exchange', 'did', "n't", 'fall', 'apart', 'Friday', 'as', 'the', 'Dow', 'Jones', 'Industrial', 'Average', 'plunged', '190.58', 'points', '--', 'most', 'of', 'it', 'in', 'the', 'final', 'hour', '--', 'it', 'barely', 'managed', 'to', 'stay', 'this', 'side', 'of', 'chaos', '.'], 'pos': ['CC', 'IN', 'DT', 'NNP', 'NNP', 'NNP', 'NNP', 'VBD', 'RB', 'VB', 'RB', 'NNP', 'IN', 'DT', 'NNP', 'NNP', 'NNP', 'NNP', 'VBD', 'CD', 'NNS', ':', 'JJS', 'IN', 'PRP', 'IN', 'DT', 'JJ', 'NN', ':', 'PRP', 'RB', 'VBD', 'TO', 'VB', 'DT', 'NN', 'IN', 'NN', '.'], 'head': [33, 10, 7, 7, 7, 7, 10, 10, 10, 33, 10, 10, 19, 18, 18, 18, 18, 19, 10, 21, 19, 23, 21, 25, 23, 29, 29, 29, 23, 23, 33, 33, 0, 35, 33, 37, 35, 39, 37, 33], 'label': ['cc', 'mark', 'det', 'compound', 'compound', 'compound', 'nsubj', 'aux', 'neg', 'advcl', 'advmod', 'nmod:tmod', 'mark', 'det', 'compound', 'compound', 'compound', 'nsubj', 'advcl', 'nummod', 'dobj', 'punct', 'dep', 'case', 'nmod', 'case', 'det', 'amod', 'nmod', 'punct', 'nsubj', 'advmod', 'root', 'mark', 'xcomp', 'det', 'dobj', 'case', 'nmod', 'punct']}]
print(len(k)) #2
print(k[0]["word"]) #['No', ',', 'it', 'was', "n't", 'Black', 'Monday', '.']
