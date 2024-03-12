def mutate_string(string, position, character):
    listString = list(string)
    listString[position] = character
    return ''.join(listString)