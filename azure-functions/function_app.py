import os

import azure.functions as func

# loadgen/app.py is copied to app.py (this directory) as a build step
# before publishing/testing - see deploy.sh/test-local.sh. Azure's remote
# build only packages this directory, not sibling repo folders, so the
# source of truth stays in loadgen/app.py but the deployed/tested artifact
# needs its own local copy.
from app import ping_frontend

func_app = func.FunctionApp()

# loadgen's container default is SLEEP_TIME=5000ms between requests; a Timer
# trigger fires once per schedule instead of looping, so this NCRONTAB
# expression (every 5 seconds) is the equivalent. Override via the
# LOADGEN_SCHEDULE app setting if you want a different cadence.
_schedule = os.environ.get("LOADGEN_SCHEDULE", "*/5 * * * * *")


@func_app.timer_trigger(schedule=_schedule, arg_name="timer")
def loadgen_timer(timer: func.TimerRequest) -> None:
    ping_frontend()
