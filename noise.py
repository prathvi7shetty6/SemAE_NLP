import json
import random
import string
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

def get_noise():
    # Function to add noise to a sentence
    noise = ''.join(random.choices(string.ascii_lowercase, k=3))
    return noise

def random_bool(probability=0.5):
    """Returns True with given probability

    Args:
        probability: probability to return True

    """
    assert (0 <= probability <= 1), "probability needs to be >= 0 and <= 1"
    return random.random() < probability

def replace_random_token(line, probability):
    line_split = line.split()
    for i in range(len(line_split)):
        if random_bool(probability):
            line_split[i] = get_noise()
    return " ".join(line_split)

def random_insertion(words, n=1):
    tokens = word_tokenize(words)
    for _ in range(n):
        tokens.insert(random.randint(0, len(tokens) - 1), get_noise())
    return " ".join(tokens)

def process_data(input_file, output_file):
    # Read the JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Add noise to sentences
    for entity in data:
        print('Entity id')
        print(entity['entity_id'])
        for review in entity['reviews']:
            print('Review id')
            print(review['review_id'])
            review['sentences'] = [random_insertion(replace_random_token(sentence, 0.25)) for sentence in review['sentences']]

    # Save the modified data to a new JSON file
    with open(output_file, 'w') as f:
        json.dump(data, f, indent=2)

# Replace 'input.json' and 'output.json' with your actual file names
process_data('space_train.json', 'output_replace_randomn_insert.json')
