# IIUK Coding challenge

Welcome to the Insmed Innovation UK coding challenge! Congratulations on making it to this stage.

For this we ask you to solve the following coding problems (see below), for the given inputs supplied.
We ask that you return a list of answers, along with the code written to solve the challenges (**_Please return the code as a .txt file_**)

We expect this coding challenge to take roughly between **_1-2 hours_** to solve, and you have **_five days_** to complete the challenge and return it back to us.

If you are unable to solve any of the problems please return your workings for that problem, as your approach to the problem is equally as important as the solution.

### Guidelines to follow
- Please stick to base libraries when writing your solutions, **_avoid importing external packages_**
- Please **_don't directly copy answers from stack overflow_**/the internet more generally: we want to get a feel for how you code, not
  someone else.
- **_Refrain from using machine generated solutions such as llms_** (e.g. chat-gpt or copilot): we are attempting to gauge
  your skills not a language model's and it's as much a test to see if you enjoy this type of coding, as it is ensuring you're capable
  of performing at a given level.
- **Have fun!**

Best of luck! Insmed Innovation UK's Informatics team.



## Problem 1:
Find the consensus sequence from a list of sequences, where the input is a file with each
line representing a sequence of nucleotides. The consensus sequence is the most common
nucleotide at each position in the sequences.

In the case of a tie, the consensus sequence should be 'N'.

Calculate the score of the consensus sequence by summing the values of each nucleotide
according to the following values:
A = 2, C = 5, G = 3, T = 4, N = -1

Example:
- ACGAT
- CCGATGG
- ACGA
- TCGAG
- ACGAG

The consensus sequence is 'ACGANGG' and the score is 2+5+3+2-1+3+3 = 17

- [input_file](https://pastebin.com/raw/hHzaMRua)

## Problem 2:
Your input is a file, where each line represents a roll of 6 dice.
Your task is to calculate the score of each roll according to the rules below.
You final output should be the sum of the top 5 scores.

You should calculate the best possible score for the game, where a score can be assembled as a combination of a set of dice using the following rules:
- 1s not part of other combinations are worth 100 points each.
- 5s not part of other combinations are worth 50 points each.
- N>=3 of a kind is worth 100 × the face value of the die × (N - 2); e.g. 4 of a kind of 3s is worth 600 points.
- For the purpose of the rule above, the face value of a 1 is 10.
- A straight of N>4 dice is worth 1500 points.

A single die can only be part of one scoring combination, e.g. a straight from 1 to 5 would not include additional scores for 1s or 5s.
Where multiple scoring combinations are possible, you should choose the highest scoring combination.

Examples:
- ⚅ ⚀ ⚄ ⚀ ⚄ ⚄ - 3 of a kind of 5s, worth 500 points, plus two 1s worth 100 points each, giving a total of 700 points. 
- ⚀ ⚀ ⚀ ⚀ ⚀ ⚀ - 6 of a kind of 1s, worth 4000 points. 
- ⚀ ⚁ ⚂ ⚃ ⚄ ⚄ - Straight of 1 to 5, worth 1500 points, plus a single 5 worth 50 points, giving a total of 1550 points.


- [input_file](https://pastebin.com/raw/hmGFtGwa)

## Problem 3:
The input is an unrefined macrodata set consisting of two-dimensional array of positive integers.
The rows are given as lines in the input file, with integers separated by commas to represent the columns.
Certain linearly-adjacent pairs of these integers invoke Dread and require refinement.
The output is a score representing the overall Dread in the macrodata set, measuring the extent to which the
data require further refinement.

- The overall Dread is the sum of the sums of Dread-invoking pairs, multiplied by the number of Dread-invoking pairs.
- A pair of linearly-adjacent numbers invokes Dread if their sum has 7 or 9 as a factor but not both. (e.g. 21, 45 but not 63)

Consider the input:

11, 19, 33, 64
14, 22, 47, 75
81, 14, 75, 82
9, 54, 41, 67

The Dread-invoking pairs are:

      -,-,-,-   -,-,-,-   -,-,-,-    -,-,-,-
      -,-,-,-   -,22,-,-  14,22,-,-  -,-,-,-
      81,-,-,-  -,14,-,-  -,-,-,-    -,-,-,-
      9,-,-,-   -,-,-,-   -,-,-,-    -,-,41,67

So the overall Dread is:
(90 + 36 + 36 + 108) * 4 = 1080

- [input_file](https://pastebin.com/raw/i7kJgsMR)
