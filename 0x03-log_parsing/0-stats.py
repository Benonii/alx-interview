#!/usr/bin/python3

import sys
import re

try:
    ip_address_pattern = r'[0-2]?[0-9]?[0-9]\.[0-2]?[0-9]?[0-9]\.'
    +r'[0-2]?[0-9]?[0-9]\.[0-2]?[0-9]?[0-9]'
    date_pattern = r'[12][0-9][0-9][0-9]-[01][0-9]-[0-3][0-9] [0-2]'
    +r'[0-9]:[0-6][0-9]:[0-6][0-9].\d{6}'
    string_pattern = '"GET \/projects\/260 HTTP\/1.1"'
    status_size_pattern = '(200|301|400|401|403|404|405|500) \d{1,4}'
    final_pattern = f'{ip_address_pattern} - \[{date_pattern}\]'
    +f' {string_pattern} {status_size_pattern}'
    total_size = 0
    statuses = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    count = 0
    logs = sys.stdin.readlines()

    for log in logs:
        if re.match(final_pattern, log) is not None:
            status_size = re.search(status_size_pattern, log)
            status_size = str(status_size.group())
            status, size = int(status_size[:3]), int(status_size[4: 8])
        else:
            print("log not a match")
            continue

        if status in statuses.keys():
            statuses[status] += 1
        else:
            print(f"{status} not in statuses")

        count += 1
        total_size += size

        if count == 10:
            print(f"File size: {total_size}")
            for key, value in sorted(statuses.items()):
                if statuses[key] == 0:
                    continue
                else:
                    print(f'{key}: {value}')
            count = 0
except KeyboardInterrupt:
    print(f"File size: {total_size}")
    for key, value in sorted(statuses.items()):
        if statuses[key] == 0:
            continue
        else:
            print(f'{key}: {value}')
    # raise KeyboardInterrupt
