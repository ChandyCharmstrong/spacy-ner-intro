# import spacy + english language module 
import spacy
nlp = spacy.load('en_core_web_md')

#  garden path sentence list
garden_path_sentences = [
    "The old man the boat.",
    "The complex houses married and single soldiers and their families.",
    "The hourse raced past the barn fell.",
    "We painted the wall with cracks.",
    "Mary gave the child a band aid.",
    "The Jill is never here hurts.",
    "The cotton clothing is made from grows in Mississippi.",
]

# loop through list, tokenise, perform named entity recognition 
for sentence in garden_path_sentences:
    doc = nlp(sentence)
    print(f"Sentence: {sentence}")
    for token in doc:
        print(f"Token: {token.text}\t\tNER: {token.ent_type_ if token.ent_type_ else '-'}")
    print()

# examine how spaCy catagorised the sentenses, does this make sense? 
print(spacy.explain("GPE")) # Yes, Mississippi = City 
print(spacy.explain("PERSON")) # Yes, Jill & Mary = People, including fictional

# My output reads as follows: 
# I'm surprised by the amount of """ Ner: - """ but Person and GPE make sense 
"""Sentence: The old man the boat.
Token: The              NER: -
Token: old              NER: -
Token: man              NER: -
Token: the              NER: -
Token: boat             NER: -
Token: .                NER: -

Sentence: The complex houses married and single soldiers and their families.
Token: The              NER: -
Token: complex          NER: -
Token: houses           NER: -
Token: married          NER: -
Token: and              NER: -
Token: single           NER: -
Token: soldiers         NER: -
Token: and              NER: -
Token: their            NER: -
Token: families         NER: -
Token: .                NER: -

Sentence: The hourse raced past the barn fell.
Token: The              NER: -
Token: hourse           NER: -
Token: raced            NER: -
Token: past             NER: -
Token: the              NER: -
Token: barn             NER: -
Token: fell             NER: -
Token: .                NER: -

Sentence: We painted the wall with cracks.
Token: We               NER: -
Token: painted          NER: -
Token: the              NER: -
Token: wall             NER: -
Token: with             NER: -
Token: cracks           NER: -
Token: .                NER: -

Sentence: Mary gave the child a band aid.
Token: Mary             NER: PERSON
Token: gave             NER: -
Token: the              NER: -
Token: child            NER: -
Token: a                NER: -
Token: band             NER: -
Token: aid              NER: -
Token: .                NER: -

Sentence: The Jill is never here hurts.
Token: The              NER: -
Token: Jill             NER: PERSON
Token: is               NER: -
Token: never            NER: -
Token: here             NER: -
Token: hurts            NER: -
Token: .                NER: -

Sentence: The cotton clothing is made from grows in Mississippi.
Token: The              NER: -
Token: cotton           NER: -
Token: clothing         NER: -
Token: is               NER: -
Token: made             NER: -
Token: from             NER: -
Token: grows            NER: -
Token: in               NER: -
Token: Mississippi              NER: GPE
Token: .                NER: -"""