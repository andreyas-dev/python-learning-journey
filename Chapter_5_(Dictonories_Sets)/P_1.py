# Create a dictionay of urdu words with values as english translation.Provide userwith na option to look it up!

urdu_dict = {
    'Kitab' : 'Book',
    'Qalam' : 'Pen',
    'Makan' : 'House',
    'Dost' : 'Friend',
    'Pani' : 'Water'
}

word = input('Enter an urdu word to look it up in english:')
print(urdu_dict[word])