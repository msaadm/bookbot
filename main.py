def main():
    text = None
    with open("./books/frankenstein.txt") as f:
        text = f.read()

    words_count = count_words(text)

    characaters_dict = count_characters(text)
    sorted_characters_list = sort_by_count(characaters_dict)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{words_count} words found in the document\r\n")

    for c in sorted_characters_list:
        print(f"The '{c['char']}' character was found {c['count']} times")

    print("--- End report ---")


def sort_by_count(dict):
    temp_list = []
    for i in dict:
        if i.isalpha():
            temp_list.append({"char": i, "count": dict[i]})

    def sort_on(dict):
        return dict["count"]

    temp_list.sort(reverse=True, key=sort_on)

    return temp_list


def count_words(text):
    return len(text.split())


def count_characters(text):
    character_map = {}
    for c in text:
        _c = c.lower()
        if _c in character_map:
            character_map[_c] += 1
        else:
            character_map[_c] = 1

    return character_map


if __name__ == "__main__":
    main()
