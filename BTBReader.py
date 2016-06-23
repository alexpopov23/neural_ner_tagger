import os

def get_tagged_sentences(input_folder):

    tagged_sentences = []
    pos_tags = set()
    files = os.listdir(input_folder)
    for f_name in files:
        f = open(os.path.join(input_folder, f_name), "r")
        # remove the .encode/.decode part for NER/POS
        text = f.read().decode("cp1251")
        sentences = text.split("##")
        for sentence in sentences:
            tagged_sentence = []
            lines = sentence.strip("##").strip().split("\n")
            for line in lines:
                fields = line.split(" ")
                if len(fields) != 2:
                    continue
                word, tag = fields
                tag = tag.strip()[0]
                tagged_sentence.append((word, tag))
                pos_tags.add(tag)
            tagged_sentences.append(tagged_sentence)

    return tagged_sentences, pos_tags
