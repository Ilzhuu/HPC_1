
import pandas as pd
import sys
import time
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer  # Frequency transformer - counts to frequencies


def read_file(filename, full):  # Reads given data file into a list
    file = open(filename, "r", encoding='utf-8')  # Reding file
    full_input = file.readlines()
    if full.lower() == "full":  # Returns full list or reduced list
        raw_file = full_input
    else:
        raw_file = full_input[:2000]
    file.close()
    print("Using ", filename)

    return raw_file


def process_file(raw_file):  # Cleans the data
    corpus = []
    for line in raw_file:
        line = line.replace('\'', '')
        line = line.replace('?', '')
        line = line.replace('!', '')
        line = line.replace(':', '')
        line = line.replace(';', '')
        line = line.replace(')', '')
        line = line.replace('(', '')
        line = line.replace('-', '')
        line = line.replace('_', '')
        line = line.replace('.', '')
        line = line.replace(',', '')
        line = line.replace('&', '')
        line = line.replace('👦', '')

        corpus.append(line.lower())

    return corpus


def vectorize(corpus):
    # Vectorization - process of turning a collection of text documents into numerical feature vectors

    singleline = ' '.join(corpus)  # All lines are joined into a single line (for simplicity reasons)
    singleline = singleline.replace('\n', '')  # Removing 'new line' symbols

    vectorizer2 = CountVectorizer(analyzer='word')  # Building a word count vector transformer
    x2 = vectorizer2.fit_transform([singleline])  # Building the word count vector matrix

    # Transform a count matrix to a normalized tf or tf-idf representation. Tf means term-frequency while tf-idf means term-frequency times inverse document-frequency.
    tf_transformer = TfidfTransformer(use_idf=False).fit(x2)  # Creating the transformer instance
    x2_tf = tf_transformer.transform(x2)  # Applying the transformer

    unique_words = vectorizer2.get_feature_names_out()  # Getting unique words in a separate list for convenience

    lst = []
    for i in range(0, len(unique_words)):  # Filling the data frame with data Unique word, Frequency
        word = unique_words[i]
        freq = x2_tf[0, i]
        lst.append({'Words': word, 'Frequency': freq})
    word_use_df = pd.DataFrame(lst, columns=['Words', 'Frequency'])
    word_use_df = word_use_df.sort_values(by=['Frequency'],
                                          ascending=False)  # Sorting the data by frequency - highest first
    word_use_df = word_use_df.set_index('Words')  # Setting index for data selection
    word_use_df['Words'] = word_use_df.index.values  # Creating a separate column for prediction needs

    return word_use_df


def predict(query, word_use_df):  # Predicts 10 most common words, based on use query term
    output = word_use_df[word_use_df.Words.str.startswith(query)]  # Selecting matching words
    print(output['Words'].head(10).values)  # Selecting the 10 top frequent


def main():
    st = time.time()  # Starting time
    print("Let's start!")
    try:
        file_to_use = sys.argv[1]
    except IndexError:
        file_to_use = 'tweets.txt'  # Default file to use

    try:
        query = sys.argv[2]
    except IndexError:
        query = "no"  # Default first letters to search for

    try:
        full = sys.argv[3]
    except IndexError:
        full = " "   # Default usage of reduced data set

    raw_file = read_file(file_to_use, full)  # "blogs.txt" or "tweets.txt"
    preprocessed_file = process_file(raw_file)
    word_use = vectorize(preprocessed_file)
    predict(query, word_use)

    et = time.time()  # Execution end time
    print("Time to execute in seconds", et - st)  # To evaluate running time


if __name__ == "__main__":
    main()
