import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-a", "--api", action="store_true",
                    help="output for api usage")
parser.add_argument("-q", "--quiet", action="store_true",
                    help="suppress status messages to be printed on command like")
parser.add_argument("-s", "--skip", type=float,
                    help="amount of frames to skip before executing the next frame", default=1)
parser.add_argument("-e", "--end", type=int,
                    help="the last second to process (excluded)", default=2147483646)
parser.add_argument("-b", "--begin", type=int,
                    help="the first second to process", default=0)
