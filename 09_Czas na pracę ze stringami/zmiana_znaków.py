"""Napisz program, który dla podanego łańcucha znaków zamieni podaną pozycję na jakiś znak (też podany przez użytkownika).
Funkcja, która dokona zamiany znaku z podanej pozycji musi sprawdzić, czy wskazana pozycja jest prawidłowa
(nie możemy zmienić szóstego znaku, podczas gdy łańcuch ma tylko 5 znaków).
Funkcja powinna przyjmować 3 parametry (łańcuch do analizy, pozycję, którą należy podmienid i znak, który ma służyć do podmiany).
Niech program wyświetla łańcuch przed i po zamianie.
"""


def new_word(origin_word, swap_letters_location, swap_letters):
    begging_swap_letters_location = swap_letters_location - 1
    swap_letters_length = len(swap_letters)
    end_swap_letters_location = begging_swap_letters_location + swap_letters_length
    first_part_new_word = origin_word[:begging_swap_letters_location]
    last_part_new_word = origin_word[end_swap_letters_location:]

    if swap_letters_location > len(origin_word):
        print("Origin word is too short")
    elif swap_letters_length <= len(origin_word) and swap_letters_location > 0 \
            and swap_letters_length <= len(origin_word[begging_swap_letters_location:]):
        new_word = [first_part_new_word, swap_letters, last_part_new_word]
        new_word = ''.join(new_word)
        print("The origin word was: {}".format(origin_word))
        print("The word word is: {}".format(new_word))
    else:
        print("There are too many letters to swap")


origin_word = input("Please enter the word we will modify: ")
swap_letters_location = int(input("Please give the position of the letter from which we will start to change: "))
swap_letters = input("Please enter the new letters you want to insert: ")


new_word(origin_word, swap_letters_location, swap_letters)

    


