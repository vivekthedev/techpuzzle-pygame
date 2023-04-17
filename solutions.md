# Solutions of all the levels in the Hardest puzzle in Tech

This puzzle is designed to think in the technical way. 
To successfully solve each puzzle, one must exhibit heightened levels of observational skills. I am confident in your abilities to solve these puzzles, and I hope that you have exerted your utmost efforts before referring to the answers. While solving each puzzle independently is an enjoyable experience, there is no harm in utilizing the answers as a reference.

## Answer Level 1
The puzzle is related to sorting, albeit in an unconventional way. The puzzle features four distinct objects, each accompanied by a numerical value. Upon closer inspection, it becomes apparent that each of these objects can be found in the logo of a popular programming language.


- Snake (15) - Python
- Coffee (32) - Java
- Elephant (53) - PHP
- Ring (75) - Ruby

Now the clue say:
> 'To solve this riddle',
> 'you must arrange', 
> 'key is the father,
> 'when he first breathed,'

It appears that the sorting of the numbers in the puzzle should not be based on conventional methods, despite previous attempts to do so. The crucial clue lies in the inventor or father of the language and the concept of their "first breath," which refers to their date of birth. As such, the numerical values must be arranged in accordance with the date of birth of each respective inventor.
 
After Deducing this we get
 - Java (32) - James Gosling, 1955
 - Python (15) - Guido Van Rossum, 1956
 - Ruby (75) - Yukihiro Matsumoto, 1965
 - PHP (53) - Rasmus Lerdorf, 1968

 Answer - 32157553 

 ## Answer Level 2

This puzzle pertains to the topic of colors. On the left-hand side of the puzzle, various color boxes can be observed, while on the right-hand side, a grid of 5 rows and 3 columns of switches can be found. The crucial hint in this puzzle is to contemplate the colors presented and to take note of the three switches in each row, which resemble the RGB (Red, Green, Blue) color channels. Additionally, the clue stipulates that the objective is to attain either the minimum or maximum value. As such, the task at hand involves activating the switches in a manner that produces the corresponding color for each row.


 Answer:
 ```
  ON  ON  ON    (WHITE) 
 OFF  OFF ON    (BLUE)
  ON OFF OFF    (RED)
 OFF  ON OFF    (GREEN)
 OFF OFF OFF    (BLACK)
 ```

 ## Answer Level 3

The task at hand requires one to exercise their cognitive abilities to decipher a code. Based on the provided clue, "A famous cryptography, back in time," it is likely that the text has undergone a Caesar Cipher encryption. However, the challenge lies in determining the precise shift value employed in the encryption process. A careful examination of the window will provide a vital clue necessary to proceed.
Look at the following:
- the number of letters in each word
- the number of sentences in clue
- the number of words in each sentence
- the number of words in title

The Puzzle window revolves around 3, so if you take the chance and try decrypting the text with shift value of 3 you get:
Answer : YOU WON


## Answer Level 4

This is a pretty hard one. The clue says the following:
```
'each rOw is a letter,'
'look carEfully,'
'to approPriate form,'
'coNvert the letter'
```
 
You have to determine:
- Why there is a grid of switches
- what letter can you make with switches

The clue requires you to convert each letter into a sequence of switches (On or Off, True or False) What type of conversion can be represented in True/False? Yes, you guessed it right its Binary. By examining the clue carefully, you must determine which four-letter word the clue is referring to. Each sentence in the clue has only one letter capitalized, providing a crucial hint to help you solve the puzzle.

OPEN, if you convert "OPEN" to binary you get:

```
[False, True, False, False, True, True, True, True]
[False, True, False, True, False, False, False, False]
[False, True, False, False, False, True, False, True]
[False, True, False, False, True, True, True, False]
```

