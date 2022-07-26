import re


def welcome():

    print("""
    ***********************************************
    **     Welcome to Mad Matt's Madlib Maker    **
    **      You will be provided with some       **
    **   text that has {Adjective's}, {Noun's}   **
    **    {Verb's}, or {Adverb's}. As a user     **
    **  you should submit words that fit these   **
    ** categories to build your custom sentence. **
    ***********************************************
    """)


regex = r"(?<={).*?(?=})"


def read_template(file_path):
    with open(f"{file_path}") as file:
        unparsed_message = file.read().strip()
        return(unparsed_message)


def parse_template(string):

    def pieces(text, prompts):
        stripped = text
        parts = prompts
        return stripped,parts

    parts_of_speech = re.findall(regex, string)
    parsed_message = re.sub(regex, "", string)

    return pieces(parsed_message, tuple(parts_of_speech))


def merge(string, prompts):
    return string.format(*prompts)


if __name__ == '__main__':
    welcome()

    unparsed_message = read_template("assets/example1.txt")
    parsed_message, parts_of_speech = parse_template(unparsed_message)

    user_filler = []
    for part in parts_of_speech:
        user_filler.append(input(f"{part} -> "))

    filled_message = merge(parsed_message, tuple(user_filler))
    print(filled_message)

    with open("assets/finished_madlibs.txt", 'w') as file:
        file.writelines(filled_message)