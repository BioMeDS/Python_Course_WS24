def PatternCount(Text, Pattern):
    """Count number of times that Pattern occurs within Text

    Parameters
    ----------
    Text : str
        DNA Sequence
    Pattern : str
        Short pattern of DNA

    Returns
    -------
    int
        count
    """
    count = 0
    for i in range(len(Text) - len(Pattern) + 1):
        if Text[i : i + len(Pattern)] == Pattern:
            count += 1  # increase count by one
    return count
