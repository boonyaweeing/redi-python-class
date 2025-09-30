"""
## Expected Behavior
```
Text Analyzer
=============

Enter your text (press Enter twice to finish):
This is a sample text for analysis. It contains multiple sentences and various words. 
Some words are repeated to test the frequency analysis. This tool helps writers 
understand their writing style and improve readability.

TEXT ANALYSIS REPORT
====================

BASIC STATISTICS:
- Total words: 32
- Characters (with spaces): 159
- Characters (without spaces): 127
- Sentences: 3
- Paragraphs: 1

ADVANCED ANALYSIS:
- Average words per sentence: 10.7
- Average word length: 4.0 characters
- Reading difficulty: Easy
- Text sentiment: Positive (60% positive words)

MOST COMMON WORDS:
1. "and" (3 times)
2. "text" (2 times)
3. "analysis" (2 times)
4. "words" (2 times)
5. "writing" (2 times)

SUMMARY:
Your text is easy to read with a positive tone. Consider varying sentence length for better flow.
```

## The Challenge
This exercise demonstrates how a program that could be 100+ lines of messy code becomes clean and readable when broken into focused functions. 
Each function should have a single, clear purpose.
"""
characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
characters_and_space = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
def cal_character_with_space(text):
    num_character_with_space = 0
    for cha in text.lower():
        if cha in characters_and_space:
           num_character_with_space += 1 
    return num_character_with_space

def cal_character_without_space(text):
    num_character_without_space = 0
    for cha in text.lower():
        if cha in characters:
           num_character_without_space += 1 
    return num_character_without_space
    
def cal_word(text):
    words = list(text.split())
    num_word = len(words)
    return num_word

def cal_sentence(text):
    num_sentence = 0
    for cha in text:
        if cha == ".":
           num_sentence += 1 
    return num_sentence



print("Text Analyzer")
print("=============")

text = input("Enter your text (press Enter twice to finish):\n")


print(f"- Total words: {cal_word(text)}")
print(f"- Characters (with spaces): {cal_character_with_space(text)}")
print(f"- Characters (without spaces): {cal_character_without_space(text)}")
print(f"- Sentences: {cal_sentence(text)}")