def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    final_phrase = ''
    for letter in phrase:
        if letter.lower() == to_swap.lower():
            if letter.islower():
                final_phrase += letter.upper()
            else:
                final_phrase += letter.lower()
        else:
            final_phrase += letter
    return final_phrase

