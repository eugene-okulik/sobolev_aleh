import os
import re
import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(description="Log Analyzer")
    parser.add_argument('log_directory', type=str, help="Full path directory")
    parser.add_argument('--text', type=str, required=True, help="Text search")
    return parser.parse_args()


def search_in_logs(log_directory, search_text):
    if not os.path.isdir(log_directory):
        print(f"Directory {log_directory} not exist.")
        sys.exit(1)

    for log_file in os.listdir(log_directory):
        log_path = os.path.join(log_directory, log_file)

        with open(log_path, 'r') as file:
            for line_num, line in enumerate(file, 1):
                if re.search(re.escape(search_text), line):
                    print_result(log_file, line_num, line, search_text)


def print_result(filename, line_num, line, search_text):
    words = line.split()
    try:
        index = words.index(search_text)
    except ValueError:
        return

    start_index = max(index - 5, 0)
    end_index = min(index + 6, len(words))

    context = " ".join(words[start_index:end_index])
    print(f"File name: {filename}, line: {line_num}, CONTEXT: {context}")


if __name__ == "__main__":
    args = parse_args()
    search_in_logs(args.log_directory, args.text)
