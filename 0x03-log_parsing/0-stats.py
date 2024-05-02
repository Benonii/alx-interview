import sys
import signal

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def print_stats():
    global total_size
    print("Total file size:", total_size)
    for status_code in sorted(status_codes.keys()):
        print(status_code, ":", status_codes[status_code])

total_size = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}

try:
    line_count = 0
    for line in sys.stdin:
        line_count += 1
        if line_count % 10 == 0:
            print_stats()

        parts = line.split()
        if len(parts) != 7:
            continue

        ip_address, date, method, status_code, file_size = parts[0], parts[3][1:], parts[5], parts[6], parts[7]
        if not status_code.isdigit():
            continue

        status_code = status_code.strip()
        if status_code in status_codes:
            status_codes[status_code] += 1

        total_size += int(file_size)

except KeyboardInterrupt:
    pass
finally:
    print_stats()