import os
import string 
import json
import time
import argparse


def main():
    datetime = time.strftime("%Y%m%d_%H_%M_%S")

    file = open(args.file, 'r', encoding='utf-8')
    lines = file.readlines()

    users = {}
    for i, line in enumerate(lines):
        stripped_line = line.strip()
        if len(stripped_line) != 0:
            stripped_line = stripped_line.split(' ')
            filtered_list = [element for element in stripped_line if len(element) > 0]
            
            print(filtered_list)
            if i > 0:
                users[filtered_list[0]] = {'PasswordExpires': filtered_list[1],
                                        'PasswordRequired': filtered_list[2],}
    print(users)
    file_name = f'{datetime}_user_passwords.json'
    json.dump(users, open(file_name, 'w'), indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help='The file to be read')
    args = parser.parse_args()
    main()