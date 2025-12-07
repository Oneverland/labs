from bs4 import BeautifulSoup
import requests
import os

class MyFile:
    def __init__(self, name='new_file.txt', action='read'):
        self.name = name
        self.action = action

    def read(self):
        if self.action == 'read':
            with open(self.name, 'r') as file:
                for line in file.readlines():
                    print(line, end='')
            print('\n')
        else:
            print(f"Wrong action. Ur current action: \"{self.action}\"")

    def write(self, inp):
        if self.action == 'write':
            with open(self.name, "w") as file:
                file.write(inp)
        elif self.action == 'append':
            with open(self.name, "a") as file:
                file.write('\n' + inp)
        else:
            print(f"Wrong action. Ur current action: \"{self.action}\"")

    def read_url(self):
        if self.action == 'url':
            response = requests.get(self.name)
            print(response.text)
        else:
            print(f"Wrong action. Ur current action: \"{self.action}\"")

    def count_urls(self):
        if self.action == 'url':
            c = 0
            response = requests.get(self.name)
            soup = BeautifulSoup(response.text, 'html.parser')
            all_links = soup.find_all('a')
            for link in all_links:
                url = str(link.get('href'))
                if url.startswith('http'):
                    c += 1
            print('count of urls: ', c)
        else:
            print(f"Wrong action. Ur current action: \"{self.action}\"")

    def write_url(self, filename):
        if self.action == 'url':
            with open(filename, 'w') as file:
                file.write(requests.get(self.name).text)



action = '1'
while action != '0':
    print("=================|START|====================")
    print("Hi, it's user friendly interface for lab2.2")
    print("1. Read a file")
    print("2. Write a file")
    print("3. Append to file")
    print("4. Read url")
    print("5. Save html from url to txt")
    print("6. Count urls in url")
    print("0. Quit from program")
    print("============================================")
    action = input("What u wanna do? ")
    match action:

        case '1':
            my_file = MyFile(input("i need ur file name: "), 'read')
            if os.path.isfile(my_file.name):
                my_file.read()
            else:
                print('i cant see the file. ERROR')

        case '2':
            my_file = MyFile(input("i need ur file name: "), 'write')
            if os.path.isfile(my_file.name):
                my_file.write(input("What u wanna write?: "))
            else:
                print('i cant see the file. ERROR')

        case '3':
            my_file = MyFile(input("i need ur file name: "), 'append')
            if os.path.isfile(my_file.name):
                my_file.write(input("What u wanna write?: "))
            else:
                print('i cant see the file. ERROR')

        case '4':
            my_file = MyFile(input("i need ur url: "), 'url')
            try:
                if requests.get(my_file.name).status_code == 200:
                    my_file.read_url()
            except requests.exceptions.RequestException as e:
                print(f'Cant open url: {e}')

        case '5':
            my_file = MyFile(input("i need ur url: "), 'url')
            try:
                if requests.get(my_file.name).status_code == 200:
                    filename = input("where r u wanna write this html? ")
                    if os.path.isfile(filename):
                        my_file.write_url(filename)
                    else:
                        print('i cant see the file. ERROR')
            except requests.exceptions.RequestException as e:
                print(f'Cant open url: {e}')

        case '6':
            my_file = MyFile(input("i need ur url: "), 'url')
            try:
                if requests.get(my_file.name).status_code == 200:
                    my_file.count_urls()
            except requests.exceptions.RequestException as e:
                print(f'Cant open url: {e}')

        case '0':
            print('bye bye')

        case _:
            print(f"Wrong action. Ur current action: \"{action}\"")