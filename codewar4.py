"""
Bangkok in NATO. How long is it?
Answer is using ord and offset it and concat the string
Finish it by len()
"""

NATO = [
    "ALFA", "BRAVO", "CHARLIE", "DELTA", "ECHO", "FOXTROT", "GOLF", "HOTEL",
    "INDIA", "JULIETT", "KILO", "LIMA", "MIKE", "NOVEMBER", "OSCAR", "PAPA",
    "QUEBEC", "ROMEO", "SIERRA", "TANGO", "UNIFORM", "VICTOR", "WHISKEY",
    "XRAY", "YANKEE", "ZULU"
]

def nato(input: str):
    """
    Return NATO given
    :param input:
    :return:
    """
    for i in 'bangkok':
        print(ord(i))

def main():
    nato(11)


if __name__ == '__main__':
    main()
