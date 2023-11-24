alphabet = list("abcdefghijklmnopqrstuvwxyz")
sentence = "Je sers la science et c'est ma joie!"

# Question 1
def encode_ceasar(sentence, alphabet, shifting):
    sentence_low = sentence.lower()
    sentence_list = list(sentence_low)
    for idx, letter in enumerate(sentence_list):
        if letter in alphabet:
            idx_dict = alphabet.index(letter)
            idx_dict_shifted = (idx_dict+int(shifting))%len(alphabet)
            sentence_list[idx] = alphabet[idx_dict_shifted]
    new_sentence = "".join(sentence_list)
    return new_sentence

new_sentence = encode_ceasar(sentence,alphabet,22)
print("Phrase  codé :\n", new_sentence)

# Question 2
def decode_ceasar(sentence, alphabet, shifting):
    sentence_low = sentence.lower()
    sentence_list = list(sentence_low)
    for idx, letter in enumerate(sentence_list):
        if letter in alphabet:
            idx_dict = alphabet.index(letter)
            idx_dict_shifted = (idx_dict-int(shifting))%len(alphabet)
            sentence_list[idx] = alphabet[idx_dict_shifted]
    new_sentence = "".join(sentence_list)
    return new_sentence

decode_sentence  = decode_ceasar(new_sentence, alphabet, 22)
print("Phrase  décodé :\n", decode_sentence)

#Question 3
import random
alphabet_1 = list("abcdefghijklmnopqrstuvwxyz ,é'ù1234567890°+/*<>&(-çà)=ç@è_}{!?")
alphabet_2 = alphabet_1[:] # Create a copy
random.shuffle(alphabet_2) # Shuffle the order of the second alphabet list
sentence = "On va rajouter un peu de la complexité, avec de la ponctuation. Combien font 2+3? => à peux près 5 bien sùr!"

def encode_ceasar_plus(sentence, alphabet_1, alphabet_2, decode=False):
    sentence_low = sentence.lower()
    sentence_list = list(sentence_low)
    for idx, letter in enumerate(sentence_list):
        if letter in alphabet_1:
            if decode == False:
                idx_dict = alphabet_1.index(letter)
                sentence_list[idx] = alphabet_2[idx_dict]
            else:
                idx_dict = alphabet_2.index(letter)
                sentence_list[idx] = alphabet_1[idx_dict]

    new_sentence = "".join(sentence_list)
    return new_sentence

encoded = encode_ceasar_plus(sentence,alphabet_1,alphabet_2)
print("Phrase complexe codé :\n", encoded)
decoded = encode_ceasar_plus(encoded,alphabet_1,alphabet_2,decode=True)
print("Phrase complexe décodé :\n", decoded)
