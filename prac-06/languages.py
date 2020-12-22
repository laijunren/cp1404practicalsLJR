from programming_language import ProgrammingLanguage


def main():
    java = ProgrammingLanguage("Java", "Static", True, 1995)
    c_plus_plus = ProgrammingLanguage("C++", "Static", False, 1983)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    vb = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)

    languages = [java, c_plus_plus, python, vb, ruby]
    print("The all languages:")
    for lang in languages:
        print(lang)
    print()
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
