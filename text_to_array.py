import numpy as numpy

def text_to_array(self, path):

    my_file = open(path, "r")
    content = my_file.read()

    def split(word):
        return [char for char in word]

    content_list = content.split("\n")
    my_file.close()

    final = []
    for i in range(len(content_list)):
        final.append(split(content_list[i]))

    return numpy.asarray(final)