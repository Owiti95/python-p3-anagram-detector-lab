# your code goes here!
# ANAGRAM DETECTOR
# Take letters from word into list
# Take letters from list words into list
# Compare the two lists
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, list=[]):
        print(f"Finding Anagram for '{self.word}'...")
        word_characters = [character for character in self.word]
        matching_words = []
        print("Words with an equal length")

        for potential_matching_word in list:
            if len(potential_matching_word) == len(self.word):
                potential_match_characters = [
                    character for character in potential_matching_word
                ]
                potential_match_characters.sort()
                word_characters.sort()
                # print(potential_match_characters)
                print(f"- {potential_matching_word}")
                if potential_match_characters == word_characters:
                    matching_words.append(potential_matching_word)
        print(f"Word: {self.word}\nMatch(es):{matching_words}")
        return matching_words


listen = Anagram("listen")
listen.match(["enlists", "google", "inlets", "banana"])