import wikipedia

user_input = input("search/title: ")

while user_input != ' ':
    try:
        wikipedia.summary(user_input)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
