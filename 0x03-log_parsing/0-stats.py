#!/usr/bin/python3

''' Parses log and reports stats '''

import sys
import re
import signal


def signal_handler(signal, form):
    ''' Handler for SIGINT '''
    print_stats()


signal.signal(signal.SIGINT, signal_handler)


def print_stats():
    ''' Prints number of status codes and total file size '''
    global total_size
    print(f"File size:", total_size)
    for key, value in sorted(statuses.items()):
        if statuses[key] == 0:
            continue
        else:
            print(key, ":", value)


ip_addr_pattern = r'[0-2]?[0-9]?[0-9]\.[0-2]?[0-9]?[0-9]\.'\
                    + r'[0-2]?[0-9]?[0-9]\.[0-2]?[0-9]?[0-9]'
date_pattern = r'[12][0-9][0-9][0-9]-[01][0-9]-[0-3][0-9] '\
                + r'[0-2][0-9]:[0-6][0-9]:[0-6][0-9].\d{6}'
string_pattern = r'"GET /projects/260 HTTP/1.1"'
status_size_pattern = r'(200|301|400|401|403|404|405|500) \d{1,4}'
final_pattern = f'{ip_addr_pattern} - \\[{date_pattern}\\]'\
                + f' {string_pattern} {status_size_pattern}'

total_size = 0
statuses = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

count = 0
for log in sys.stdin:
    count += 1
    if re.match(final_pattern, log) is not None:
        status_size = re.search(status_size_pattern, log)
        status_size = str(status_size.group())
        status, size = int(status_size[:3]), int(status_size[4: 8])
    if type(status) == int and status in statuses:
        statuses[status] += 1
    total_size += size
    if count % 10 == 0 or KeyboardInterrupt:
        print_stats()
