from chat import socketapp, app
import argparse

parser = argparse.ArgumentParser(
    usage = "Starts Chat Application."
)

parser.add_argument(
    "--port",
    type = int,
    help = "Port to listen on"
)
parser.add_argument(
    "--host",
    type = str,
    help = "Host to bind to."
)

parser.add_argument(
    "--debug",
    type = bool,
    help = "Enable debugging."
)

args = parser.parse_args()

socketapp.run(app, **vars(args))