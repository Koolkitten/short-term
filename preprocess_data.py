import ast
import csv
import nltk
import re
import pprint
from sys import argv

combinedFileLoc = "data/stocknews/Combined_News_DJIA.csv"


def inputGenerator(fileName):
    with open(fileName, newline="", encoding="utf-8") as fp:
        reader = csv.reader(fp)
        reader.__next__()
        for row in reader:
            labels = row[1]
            texts = [ast.literal_eval(i).decode("utf-8") for i in row[2:]]
            yield tuple((texts, labels))


def postTagSentence(text):
    tokenizedSentence = nltk.tokenize.TweetTokenizer().tokenize(text)
    posTaggedSentence = nltk.pos_tag(tokenizedSentence)
    return posTaggedSentence


def main():
    pass


if __name__ == "__main__":
    main()
