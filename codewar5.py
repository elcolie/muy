"""
T9 `contacts.txt`
Questions:
728
5203
273
2738
"""
KEY_DICT = {
    '0': None,
    '1': None,
    '2': "A",
    '3': "D",
    '4': "G",
    '5': "J",
    '6': "M",
    '7': "P",
    '8': "T",
    '9': "W"
}

def get_list():
    """
    Read file to list
    :return:
    """
    with open('contacts.txt') as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]
    return content

def main():
    questions = [
        '728',
        '5203',
        '273',
        '2738',
    ]
    for q in questions:
        for i in q:
            print(KEY_DICT[i])
        print('---' * 10)
    list = get_list()

if __name__ == '__main__':
    main()
