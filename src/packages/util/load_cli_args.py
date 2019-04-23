"""Loads cli arguments."""

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-DH",
                    "--db-host",
                    type=str,
                    help="host of database server")

parser.add_argument("-DU",
                    "--db-username",
                    type=str,
                    help="username of database")

parser.add_argument("-DP",
                    "--db-password",
                    type=str,
                    help="password of database")

parser.add_argument("-DN",
                    "--db-name",
                    type=str,
                    help="database name")

parser.add_argument("-a",
                    "--api",
                    action="store_true",
                    help="output for api usage")

parser.add_argument("-q",
                    "--quiet",
                    action="store_true",
                    help="suppress status messages to be printed on command line")

parser.add_argument("-s",
                    "--skip",
                    type=int,
                    help="number of frames to skip before processing next frame", default=5)

parser.add_argument("-b",
                    "--begin",
                    type=int,
                    help="the first second to process", default=0)

parser.add_argument("-e",
                    "--end",
                    type=int,
                    help="the last second to process (excluded)")
