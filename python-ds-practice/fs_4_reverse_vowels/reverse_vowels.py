def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    lst_string = list(s)
    first = 0
    end = len(s) - 1

    vowels = 'aeiouAEIOU'
    while first <= end:
        if lst_string[first] not in vowels:
            first += 1
        if lst_string[end] not in vowels:
            end -= 1
        if lst_string[first] in vowels and lst_string[end] in vowels:
            temp = lst_string[first]
            lst_string[first] = lst_string[end]
            lst_string[end] = temp
            first += 1
            end -= 1
    return ''.join(lst_string)

        
