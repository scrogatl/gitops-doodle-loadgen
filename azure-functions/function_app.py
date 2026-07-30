import os
import sys

# Reuse the existing ping_frontend() helper from loadgen/app.py instead of
# duplicating the request logic for the Functions runtime.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "loadgen"))

import azure.functions as func
from app import ping_frontend  # noqa: E402

func_app = func.FunctionApp()

# loadgen's container default is SLEEP_TIME=5000ms between requests; a Timer
# trigger fires once per schedule instead of looping, so this NCRONTAB
# expression (every 5 seconds) is the equivalent. Override via the
# LOADGEN_SCHEDULE app setting if you want a different cadence.
_schedule = os.environ.get("LOADGEN_SCHEDULE", "*/5 * * * * *")


@func_app.timer_trigger(schedule=_schedule, arg_name="timer")
def loadgen_timer(timer: func.TimerRequest) -> None:
    ping_frontend()
