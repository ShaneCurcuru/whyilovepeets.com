#!/usr/local/bin/python3
#
import sys
import os
import markovify
DEFAULT_TEXT ="All-About-Coffee.txt"
DEFAULT_MODEL ="All-About-Coffee.txt.json"

def usage():
    print("Usage: " + sys.argv[0] + " [" + DEFAULT_TEXT + "]")
    print("   Markovifys the input and produces some text")

# Parse opened file handle, create model, save it
def makemodel(fnam):
    # Read file, then model it
    f = open(fnam, encoding="utf-8")
    rawtext = f.read()
    f.close()    
    text_model = markovify.Text(rawtext)  # , state_size=3) option?
    model_json = text_model.to_json()
    fout = fnam + ".json"
    f = open(fout, mode="w")
    f.write(model_json)
    f.close()
    print("Created model: " + fout)

    
    # Print five randomly-generated sentences
    for i in range(5):
        print(text_model.make_sentence())

    # Print three randomly-generated sentences of no more than 140 characters
    for i in range(10):
        print(text_model.make_short_sentence(160))
    
# Using a model, dump some sentences to a file
def usemodel(fnam, n, m):
    f = open(fnam, encoding="utf-8")
    text_model = markovify.Text.from_json(f.read())
    f.close()
    outlines = []

    # Print n default sentences
    for i in range(n):
        outlines.append(text_model.make_sentence() + '\n')

    # Print some short sentences
    for i in range(n):
        outlines.append(text_model.make_short_sentence(m) + '\n')

    with open(fnam + ".out", mode="w", encoding="utf-8") as f:
        f.writelines(outlines)



# ##########################################################
if __name__ == '__main__':
    usage()
    #makemodel(DEFAULT_TEXT)
    usemodel(DEFAULT_MODEL, 10, 160)
    print("DONE ----")
    

        


