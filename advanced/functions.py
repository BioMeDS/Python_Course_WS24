from collections import defaultdict


def FrequencyTable(Text, k):
    counts = defaultdict(int)
    for i in range(len(Text) - k + 1):
        pattern = Text[i : i + k]
        counts[pattern] += 1
    return counts


def FrequentWords(Text, k):
    counts = FrequencyTable(Text, k)
    maxValue = max(counts.values())
    words = [key for key, value in counts.items() if value == maxValue]
    return words


def ReverseComplement(Pattern: str) -> str:
    if not isinstance(Pattern, str):
        raise TypeError("ReverseComplement only works on strings")
    return Pattern.translate(str.maketrans("ACGTacgt", "TGCAtgca"))[::-1]


def PatternMatching(Genome, Pattern):
    positions = list()
    for i in range(len(Genome) - len(Pattern) + 1):
        if Genome[i : i + len(Pattern)] == Pattern:
            positions.append(i)
    return positions
