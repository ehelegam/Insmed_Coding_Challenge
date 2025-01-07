from collections import Counter
import sys

def retrieve_sequences_from_file(file: str) -> list:
    """
    Retrieve a list of sequences from a given file.

    This function reads a file where each line represents a sequence, strips any leading or 
    trailing whitespace from each line, and returns the sequences as a list of strings.
    """
    # handle missing file error
    try:
        with open(file, 'r') as file:
            # get sequences as list
            seqs = [line.strip() for line in file.readlines()]
        return seqs
    # raise exception if file is not found
    except FileNotFoundError:
        print(f"The file {file} does not exist.")


def get_consensus_sequence(sequences: list) -> str:
    """
    Generate a consensus sequence from a list of input sequences.

    This function takes a list of sequences and computes  a consensus sequence based on the most frequent base at each position. If there is a tie for the most frequent base, the function appends 'N' (denoting ambiguity) at that position.
    """
    # determine the length of the maximum sequence
    max_length = max(len(seq) for seq in sequences)
    
    # align the sequences
    aligned_sequences = [seq.ljust(max_length, 'N') for seq in sequences]
    
    # create a list to collect the consensus information
    consensus = []
    
    # loop over each position and count each base, ignoring 'N'
    for i in range(max_length):
        column_bases = [seq[i] for seq in aligned_sequences if seq[i] != 'N']
        
        # use Counter to record the counts
        counts = Counter(column_bases)
        
        # find the highest count and check if other bases had similar counts
        # ignore 'Ns'
        if column_bases: 
            most_common_bases = counts.most_common()
            highest_count = most_common_bases[0][1]
            
            # check if there is a tie for the highest count
            # if so append 'N'
            if len([base for base, count in most_common_bases if count == highest_count]) > 1:
                consensus.append('N')
            else:
                # append the base with the highest count
                consensus.append(most_common_bases[0][0])
        else:
            consensus.append('N')
    
    # return the consensus sequence as a string
    return ''.join(consensus)


def determine_sequence_alignment_score(sequence: str) -> int:
    """
    Calculate the alignment score of a given sequence based on predefined base scores.

    This function calculates the score of a sequence by summing the values assigned to each nucleotide base ('A', 'C', 'G', 'T', 'N') using a predefined score mapping.
    """
    # define a dictionary with the mapping scores
    score_map = {
        'A': 2,
        'C': 5,
        'G': 3,
        'T': 4,
        'N': -1
    }
    
    # calculate the total score
    score = sum(score_map[base] for base in sequence)
    
    return score


# get the input sequences from file
input_sequences = retrieve_sequences_from_file(f'{sys.path[0]}/input_sequences.txt')

# get the consensus
consensus_sequence = get_consensus_sequence(input_sequences)
print("Consensus Sequence:", consensus_sequence)

# calculate the alignment score
alignment_score = determine_sequence_alignment_score(consensus_sequence)
print("Consensus Sequence Alignment score:", alignment_score)

