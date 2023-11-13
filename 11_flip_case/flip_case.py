def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_phrase = ""
    for letter in phrase:
        if to_swap == letter.lower():
            if to_swap.islower() and letter.isupper():
                new_phrase += letter.lower()
            elif to_swap.islower() and letter.islower():
                new_phrase += letter.upper()
        elif to_swap == letter.upper():
            if to_swap.isupper() and letter.islower():
                new_phrase += letter.upper()
            elif to_swap.isupper() and letter.isupper():
                new_phrase += letter.lower()
        else:
            new_phrase += letter

    return new_phrase
