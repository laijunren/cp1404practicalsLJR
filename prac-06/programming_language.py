class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return string representation of a ProgrammingLanguage."""
        return "{}, Typing: {}, Reflection: {}, in {}".format(
            self.name, self.typing, self.reflection, self.year)

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        if self.typing == "Dynamic":
            return True
        return False


def tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
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
