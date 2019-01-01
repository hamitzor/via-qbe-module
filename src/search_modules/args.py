import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-a", "--api", action="store_true", help="output for api usage purpose")
parser.add_argument("-q", "--quiet", action="store_true", help="suppress status messages to be printed on command like")
parser.add_argument("-r", "--skip", type=float, help="frame rate of processing", default=1)
parser.add_argument("-e", "--end", type=int, help="last second to be processed", default=2147483646)
parser.add_argument("-b", "--begin", type=int, help="number of seconds to skip before start to process video", default=0)