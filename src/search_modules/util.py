import time
from args import parser

args = parser.parse_args()


def get_time():
    return time.time() * 1000


def passed_time(start_time, desc):
    if not args.quiet and not args.api:
        print ""
        elapsed_time = time.time() * 1000 - start_time
        print desc, str(int(elapsed_time)) + "ms"
        return int(elapsed_time)


def info_function(percentage):
    import sys
    if not args.quiet and not args.api:
        sys.stdout.write("\r" + str(percentage) + "% of video processed")
        sys.stdout.flush()


def write(s):
    if not args.quiet and not args.api:
        print str(s)