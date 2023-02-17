#!/usr/bin/python3
'''A script that reads stdin line by line and computes metrics'''


import sys

cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_size = 0
counter = 0

try:
    for line in sys.stdin:
        line_list = line.split(" ")
        if len(line_list) > 4:
            code = line_list[-2]
            size = int(line_list[-1])
            if code in cache.keys():
                cache[code] += 1
            total_size += size
            counter += 1

        if counter == 10:
            counter = 0
            print('File size: {}'.format(total_size))
            for key, value in sorted(cache.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))


'''#!/usr/bin/python3
""" A script for log parsing from stdin"""


import sys


def status_writer():
    """ Extracts the data fields from the stream
        and prints the status log
    """
    line_count = 0
    total_size = 0
    status_code = ['200', '301', '400', '401', '403', '404', '405', '500']
    status_count = dict([(code, 0) for code in status_code])

    try:
        for line in sys.stdin:
            capture = re.findall(match, line)
            try:
                total_size += int(capture[0][1])
                status_count[capture[0][0]] += 1
            except IndexError:
                continue
            line_count += 1

            if line_count == 10:
                line_count = 0
                print(f"File size: {total_size}")
                for status_code, number in status_count.items():
                    if number != 0:
                        print(f"{status_code}: {number}")

    except KeyboardInterrupt:
        print(f"File size: {total_size}")
        for status_code, number in status_count.items():
            if number != 0:
                print(f"{status_code}: {number}")

if __name__ == '__main__':
    status_writer()
'''
