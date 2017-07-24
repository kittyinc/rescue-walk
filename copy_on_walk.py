#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author Jordi Loyzaga

"""Copy on walk, file rescue script.
    Give it a path to walk and exception lists and it will salvage all files from there."""

import os
import sys
from shutil import copyfile
from time import sleep


def prep(root_dir, avoid_exts=[], avoid_dirs=[], avoid_words=[]):
    """
    Walks the directory and prepares for copying.

    @params
        [string] directory: the target directory
        [string] root_dir: We're we'll be walking.

        optional [<string>list] avoid_exts: extensions to avoids
        optional [<string>list] avoid_dirs: directorys to avoid
        optional [<string>list] avoid_words: filenames to avoid

    @returns
        [dict] key-value filname:source"""

    destinations = {}
    dups = {}

    for dirName, subdirList, fileList in os.walk(root_dir):
        for avoid in avoid_dirs:
            if avoid in dirName:
                continue

        for fname in fileList:
            fullname = '{0}/{1}'.format(dirName, fname)
            filename, file_extension = os.path.splitext(fname)

            if fname in avoid_words or file_extension in avoid_exts:
                continue

            if fname in destinations:
                if fname in dups:
                    dups[fname] += 1
                else:
                    dups[fname] = 1

                fname = filename + "_" + str(dups[fname]) + file_extension
            destinations[fname] = fullname
    return destinations


def rescue_copy(destinations, directory, mock=False):
    """
    Performs a rescue copy.

    @params
        [string] directory: the target directory

        optional [bool] mock: use mock = True for a report

    @returns
        [int] stdio error code"""

    totals = len(destinations)
    copied = 0

    if mock:
        report = []

    if directory[-1] != "/":
        target = directory + "/"

    print "Copying {0} files to {1}".format(totals, target)

    for file in destinations:

        if mock:
            report.append(file)
            copied += 1
        else:
            copyfile(destinations[file], target + file)
            copied += 1

        print_progress(copied, totals)

    if mock:
        print "Mock report:"
        print "Found: {0} files.\n".format(copied)
        report = sorted(report)
        for file in report:
            print "File: {0}".format(file)
    else:
        print "Copied {0} files successfully to {1}".format(copied, target)
    return 0


def print_progress(iteration, total, prefix='', suffix='', decimals=1, bar_length=100):
    """
    Call in a loop to create terminal progress bar

    @params:
         [int] iteration : current iteration
         [int] total : total iterations

         optional [str] prefix : prefix string
         optional [str] suffix : suffix string
         optional [int] decimals : positive number of decimals in percent complete
         optional [int] bar_length : character length of bar

    @returns:
        [void]
    """
    str_format = "{0:." + str(decimals) + "f}"
    percents = str_format.format(100 * (iteration / float(total)))
    filled_length = int(round(bar_length * iteration / float(total)))
    bar = '█' * filled_length + '-' * (bar_length - filled_length)

    sys.stdout.write('\r%s |%s| %s%s %s' % (prefix, bar, percents, '%', suffix)),

    if iteration == total:
        sys.stdout.write('\n')
    sys.stdout.flush()


def main():
    root_dir = '.'
    avoid_exts = [".py", ".pyc", ]
    avoid_words = [""]
    avoid_dirs = [""]
    target = ""

    files = prep(root_dir, avoid_exts=avoid_exts, avoid_dirs=avoid_dirs, avoid_words=avoid_words)
    rescue_copy(files, target)


if __name__ == '__main__':
    main()
