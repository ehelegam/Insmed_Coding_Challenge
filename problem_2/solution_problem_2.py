from collections import Counter
import sys

def parse_dice_rolls(file: str) -> list:
    """
    Parse a file containing dice rolls represented by symbols and return a list of integer values.

    This function reads a file where each line contains a sequence of dice roll symbols which are mapped to their respective integer values.
    """
    symbols = {
        '⚅': 6,
        '⚄': 5,
        '⚃': 4,
        '⚂': 3,
        '⚁': 2,
        '⚀': 1
    }
    
    # handle missing file
    try:
        diced_rolls = []
        with open(file, 'r', encoding='utf-8') as file:
            for line in file:
                file_content = line.strip().split()
                rolls = [symbols.get(symbol) for symbol in file_content]
                diced_rolls.append(rolls)
            
            return diced_rolls
    
    # raise file not found error
    except FileNotFoundError:
        print(f"The file {file} does not exist.")



def calculate_roll_score(rolls: list) -> int:
    """
    Calculate the score for a given dice roll based on the rules of the game.

    This function calculates the score for a roll of dice according to the rules provided.
    """

    # use Counter to get the number each face
    # set the initial score to zero
    count = Counter(rolls)
    score = 0

    # set a list with unique combinations of used combinations
    used = set()
    
    # check the all faces appears only once
    if all(count[d] >= 1 for d in range(1, 7)): 
        score = 1500
        return score  

    # check if a face is repeated more than once
    for die_face in range(1, 7):
        num = count[die_face]
        if num >= 3 and die_face not in used:
            if die_face == 1:
                # 1 is worth 10 per die in 3+ of a kind
                score += 100 * 10 * (num - 2)
            else:
                # the other faces are worth 100 * face_value * (num - 2)
                score += 100 * die_face * (num - 2)
                # mark all faces as used
            used.update([die_face] * num)

    # score occurences of ones and fives when not part of any other combination
    for die_face, points in [(1, 100), (5, 50)]:
        if die_face not in used:
            score += points * count[die_face]
            # mark all faces as used
            used.update([die_face] * count[die_face])
    
    return score


rolls = parse_dice_rolls(f'{sys.path[0]}/dice_rolls.txt')
for roll in rolls or []:
    score = calculate_roll_score(roll)
    print(f'Roll: {roll} | Score: {score}')