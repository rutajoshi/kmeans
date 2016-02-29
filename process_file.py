#!/usr/bin/env python
__author__ = 'dtalessi'


import re
import collections
import sys



def process(input_file, unique_names):
    infile = open(input_file, "r")
    name_record = []
    activity_sequence = collections.defaultdict(lambda: [])
    for line in infile:
        line = re.sub("\"", "", line)   # delete quotation marks
        time, activity, name = line.strip().split(",")  # split into tokens
        if name in name_record:     # define new time interval
            inactive_users = unique_names.difference(name_record)  # users that didn't participate in this time interval
            for user in inactive_users:
                activity_sequence[user] += ["0"]
            name_record = []        # reset name record
        name_record.append(name)
        activity_sequence[name] += [activity]
    infile.close()
    return activity_sequence


def find_unique_names(input_file):
    infile = open(input_file, "r")
    unique_names = set()
    for line in infile:
        line = re.sub("\"", "", line)   # delete quotation marks
        time, activity, name = line.strip().split(",")  # split into tokens
        unique_names.add(name)
    infile.close()
    return unique_names


def create_output_file(activity_sequence, unique_names):
    outfile = open("activity_sequence_output", "w")
    for name in unique_names:
        seq = activity_sequence[name]
        seq = "\t".join(seq)
        print(len(seq))
        outfile.write(seq + "\n")
    outfile.close()


def main(input_file):
    unique_names = find_unique_names(input_file)
    activity_sequence = process(input_file, unique_names)
    create_output_file(activity_sequence, unique_names)
    print("Each row in output file represents info for each person, in the following order:")
    for name in unique_names:
        print(name)


if __name__ == '__main__':
    main(*sys.argv[1:])
