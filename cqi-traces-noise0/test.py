import re

def count_numbers_in_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    numbers = re.findall(r'\d+', content)
    return len(numbers)

if __name__ == '__main__':
    filename = '/home/wooyoung/LTE-openairinterface/cqi-traces-noise0/ue95.log'
    count = count_numbers_in_file(filename)
    print(f"num count: {count}")
