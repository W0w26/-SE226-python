from abc import ABC, abstractmethod


class FrequencyCounter(ABC):
    address = ""

    def __init__(self, address):
        self.address = address

    @abstractmethod
    def calculateFreqs(self):
        pass


class ListCount(FrequencyCounter):
    def calculateFreqs(self):
        frequencies = [0] * 26  # assuming only lowercase letters

        with open(self.address, 'r') as file:
            for line in file:
                for char in line.lower():
                    if char.isalpha():
                        frequencies[ord(char) - ord('a')] += 1

        for i, freq in enumerate(frequencies):
            print(chr(ord('a') + i), '=', freq)


class DictCount(FrequencyCounter):
    def calculateFreqs(self):
        frequencies = {}

        with open(self.address, 'r') as file:
            for line in file:
                for char in line.lower():
                    if char.isalpha():
                        frequencies[char] = frequencies.get(char, 0) + 1

        for char, freq in frequencies.items():
            print(char, '=', freq)


# Testing the script
file_address = "weirdWords.txt"

list_counter = ListCount(file_address)
print("List Count:")
list_counter.calculateFreqs()

print()

dict_counter = DictCount(file_address)
print("Dictionary Count:")
dict_counter.calculateFreqs()
