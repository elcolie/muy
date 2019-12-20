"""
Where is your last direction x=0, y=0 is your starting point
Read file from `direction.txt`
"""


def get_list():
    with open('direction.txt', 'r') as file:
        ans = file.readlines()
    return ans

def main():
    get_list()

if __name__ == '__main__':
    main()
