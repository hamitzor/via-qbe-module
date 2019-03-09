"""Loads cli arguments."""

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-a", "--api", action="store_true",
                    help="output for api usage")
parser.add_argument("-q", "--quiet", action="store_true",
                    help="suppress status messages to be printed on command like")
parser.add_argument("-s", "--skip", type=float,
                    help="number of frames to skip before processing next frame", default=5)
parser.add_argument("-e", "--end", type=int,
                    help="the last second to process (excluded)", default=2147483646)
parser.add_argument("-b", "--begin", type=int,
                    help="the first second to process", default=0)
parser.add_argument("-d", "--display", action="store_true",
                    help="display matches (gui required)")
parser.add_argument("-f", "--display-features", action="store_true",
                    help="display matched features along with matches (gui required)")
